# Graphs

Graphs are where NeetCode 150 stops being about one fixed data structure and starts being about a *way of moving* through data. The nodes might be cells in a grid, courses with prerequisites, or words one edit apart — but the traversal is almost always the same two moves (DFS or BFS) wearing different costumes. Once you stop seeing "island problems" and "course problems" as separate and start seeing them as "the same flood fill on a different input shape," this whole section collapses into a handful of templates.

## The core structure — graphs don't have one shape, they have three

Unlike trees, a graph arrives in one of a few representations, and half the battle is recognizing which one you got:

```python
# 1. Grid (implicit graph): each cell is a node, neighbors are up/down/left/right
grid = [
    ["1", "1", "0"],
    ["1", "0", "0"],
    ["0", "0", "1"],
]

# 2. Adjacency list: node -> list of neighbors (build this from an edge list)
from collections import defaultdict
adj = defaultdict(list)
for u, v in edges:      # undirected: add both directions
    adj[u].append(v)
    adj[v].append(u)

# 3. Node object (like Clone Graph)
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

Your first instinct on any graph problem should be: *what's a node, what's an edge, and which of these three shapes am I in?* Grids are the most common in this section and the ones people under-recognize as graphs at all.

## The single most important mental habit: "have I been here before?"

The one thing that separates a graph traversal from a tree traversal is **cycles**. Trees can't revisit a node; graphs can, and if you don't guard against it you'll loop forever. So before writing any graph code, answer one question:

**"How am I marking a node as visited, and where in the code do I mark it?"**

You have two tools:

- A **`visited` set** (or `seen` dict) — the general answer, works everywhere.
- **Mutating the input in place** — on grids you can often overwrite a visited `"1"` with `"0"` (or `"#"`) instead of carrying a set. Cheaper, but destroys the input, so only do it when the problem lets you.

The classic bug is marking a node visited *after* you process it instead of *when you enqueue/enter it* — that lets the same node get added to your queue multiple times. Mark on entry, every time.

## The 30-second mental check (do this before writing anything)

1. **Do I need the shortest path / fewest steps, or spreading in "waves"? →** BFS with a queue (level by level). "Minimum," "shortest," "fewest," "rotting outward" all scream BFS.
2. **Do I just need to explore a whole connected region / count components / detect a cycle? →** DFS is usually simplest (recursive flood fill), though BFS works too.
3. **Is there a "do X before Y" ordering / dependency? →** topological sort (Course Schedule family) — DFS with cycle detection, or BFS on in-degrees (Kahn's).
4. **Am I merging things into groups / asking "are these two connected"? →** union-find (Redundant Connection, Graph Valid Tree, Connected Components).

## Traversal patterns — know these cold

**DFS flood fill on a grid** — the workhorse for island problems:

```python
def dfs(r, c):
    if (r < 0 or r >= rows or c < 0 or c >= cols
            or grid[r][c] != "1"):
        return
    grid[r][c] = "0"                 # mark visited by mutating
    dfs(r + 1, c); dfs(r - 1, c)
    dfs(r, c + 1); dfs(r, c - 1)
```

**BFS on a grid** — for shortest distance / multi-source spreading:

```python
from collections import deque
q = deque(sources)                   # can seed with MANY starts at once
while q:
    for _ in range(len(q)):          # one "minute"/level at a time
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))
    time += 1
```

The **multi-source BFS** trick (seeding the queue with every start cell before the loop) is the whole idea behind Rotting Oranges and Walls and Gates — don't run one BFS per source, run one BFS from all of them.

**Topological sort (Kahn's / BFS on in-degrees)** — for dependency ordering:

```python
indegree = {n: 0 for n in range(numCourses)}
adj = defaultdict(list)
for course, pre in prerequisites:
    adj[pre].append(course)
    indegree[course] += 1
q = deque([n for n in indegree if indegree[n] == 0])
order = []
while q:
    n = q.popleft()
    order.append(n)
    for nxt in adj[n]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)
# if len(order) < numCourses there was a cycle
```

**Union-Find (Disjoint Set Union)** — for "are these connected / does adding this edge make a cycle":

```python
parent = list(range(n))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]   # path compression
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False                    # already connected -> cycle
    parent[ra] = rb
    return True
```

## Pattern groups in NeetCode 150's graph section

1. **Grid DFS flood fill (connected regions)** — Number of Islands, Max Area of Island. Same move: scan the grid, and every time you hit an unvisited land cell, DFS to sink the whole region. Count regions (islands) or track region size (max area).
2. **Grid BFS / multi-source spreading** — Rotting Oranges, Islands and Treasure (Walls and Gates). Seed the queue with every source cell, then expand level by level counting the number of rounds. Distance = the level at which a cell is reached.
3. **Grid DFS "from the border inward"** — Pacific Atlantic Water Flow, Surrounded Regions. The trick that flips these from hard to easy: instead of asking "can this inner cell escape," start the DFS from the *edges* and mark everything reachable back from them. Two runs (from Pacific edges, from Atlantic edges) and intersect; or one run marking border-connected regions as safe.
4. **Topological sort (dependency ordering + cycle detection)** — Course Schedule (can you finish → is there a cycle?), Course Schedule II (return a valid order). Build adjacency + in-degrees, run Kahn's BFS (or DFS with a recursion-stack visited set). If you can't consume all nodes, there's a cycle.
5. **Union-Find (connectivity & cycle detection on undirected graphs)** — Number of Connected Components, Graph Valid Tree (connected AND exactly n-1 edges AND no cycle), Redundant Connection (the edge that first closes a cycle). All three are the DSU template above; the only difference is what you report.
6. **Adjacency-list graph rebuild / traversal** — Clone Graph (DFS/BFS copying nodes into a `old -> new` map), Word Ladder (BFS over an implicit graph where words one letter apart are neighbors — shortest transformation = shortest path = BFS).

## Suggested order to attack them

1. Number of Islands (learn the grid DFS flood fill)
2. Max Area of Island (same flood fill, now return a size)
3. Clone Graph (DFS/BFS with an old→new hashmap)
4. Islands and Treasure / Walls and Gates (first multi-source BFS)
5. Rotting Oranges (multi-source BFS, count the rounds)
6. Pacific Atlantic Water Flow (DFS inward from the borders)
7. Surrounded Regions (same border trick, marking survivors)
8. Course Schedule (topological sort as cycle detection)
9. Course Schedule II (topological sort, now return the order)
10. Graph Valid Tree (union-find, or connectivity + edge count)
11. Number of Connected Components in an Undirected Graph (union-find count)
12. Redundant Connection (union-find, catch the cycle-closing edge)
13. Word Ladder (BFS on an implicit word graph)

By #8 the DFS/BFS mechanics are automatic and you're really just learning two new tools — topological sort and union-find — that the rest of the section reuses.

One practical tip: on every graph problem, before writing code, write a one-line comment stating your node, your edge, and your visited strategy — e.g. `# node = grid cell, edge = 4-way neighbor, visited = overwrite '1' with '0'`. Getting those three straight up front is 80% of not writing an infinite loop.
