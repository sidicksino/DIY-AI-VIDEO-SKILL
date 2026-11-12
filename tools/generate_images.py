#!/usr/bin/env python3
import argparse
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')

def main():
    parser = argparse.ArgumentParser(description="Generate images from prompts.md")
    parser.add_argument("project_dir", help="Path to the project directory")
    args = parser.parse_args()
    
    project_dir = Path(args.project_dir).resolve()
    prompts_file = project_dir / "prompts.md"
    
    if not prompts_file.exists():
        print(f"Error: {prompts_file} not found.")
        return
        
    out_dir = project_dir / "generated_images"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    content = prompts_file.read_text()
    
    # Extract visual lock text to prepend to prompts for better context
    visual_lock_match = re.search(r"# VISUAL LOCK\n(.*?)(?=\n#|\Z)", content, re.DOTALL)
    visual_lock_text = visual_lock_match.group(1).strip() if visual_lock_match else ""
    
    # Extract object lock text to enforce strict geometry continuity
    object_lock_match = re.search(r"# OBJECT LOCK\n(.*?)(?=\n#|\Z)", content, re.DOTALL)
    object_lock_text = object_lock_match.group(1).strip() if object_lock_match else ""
    
    # Extract all text-to-image prompts
    matches = list(re.finditer(r"### 🖼️ TEXT-TO-IMAGE PROMPT(.*?)\n(.*?)(?=\n###|\Z)", content, re.DOTALL))
    
    if not matches:
        print("No image prompts found in the file.")
        return
        
    print(f"Found {len(matches)} image prompts.")
    
    previous_image = None
    
    for i, match in enumerate(matches):
        title_suffix = match.group(1).strip()
        prompt_text = match.group(2).strip()
        
        # Combine visual lock with the specific prompt text
        full_prompt = f"VISUAL LOCK CONTEXT:\n{visual_lock_text}\n\nOBJECT LOCK (STRICT GEOMETRY):\n{object_lock_text}\n\nSCENE PROMPT:\n{prompt_text}"
        
        # Determine filename
        if title_suffix:
            slug = slugify(title_suffix)
            filename = f"scene_{i+1:02d}_{slug}.png"
        else:
            filename = f"scene_{i+1:02d}.png"
            
        out_img = out_dir / filename
        prompt_tmp = out_dir / f"temp_prompt_{i+1}.txt"
        prompt_tmp.write_text(full_prompt)
        
        print(f"\n--- Generating {filename} ---")
        
        cmd = [
            str(ROOT / ".venv/bin/python"), str(ROOT / "tools/gen_image.py"),
            "--prompt-file", str(prompt_tmp),
            "--ref", str(ROOT / "brand/luna-sheet.png"),
            "--ref", str(ROOT / "brand/luna-garden.png"),
            "--out", str(out_img),
            "-n", "1"
        ]
        
        if previous_image and previous_image.exists():
            cmd.extend(["--ref", str(previous_image)])
            
        try:
            subprocess.run(cmd, check=True)
            previous_image = out_img
        except subprocess.CalledProcessError as e:
            print(f"Error generating {filename}: {e}")
            break
            
        # Cleanup temp file
        if prompt_tmp.exists():
            prompt_tmp.unlink()

if __name__ == "__main__":
    main()
