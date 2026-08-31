# Heap / Priority Queue

A heap is the data structure you reach for whenever the phrase "the k-th largest," "the smallest so far," "the most frequent," or "the median as data streams in" shows up. It answers one question extremely fast — *what's the minimum (or maximum) element right now?* — in O(log n) per insert/remove, without keeping the whole collection sorted. The entire section is about training yourself to hear those trigger phrases and reach for a heap instead of re-sorting an array every time the data changes. There's no custom node class to learn; in Python a heap is just a list you only ever touch through `heapq`.

## The core tool: `heapq` on a plain list

Python's `heapq` gives you a **min-heap** built on an ordinary list — the smallest element is always at index 0:

```python
import heapq
h = []
heapq.heappush(h, 5)         # add
heapq.heappush(h, 1)
smallest = h[0]              # peek the min — O(1), does not remove
x = heapq.heappop(h)         # remove & return the min — O(log n)
heapq.heapify(nums)          # turn an existing list into a heap in-place — O(n)
```

Two idioms you'll use constantly:

- **Max-heap by negating.** `heapq` is min-only, so to pop the *largest*, push `-value` and negate again on the way out: `heapq.heappush(h, -x)`, then `-heapq.heappop(h)`.
- **Priority by tuple.** Push `(priority, item)` tuples; the heap orders by the first element (ties broken by the next). This is how you sort points by distance, tasks by count, tweets by timestamp.

## The single most important mental habit: "do I need the extreme element repeatedly, as the data changes?"

Before reaching for a heap, ask: "Am I going to need the min/max *over and over*, while the set of elements keeps shifting under me?"

If you needed the extreme element *once*, you'd just call `max()`. The heap earns its keep only when you need it *repeatedly* on a *changing* collection — pull the smallest, add two more, pull the smallest again. That's the tell. And the sharpest version of this instinct is the **bounded heap for "k-th largest"**: instead of a max-heap of everything, keep a **min-heap of size k**. Its root is the k-th largest, and every time a new element beats the root you pop the root and push the newcomer — the heap never grows past k, giving O(n log k) instead of O(n log n). "Keep a heap of exactly the k things I care about, evicting the weakest" is the pattern that unlocks half this section.

## The pattern families

**Bounded size-k heap ("k-th largest / k closest").** Keep a min-heap capped at k; the root is your answer, and you evict the root whenever something better arrives.

```python
import heapq
def kth_largest(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)     # drop the smallest — keep only the top k
    return h[0]                  # the k-th largest is the min of the top k
```

**Repeated extract-and-reinsert.** Some problems repeatedly pull the top one or two elements, transform them, and push a result back. Last Stone Weight (smash the two heaviest, push the difference) is the canonical shape — a max-heap you drain in a loop.

**Heap of tuples for prioritized selection.** When "priority" is a computed key, push `(key, payload)`. K Closest Points pushes `(distance, point)`; Task Scheduler pushes `-count` to always grab the most frequent remaining task; Design Twitter's feed merges each followee's recent tweets by timestamp.

**Two heaps for a running median.** Find Median from Data Stream keeps a max-heap of the smaller half and a min-heap of the larger half, balanced so their sizes differ by at most one. The median is then either the top of the larger heap or the average of both tops — O(log n) per insert, O(1) per query.

```python
# small = max-heap (negated) of the lower half; large = min-heap of the upper half
# keep len(small) >= len(large) and |len(small) - len(large)| <= 1
```

## Pattern groups in NeetCode 150's heap section

1. **Bounded size-k heap** — Kth Largest Element in a Stream (a *design* problem: hold a size-k min-heap across many `add` calls), Kth Largest Element in an Array, K Closest Points to Origin. All keep a heap capped at k and read/evict the root.
2. **Drain-and-recombine** — Last Stone Weight. A max-heap (via negation) that you repeatedly pop twice, combine, and push back until one or zero elements remain.
3. **Greedy scheduling with counts** — Task Scheduler. Use a max-heap of task frequencies to always run the most common available task, with a cooldown queue holding tasks waiting to become available again.
4. **Design with heaps + hashing** — Design Twitter. Combine a follow graph (hash map of sets) with a heap-merge of followees' recent tweets by timestamp to build each news feed.
5. **Two balanced heaps** — Find Median from Data Stream. A max-heap for the lower half and a min-heap for the upper half, rebalanced on every insert so the median is always at the tops.

## Suggested order to attack them

1. Kth Largest Element in a Stream (the size-k heap idea, in its simplest design form)
2. Last Stone Weight (max-heap via negation, drain-in-a-loop)
3. K Closest Points to Origin (heap of `(distance, point)` tuples)
4. Kth Largest Element in an Array (bounded size-k heap on a static array)
5. Task Scheduler (heap + cooldown; greedy scheduling)
6. Design Twitter (heap-merge inside a larger design problem)
7. Find Median from Data Stream (the boss: two balanced heaps)

Do problems 1 and 4 close together — they're the same size-k heap idea, one arriving as a stream and one over a fixed array, and seeing them side by side cements when the bounded heap beats a full sort. By the time you reach Find Median, the "a heap gives me the extreme in O(log n)" reflex will be automatic, and the only new idea is running *two* of them.

One practical tip: before coding, write a one-line comment naming your heap and what its root means — e.g. `# min-heap of the k largest seen; root == the k-th largest`. Committing to whether it's a min- or max-heap, whether you're negating, and what the root represents is what turns "I'll use a heap somewhere" into a correct solution.
