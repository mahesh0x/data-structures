import heapq
from typing import List
from collections import Counter, deque, defaultdict


# 1. Kth Largest Element in a Stream
# A design problem: hold a size-k min-heap across calls so its root is always the
# k-th largest element seen so far; add() pushes, evicts down to k, and returns the root.
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = self.create_heap_with_k_elements(nums, k)
        self.k = k 

    def create_heap_with_k_elements(self, nums, k):
        heapq.heapify(nums)
        if k > len(nums):
            return nums
        else:
            while len(nums) > k:
                heapq.heappop(nums)
            return nums

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        
        return self.heap[0]


# 6. Design Twitter
# A design problem: a follow graph (userId -> set of followees) plus per-user tweets
# tagged with a global timestamp; getNewsFeed heap-merges the 10 most recent tweets
# from the user and everyone they follow.
class Twitter:
    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        self.followers[userId].add(userId)
        heap = []

        for followee_id in self.followers[userId]:
            if followee_id in self.user_tweets:
                index = len(self.user_tweets[followee_id]) - 1
                counter, last_tweet_id = self.user_tweets[followee_id][index]
                heapq.heappush(heap, [counter, last_tweet_id, followee_id, index])

        for i in range(10):
            if not heap:
                break
            
            counter, tweet_id, followee_id, index = heapq.heappop(heap)
            res.append(tweet_id)

            if index > 0:
                index = index - 1
                counter, tweet_id = self.user_tweets[followee_id][index]
                heapq.heappush(heap, [counter, tweet_id, followee_id, index])

        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].remove(followeeId)


# 7. Find Median from Data Stream
# A design problem: a max-heap of the lower half and a min-heap of the upper half,
# kept balanced so findMedian reads the median off the heap tops in O(1).
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2



class Solution:
    # 2. Last Stone Weight
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1 * s for s in stones]
        heapq.heapify(max_heap)

        while True:
            if len(max_heap) <= 1:
                break

            first = -1 * heapq.heappop(max_heap)
            second = -1 * heapq.heappop(max_heap)

            if first != second:
                heapq.heappush(max_heap, -1 * (first - second))
        
        return -1 * max_heap[0] if max_heap else 0

    # 3. K Closest Points to Origin
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            x, y = point
            d = (x**2 + y**2)

            if len(min_heap) < k:
                heapq.heappush(min_heap, (-d, (x,y)))
            else:
                max_val = -min_heap[0][0]
                if d <= max_val:
                    heapq.heapreplace(min_heap, (-d, (x,y)))
            

        res = []
        for i in range(k):
            _, cds = heapq.heappop(min_heap)
            res.append(cds)

        return res

    # 4. Kth Largest Element in an Array
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, 1 * num)
            elif num > heap[0]:
                heapq.heappushpop(heap, num)

        return heap[0]

    # 5. Task Scheduler
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        
        heap = [-1 * v for v in task_counter.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time += 1

            if heap:
                task = heapq.heappop(heap)
                if task + 1 < 0:
                    q.append([task+1, time + n])

            if q and time == q[0][1]:
                task, _ = q.popleft()
                heapq.heappush(heap, task)
            
        return time


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
    # stones = [2, 7, 4, 1, 8, 1]
    # print(stones)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.lastStoneWeight(stones))

    print()
    run_tests()
