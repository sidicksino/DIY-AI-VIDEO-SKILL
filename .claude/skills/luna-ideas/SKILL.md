---
name: luna-ideas
description: Find new, research-backed video ideas for the Luna Upcycles Shorts channel — Luna turns ordinary objects and junk into luxury, satisfying builds (furniture, lamps, décor, fire pits, glowing pieces, floors, garden builds, pet houses) across many locations. Researches what DIY / upcycling / "trash to luxury" Shorts are breaking out now (vidIQ + the user's reference videos), enforces variety in category, place and payoff, and saves a ranked shortlist. Use when the user says "find ideas", "new ideas", "give me an idea", "what should the next video be", "idea for Luna", or runs /luna-ideas. Ideas only — never generates images or video.
---

# Luna Ideas

Produces a ranked, **varied** shortlist of original video ideas for **Luna
Upcycles**. It stops at the idea: no prompts, frames or video.

The user should never have to explain the channel. Everything you need is in
this file and in the project folder.

**The channel is not "garden houses for animals".** It's Luna turning ordinary
things into luxury, satisfying results, in many places. Small garden animal
builds are one category of nine, and the variety rules below stop any
category from taking over.

## 1. Load context (always)

Read these files from the project root:
- `brand/luna.md` (Luna) and `brand/realism-playbook.md` (what AI can show
  convincingly)
- `brand/locations.md`: build places and luxury reveal places
- `ideas/log.md`: every idea ever, with **tags**. Never repeat an idea or a
  close variant. Use the tags for the variety rules in section 3.
- The newest `ideas/shortlist-*.md`
- **`references/`**: the user's reference videos (Instagram compilations).
  If a video there isn't listed in `references/README.md`, analyse it first:
  pull a 1-frame-per-1.5-s grid with ffmpeg, then list every project inside
  it (object → method → result → reveal place → payoff), and append those
  projects to `references/README.md`.

## 2. The variety system

### Categories (every idea belongs to exactly one)

| Key | Category | Examples |
|---|---|---|
| `furniture` | Big junk → luxury furniture | bathtub → velvet sofa, oil drum → armchair, TV → aquarium, tire → dog bed |
| `fabric-cast` | Fabric or clothes dipped in cement → sculpture or planter | jeans, skirt, dress, lace curtain, towel, hat |
| `mould-decor` | Cast in a mould → luxury décor | gold vases, terrazzo tables, mosaic sinks, letter-shaped side tables |
| `glow` | Glass, bottles, jars or lights in concrete → glows at night | bottle steps, jar walls, mosaic lamps, pendant lamps |
| `melt-tiles` | Waste melted or recycled into tiles, floors or paths | plastic → hexagon tiles, caps → terrazzo |
| `outdoor-build` | Big outdoor features | fire pits, ponds, waterfalls, wishing wells, paths, topiary |
| `grow-hack` | Growing tricks and garden hacks | fruit in moulds, grow bags, harvest reveals |
| `pet-wildlife` | Homes and baths for animals (the original niche) | igloo, hedgehog house, bird bath, cat bed |
| `room-reveal` | Whole-room or surface transformations | epoxy floor, feature wall, outdoor kitchen |

### Payoff types
`animal` · `night-glow` · `fire` · `water-running` · `luxury-room-reveal` ·
`harvest-cut-open` · `sit-and-use` (Luna or a guest uses it) ·
`shape-reveal` (unmould or peel)

### Rules, checked before saving the shortlist
1. **8 ideas cover at least 6 categories.** No category more than twice.
   `pet-wildlife` at most 2.
2. **At least 5 different payoff types.** `animal` at most 2.
3. **At least 4 different reveal places** from `brand/locations.md`;
   `cottage` at most 1.
4. **Freshness:** read the tags of the last 6 `picked`/`made` ideas in
   `ideas/log.md`. Any category used 2+ times in those 6 gets at most 1 idea
   now. Any category used 0 times gets at least 1 idea now (if it's
   buildable).
5. **Formats:** mark each idea **A** (one of 3 projects in a compilation
   Short, about 11 s each) or **B** (single 12–18 s Short). Include at least
   one named 3-project compilation built from A ideas of different
   categories.

## 3. Research

**a) References first (free).** Use the projects listed in
`references/README.md` as the strongest signal: these are what the user
wants. Take their *formats* (object type, method, finish, reveal), never
their exact builds.

**b) vidIQ (about 5 credits per call).** Load the tools with ToolSearch:
`select:mcp__89600bfe-3350-405e-97da-b6603d93a473__vidiq_outliers,mcp__89600bfe-3350-405e-97da-b6603d93a473__vidiq_trending_videos`
(If the server id has changed, search for `vidiq outliers`.)

Pick the **3 categories used least recently** (from the log tags) and run one
`vidiq_outliers` call per category, in parallel: contentType `short`,
publishedWithin `thisMonth` (or `threeMonths` if results are thin), limit 25.
Use keywords like these:

| Category | Keyword |
|---|---|
| `furniture` | `turning old junk into luxury furniture upcycle` |
| `fabric-cast` | `dipping clothes fabric in cement sculpture planter` |
| `mould-decor` | `DIY cement mould luxury home decor gold` |
| `glow` | `glass bottles in concrete glowing at night DIY` |
| `melt-tiles` | `melting plastic waste into tiles` |
| `outdoor-build` | `DIY fire pit pond backyard transformation` |
| `grow-hack` | `garden hack growing fruit in mould` |
| `pet-wildlife` | `DIY house for pets animals cement` |
| `room-reveal` | `epoxy floor room transformation` |

Add one `vidiq_trending_videos` call: videoFormat `short`, sortBy `vph`,
titleQuery `trash to luxury DIY`, videoPublishedAfter = 30 days ago, limit 25.

**Filter the results.** Ignore off-topic videos, videos under 10K views, and
breakout scores under 5x (unless views are above 500K). Group what's left
into patterns ("object → result + payoff") with counts and the best numbers.

## 4. Build ideas: result first

For each idea:
1. **Dream result.** The beautiful, luxurious finished piece in its reveal
   place (gold, mosaic, terrazzo, marble, glowing, velvet).
2. **Object.** The everyday object or junk whose own shape naturally makes
   that result: as a mould, as a base to coat, or kept visible with a job.
3. **Shape test:** write "object outline → final outline". If the result is a
   new shape that only hides the object, change the **object**, never lower
   the result. (Rejected example: a long water jug → a round igloo. The
   igloo got an exercise ball instead.)
4. **Buildable and AI-friendly.** Real steps, one action per clip, 3–4 clips
   per project for Format A, 5–7 for Format B. Avoid tiny precise hand work,
   text on objects, crowds and complex liquids.
5. **Original:** change at least the object or the result compared with any
   reference.

Generate about 14 candidates, then pick 8 that **pass the variety rules** and
score best.

**Score each idea from 1 to 5 on:**
- **Proof:** reference or vidIQ evidence
- **Hook:** whether the first frame stops the scroll
- **Ease:** how convincingly it can be generated
- **Payoff:** how satisfying the ending is
- **Luxury:** how wanted the result is

Rank by the total.

## 5. Save

Write `ideas/shortlist-YYYY-MM-DD.md` with these parts:
1. **What's working:** reference projects and vidIQ patterns, with numbers.
2. **Ideas table:** #, category, format A/B, dream result, object → method
   (shape line), build place → reveal place, payoff, title, score.
3. **A variety check line,** e.g. "7 categories · 6 payoffs · 5 reveal places · pet-wildlife 1".
4. **Compilations:** named 3-project groups from the A ideas.
5. **Recommended next:** 1 compilation or 1–2 singles, with reasons.

Append every idea to `ideas/log.md` with status `proposed` and a tag line in
the idea text:
`[cat:<key> · <build>→<reveal> · payoff:<type> · fmt:<A|B>]`
Update the pointer at the top of `ideas/ideas.md`.

## 6. Report

Keep it short:
- the biggest patterns
- the 8 ideas, one line each with category and payoff
- the variety check line
- your recommendation
- the link to the shortlist file

Then ask which idea or compilation to make, and stop. When the user picks or
rejects an idea, update its status in the log, with a short reason for
rejections.
