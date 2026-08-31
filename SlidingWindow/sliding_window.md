# Sliding Window

Sliding Window is the pattern for "find the best/valid contiguous stretch of an array or string." It's really a specialized two-pointer technique where both pointers move in the *same* direction and the region between them — the window — is the thing you're reasoning about. The reason it deserves its own section is that the hard part isn't the pointers, it's the bookkeeping: knowing exactly when the window is valid, and updating your running state in O(1) as the window's edges move so the whole thing stays O(n) instead of collapsing back into an O(n·k) recount.

## The single most important mental habit: "when do I grow the window, and when do I shrink it?"

Before writing any sliding-window code, answer one question: "My `right` pointer always moves forward to include new elements — but under what condition do I move `left` forward to *evict* elements from the left?"

That shrink condition is the entire problem. There are two shapes:

- **Grow until invalid, then shrink until valid again** (variable-size window). You expand `right` greedily; the moment the window breaks a constraint (a duplicate character, too many replacements needed, a missing required character), you advance `left` to repair it. Longest Substring Without Repeating Characters, Longest Repeating Character Replacement, and Minimum Window Substring all live here.
- **Fixed-size window that slides** (size `k` is given). `right` and `left` move together keeping a constant width; you just add the entering element and remove the leaving one each step. Permutation in String and Sliding Window Maximum live here.

If you can state the shrink condition in one sentence before coding, you're done thinking. If you can't, you don't yet know what makes the window valid — and that's the actual problem.

## The two templates

**Variable-size window (expand right, contract left on violation):**

```python
left = 0
state = {}                       # whatever you need to test validity in O(1)
best = 0
for right in range(len(s)):
    # add s[right] to state
    while window_is_invalid(state):
        # remove s[left] from state
        left += 1
    best = max(best, right - left + 1)   # or min, for "shortest valid window"
return best
```

The single subtlety: for "longest valid" you record the answer *after* repairing; for "shortest valid" (Minimum Window Substring) you record *while* the window is valid, and shrink to try to make it even smaller.

**Fixed-size window (slide a width-k frame):**

```python
for right in range(len(nums)):
    # add nums[right]
    if right >= k:
        # remove nums[right - k]  (the element falling out of the left edge)
    if right >= k - 1:
        # window [right-k+1 .. right] is full — record its answer
```

## Techniques you'll reuse

**Keep a frequency map of the current window.** Most string-window problems track counts of characters currently inside `[left, right]`. Growing adds one; shrinking subtracts one (and deletes the key when it hits zero). Validity is a check against that map.

**Track "what makes this window valid" as a single number, not a rescan.** The move that keeps sliding window O(n): don't recompute the window's property from scratch each step. For Longest Repeating Character Replacement, keep `max_freq` (the count of the most common char in the window); the window is valid while `window_size - max_freq <= k`. For Permutation in String, keep a `matches` counter of how many of the 26 letters have exactly the right count, and update it by ±1 as characters enter and leave — so validity is an O(1) `matches == 26` check.

**A monotonic deque for window max/min.** Sliding Window Maximum is the odd one out: a frequency map won't give you the max in O(1). Instead keep a deque of *indices* whose values are decreasing; the front is always the current max. When a new element enters, pop smaller elements off the back (they can never be the max while this bigger one is in the window); when the front index falls outside the window, pop it off the front.

```python
from collections import deque
dq = deque()                     # holds indices, values decreasing front->back
for right in range(len(nums)):
    while dq and nums[dq[-1]] < nums[right]:
        dq.pop()
    dq.append(right)
    if dq[0] <= right - k:       # front index slid out of the window
        dq.popleft()
    if right >= k - 1:
        # nums[dq[0]] is the max of the current window
```

**Best Time to Buy and Sell Stock is a window in disguise.** `left` = buy day, `right` = sell day; if `price[right] < price[left]`, move `left` to `right` (a cheaper buy day); otherwise the profit is `price[right] - price[left]`. It's the gentlest introduction to the two-pointer sweep.

## Pattern groups in NeetCode 150's sliding-window section

1. **Single-pass min/max sweep** — Best Time to Buy and Sell Stock. Track the minimum seen so far and the best profit against it; barely a window, but the same left/right instinct.
2. **Longest-valid variable window** — Longest Substring Without Repeating Characters, Longest Repeating Character Replacement. Expand right, shrink left on violation, record the max width after repair. The second adds the `max_freq` trick.
3. **Fixed-size anagram/permutation window** — Permutation in String. Slide a width-`len(s1)` window over `s2`, keeping character counts (or a `matches` counter) and checking for an exact match.
4. **Shortest-valid variable window** — Minimum Window Substring. The mirror image of group 2: grow until the window *covers* all required characters, then shrink from the left as far as you can while it still covers, recording the minimum. The trickiest bookkeeping in the section.
5. **Monotonic-deque window** — Sliding Window Maximum. A separate technique entirely; the deque of decreasing indices is the thing to memorize.

## Suggested order to attack them

1. Best Time to Buy and Sell Stock (the gentlest left/right sweep)
2. Longest Substring Without Repeating Characters (first real variable window)
3. Longest Repeating Character Replacement (add the `max_freq`-in-window trick)
4. Permutation in String (switch to a fixed-size window with count matching)
5. Sliding Window Maximum (learn the monotonic deque)
6. Minimum Window Substring (the boss: shortest-valid window with have/need counting)

By the time you reach Minimum Window Substring, the "grow right, shrink left, keep validity as one number" loop from problems 2–3 will be automatic, and you'll only be adding the have/need counter on top of a loop shape you already trust.

One practical tip: before coding, write two comments — `# window is valid when: ...` and `# shrink from the left when: ...`. Filling in those two blanks is 90% of every problem in this section; the pointer mechanics are the same every time.
