#!/usr/bin/env python3
import argparse
import base64
import json
import os
import subprocess
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

import cv2
from scenedetect import detect, ContentDetector

ROOT = Path(__file__).resolve().parent.parent
API = "https://generativelanguage.googleapis.com/v1beta/models"
MODEL = "gemini-3.1-pro-preview"

def api_key():
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.strip().startswith(("GEMINI_API_KEY=", "GEMIMIAI_API_KEY=")):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("No GEMINI_API_KEY in .env")

def get_next_project_id():
    projects_dir = ROOT / "projects"
    if not projects_dir.exists():
        return 1
    existing_ids = []
    for d in projects_dir.iterdir():
        if d.is_dir():
            try:
                prefix = int(d.name.split("-")[0])
                existing_ids.append(prefix)
            except ValueError:
                pass
    return max(existing_ids) + 1 if existing_ids else 1

def download_video(url, output_path):
    print(f"Downloading video from {url}...")
    cmd = ["yt-dlp", url, "-o", str(output_path)]
    subprocess.run(cmd, check=True)

def extract_scenes(video_path, out_dir):
    print("Extracting scenes...")
    out_dir.mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(str(video_path))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    
    # Using threshold 15.0 to catch subtle cuts, with 1 second min length
    scene_list = detect(str(video_path), ContentDetector(threshold=15.0, min_scene_len=int(fps*1)))
    
    print(f"Found {len(scene_list)} scenes.")
    extracted_frames = []
    
    for i, scene in enumerate(scene_list):
        offset = 10 # Avoid transition blur
        start_frame = scene[0].frame_num + offset
        end_frame = scene[1].frame_num - 1 - offset
        if end_frame < start_frame:
            end_frame = start_frame
            
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        ret, frame = cap.read()
        if ret:
            frame_path = out_dir / f"scene_{i+1:02d}_start.jpg"
            cv2.imwrite(str(frame_path), frame)
            extracted_frames.append(frame_path)
            
    cap.release()
    return extracted_frames

def generate_prompt_package(url, title, frames, key, output_path):
    print("Calling Gemini API for analysis and prompt generation...")
    prompt_md = (ROOT / "prompt.md").read_text()
    second_md = (ROOT / "second_prompt.md").read_text()
    
    # Fill in the second prompt
    second_md = second_md.replace("[PASTE YOUTUBE / TIKTOK / PINTEREST URL HERE]", url)
    second_md = second_md.replace("[Example: Chrome Gold DIY Concrete Bear Coffee Table]", title)
    
    luna_md = (ROOT / "brand/luna.md").read_text() if (ROOT / "brand/luna.md").exists() else "Use Luna character."
    
    parts = []
    parts.append({"text": f"MASTER INSTRUCTIONS:\n{prompt_md}\n\nLUNA CHARACTER REFERENCE:\n{luna_md}\n\nPROJECT REQUEST:\n{second_md}\n\nMANDATORY: You must change the core shape of the final object and the primary colors (e.g. umbrella color) to be distinctly different from the reference video to make it an original project. CRITICAL LOGIC RULE: If you change the final shape to be a square or rectangle, you CANNOT use an umbrella as the mold in the first step. You MUST change the physical starting mold to match the shape you choose (e.g., use a rectangular plastic storage bin or a cardboard box instead of an umbrella). The physics of the DIY process must make perfect sense from start to finish.\nCRITICAL CHARACTER RULE: You MUST copy the Luna character description exactly word-for-word from the LUNA CHARACTER REFERENCE into your VISUAL LOCK and SCENE PROMPTS. Do NOT change her clothing (she must wear the sage-green t-shirt, beige apron, olive cargo pants), hair, or appearance in any way.\nCRITICAL DETAIL RULE: If your object has decorative elements (like stones on the rim), you MUST strongly emphasize them in every single scene prompt where the object is visible, especially the final installed reveal, so the image generator does not forget them.\n\nHere are the extracted reference frames from the video. Please follow the instructions and create the production plan."})
    
    for frame_path in frames:
        mime = "image/jpeg" if frame_path.suffix.lower() in [".jpg", ".jpeg"] else "image/png"
        parts.append({
            "inlineData": {
                "mimeType": mime,
                "data": base64.b64encode(frame_path.read_bytes()).decode()
            }
        })
        
    body = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "temperature": 0.7
        }
    }
    
    req = urllib.request.Request(
        f"{API}/{MODEL}:generateContent", data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": key})
        
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                resp = json.loads(r.read())
                text = resp["candidates"][0]["content"]["parts"][0]["text"]
                output_path.write_text(text)
                print(f"Successfully generated prompt package to {output_path}")
                return
        except urllib.error.HTTPError as e:
            print(f"HTTP {e.code}: {e.read()[:400].decode(errors='replace')}")
            if attempt < 2:
                time.sleep(5)
                continue
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Automate project extraction and prompting.")
    parser.add_argument("url", help="YouTube/TikTok URL")
    parser.add_argument("title", help="Title for the new project")
    args = parser.parse_args()
    
    key = api_key()
    
    project_id = get_next_project_id()
    folder_name = f"{project_id:03d}-{args.title.lower().replace(' ', '-')}"
    project_dir = ROOT / "projects" / folder_name
    project_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Creating new project: {folder_name}")
    
    video_path = project_dir / "reference_video.webm"
    download_video(args.url, video_path)
    
    frames_dir = project_dir / "reference_frames"
    extracted_frames = extract_scenes(video_path, frames_dir)
    
    prompts_path = project_dir / "prompts.md"
    generate_prompt_package(args.url, args.title, extracted_frames, key, prompts_path)

if __name__ == "__main__":
    main()
