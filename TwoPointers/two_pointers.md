# Two Pointers

Two Pointers is a small section — five problems — but it's one of the highest-leverage patterns in the whole list, because it's the trick that turns an O(n²) scan into an O(n) sweep without spending any extra memory. Nearly every two-pointer problem is the same physical picture: two indices walking a line, and the only real decision is *which one moves next and why*. Once that decision rule is clear in your head, the code writes itself.

## The single most important mental habit: "which pointer moves, and what does moving it buy me?"

Before writing any two-pointer code, answer one question: "At each step, based on comparing the two ends, which pointer should I advance — and why is it *safe* to throw away the element I'm moving past?"

That word *safe* is the whole pattern. A two-pointer solution works only because every time you move a pointer inward, you can prove you're not skipping a better answer. In Container With Most Water you move the shorter wall in, because the shorter wall is the bottleneck — keeping it and shrinking the width can never help. In sorted Two Sum you move `left` up when the sum is too small, because every pair using the current `left` with a smaller partner is also too small. If you can articulate *why moving past this element loses nothing*, you have the solution; if you can't, two pointers probably isn't the right tool.

## The two flavors of "two pointers"

**Converging (opposite ends).** `left` starts at 0, `right` at the end; they walk toward each other until they meet. This is for sorted arrays and palindromes — anywhere the comparison of the two ends tells you which side to move.

```python
left, right = 0, len(arr) - 1
while left < right:
    if some_condition(arr[left], arr[right]):
        left += 1
    else:
        right -= 1
```

**Same-direction (fast/slow, or a fixed anchor with a moving partner).** Both pointers start near the front; one advances faster or the inner pointer sweeps while an outer one anchors. 3Sum uses this: fix one element with an outer loop, then run a converging two-pointer pair on the rest.

The converging flavor dominates this section. The mental cue: **sorted input + "find a pair/triple" almost always means two pointers**, because sorting is what makes "move past this and never regret it" provable.

## Techniques you'll reuse

**Skip duplicates by advancing while equal.** In problems that must return *unique* results (3Sum), after you record an answer, slide the pointer past any repeats so you don't emit the same triple twice:

```python
while left < right and nums[left] == nums[left + 1]:
    left += 1
```

**Sort first when order doesn't matter.** 3Sum and sorted Two Sum both depend on sorted input. If the problem returns *values* (not original indices) and asks for pairs/triples summing to a target, sorting is usually step one — it's what unlocks the converging sweep.

**Track a running best as the window changes.** Container With Most Water and Trapping Rain Water both walk two pointers inward while keeping a max/accumulated total. The area/water at each step is a function of the two current heights and the gap between the pointers.

**Precompute or track max-so-far from both sides.** Trapping Rain Water is the hard one: water above each bar is `min(max_left, max_right) - height`. The two-pointer version tracks `left_max` and `right_max` as the pointers converge, always moving the side whose max is smaller — because that side is the one that *bounds* the water.

## Pattern groups in NeetCode 150's two-pointers section

1. **Palindrome / character walk** — Valid Palindrome. Converging pointers from both ends, skipping non-alphanumerics, comparing lowercased characters. No sorting; the string order *is* the structure.
2. **Sorted-pair search** — Two Sum II. Converging pointers; sum too small → move `left` up, too big → move `right` down. The cleanest illustration of "moving is safe."
3. **Fixed anchor + inner sweep** — 3Sum. Sort, then for each index run a Two-Sum-II converging pair on the remainder, skipping duplicates on all three positions.
4. **Area / geometry between two walls** — Container With Most Water, Trapping Rain Water. Converging pointers where the answer at each step is a geometric function of the two heights; always move the limiting (shorter / smaller-max) side.

## Suggested order to attack them

1. Valid Palindrome (get the converging-pointer muscle memory with no math)
2. Two Sum II - Input Array Is Sorted (the canonical "which side moves" decision)
3. 3Sum (compose Two Sum II inside an outer loop + duplicate skipping)
4. Container With Most Water (introduce the "move the limiting side" idea on areas)
5. Trapping Rain Water (the boss: two-sided maxes + move-the-smaller-side, the hardest to derive)

By the time you reach Trapping Rain Water, the "move the limiting side, and prove it's safe" reasoning from Container With Most Water will make the water-bounding argument click instead of feeling arbitrary.

One practical tip: before coding, write a one-line comment stating your move rule as an if/else in plain English — e.g. `# sum < target: left++ (need bigger); sum > target: right-- (need smaller)`. If you can't fill in the "why" after each branch, you don't yet understand the problem well enough to code it.
