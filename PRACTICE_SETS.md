# Mixed Revision Sets

Cross-topic practice sets for spaced revision. Each set pulls one medium/hard problem
from **every** topic folder, plus one extra **Hard** highlight — a ~9-problem sitting that
touches the whole toolbox instead of drilling a single pattern.

Each set is a self-checking harness (like every `practice.py` in this repo). To revise:

```bash
cp practice_set_1.py practice_set_1_copy.py   # keep the stubs pristine
python3 practice_set_1_copy.py                 # fill in the methods, watch FAIL -> PASS
```

Shared tree/linked-list builders live in `practice_helpers.py` (imported by each set).

## What's in each set

| Topic | Set 1 | Set 2 | Set 3 |
|---|---|---|---|
| Arrays & Hashing | Product of Array Except Self | Longest Consecutive Sequence | Group Anagrams |
| Two Pointers | 3Sum · **Trapping Rain Water** (H) | Container With Most Water | Two Sum II |
| Sliding Window | Longest Substring w/o Repeat | Char Replacement · **Sliding Window Max** (H) | Permutation in String |
| Stack | Daily Temperatures | Evaluate RPN | Min Stack · **Largest Rectangle** (H) |
| Binary Search | Koko Eating Bananas | Search in Rotated Sorted Array | Search a 2D Matrix |
| Heap | Kth Largest in Array | Task Scheduler | K Closest Points to Origin |
| Linked List | Reorder List | Add Two Numbers | Remove Nth Node From End |
| Tree | Validate BST | Kth Smallest in a BST | Lowest Common Ancestor of a BST |

No problem repeats across the three sets, so finishing all three covers 27 distinct
medium/hard problems spanning eight topics.

## Interview-specific sets

Besides the topic-balanced sets above, themed sets drill a specific interview's
predicted problems (grouped by *pattern*, not one-per-topic):

- **`practice_set_coderabbit.py`** — the 15-problem drill from `practice_coderabbit.md`
  (CodeRabbit phone screen, Hawan Lee). Stack-parsing, sliding window, intervals
  (incl. Meeting Rooms I & II), hashmap/heap, LRU Cache design, AST-flavored trees,
  and graphs, plus 3 harder stretch follow-ups. `LRUCache` lives as its own stub class in the file (it's a
  design problem, not a `Solution` method).
