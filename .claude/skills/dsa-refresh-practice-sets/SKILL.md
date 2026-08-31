---
name: dsa-refresh-practice-sets
description: Update the mixed cross-topic revision sets at this repo's root (practice_set_*.py) when a new NeetCode topic folder is added, or spin up a whole new mixed set. Use whenever the practice sets need to reflect a topic they don't cover yet, or the user wants another set to revise from — e.g. "add graphs to my practice sets", "refresh the practice sets", "I added a new topic, update the sets", "make another mixed practice set", "the sets don't include tries yet". This maintains the root-level practice_set_1.py / practice_set_2.py / … and PRACTICE_SETS.md, NOT the per-topic folders (that's dsa-new-topic).
---

# Refresh Mixed Practice Sets

This repo has per-topic study folders (`Tree/`, `Heap/`, …) and, at the root, a set of
**mixed revision sets** — `practice_set_1.py`, `practice_set_2.py`, … — each pulling one
medium/hard problem from *every* topic plus one extra Hard highlight, so a single sitting
exercises the whole toolbox. This skill keeps those mixed sets in sync as the repo grows.
The companion skill `dsa-new-topic` creates the per-topic folders; this one maintains the
cross-topic sets on top of them. Never invent problems or signatures here — the topic
folders are the single source of truth, so read from them.

## Before anything: read the current state

1. Read `PRACTICE_SETS.md` (the index) and every `practice_set_*.py` at the root.
2. Read `practice_helpers.py` — the shared `TreeNode`/`ListNode` + `build_tree`/`build_list`/
   `tree_to_list`/`list_to_values`/`find_node` builders the sets import. Reuse it; only add
   to it if a genuinely new build/serialize primitive is needed (e.g. a new custom node type).
3. List the topic folders (each PascalCase dir with a `practice.py`) to see the full topic
   set, including any newly added since the sets were last refreshed.

## Step 1 — Figure out the true problem pool per topic (from the folders, never hardcoded)

For each topic folder, open its `practice.py` and read the **real** method names, parameter
names, and return types already stubbed there — including class-design problems (`MinStack`,
`TimeMap`, `KthLargest`, `Twitter`, `MedianFinder`, `LRUCache`, …) which are declared as their
own classes, not `Solution` methods. That stubbed file is authoritative; it already went
through `dsa-new-topic`'s live-verification, so don't re-fetch or second-guess signatures.

Then classify each problem's difficulty (Easy / Medium / Hard) by its well-known LeetCode
rating — cross-check against your own knowledge; only WebSearch if you're genuinely unsure.
The sets draw **only from Medium and Hard** problems. Keep a per-topic list of the eligible
(medium/hard) problems and their exact signatures.

## Step 2 — Know what's already used, so sets never repeat

Scan the existing `practice_set_*.py` files and build the set of problems each one already
contains (match by method name / class name). The invariant across the whole family of sets:
**no problem appears in two sets.** When you pick problems in Step 3, pick from each topic's
*unused* medium/hard pool first. Only if a topic's medium/hard pool is exhausted (every one
already lives in some set) may you either reuse the least-recently-used one or skip that topic
for the new row — and if you do, say so explicitly to the user.

## Step 3 — Pick the operation: extend existing sets, or add a new set

Confirm with the user which they want (default to **extend** if they just said "a new topic
was added / refresh the sets"):

- **Extend (default when a topic was added):** every existing set is currently missing the new
  topic. Add one row (one method, or one design-class) for the new topic to *each* existing set,
  choosing a *different* unused medium/hard problem from that topic for each set so they stay
  distinct. If the topic has fewer eligible problems than there are sets, distribute what exists
  and leave the remaining sets without that topic (noting it). This keeps a fixed number of sets,
  each one growing to stay comprehensive.
- **New set (when the user wants more to revise from):** create `practice_set_<N+1>.py` picking
  one unused medium/hard problem per topic plus one Hard highlight, exactly mirroring the shape
  of the existing sets. `N` = current highest set number + 1.

If both apply (a topic was added *and* the user wants a fresh set), do the extend first so the
new set can also include the new topic.

## Step 4 — Write, matching the existing set files exactly

Mirror the structure of the current `practice_set_*.py` files (read one as the template):

- A module docstring listing which problem each topic contributes, and the copy-to-revise note.
- Imports: `from typing import ...` and `from practice_helpers import (...)` — only the
  builders that set actually uses. Import a topic's design-class problems as normal (they're
  defined *in this file*, like `MinStack`, since the sets are self-contained).
- Any class-design problems declared as their own top-level classes above `Solution`
  (following how the topic folder declares them), with stubbed methods.
- One `Solution` class with every non-class problem as a stubbed method: exact LeetCode method
  name, real parameter/return types, a one-line comment naming the topic and problem
  (`# Stack — Daily Temperatures`), body `pass`. Preserve a stable ordering (topic order).
- **Method-name collisions:** two problems can share a LeetCode method name (the classic case is
  Binary Search's `search` and Search-in-Rotated's `search`). Within one set, two methods can't
  share a name — if a collision would occur, keep the real name for one and rename the other with
  a comment noting LeetCode's real name (mirror how `BinarySearch/practice.py` handles it). When
  a name is unique within the set, always use the real LeetCode name.
- Order-insensitive comparison helpers where a problem returns unordered structure
  (`normalize_triples` for 3Sum, `normalize_groups` for Group Anagrams, `normalize_points` for
  K Closest Points, etc.) — copy them from the existing sets / topic files verbatim.
- A `run_tests()` with **one test per problem**, each building a small input (via
  `practice_helpers` builders for tree/linked-list problems, plain literals otherwise), calling
  the stub, and asserting the known-correct answer — reuse the exact expected values already
  encoded in that problem's own topic-folder `practice.py`, so the harness stays trustworthy.
  Then the same loop as every other file: `AssertionError` → `FAIL`, other → `ERROR`, else
  `PASS`, printing `{passed}/{len(tests)} passed`.
- An `if __name__ == "__main__": run_tests()` block.

The file must import cleanly and run as-is from the repo root, every test `FAIL`/`ERROR` against
the `pass` stubs — that's the point, it's a self-checking sheet to fill in later.

## Step 5 — Update the index and smoke-test

1. Update `PRACTICE_SETS.md`: add the new topic's row to the comparison table (extend case) or a
   new `Set N` column, and refresh the distinct-problem count in the closing line.
2. Run each changed/created set from the root (`python3 practice_set_X.py`) and confirm it imports
   and prints `0/<n> passed` with only FAIL/ERROR lines — no `ImportError`/`SyntaxError`. Report
   the result.

## Step 6 — Confirm before writing

Briefly tell the user the plan first: which operation (extend vs. new set), which specific
problem each set will gain (or the full lineup of the new set), and call out anything forced —
a topic whose medium/hard pool ran out, or a method-name collision you had to rename.
