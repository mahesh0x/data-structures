# Definition for a binary tree node.

import tree_helper
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_path_sum = 0
        def dfs(node):
            if not node:
                return 0 
            

            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            
            curr_path_sum = node.val + left_max + right_max
            self.max_path_sum = max(self.max_path_sum, curr_path_sum)

            return node.val + max(left_max, right_max)
        
        dfs(root)
        return self.max_path_sum


values = [-15,10,20,None,None,15,5,-5]
helper = tree_helper.TreeHelper()
root = helper.build_tree(values)

helper.print_tree(root)

sl = Solution()
count = sl.maxPathSum(root)
print(count)