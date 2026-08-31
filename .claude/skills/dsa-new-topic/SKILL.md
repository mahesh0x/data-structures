---
name: dsa-new-topic
description: Scaffold a new NeetCode 150 section in this repo the same way Tree/ was built — a teaching markdown doc written in a specific voice, a practice.py with every problem in that section stubbed out as an empty placeholder method, and (only when the topic genuinely has one) a shared build/print helper. Use this whenever the user wants to start studying a new NeetCode 150 category and there's no folder for it yet — e.g. "let's do linked lists next", "set up graphs like we did for tree", "create a heap folder", "start backtracking", or they name any NeetCode 150 topic (arrays & hashing, two pointers, sliding window, stack, binary search, linked list, tries, heap/priority queue, backtracking, graphs, advanced graphs, 1-D DP, 2-D DP, greedy, intervals, math & geometry, bit manipulation).
---

# New NeetCode 150 Topic

This repo is a personal NeetCode 150 study tracker. Each section gets its own folder (e.g. `Tree/`) containing a teaching doc, a stubbed practice file, and — where it genuinely makes sense — a shared helper module. `Tree/` is the reference implementation; read `Tree/tree.md`, `Tree/tree_helper.py`, and `Tree/practice.py` before generating anything, since the goal is to match their voice and shape exactly, not reinvent them.

## Step 1 — Confirm the topic and folder name

Map the user's request to one of NeetCode 150's actual category names (Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary Search, Linked List, Trees, Tries, Heap / Priority Queue, Backtracking, Graphs, Advanced Graphs, 1-D DP, 2-D DP, Greedy, Intervals, Math & Geometry, Bit Manipulation). If ambiguous, ask.

Use a short PascalCase folder name in the same spirit as `Tree/` (e.g. `LinkedList/`, `Graphs/`, `Heap/`, `Tries/`, `Backtracking/`). Check whether the folder already exists before creating it — don't clobber existing work.

## Step 2 — Get the real problem list, don't invent it

NeetCode 150's list is fixed and well known, but don't trust a hardcoded list baked into this skill — it can drift. Before generating anything, verify the exact problem set and current LeetCode-style method signatures for the requested category, using WebSearch/WebFetch against a reliable source (neetcode.io's roadmap, or the well-known NeetCode 150 GitHub lists). Cross-check names and signatures against what you already know; if a fetch fails, fall back to your own knowledge but flag to the user that you couldn't verify it live so they can sanity-check the list.

Get this right: the whole point of `practice.py` is that every method in it corresponds to a real problem the user will actually solve later, with a signature that matches what LeetCode expects.

## Step 3 — Decide if this topic needs a shared helper

`Tree/tree_helper.py` exists because trees have one canonical way to build/print a test structure that's reused across every problem in the section. That's true for a few other sections but not most:

- **Linked List** — genuinely benefits from a helper: `build_list(values) -> ListNode` and `print_list(head)`, mirroring `build_tree`/`print_tree`'s shape.
- **Graphs / Advanced Graphs** — the input shape varies a lot per problem (grid of islands vs. adjacency list vs. weighted edges), so a single shared helper usually doesn't fit cleanly. It's fine to skip a dedicated helper file here and build sample inputs inline per solved file, the way most NeetCode graph solutions do. Only add a helper if there's a genuinely common shape (e.g. `build_adjacency_list(n, edges)`) worth reusing.
- **Tries** — the trie itself *is* the first problem (Implement Trie), so there's nothing to pre-build. Skip the helper.
- **Heap / Priority Queue** — Python's `heapq` operates on plain lists directly; no custom node or helper needed. Skip it.
- **Everything else** (Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary Search, Backtracking, 1-D/2-D DP, Greedy, Intervals, Math & Geometry, Bit Manipulation) — these are technique categories over plain lists/strings/ints, not custom data structures. No helper file at all.

When a helper is warranted, name it `<topic>_helper.py` and give it a class with `build_x`/`print_x` methods, following `tree_helper.py`'s style (a plain `deque`-based level-order build from a values list with `None` gaps, and a print that renders the structure readably).

## Step 4 — Write `<topic>.md`

Match `Tree/tree.md`'s voice and structure exactly:

1. Opening paragraph framing why this section is worth building real pattern recognition in.
2. The core structure/data type as a code block (skip this if the topic has no custom type — e.g. Greedy or Sliding Window just operate on arrays).
3. One core-habit / mental-model section — the single question or reframing that unlocks most problems in this category, the way "the recursive contract" does for trees. Every NeetCode topic has one of these (e.g. for sliding window: "when do I shrink vs. grow the window"; for backtracking: "choose, explore, un-choose"; for graphs: "am I visiting nodes or edges, and do I need a visited set or can I mutate in place").
4. A technique/pattern-family section with short code snippets — the equivalent of the DFS/BFS traversal rundown in tree.md.
5. "Pattern groups" — group the section's actual problem list into 4-6 clusters by shared technique, exactly like tree.md's numbered list (1. Simple bottom-up combine, 2. BFS/level order family, etc.), naming the real problems in each cluster.
6. A suggested attack order — numbered list of the section's real problems, sequenced easy-to-hard / foundational-to-advanced.
7. Closing practical tip — one concrete habit to build while grinding the section (tree.md's is "write what your function returns before writing code").

## Step 5 — Write `practice.py`

Follow `Tree/practice.py` line for line in spirit:

- Import the helper module if one exists (`import <topic>_helper`), plus `typing` imports as needed.
- Redefine the node/structure class locally if the topic has one (matching what the helper module defines — this mirrors how every solved Tree file redeclares `TreeNode` locally even though `tree_helper.py` also has it).
- One `Solution` class containing every problem in the section as a method: real LeetCode method name, real parameter/return types, a one-line numbered comment above each (`# 3. Diameter of Binary Tree`), and just `pass` as the body. Preserve NeetCode's problem order within the file (this canonical file order can differ from the teaching/attack order in `<topic>.md` — that's expected).
- Any generic comparison/lookup helpers the section's tests need to check results by value rather than by object identity. `Tree/practice.py` has `tree_to_list` (serialize a returned tree back to LeetCode list form, trailing `None`s trimmed) and `find_node` (BFS lookup so a test can pass a real node into methods like `lowestCommonAncestor`). Include the equivalents when the topic returns structures rather than plain values (e.g. Linked List needs a `list_to_values`); skip them for pure value-returning topics.
- A `run_tests()` function that mirrors `Tree/practice.py`: build a `tests` list of `(name, test_fn)` pairs — **one test per problem**, each building a small input (via the helper if there is one), calling the stubbed method, and `assert`-ing the expected answer; then loop the tests catching `AssertionError` → `FAIL`, other exceptions → `ERROR`, else `PASS`, and print a final `{passed}/{len(tests)} passed`. The tests encode the correct answers so the file is a self-checking harness once the user fills in the stubs.
- An `if __name__ == "__main__":` block that builds one small sample input (via the helper if there is one, otherwise a plain list/string/int literal), prints or displays it, instantiates `Solution`, shows one commented-out example call, then calls `run_tests()`.

This file is meant to be copied to `practice_1.py` (or similar) and filled in during a revision session — it must import cleanly and run as-is with no implementations yet (every test will `FAIL`/`ERROR` against the `pass` stubs until the user implements each method, which is the point).

## Step 6 — Confirm before writing

Since this touches new files across a repo, briefly tell the user what you're about to create (folder name, whether a helper is included and why/why not, doc + practice file) before writing, especially if a folder with that name already partially exists.
