# NeetCode 150 — Graphs
# No shared helper module: graph inputs vary too much per problem (grids vs.
# adjacency lists vs. edge lists), so each test builds its sample input inline.
from collections import deque
from typing import List, Optional


# Definition for a Node (adjacency-list graph node, used by Clone Graph).
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # 1. Number of Islands
    def numIslands(self, grid: List[List[str]]) -> int:
        pass

    # 2. Max Area of Island
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        pass

    # 3. Clone Graph
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        pass

    # 4. Islands and Treasure (Walls and Gates)
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """Do not return anything, modify grid in-place instead."""
        pass

    # 5. Rotting Oranges
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pass

    # 6. Pacific Atlantic Water Flow
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pass

    # 7. Surrounded Regions
    def solve(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        pass

    # 8. Course Schedule
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass

    # 9. Course Schedule II
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pass

    # 10. Graph Valid Tree
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pass

    # 11. Number of Connected Components in an Undirected Graph
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass

    # 12. Redundant Connection
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pass

    # 13. Word Ladder
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass


def build_graph(adj_list):
    """Build an adjacency-list graph of Node objects from LeetCode's [[neighbors...]] form
    (vals are 1-indexed: row i describes the neighbors of node i+1). Returns the node with
    val 1, or None if empty."""
    if not adj_list:
        return None
    nodes = {i: Node(i) for i in range(1, len(adj_list) + 1)}
    for i, neighbors in enumerate(adj_list, start=1):
        nodes[i].neighbors = [nodes[j] for j in neighbors]
    return nodes[1]


def graph_to_adj_list(node):
    """Serialize a Node graph back to LeetCode [[neighbors...]] form so a returned clone can
    be compared by structure rather than by object identity."""
    if not node:
        return []
    seen = {node.val: node}
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        for nb in cur.neighbors:
            if nb.val not in seen:
                seen[nb.val] = nb
                queue.append(nb)
    return [[nb.val for nb in seen[v].neighbors] for v in sorted(seen)]


def run_tests():
    sl = Solution()
    tests = []

    def test_num_islands():
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        assert sl.numIslands(grid) == 3
    tests.append(("1. numIslands", test_num_islands))

    def test_max_area_of_island():
        grid = [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1],
        ]
        assert sl.maxAreaOfIsland(grid) == 3
    tests.append(("2. maxAreaOfIsland", test_max_area_of_island))

    def test_clone_graph():
        original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
        clone = sl.cloneGraph(original)
        assert clone is not None and clone is not original  # must be a fresh object
        assert graph_to_adj_list(clone) == [[2, 4], [1, 3], [2, 4], [1, 3]]
    tests.append(("3. cloneGraph", test_clone_graph))

    def test_islands_and_treasure():
        INF = 2147483647
        grid = [
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF],
        ]
        sl.islandsAndTreasure(grid)
        assert grid == [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ]
    tests.append(("4. islandsAndTreasure", test_islands_and_treasure))

    def test_oranges_rotting():
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1],
        ]
        assert sl.orangesRotting(grid) == 4
    tests.append(("5. orangesRotting", test_oranges_rotting))

    def test_pacific_atlantic():
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        # order of the returned coordinates isn't specified, so compare as sets
        assert sorted(sl.pacificAtlantic(heights)) == sorted(expected)
    tests.append(("6. pacificAtlantic", test_pacific_atlantic))

    def test_surrounded_regions():
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        sl.solve(board)
        assert board == [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
    tests.append(("7. solve (surrounded regions)", test_surrounded_regions))

    def test_can_finish_true():
        assert sl.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]) is True
    tests.append(("8. canFinish (no cycle)", test_can_finish_true))

    def test_can_finish_false():
        assert sl.canFinish(2, [[0, 1], [1, 0]]) is False
    tests.append(("8. canFinish (cycle)", test_can_finish_false))

    def test_find_order():
        numCourses = 4
        prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
        order = sl.findOrder(numCourses, prereqs)
        # any valid topological order is acceptable, so validate the ordering
        assert len(order) == numCourses and set(order) == set(range(numCourses))
        pos = {c: i for i, c in enumerate(order)}
        assert all(pos[pre] < pos[c] for c, pre in prereqs)
    tests.append(("9. findOrder", test_find_order))

    def test_valid_tree_true():
        assert sl.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    tests.append(("10. validTree (is a tree)", test_valid_tree_true))

    def test_valid_tree_false():
        assert sl.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    tests.append(("10. validTree (has cycle)", test_valid_tree_false))

    def test_count_components():
        assert sl.countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]) == 2
    tests.append(("11. countComponents", test_count_components))

    def test_redundant_connection():
        assert sl.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    tests.append(("12. findRedundantConnection", test_redundant_connection))

    def test_ladder_length():
        assert sl.ladderLength(
            "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
        ) == 5
    tests.append(("13. ladderLength", test_ladder_length))

    passed = 0
    for name, test_fn in tests:
        try:
            test_fn()
        except AssertionError:
            print(f"FAIL   {name}")
        except Exception as e:
            print(f"ERROR  {name}: {type(e).__name__}: {e}")
        else:
            print(f"PASS   {name}")
            passed += 1

    print(f"\n{passed}/{len(tests)} passed")


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    for row in grid:
        print(" ".join(row))

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.numIslands(grid))

    print()
    run_tests()
