import tree_helper

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, prev_val=None):
            if not node:
                return True
            
            dfs(node.left, prev_val)

            if not prev_val:
                prev_val = node.val
            else:
                if node.val < prev_val:
                    return False

            dfs(node.right, prev_val)

        return dfs(root) != False

values = [2,1,3]
helper = tree_helper.TreeHelper()
root = helper.build_tree(values)
helper.print_tree(root)

sl = Solution()
res = sl.isValidBST(root)
print(res)