from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeHelper:
    def print_tree(self, node, level=0, label="."):
        if not node:
            return
        # Print right subtree first (so it appears at the top right)
        self.print_tree(node.right, level + 1, "/")
        
        # Print current node with indentation
        print("    " * level + f"{label} {node.val}")
        
        # Print left subtree
        self.print_tree(node.left, level + 1, "\\")

    def build_tree(self, values):
        if not values or values[0] is None:
            return None
            
        root = TreeNode(values[0])
        queue = deque([root])
        
        # Start at index 1 because index 0 is the root
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            
            # 1. Process the Left Child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            # 2. Process the Right Child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
            
        return root
        
