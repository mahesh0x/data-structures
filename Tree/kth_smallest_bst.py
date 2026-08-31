import tree_helper
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.node_count = 0

        def dfs(node):
            if not node:
                return None
            
            target_val = dfs(node.left)
            if target_val:
                return target_val

            self.node_count += 1
            print(f"node count: {self.node_count}. node val: {node.val}")
            if self.node_count == k:
                return node.val
            
            target_val = dfs(node.right)
            if target_val:
                return target_val

        
        res = dfs(root)

        return res

values = [4,3,5,2,None]
k = 4
helper = tree_helper.TreeHelper()
root = helper.build_tree(values)
helper.print_tree(root)

sl = Solution()
res = sl.kthSmallest(root, k)
print(res)