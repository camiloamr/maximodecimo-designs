# Graph Report - maximodecimo-designs  (2026-11-03)

## Corpus Check
- 17 files · ~12,438 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1 file(s) not represented in the graph (top: (none) 1)

## Summary
- 90 nodes · 227 edges · 14 communities (7 shown, 7 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `05190476`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- arched
- lib.py
- mockups.py
- random
- fit_size
- d_pillow_santa.py
- math
- b64
- doc
- sticker
- README.md

## God Nodes (most connected - your core abstractions)
1. `b64()` - 11 edges
2. `fit_size()` - 10 edges
3. `render()` - 9 edges
4. `doc()` - 9 edges
5. `text()` - 8 edges
6. `square()` - 7 edges
7. `font()` - 7 edges
8. `esc()` - 7 edges
9. `arched()` - 7 edges
10. `svg()` - 7 edges

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

## Communities (14 total, 7 thin omitted)

### Community 1 - "arched"
Cohesion: 0.24
Nodes (7): bubbly_line(), multicolor(), word(), arched(), esc(), font(), text_width()

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
Cohesion: 0.53
Nodes (4): pine(), snow(), square(), text()

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

- **Why does `arched()` connect `arched` to `math`, `lib.py`, `d_ornament_xmas.py`, `fit_size`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Should `sys` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Why does `card()` connect `mockups.py` to `b64`, `doc`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `fit_size()` connect `fit_size` to `arched`, `lib.py`, `d_pillow_santa.py`, `math`, `d_ornament_xmas.py`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._