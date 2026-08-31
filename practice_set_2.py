"""Mixed revision set 2 — one medium/hard problem per NeetCode topic, plus a hard highlight.

Copy this to practice_set_2_copy.py and fill in the stubs during a revision session.
Runs as-is: every test FAILs against the `pass` stubs until you implement each method.

    Arrays & Hashing : Longest Consecutive Sequence
    Two Pointers     : Container With Most Water
    Sliding Window   : Longest Repeating Character Replacement  +  Sliding Window Maximum (hard)
    Stack            : Evaluate Reverse Polish Notation
    Binary Search    : Search in Rotated Sorted Array
    Heap             : Task Scheduler
    Linked List      : Add Two Numbers
    Tree             : Kth Smallest Element in a BST
"""
from typing import List, Optional

from practice_helpers import (
    ListNode,
    TreeNode,
    build_list,
    build_tree,
    list_to_values,
)


class Solution:
    # Arrays & Hashing — Longest Consecutive Sequence
    def longestConsecutive(self, nums: List[int]) -> int:
        pass

    # Two Pointers — Container With Most Water
    def maxArea(self, heights: List[int]) -> int:
        pass

    # Sliding Window — Longest Repeating Character Replacement
    def characterReplacement(self, s: str, k: int) -> int:
        pass

    # Sliding Window — Sliding Window Maximum (hard)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass

    # Stack — Evaluate Reverse Polish Notation
    def evalRPN(self, tokens: List[str]) -> int:
        pass

    # Binary Search — Search in Rotated Sorted Array
    # (LeetCode names this `search`; unique within this set so the real name is used.)
    def search(self, nums: List[int], target: int) -> int:
        pass

    # Heap — Task Scheduler
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass

    # Linked List — Add Two Numbers
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass

    # Tree — Kth Smallest Element in a BST
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pass


def run_tests():
    sl = Solution()
    tests = []

    def test_longest_consecutive():
        assert sl.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    tests.append(("Arrays & Hashing — longestConsecutive", test_longest_consecutive))

    def test_max_area():
        assert sl.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    tests.append(("Two Pointers — maxArea", test_max_area))

    def test_character_replacement():
        assert sl.characterReplacement("AABABBA", 1) == 4
    tests.append(("Sliding Window — characterReplacement", test_character_replacement))

    def test_max_sliding_window():
        assert sl.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    tests.append(("Sliding Window — maxSlidingWindow (hard)", test_max_sliding_window))

    def test_eval_rpn():
        assert sl.evalRPN(["2", "1", "+", "3", "*"]) == 9
    tests.append(("Stack — evalRPN", test_eval_rpn))

    def test_search_rotated():
        assert sl.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
        assert sl.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    tests.append(("Binary Search — search (rotated)", test_search_rotated))

    def test_least_interval():
        assert sl.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    tests.append(("Heap — leastInterval", test_least_interval))

    def test_add_two_numbers():
        l1 = build_list([2, 4, 3])  # 342
        l2 = build_list([5, 6, 4])  # 465
        assert list_to_values(sl.addTwoNumbers(l1, l2)) == [7, 0, 8]  # 807
    tests.append(("Linked List — addTwoNumbers", test_add_two_numbers))

    def test_kth_smallest():
        assert sl.kthSmallest(build_tree([3, 1, 4, None, 2]), 1) == 1
    tests.append(("Tree — kthSmallest", test_kth_smallest))

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
