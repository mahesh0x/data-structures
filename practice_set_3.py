"""Mixed revision set 3 — one medium/hard problem per NeetCode topic, plus a hard highlight.

Copy this to practice_set_3_copy.py and fill in the stubs during a revision session.
Runs as-is: every test FAILs against the `pass` stubs until you implement each method.

    Arrays & Hashing : Group Anagrams
    Two Pointers     : Two Sum II - Input Array Is Sorted
    Sliding Window   : Permutation in String
    Stack            : Min Stack  +  Largest Rectangle in Histogram (hard)
    Binary Search    : Search a 2D Matrix
    Heap             : K Closest Points to Origin
    Linked List      : Remove Nth Node From End of List
    Tree             : Lowest Common Ancestor of a BST
"""
from typing import List, Optional

from practice_helpers import (
    ListNode,
    TreeNode,
    build_list,
    build_tree,
    find_node,
    list_to_values,
)


# Stack — Min Stack (a design problem: every operation O(1))
class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


class Solution:
    # Arrays & Hashing — Group Anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass

    # Two Pointers — Two Sum II - Input Array Is Sorted
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pass

    # Sliding Window — Permutation in String
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass

    # Stack — Largest Rectangle in Histogram (hard)
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass

    # Binary Search — Search a 2D Matrix
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass

    # Heap — K Closest Points to Origin
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass

    # Linked List — Remove Nth Node From End of List
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        pass

    # Tree — Lowest Common Ancestor of a BST
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        pass


def normalize_groups(groups):
    """Order-insensitive form for Group Anagrams."""
    return sorted(sorted(g) for g in groups)


def normalize_points(points):
    """Order-insensitive form for K Closest Points."""
    return sorted([list(p) for p in points])


def run_tests():
    sl = Solution()
    tests = []

    def test_group_anagrams():
        result = sl.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        assert normalize_groups(result) == normalize_groups(expected)
    tests.append(("Arrays & Hashing — groupAnagrams", test_group_anagrams))

    def test_two_sum():
        assert sl.twoSum([2, 7, 11, 15], 9) == [1, 2]  # 1-indexed
    tests.append(("Two Pointers — twoSum (II)", test_two_sum))

    def test_check_inclusion():
        assert sl.checkInclusion("ab", "eidbaooo") is True
        assert sl.checkInclusion("ab", "eidboaoo") is False
    tests.append(("Sliding Window — checkInclusion", test_check_inclusion))

    def test_min_stack():
        st = MinStack()
        st.push(-2)
        st.push(0)
        st.push(-3)
        assert st.getMin() == -3
        st.pop()
        assert st.top() == 0
        assert st.getMin() == -2
    tests.append(("Stack — MinStack", test_min_stack))

    def test_largest_rectangle_area():
        assert sl.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    tests.append(("Stack — largestRectangleArea (hard)", test_largest_rectangle_area))

    def test_search_matrix():
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        assert sl.searchMatrix(matrix, 3) is True
        assert sl.searchMatrix(matrix, 13) is False
    tests.append(("Binary Search — searchMatrix", test_search_matrix))

    def test_k_closest():
        result = sl.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
        assert normalize_points(result) == normalize_points([[3, 3], [-2, 4]])
    tests.append(("Heap — kClosest", test_k_closest))

    def test_remove_nth():
        head = build_list([1, 2, 3, 4, 5])
        assert list_to_values(sl.removeNthFromEnd(head, 2)) == [1, 2, 3, 5]
    tests.append(("Linked List — removeNthFromEnd", test_remove_nth))

    def test_lca_bst():
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 2)
        q = find_node(root, 8)
        assert sl.lowestCommonAncestor(root, p, q).val == 6
    tests.append(("Tree — lowestCommonAncestor (BST)", test_lca_bst))

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
    run_tests()
