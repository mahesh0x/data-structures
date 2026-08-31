# Definition for a binary tree node.
from collections import deque
from typing import List, Optional

import tree_helper


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 1. Invert Binary Tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass

    # 2. Maximum Depth of Binary Tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pass

    # 3. Diameter of Binary Tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        pass

    # 4. Balanced Binary Tree
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        pass

    # 5. Same Tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass

    # 6. Subtree of Another Tree
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pass

    # 7. Lowest Common Ancestor of a BST
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        pass

    # 8. Binary Tree Level Order Traversal
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    # 9. Binary Tree Right Side View
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        pass

    # 10. Count Good Nodes in Binary Tree
    def goodNodes(self, root: TreeNode) -> int:
        pass

    # 11. Validate Binary Search Tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pass

    # 12. Kth Smallest Element in a BST
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pass

    # 13. Construct Binary Tree from Preorder and Inorder Traversal
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass

    # 14. Binary Tree Maximum Path Sum
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pass

    # 15. Serialize and Deserialize Binary Tree
    def serialize(self, root: Optional[TreeNode]) -> str:
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        pass


def tree_to_list(root):
    """Serialize back to LeetCode list form (with trailing Nones trimmed) so tree-returning
    methods can be compared against an expected list instead of by object identity."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def find_node(root, val):
    """BFS lookup by value, so tests can grab a real node reference to pass into
    methods like lowestCommonAncestor that take TreeNode args rather than values."""
    if not root:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.val == val:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None


def run_tests():
    helper = tree_helper.TreeHelper()
    sl = Solution()
    tests = []

    def test_invert_tree():
        root = helper.build_tree([4, 2, 7, 1, 3, 6, 9])
        result = sl.invertTree(root)
        assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]
    tests.append(("1. invertTree", test_invert_tree))

    def test_max_depth():
        root = helper.build_tree([3, 9, 20, None, None, 15, 7])
        assert sl.maxDepth(root) == 3
    tests.append(("2. maxDepth", test_max_depth))

    def test_diameter():
        root = helper.build_tree([1, 2, 3, 4, 5])
        assert sl.diameterOfBinaryTree(root) == 3
    tests.append(("3. diameterOfBinaryTree", test_diameter))

    def test_balanced_true():
        root = helper.build_tree([3, 9, 20, None, None, 15, 7])
        assert sl.isBalanced(root) is True
    tests.append(("4. isBalanced (balanced case)", test_balanced_true))

    def test_balanced_false():
        root = helper.build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
        assert sl.isBalanced(root) is False
    tests.append(("4. isBalanced (unbalanced case)", test_balanced_false))

    def test_same_tree_true():
        p = helper.build_tree([1, 2, 3])
        q = helper.build_tree([1, 2, 3])
        assert sl.isSameTree(p, q) is True
    tests.append(("5. isSameTree (same)", test_same_tree_true))

    def test_same_tree_false():
        p = helper.build_tree([1, 2])
        q = helper.build_tree([1, None, 2])
        assert sl.isSameTree(p, q) is False
    tests.append(("5. isSameTree (different)", test_same_tree_false))

    def test_is_subtree():
        root = helper.build_tree([3, 4, 5, 1, 2])
        sub = helper.build_tree([4, 1, 2])
        assert sl.isSubtree(root, sub) is True
    tests.append(("6. isSubtree", test_is_subtree))

    def test_lca_bst():
        root = helper.build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 2)
        q = find_node(root, 8)
        result = sl.lowestCommonAncestor(root, p, q)
        assert result.val == 6
    tests.append(("7. lowestCommonAncestor (BST)", test_lca_bst))

    def test_level_order():
        root = helper.build_tree([3, 9, 20, None, None, 15, 7])
        assert sl.levelOrder(root) == [[3], [9, 20], [15, 7]]
    tests.append(("8. levelOrder", test_level_order))

    def test_right_side_view():
        root = helper.build_tree([1, 2, 3, None, 5, None, 4])
        assert sl.rightSideView(root) == [1, 3, 4]
    tests.append(("9. rightSideView", test_right_side_view))

    def test_good_nodes():
        root = helper.build_tree([3, 1, 4, 3, None, 1, 5])
        assert sl.goodNodes(root) == 4
    tests.append(("10. goodNodes", test_good_nodes))

    def test_valid_bst_true():
        root = helper.build_tree([2, 1, 3])
        assert sl.isValidBST(root) is True
    tests.append(("11. isValidBST (valid)", test_valid_bst_true))

    def test_valid_bst_false():
        root = helper.build_tree([5, 1, 4, None, None, 3, 6])
        assert sl.isValidBST(root) is False
    tests.append(("11. isValidBST (invalid)", test_valid_bst_false))

    def test_kth_smallest():
        root = helper.build_tree([3, 1, 4, None, 2])
        assert sl.kthSmallest(root, 1) == 1
    tests.append(("12. kthSmallest", test_kth_smallest))

    def test_build_tree():
        result = sl.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        assert tree_to_list(result) == [3, 9, 20, None, None, 15, 7]
    tests.append(("13. buildTree", test_build_tree))

    def test_max_path_sum():
        root = helper.build_tree([-10, 9, 20, None, None, 15, 7])
        assert sl.maxPathSum(root) == 42
    tests.append(("14. maxPathSum", test_max_path_sum))

    def test_serialize_deserialize():
        root = helper.build_tree([1, 2, 3, None, None, 4, 5])
        data = sl.serialize(root)
        result = sl.deserialize(data)
        assert tree_to_list(result) == tree_to_list(root)
    tests.append(("15. serialize/deserialize", test_serialize_deserialize))

    passed = 0
    for name, test_fn in tests:
        try:
            test_fn()
        except AssertionError:
            print(f"FAIL   {name}")
        except Exception as e:
            print(f"ERROR  {name}: {type(e).__name__}: {e}")
        else:
            print(f"PASS   {name}")
            passed += 1

    print(f"\n{passed}/{len(tests)} passed")


if __name__ == "__main__":
    values = [3, 9, 20, None, None, 15, 7]
    helper = tree_helper.TreeHelper()
    root = helper.build_tree(values)
    helper.print_tree(root)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.maxDepth(root))

    print()
    run_tests()
