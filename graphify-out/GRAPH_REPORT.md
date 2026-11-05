# Graph Report - maximodecimo-designs  (2026-11-04)

## Corpus Check
- 20 files · ~14,342 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1 file(s) not represented in the graph (top: (none) 1)

## Summary
- 103 nodes · 276 edges · 14 communities (7 shown, 7 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `cd26af9d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- arched
- sys
- lib.py
- mockups.py
- random
- d_snow_zoomies_sweatshirt.py
- math
- b64
- doc
- sticker
- d_ornament_xmas.py
- README.md
- d_tree_farm_poster.py

## God Nodes (most connected - your core abstractions)
1. `fit_size()` - 13 edges
2. `text()` - 12 edges
3. `render()` - 12 edges
4. `svg()` - 11 edges
5. `b64()` - 11 edges
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
- `mtbc()` --calls--> `fit_size()`  [EXTRACTED]
  sources/d_engineers.py → sources/lib.py

## Import Cycles
- None detected.

## Communities (14 total, 7 thin omitted)

### Community 1 - "sys"
Cohesion: 0.25
Nodes (6): bubbly_line(), multicolor(), word(), esc(), font(), text_width()

### Community 4 - "mockups.py"
Cohesion: 0.38
Nodes (3): card(), esc(), wrap()

### Community 5 - "random"
Cohesion: 0.43
Nodes (6): mug(), ornament(), pine_sprig(), poster(), table_scene(), wood_grain()

### Community 6 - "d_snow_zoomies_sweatshirt.py"
Cohesion: 0.39
Nodes (5): saw_failure(), build(), dog(), fit_size(), svg()

### Community 7 - "math"
Cohesion: 0.14
Nodes (4): pine(), snow(), square(), star_path()

### Community 10 - "doc"
Cohesion: 0.67
Nodes (4): blanket(), doc(), pillow(), sofa()

### Community 11 - "sticker"
Cohesion: 0.50
Nodes (4): garment(), gift_box(), shadow_of(), sticker()

## Knowledge Gaps
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `arched()` connect `arched` to `sys`, `lib.py`, `d_ornament_xmas.py`, `math`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Should `math` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Why does `dog()` connect `d_snow_zoomies_sweatshirt.py` to `random`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **Why does `card()` connect `mockups.py` to `b64`, `doc`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._