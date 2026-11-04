# Graph Report - maximodecimo-designs  (2026-11-04)

## Corpus Check
- 19 files · ~13,862 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1 file(s) not represented in the graph (top: (none) 1)

## Summary
- 98 nodes · 257 edges · 16 communities (7 shown, 9 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ca5ee2ea`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- sys
- lib.py
- mockups.py
- random
- fit_size
- d_pillow_santa.py
- d_fox_stocking.py
- b64
- doc
- sticker
- README.md
- d_tree_farm_poster.py

## God Nodes (most connected - your core abstractions)
1. `fit_size()` - 11 edges
2. `render()` - 11 edges
3. `b64()` - 11 edges
4. `text()` - 10 edges
5. `svg()` - 9 edges
6. `doc()` - 9 edges
7. `esc()` - 8 edges
8. `arched()` - 8 edges
9. `star_path()` - 8 edges
10. `square()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `saw_failure()` --calls--> `render()`  [INFERRED]
  sources/d_engineers.py → sources/lib.py
- `mtbc()` --calls--> `render()`  [INFERRED]
  sources/d_engineers.py → sources/lib.py
- `bubbly_line()` --calls--> `fit_size()`  [EXTRACTED]
  sources/d_cookie_mug.py → sources/lib.py
- `saw_failure()` --calls--> `text()`  [EXTRACTED]
  sources/d_engineers.py → sources/lib.py
- `mtbc()` --calls--> `arched()`  [EXTRACTED]
  sources/d_engineers.py → sources/lib.py

## Import Cycles
- None detected.

## Communities (16 total, 9 thin omitted)

### Community 1 - "sys"
Cohesion: 0.14
Nodes (6): bubbly_line(), multicolor(), word(), esc(), font(), text_width()

### Community 4 - "mockups.py"
Cohesion: 0.38
Nodes (3): card(), esc(), wrap()

### Community 5 - "random"
Cohesion: 0.43
Nodes (6): mug(), ornament(), pine_sprig(), poster(), table_scene(), wood_grain()

### Community 6 - "fit_size"
Cohesion: 0.47
Nodes (4): mtbc(), saw_failure(), fit_size(), svg()

### Community 7 - "d_pillow_santa.py"
Cohesion: 0.48
Nodes (5): pine(), snow(), square(), star_path(), text()

### Community 10 - "doc"
Cohesion: 0.67
Nodes (4): blanket(), doc(), pillow(), sofa()

### Community 11 - "sticker"
Cohesion: 0.50
Nodes (4): garment(), gift_box(), shadow_of(), sticker()

## Knowledge Gaps
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `arched()` connect `lib.py` to `sys`, `d_ornament_xmas.py`, `fit_size`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `render()` (e.g. with `mtbc()` and `saw_failure()`) actually correct?**
  _`render()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `sys` be split into smaller, more focused modules?**
  _Cohesion score 0.14035087719298245 - nodes in this community are weakly interconnected._
- **Why does `card()` connect `mockups.py` to `b64`, `doc`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **Why does `fit_size()` connect `fit_size` to `sys`, `lib.py`, `d_pillow_santa.py`, `d_fox_stocking.py`, `d_ornament_xmas.py`, `d_tree_farm_poster.py`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._