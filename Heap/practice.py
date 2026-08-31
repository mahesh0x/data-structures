import heapq
from typing import List


# 1. Kth Largest Element in a Stream
# A design problem: hold a size-k min-heap across calls so its root is always the
# k-th largest element seen so far; add() pushes, evicts down to k, and returns the root.
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


# 6. Design Twitter
# A design problem: a follow graph (userId -> set of followees) plus per-user tweets
# tagged with a global timestamp; getNewsFeed heap-merges the 10 most recent tweets
# from the user and everyone they follow.
class Twitter:
    def __init__(self):
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass


# 7. Find Median from Data Stream
# A design problem: a max-heap of the lower half and a min-heap of the upper half,
# kept balanced so findMedian reads the median off the heap tops in O(1).
class MedianFinder:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


class Solution:
    # 2. Last Stone Weight
    def lastStoneWeight(self, stones: List[int]) -> int:
        pass

    # 3. K Closest Points to Origin
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass

    # 4. Kth Largest Element in an Array
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass

    # 5. Task Scheduler
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass


def normalize_points(points):
    """Order-insensitive form for K Closest Points: sort the returned points so a correct
    answer compares equal regardless of the order the heap happened to emit them in."""
    return sorted([list(p) for p in points])


def run_tests():
    sl = Solution()
    tests = []

    def test_kth_largest_stream():
        kl = KthLargest(3, [4, 5, 8, 2])
        assert kl.add(3) == 4
        assert kl.add(5) == 5
        assert kl.add(10) == 5
        assert kl.add(9) == 8
        assert kl.add(4) == 8
    tests.append(("1. KthLargest (stream)", test_kth_largest_stream))

    def test_last_stone_weight():
        assert sl.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    tests.append(("2. lastStoneWeight", test_last_stone_weight))

    def test_k_closest():
        result = sl.kClosest([[1, 3], [-2, 2]], 1)
        assert normalize_points(result) == [[-2, 2]]
        result2 = sl.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
        assert normalize_points(result2) == normalize_points([[3, 3], [-2, 4]])
    tests.append(("3. kClosest", test_k_closest))

    def test_find_kth_largest():
        assert sl.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
        assert sl.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    tests.append(("4. findKthLargest", test_find_kth_largest))

    def test_least_interval():
        assert sl.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
        assert sl.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    tests.append(("5. leastInterval", test_least_interval))

    def test_design_twitter():
        tw = Twitter()
        tw.postTweet(1, 5)
        assert tw.getNewsFeed(1) == [5]
        tw.follow(1, 2)
        tw.postTweet(2, 6)
        assert tw.getNewsFeed(1) == [6, 5]
        tw.unfollow(1, 2)
        assert tw.getNewsFeed(1) == [5]
    tests.append(("6. Twitter", test_design_twitter))

    def test_median_finder():
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        assert mf.findMedian() == 1.5
        mf.addNum(3)
        assert mf.findMedian() == 2.0
    tests.append(("7. MedianFinder", test_median_finder))

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
    stones = [2, 7, 4, 1, 8, 1]
    print(stones)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.lastStoneWeight(stones))

    print()
    run_tests()
