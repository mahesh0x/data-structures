# Advanced Graphs

If the Graphs section was about *how to move* through a graph (DFS/BFS), Advanced Graphs is about *what to optimize while you move* — the cheapest way to connect everything, the shortest weighted path, a valid ordering, an unbroken trail. There are only six problems here, but each one is really a named classical algorithm in disguise. The skill to build isn't cleverness — it's **recognition**: reading the problem and instantly knowing "that's Dijkstra," "that's a minimum spanning tree," "that's a topological sort," "that's Eulerian path." Once you can name it, the code writes itself from a template.

## The core structure — weighted graphs and the heap

Almost everything here operates on a **weighted adjacency list**, and almost every shortest-path / MST algorithm here reaches for a **min-heap** (`heapq`) to always expand the cheapest option next:

```python
from collections import defaultdict
import heapq

# weighted adjacency list: node -> list of (neighbor, weight)
adj = defaultdict(list)
for u, v, w in edges:
    adj[u].append((v, w))        # directed; add the reverse too if undirected

# the universal move: a min-heap keyed by cost-so-far
heap = [(0, start)]              # (cost, node)
while heap:
    cost, node = heapq.heappop(heap)   # always pull the cheapest frontier node
    ...
    heapq.heappush(heap, (cost + w, nxt))
```

`heapq` is a plain min-heap over tuples — it sorts by the first element, so you put the thing you want to minimize (distance, edge weight) first. That single pattern powers Dijkstra, Prim, and the "swim" problem.

## The single most important mental habit: "which classical algorithm is this?"

Every problem in this section maps to one named algorithm. Before writing anything, classify:

**"Am I minimizing a total path cost, a total connection cost, finding an ordering, or tracing an unbroken trail?"**

| The problem is about... | The algorithm is... | The tell |
|---|---|---|
| Shortest path from one source, non-negative weights | **Dijkstra** | "minimum time," "cheapest," single start |
| Shortest path with an edge/stop limit | **Bellman-Ford / BFS by layers** | "within K stops" |
| Connect all nodes at minimum total cost | **MST (Prim or Kruskal)** | "connect all points," "minimum cost to link everything" |
| A valid order respecting dependencies | **Topological sort** | "must come before," building an ordering |
| Use every edge exactly once | **Eulerian path (Hierholzer's)** | "use all tickets," "reconstruct the itinerary" |

Getting this classification right in the first 30 seconds is the entire game. The implementations are short; the recognition is the hard part.

## Technique patterns — the named algorithms

**Dijkstra (single-source shortest path, non-negative weights)** — min-heap, pop cheapest, relax neighbors:

```python
def dijkstra(adj, start, n):
    dist = {}
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if node in dist:            # already finalized (lazy deletion)
            continue
        dist[node] = d
        for nxt, w in adj[node]:
            if nxt not in dist:
                heapq.heappush(heap, (d + w, nxt))
    return dist
```

**Prim's MST (grow a tree by always adding the cheapest edge to a new node)** — nearly identical shape to Dijkstra, but the heap key is the *edge weight*, not cumulative distance:

```python
def prim(adj, n):
    visited = set()
    heap = [(0, 0)]                 # (edge_weight, node), start anywhere
    total = 0
    while heap and len(visited) < n:
        w, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        total += w
        for nxt, wt in adj[node]:
            if nxt not in visited:
                heapq.heappush(heap, (wt, nxt))
    return total
```

**Kruskal's MST (sort all edges, add the cheapest that doesn't form a cycle)** — needs Union-Find (from the Graphs section):

```python
edges.sort(key=lambda e: e[2])      # by weight
total = 0
for u, v, w in edges:
    if union(u, v):                 # union returns False if u,v already connected
        total += w
```

**Bellman-Ford / layered BFS (shortest path with at most K edges)** — relax all edges K+1 times; the layer limit is exactly why plain Dijkstra doesn't fit Cheapest Flights:

```python
prices = [float("inf")] * n
prices[src] = 0
for _ in range(k + 1):              # at most k stops = k+1 edges
    tmp = prices[:]                 # freeze this round's values
    for u, v, w in flights:
        if prices[u] + w < tmp[v]:
            tmp[v] = prices[u] + w
    prices = tmp
```

**Hierholzer's algorithm (Eulerian path — use every edge exactly once)** — DFS that appends a node to the route *after* exhausting its edges, then reverse:

```python
def hierholzer(adj, start):         # adj[node] = sorted deque/heap of destinations
    route = []
    stack = [start]
    while stack:
        while adj[stack[-1]]:
            stack.append(adj[stack[-1]].popleft())
        route.append(stack.pop())
    return route[::-1]
```

## Pattern groups in NeetCode 150's advanced graph section

1. **Minimum Spanning Tree (connect everything cheaply)** — Min Cost to Connect All Points. Prim's over a complete graph where edge weight = Manhattan distance between two points (or Kruskal's on all pairs). "Connect all" + "minimum total cost" = MST, every time.
2. **Dijkstra (single-source shortest weighted path)** — Network Delay Time (time for a signal to reach *all* nodes = the max finalized distance), Swim in Rising Water (a Dijkstra variant where a path's cost is the *max* elevation along it, not the sum — so the heap key is `max(cost, elevation)`).
3. **Shortest path with a constraint** — Cheapest Flights Within K Stops. Looks like Dijkstra but the "at most K stops" cap breaks greedy finalization, so it's Bellman-Ford (relax K+1 times) or a BFS that tracks (cost, stops).
4. **Topological sort under uncertainty** — Alien Dictionary (a.k.a. Foreign Dictionary). Derive edges by comparing adjacent words letter by letter (first differing char gives one ordering constraint), then topologically sort the letters; detect cycles (invalid ordering → return "").
5. **Eulerian path (traverse every edge once)** — Reconstruct Itinerary. Use every ticket exactly once, lexicographically smallest — Hierholzer's algorithm with the destinations kept in sorted order.

## Suggested order to attack them

1. Network Delay Time (cleanest Dijkstra — get the min-heap template solid)
2. Min Cost to Connect All Points (Prim's MST — same heap shape, edge-weight key)
3. Swim in Rising Water (Dijkstra variant — path cost is a max, not a sum)
4. Cheapest Flights Within K Stops (Bellman-Ford — why the K limit breaks plain Dijkstra)
5. Reconstruct Itinerary (Eulerian path / Hierholzer's — a new shape entirely)
6. Alien Dictionary / Foreign Dictionary (topological sort + deriving the edges is the hard part)

Do Network Delay Time first even though NeetCode lists Reconstruct Itinerary first — Dijkstra is the foundational template three of these six reuse, and it's the cleanest place to build the heap muscle memory. Save Alien Dictionary for last; the algorithm is a plain topo sort, but *constructing the graph from the word list* (and handling the "prefix" edge case) is the trickiest reasoning in the section.

One practical tip: for every problem here, before touching code, write two lines — the algorithm's name, and what your heap tuple (or DSU / in-degree structure) actually holds, e.g. `# Dijkstra; heap holds (total_time_so_far, node)`. Naming the algorithm and pinning down exactly what you're minimizing is what turns these from "hard" into "type the template."
