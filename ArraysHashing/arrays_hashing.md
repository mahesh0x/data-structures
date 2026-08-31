# Arrays & Hashing

Arrays & Hashing is the first section in NeetCode 150 for a reason: it's where you build the reflex that carries the entire list — "can I trade memory for time by remembering what I've already seen?" Almost every problem here is really a question about which lookup structure to reach for, and once that clicks, half the work is done before you write a loop. There's no custom data structure to learn; the whole section is about wielding Python's `set`, `dict`, and `list` well.

## The single most important mental habit: "have I seen this before?"

Before writing any array/hashing code, ask one question: "As I walk through this array once, what do I need to remember about what I've already passed, so that when I reach the current element I can answer in O(1)?"

That "what do I need to remember" is almost always a `set` (membership: have I seen this value?) or a `dict` (mapping: what index / count / group does this value belong to?). The brute-force version of nearly every problem in this section is a nested double loop — O(n²) — and the hashing version replaces the inner loop with a single O(1) lookup into something you built on the way in. When you catch yourself about to write "for each element, scan the rest of the array," stop: that inner scan is the thing a hash structure removes.

This single habit — turn the inner loop into a lookup — solves most of NeetCode's arrays & hashing section.

## The 30-second mental check (do this before writing anything)

When an arrays problem lands in front of you, ask which of these you need:

1. **Membership / duplicates? →** `set`. "Have I seen this exact value?" (Contains Duplicate, Longest Consecutive Sequence's start-check.)
2. **Counting / frequency? →** `dict` or `collections.Counter`. "How many times does each thing appear?" (Valid Anagram, Top K Frequent, Group Anagrams.)
3. **Remembering *where* something was? →** `dict` mapping value → index. "I need the position of the complement." (Two Sum.)
4. **Grouping things that share a key? →** `defaultdict(list)` keyed by a canonical signature. "Everything with the same sorted letters goes in one bucket." (Group Anagrams.)
5. **No extra structure, just index arithmetic? →** prefix/suffix passes over the array itself. (Product of Array Except Self — the interesting one, because the "no division, no extra hash" constraint forces a different move.)

## Technique / pattern families — know these cold

**Counting with a dict.** The workhorse. Build a frequency map in one pass, then read from it:

```python
from collections import Counter
count = Counter(nums)          # {value: how many times}
count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1
```

Two strings are anagrams iff their Counters are equal — that's the entire Valid Anagram problem.

**Complement lookup (the Two Sum move).** Instead of searching for two things that combine to a target, fix one and look up the *other* one you'd need:

```python
seen = {}                      # value -> index
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i
```

You build the map as you go, so each element only ever looks *backward* at what's already stored — one pass, O(n).

**Canonical key / signature grouping.** When you need to group items that are "the same" under some transformation, compute a key that's identical for all members of a group and bucket by it:

```python
from collections import defaultdict
groups = defaultdict(list)
for s in strs:
    key = tuple(sorted(s))     # or a 26-length count tuple
    groups[key].append(s)
return list(groups.values())
```

**Bucket sort by frequency.** When a problem says "top k most frequent," you don't need a full sort or a heap — frequencies are bounded by `len(nums)`, so you can bucket by count and read from the high end:

```python
freq = [[] for _ in range(len(nums) + 1)]   # freq[c] = values that appear c times
for val, c in Counter(nums).items():
    freq[c].append(val)
# walk freq from the back to collect the k most frequent
```

**Prefix / suffix passes.** Some problems that look like they need a hash are actually solved by walking the array twice — once left-to-right accumulating a running result, once right-to-left — and combining. Product of Array Except Self is the canonical example: prefix products in one pass, suffix products in another, multiply.

## Pattern groups in NeetCode 150's arrays & hashing section

1. **Set membership** — Contains Duplicate. Drop everything in a set (or compare `len(set) != len(list)`); the whole problem is "is there a collision."
2. **Frequency counting** — Valid Anagram, Top K Frequent Elements. Build a Counter; anagram is a Counter-equality check, top-k is bucket-sort-by-count.
3. **Complement / mapping lookup** — Two Sum. Map value → index, look up the complement you still need.
4. **Signature grouping** — Group Anagrams. Bucket strings under a canonical key (sorted letters or a 26-count tuple).
5. **Encoding / design** — Encode and Decode Strings. Serialize a list of strings into one string so it round-trips unambiguously — the trick is a length-prefix delimiter (`"4#word"`) so payloads containing your delimiter don't break decoding.
6. **Index arithmetic / prefix-suffix** — Product of Array Except Self, Valid Sudoku, Longest Consecutive Sequence. These lean on positional structure: prefix/suffix products; row/column/box hashing for Sudoku; and for Longest Consecutive, a set plus the "only start counting from a number whose predecessor is absent" trick to keep it O(n).

## Suggested order to attack them

1. Contains Duplicate (get the set reflex)
2. Valid Anagram (get the Counter reflex)
3. Two Sum (complement lookup — the single most important pattern here)
4. Group Anagrams (canonical-key bucketing)
5. Top K Frequent Elements (bucket sort by frequency)
6. Encode and Decode Strings (length-prefix design)
7. Product of Array Except Self (prefix/suffix, no division)
8. Valid Sudoku (hashing rows/cols/boxes at once)
9. Longest Consecutive Sequence (set + start-of-run trick — the cleverest one, save it for last)

By the time you reach Longest Consecutive Sequence, the "trade memory for a lookup" instinct will be automatic, and its O(n) trick — only expand a run when you're standing on its smallest element — will feel like a natural extension rather than a rabbit out of a hat.

One practical tip: before you write a loop, write a one-line comment naming the structure and what its keys/values *mean* — e.g. `# count: letter -> how many times it appears in s`. Committing to what the map holds before you build it is what turns a vague "I'll use a dict somewhere" into a solution.
