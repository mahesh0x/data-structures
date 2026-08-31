import tree_helper
from collections import deque

class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def preorder(root):
    if not root:
        return None
    
    res = []
    def dfs(node):
        if not node:
            return
        
        # ROOT
        res.append(node.val)

        # LEFT
        dfs(node.left)

        # RIGHT
        dfs(node.right)

    dfs(root)

    return res


def inorder(root):

    res = []
    if not root:
        return res
    
    def dfs(node):
        if not node:
            return 
        
        # LEFT 
        dfs(node.left)

        # ROOT
        res.append(node.val)

        # RIGHT
        dfs(node.right)

    dfs(root)
    return res


def postorder(root):

    res = []
    if not root:
        return res
    
    def dfs(node):
        if not node:
            return 
        
        # LEFT 
        dfs(node.left)

        # RIGHT
        dfs(node.right)

        # ROOT
        res.append(node.val)

    dfs(root)
    return res


def level_order(root):
    if not root:
        return None
    
    queue = deque([root])
    res = []
    while queue:
        curr_length = len(queue)
        curr_level = []
        for i in range(curr_length):
            node = queue.popleft()
            curr_level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        res.append(curr_level)

    return res

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)


helper = tree_helper.TreeHelper()
print(helper.print_tree(root))

res = preorder(root)
print(res)

res = inorder(root)
print(res)


res = postorder(root)
print(res)

res = level_order(root)
print(res)