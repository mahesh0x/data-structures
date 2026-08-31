class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.is_balanced = True

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            if left_depth == -1:
                return -1
            
            right_depth = dfs(node.right)
            if right_depth == -1:
                return -1

            if abs(left_depth - right_depth) > 1:
                return -1

            return 1 + max(left_depth, right_depth)

        res = dfs(root)  

        return res != -1          



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(5)


sl = Solution()
print(sl.isBalanced(root))