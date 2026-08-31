"""Mixed revision set 1 — one medium/hard problem per NeetCode topic, plus a hard highlight.

Copy this to practice_set_1_copy.py and fill in the stubs during a revision session.
Runs as-is: every test FAILs against the `pass` stubs until you implement each method.

    Arrays & Hashing : Product of Array Except Self
    Two Pointers     : 3Sum  +  Trapping Rain Water (hard)
    Sliding Window   : Longest Substring Without Repeating Characters
    Stack            : Daily Temperatures
    Binary Search    : Koko Eating Bananas
    Heap             : Kth Largest Element in an Array
    Linked List      : Reorder List
    Tree             : Validate Binary Search Tree
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
    # Arrays & Hashing — Product of Array Except Self
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass

    # Two Pointers — 3Sum
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

    # Two Pointers — Trapping Rain Water (hard)
    def trap(self, height: List[int]) -> int:
        pass

    # Sliding Window — Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass

    # Stack — Daily Temperatures
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pass

    # Binary Search — Koko Eating Bananas
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pass

    # Heap — Kth Largest Element in an Array
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass

    # Linked List — Reorder List
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Do not return anything, modify head in-place instead."""
        pass

    # Tree — Validate Binary Search Tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pass


def normalize_triples(triples):
    """Order-insensitive form for 3Sum, so a correct answer compares equal regardless
    of the order it was built in."""
    return sorted(sorted(t) for t in triples)


def run_tests():
    sl = Solution()
    tests = []

    def test_product_except_self():
        assert sl.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    tests.append(("Arrays & Hashing — productExceptSelf", test_product_except_self))

    def test_three_sum():
        result = sl.threeSum([-1, 0, 1, 2, -1, -4])
        assert normalize_triples(result) == normalize_triples([[-1, -1, 2], [-1, 0, 1]])
    tests.append(("Two Pointers — threeSum", test_three_sum))

    def test_trap():
        assert sl.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    tests.append(("Two Pointers — trap (hard)", test_trap))

    def test_length_of_longest_substring():
        assert sl.lengthOfLongestSubstring("abcabcbb") == 3
    tests.append(("Sliding Window — lengthOfLongestSubstring", test_length_of_longest_substring))

    def test_daily_temperatures():
        assert sl.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
            1, 1, 4, 2, 1, 1, 0, 0
        ]
    tests.append(("Stack — dailyTemperatures", test_daily_temperatures))

    def test_min_eating_speed():
        assert sl.minEatingSpeed([3, 6, 7, 11], 8) == 4
    tests.append(("Binary Search — minEatingSpeed", test_min_eating_speed))

    def test_find_kth_largest():
        assert sl.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    tests.append(("Heap — findKthLargest", test_find_kth_largest))

    def test_reorder_list():
        head = build_list([1, 2, 3, 4, 5])
        sl.reorderList(head)  # in-place
        assert list_to_values(head) == [1, 5, 2, 4, 3]
    tests.append(("Linked List — reorderList", test_reorder_list))

    def test_valid_bst():
        assert sl.isValidBST(build_tree([2, 1, 3])) is True
        assert sl.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])) is False
    tests.append(("Tree — isValidBST", test_valid_bst))

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
