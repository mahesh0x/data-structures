# Binary Search

Binary search is the "throw away half the possibilities every step" pattern, and its whole value is turning O(n) into O(log n). The mechanics are trivial — a `left`, a `right`, a `mid`, and a decision to go one way or the other — but this section is deceptively hard, because the real skill isn't binary-searching a sorted array (that's problem one). It's recognizing binary search when the array *isn't* the thing you're searching over: when it's a rotated array, a 2D grid, or an abstract range of *answers* like "eating speeds." The pattern is the same three lines every time; the art is figuring out what you're halving and which direction "the answer must be over there" points.

## The single most important mental habit: "can I rule out half the search space with one check?"

Before writing any binary-search code, answer one question: "If I probe the middle of my range and look at it, can I prove the answer lies entirely in the left half *or* entirely in the right half?"

If you can make that proof, you can binary search — even if the input isn't a plainly sorted array. That's the leap this section is built to teach. On a rotated array, the trick is that *one side of `mid` is always sorted*, so you can test whether the target falls in that sorted side and eliminate the other. On Koko Eating Bananas, you're not searching the array at all — you're binary-searching over the *answer* (possible eating speeds 1…max), and the "can she finish in time at this speed?" check is monotonic (faster is always at-least-as-good), which is exactly what lets you halve the candidate speeds. **When the space of possible answers is monotonic — some threshold splits "no" from "yes" — you can binary search it even with no array in sight.**

## The core template (and the boundary trap)

```python
left, right = 0, len(nums) - 1        # inclusive bounds
while left <= right:                  # <= because both ends are valid candidates
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1                # answer is strictly right of mid
    else:
        right = mid - 1               # answer is strictly left of mid
return -1
```

The two things that cause 90% of binary-search bugs, so decide them *before* you type:

1. **Are your bounds inclusive or exclusive?** Pick `left <= right` with `right = len-1` (inclusive) and stick to it. Mixing conventions is how you get off-by-ones and infinite loops.
2. **Does `mid` move to `mid+1`/`mid-1` or stay at `mid`?** Whenever a branch keeps `mid` as a *candidate* (common in "find the minimum / find the boundary" problems), make sure the range still shrinks each iteration, or you loop forever.

## The pattern families

**Classic search on a sorted array.** Binary Search, and Search a 2D Matrix (treat the grid as one flat sorted array of length `rows*cols`, mapping a flat index back with `divmod(mid, cols)`).

**Binary search on the answer space.** Koko Eating Bananas. You don't search the piles; you search speeds `1…max(piles)`. For a candidate speed, compute hours needed (`sum(ceil(p/speed))`); "fits in `h` hours" is monotonic in speed, so binary search for the smallest speed that fits.

```python
left, right = 1, max(piles)
while left < right:
    mid = (left + right) // 2
    if hours_needed(mid) <= h:        # this speed works — try slower
        right = mid
    else:                             # too slow — must go faster
        left = mid + 1
return left                           # smallest speed that fits
```

**Rotated / partially-sorted arrays.** Find Minimum in Rotated Sorted Array and Search in Rotated Sorted Array. The invariant: at any `mid`, either `[left..mid]` or `[mid..right]` is fully sorted. Determine which half is sorted, check whether your target (or the minimum) lies within that sorted half's range, and recurse into the correct side.

**Binary search as a building block in a design problem.** Time Based Key-Value Store. Each key stores an append-only, timestamp-sorted list of `(timestamp, value)`; `get(key, t)` binary-searches that list for the largest timestamp `<= t`. (A class-design problem, not a one-off function.)

**Two sorted arrays, log time.** Median of Two Sorted Arrays. The famously hard one: binary-search a *partition point* in the smaller array such that everything left of the combined partition is `<=` everything to its right; the median falls out of the four boundary elements.

## Pattern groups in NeetCode 150's binary-search section

1. **Plain sorted search** — Binary Search, Search a 2D Matrix. Standard template; the 2D one just flattens the index.
2. **Search-on-answer (monotonic predicate)** — Koko Eating Bananas. Binary search the range of possible answers using a "does this candidate work?" check that flips from no to yes exactly once.
3. **Rotated array** — Find Minimum in Rotated Sorted Array, Search in Rotated Sorted Array. Identify the sorted half at each `mid` and eliminate the other. Do Find Minimum first — it's the same idea with a simpler goal.
4. **Design with an internal binary search** — Time Based Key-Value Store. Store sorted `(timestamp, value)` per key and binary-search for the floor timestamp.
5. **Partition search (the boss)** — Median of Two Sorted Arrays. Binary-search a partition of the smaller array; the correct partition balances left/right halves across both arrays.

## Suggested order to attack them

1. Binary Search (nail the template and the boundary conventions)
2. Search a 2D Matrix (same template, flattened index)
3. Koko Eating Bananas (the mental shift: search the answer space, not the array)
4. Find Minimum in Rotated Sorted Array (learn the "which half is sorted" test)
5. Search in Rotated Sorted Array (apply that test to find a target)
6. Time Based Key-Value Store (binary search as a component in a design problem)
7. Median of Two Sorted Arrays (the hardest — partition search)

Do problems 4 and 5 back-to-back: Find Minimum teaches the "one half is always sorted" invariant with a simpler objective, and Search in Rotated is that exact same reasoning aimed at a target instead of the minimum.

One practical tip: before writing the loop, write two comments — `# search space: [what left and right represent]` and `# I move left/right when: [the proof that the answer is on the other side]`. Especially for the answer-space and rotated problems, being explicit about *what you're halving* and *why the eliminated half can't contain the answer* is the difference between a clean solution and an infinite loop.
