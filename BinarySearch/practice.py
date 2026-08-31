from typing import List


class Solution:
    # 1. Binary Search
    def search(self, nums: List[int], target: int) -> int:
        pass

    # 2. Search a 2D Matrix
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass

    # 3. Koko Eating Bananas
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pass

    # 4. Find Minimum in Rotated Sorted Array
    def findMin(self, nums: List[int]) -> int:
        pass

    # 5. Search in Rotated Sorted Array
    # NOTE: LeetCode names this method `search` too, but that collides with problem 1
    # in a single Solution class, so it's renamed here. The signature is otherwise real.
    def searchRotated(self, nums: List[int], target: int) -> int:
        pass

    # 7. Median of Two Sorted Arrays
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


# 6. Time Based Key-Value Store
# A design problem: store each key's (timestamp, value) pairs in timestamp order and
# binary-search on get() for the largest timestamp <= the queried one.
class TimeMap:
    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


def run_tests():
    sl = Solution()
    tests = []

    def test_search():
        assert sl.search([-1, 0, 3, 5, 9, 12], 9) == 4
        assert sl.search([-1, 0, 3, 5, 9, 12], 2) == -1
    tests.append(("1. search", test_search))

    def test_search_matrix():
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        assert sl.searchMatrix(matrix, 3) is True
        assert sl.searchMatrix(matrix, 13) is False
    tests.append(("2. searchMatrix", test_search_matrix))

    def test_min_eating_speed():
        assert sl.minEatingSpeed([3, 6, 7, 11], 8) == 4
        assert sl.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    tests.append(("3. minEatingSpeed", test_min_eating_speed))

    def test_find_min():
        assert sl.findMin([3, 4, 5, 1, 2]) == 1
        assert sl.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    tests.append(("4. findMin", test_find_min))

    def test_search_rotated():
        assert sl.searchRotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
        assert sl.searchRotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    tests.append(("5. searchRotated", test_search_rotated))

    def test_time_map():
        tm = TimeMap()
        tm.set("foo", "bar", 1)
        assert tm.get("foo", 1) == "bar"
        assert tm.get("foo", 3) == "bar"
        tm.set("foo", "bar2", 4)
        assert tm.get("foo", 4) == "bar2"
        assert tm.get("foo", 5) == "bar2"
        assert tm.get("foo", 0) == ""
    tests.append(("6. TimeMap", test_time_map))

    def test_find_median_sorted_arrays():
        assert sl.findMedianSortedArrays([1, 3], [2]) == 2.0
        assert sl.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    tests.append(("7. findMedianSortedArrays", test_find_median_sorted_arrays))

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
    nums = [-1, 0, 3, 5, 9, 12]
    print(nums)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.search(nums, 9))

    print()
    run_tests()
