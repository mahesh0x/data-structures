# Backtracking

Backtracking is one of the most rewarding sections in NeetCode 150 to build real pattern recognition in, because once the core move clicks, all nine problems collapse into the same three-line template with a different "what counts as a choice" plugged in. There's no custom data structure here — you're just walking a decision tree over a list, string, or grid — so the entire difficulty is figuring out what a "choice" is at each step and when you've reached a complete answer. Let me walk you through the mental model first, then map it to the actual problems.

## The single most important mental habit: choose → explore → un-choose

Every backtracking problem is a depth-first walk over a tree of decisions. At each node you:

1. **Choose** — add a candidate to your current partial solution (`path`).
2. **Explore** — recurse to make the next decision, with that choice in place.
3. **Un-choose** — remove the candidate you just added, so the next iteration of the loop starts from a clean slate.

That third step is the whole game, and it's the one people forget. The reason it works: `path` is a single mutable list shared across the entire recursion, so after you've fully explored everything reachable from a choice, you *must* undo it before trying the next sibling choice — otherwise your state leaks across branches.

```python
def backtrack(start, path):
    if is_complete(path):          # reached a valid full solution
        result.append(path[:])     # append a COPY — path keeps mutating
        return
    for choice in choices(start):  # each option at this step
        path.append(choice)        # choose
        backtrack(next(start), path)  # explore
        path.pop()                 # un-choose
```

Burn two things into muscle memory: **append a copy** (`path[:]`) when you record a solution — if you append `path` itself, every stored answer points at the same list that keeps changing under you — and **every `append` is paired with a `pop`**. If you can write those two lines correctly, you've solved most of this section.

## The 30-second mental check (do this before writing anything)

When a backtracking problem lands in front of you, ask three quick questions to pick your shape:

1. **What is a single "choice" at this step?** — pick/skip an element (subsets), pick any unused element (permutations), pick a candidate ≥ the current index (combinations), pick a letter for a digit (phone). Naming the choice names your `for` loop.
2. **When is `path` a complete solution?** — every node in the tree (subsets: record at *every* call), only at a target sum (combination sum), only when the string is fully consumed (partitioning), only at full length (permutations). This is your base case / record condition.
3. **How do I avoid revisiting / duplicating?** — a `start` index so you never look backward (combinations/subsets), a `used[]` array (permutations), skipping equal siblings on a sorted input (the "II" problems), or marking a cell visited then restoring it (grid DFS). Getting this wrong is where 90% of backtracking bugs live.

## Technique patterns — know these cold

**Pick / skip via a `start` index** — for subsets and combinations, pass a `start` so each recursion only considers elements from `start` onward. This is what stops `[1,2]` and `[2,1]` from both appearing when you only want one.

```python
def backtrack(start, path):
    result.append(path[:])              # subsets: record at every node
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)          # i+1 → never look back
        path.pop()
```

**Use a `used[]` array for permutations** — order matters, so you *can* look backward; you just can't reuse an element already in the current path.

```python
def backtrack(path, used):
    if len(path) == len(nums):
        result.append(path[:]); return
    for i in range(len(nums)):
        if used[i]: continue
        used[i] = True;  path.append(nums[i])
        backtrack(path, used)
        path.pop();      used[i] = False
```

**Skip duplicate siblings (the "II" trick)** — sort the input first, then within a single `for` loop skip any element equal to the previous one, so you don't start two branches with the same value at the same depth:

```python
nums.sort()
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i - 1]:
        continue                        # same value already tried at this depth
    ...
```

**Grid DFS with in-place marking** — for Word Search, "choice" is a direction; mark the current cell (overwrite it or use a visited set) before recursing into neighbors, then restore it on the way out — the un-choose step applied to a 2-D board.

## Pattern groups in NeetCode 150's backtracking section

1. **Subset / combination enumeration (pick-skip with `start`)** — Subsets, Combination Sum. Record at (nearly) every node; a `start` index prevents reordered duplicates. Combination Sum's twist: an element can be reused, so you recurse with `i` instead of `i + 1`.
2. **Permutation enumeration (`used[]`, order matters)** — Permutations. Length is the base case; a `used` array (not a `start` index) governs what's still available.
3. **The "II" duplicate-handling variants** — Subsets II, Combination Sum II. Same skeleton as their non-II versions, but sort the input and skip equal siblings at the same depth so you don't emit the same set twice.
4. **String partitioning / building** — Palindrome Partitioning, Letter Combinations of a Phone Number. Here a "choice" is where to cut the string (partitioning) or which letter maps to the current digit (phone). Base case is "consumed the whole input."
5. **Grid / constraint search with in-place state** — Word Search, N-Queens. The choice is a board position or a queen placement; you mark state, recurse, and restore. N-Queens adds constraint checks (columns and both diagonals) to prune illegal branches early.

## Suggested order to attack them

1. Subsets (learn the pick/skip + `start` template)
2. Combination Sum (same shape, but reuse allowed → recurse with `i`)
3. Permutations (switch to a `used[]` array, order matters)
4. Subsets II (add the sort + skip-duplicate-siblings move)
5. Combination Sum II (combine "II" dedup with the target-sum stop)
6. Letter Combinations of a Phone Number (choices come from a digit→letters map)
7. Palindrome Partitioning (choice = where to cut; prune with an is-palindrome check)
8. Word Search (backtracking on a 2-D grid with in-place marking)
9. N-Queens (constraint pruning with column + diagonal sets — the capstone)

By the time you hit N-Queens, the "choose → recurse → un-choose" loop and the "append a copy at the base case" move will feel automatic; N-Queens is just that same loop wearing three pruning conditions.

One practical tip: before writing any backtracking code, write two one-line comments — `# choice at each step: ...` and `# record when: ...`. Those two sentences pin down your `for` loop and your base case, which is the entire skeleton. Fill in the pruning last.
