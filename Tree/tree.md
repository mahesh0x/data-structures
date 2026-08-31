# Binary Trees

Binary trees are one of the best sections in NeetCode 150 to build real pattern recognition, because almost every problem is a variation on the same handful of templates. Let me walk you through the mental models first, then map them to the actual problems.

## The core structure

A binary tree node is just:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Everything you do with trees comes down to: look at a node, decide what to do with its value, and recurse into `left` and `right`. The entire difficulty of tree problems is figuring out what information to pass down and what information to bubble back up.

## The single most important mental habit: the "recursive contract"

Before writing any tree code, answer one question: "If I had the answer for the left subtree and the right subtree, how would I combine them to get the answer for this node?"

Then trust that the recursion will handle the subtrees for you (this is the leap of faith — don't try to trace through the whole call stack in your head). Write the base case (usually `if not root: return ...`), write the combine step, done.

This single habit solves probably 80% of NeetCode's tree section.

## The 30-second mental check (do this before writing anything)

When a tree problem lands in front of you, ask three quick questions to pick your shape:

1. **Do I need information from my children before I can answer? →** bottom-up, **postorder** (return a value, combine children). See the top-down vs. bottom-up section below.
2. **Do I need to stop as soon as I find the answer? →** lean on **recursion return values to "bubble" the result up** and short-circuit the rest of the traversal (see Kth Smallest / Validate BST in group #3).
3. **Does the root define the structure of what's below it? →** top-down, **preorder** (process root first, then recurse — building, copying, serializing, constructing).

These three cover most of what you'll see; the sections below are the deeper version of each.

## Traversal patterns — know these cold

DFS (recursive), three flavors based on when you "visit" the node:

* **Preorder**: `visit(root) → left → right` — good for copying/serializing a tree, or when you need to pass info down (top-down)
* **Inorder**: `left → visit(root) → right` — the magic one for BSTs, because it visits nodes in sorted order
* **Postorder**: `left → right → visit(root)` — good when you need info from children before you can decide the current node's answer (bottom-up)

BFS (iterative, using a queue): level-by-level traversal. Whenever a problem says "level," "row," or "rightmost/leftmost at each depth," think BFS with a queue immediately.

```python
from collections import deque
def bfs(root):
    if not root: return
    q = deque([root])
    while q:
        level_size = len(q)
        for _ in range(level_size):
            node = q.popleft()
            # process node
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
```

## Top-down vs. bottom-up recursion (this is the real pattern to internalize)

**Bottom-up (postorder-style)**: the node needs answers from its children before it can compute its own answer. The function returns a value.

Example — Maximum Depth of Binary Tree:

```python
def maxDepth(root):
    if not root: return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

This exact shape (return 0 on null, combine children with `+1`/`max`/`min`) reappears in: Maximum Depth, Balanced Binary Tree, Diameter of Binary Tree, Count Good Nodes (with a twist), and Binary Tree Maximum Path Sum. Once you see it once, you'll recognize it everywhere.

**Top-down (preorder-style)**: you pass information down to children as arguments (like a running sum, a depth counter, or a max-so-far), and children use it.

Example — Path Sum:

```python
def hasPathSum(root, target):
    if not root: return False
    if not root.left and not root.right:  # leaf
        return root.val == target
    remaining = target - root.val
    return hasPathSum(root.left, remaining) or hasPathSum(root.right, remaining)
```

A lot of students get stuck because they try to force a bottom-up problem into top-down or vice versa. The tell: if the problem talks about a value accumulating as you go down (path sum, max value seen so far, depth), it's top-down. If it talks about combining what children report back (height, count, balance), it's bottom-up.

## Pattern groups in NeetCode 150's tree section

1. **Simple bottom-up combine** — Invert Binary Tree, Maximum Depth, Diameter of Binary Tree, Balanced Binary Tree, Same Tree, Subtree of Another Tree. All follow: null check → recurse both sides → combine.
2. **BFS / level order family** — Binary Tree Level Order Traversal, Binary Tree Right Side View, Average of Levels. All use the queue template above; the only difference is what you record per level (last element = right side view, average = sum/count, etc).
3. **BST-specific (inorder = sorted)** — Validate Binary Search Tree, Kth Smallest Element in a BST, Lowest Common Ancestor of a BST. The trick: either do an inorder traversal and check it's increasing, or use BST properties (compare val to root, go left or right) instead of full DFS — this makes LCA in a BST O(h) instead of O(n). This group is also where **early termination via bubbling** pays off: for Kth Smallest, keep a counter and the moment you hit the k-th node in inorder order, return that value straight up the call stack so the remaining recursion unwinds without visiting the rest of the tree; for Validate BST, the instant a node violates the bound you return `False` and don't bother checking anything else. The shape is "found it / failed → return immediately, let the answer propagate up."
4. **Path / "root somewhere" problems** — Binary Tree Maximum Path Sum (and, as a warm-up idea, the classic Path Sum shown above, though that one isn't in NeetCode 150's tree set). These require you to be careful about the difference between a path that must go through the root vs. a path that can be anywhere in the tree — this distinction trips people up constantly. For Max Path Sum specifically: your recursive function returns "best path starting at this node going one direction," but at each node you also check (and update a global/nonlocal variable) the best path that bends through both children.
5. **Construction / serialization** — Construct Binary Tree from Preorder and Inorder Traversal, Serialize and Deserialize Binary Tree. Key insight for construction: preorder's first element is always the root; find that value in inorder to split left/right subtree ranges, then recurse. Serialization is usually just preorder DFS with explicit null markers, and deserialization replays that same order using an iterator/queue.
6. **Global-state-during-recursion** — problems like Count Good Nodes where you pass a running max down (top-down) but return a count (needs a helper with an accumulator, or nonlocal counter).

## Suggested order to attack them

1. Invert Binary Tree (get the recursion muscle memory)
2. Maximum Depth of Binary Tree
3. Diameter of Binary Tree
4. Balanced Binary Tree
5. Same Tree / Subtree of Another Tree
6. Binary Tree Level Order Traversal (switch gears to BFS)
7. Binary Tree Right Side View
8. Count Good Nodes in Binary Tree
9. Validate Binary Search Tree
10. Kth Smallest Element in a BST
11. Lowest Common Ancestor of a BST
12. Construct Binary Tree from Preorder and Inorder Traversal
13. Binary Tree Maximum Path Sum
14. Serialize and Deserialize Binary Tree

(That's 15 problems across 14 steps — Same Tree and Subtree of Another Tree are paired in step 5 since they're the same move.)

By the time you hit #13-14, the earlier ones will have made the "return value + combine" and "helper function with extra state" moves feel automatic.

One practical tip: when you're stuck on a new tree problem, explicitly write out in a comment what your function returns and what it means before writing any code — e.g. `# returns: height of subtree rooted at node, or -1 if not balanced`. That one sentence usually reveals the solution shape immediately.
