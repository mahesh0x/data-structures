# Definition for a binary tree node.

import tree_helper
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, max_val=-101):
            if not node:
                return 
            
            if node.val > max_val:
                self.count += 1
                max_val = node.val

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root)
        return self.count


values = [3,3,None,4,2]
helper = tree_helper.TreeHelper()
root = helper.build_tree(values)

helper.print_tree(root)

sl = Solution()
count = sl.goodNodes(root)
print(count)