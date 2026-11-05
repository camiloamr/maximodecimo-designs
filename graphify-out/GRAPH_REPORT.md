# Graph Report - maximodecimo-designs  (2026-11-05)

## Corpus Check
- 24 files · ~16,461 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1 file(s) not represented in the graph (top: (none) 1)

## Summary
- 118 nodes · 332 edges · 7 communities (5 shown, 2 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a1ad5c23`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- lib.py
- render
- mockups.py
- math
- text
- README.md

## God Nodes (most connected - your core abstractions)
1. `fit_size()` - 17 edges
2. `text()` - 16 edges
3. `render()` - 16 edges
4. `svg()` - 15 edges
5. `b64()` - 11 edges
6. `star_path()` - 10 edges
7. `arched()` - 9 edges
8. `doc()` - 9 edges
9. `esc()` - 8 edges
10. `font()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `mtbc()` --calls--> `render()`  [INFERRED]
  sources/d_engineers.py → sources/lib.py
- `saw_failure()` --calls--> `render()`  [INFERRED]
  sources/d_engineers.py → sources/lib.py
- `face()` --calls--> `fit_size()`  [EXTRACTED]
  sources/d_tree-climbing-season-pillow.py → sources/lib.py
- `mtbc()` --calls--> `svg()`  [EXTRACTED]
  sources/d_engineers.py → sources/lib.py
- `mtbc()` --calls--> `text()`  [EXTRACTED]
  sources/d_engineers.py → sources/lib.py

## Import Cycles
- None detected.

## Communities (7 total, 2 thin omitted)

### Community 1 - "lib.py"
Cohesion: 0.18
Nodes (10): bubbly_line(), mtbc(), saw_failure(), multicolor(), word(), arched(), esc(), fit_size() (+2 more)

### Community 3 - "render"
Cohesion: 0.19
Nodes (5): build(), dog(), render(), snowflake(), svg()

### Community 4 - "mockups.py"
Cohesion: 0.20
Nodes (19): b64(), blanket(), card(), doc(), esc(), garment(), gift_box(), mug() (+11 more)

### Community 7 - "math"
Cohesion: 0.11
Nodes (4): marigold(), P(), petal_ring(), hill()

### Community 12 - "text"
Cohesion: 0.24
Nodes (7): pine(), snow(), square(), face(), tier(), star_path(), text()

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `fit_size()` connect `lib.py` to `render`, `text`, `math`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Should `math` be split into smaller, more focused modules?**
  _Cohesion score 0.10541310541310542 - nodes in this community are weakly interconnected._
- **Why does `arched()` connect `lib.py` to `render`, `text`, `math`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `text()` connect `text` to `lib.py`, `render`, `math`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._