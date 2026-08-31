"""Shared builders/serializers for the mixed revision sets at the repo root.

The per-topic folders each have their own helper (tree_helper, linked_list_helper);
this module gathers the tree + linked-list pieces the cross-topic practice sets need,
so a set file can just `from practice_helpers import ...` instead of reaching into
subfolders. Pure-value topics (arrays, strings, ints) need nothing from here.
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_tree(values):
    """Level-order build from a values list with None gaps (LeetCode's format)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    """Serialize back to LeetCode list form (trailing Nones trimmed) so tree-returning
    methods can be compared by value instead of by object identity."""
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
    """BFS lookup by value, so a test can grab a real node reference to pass into
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


def build_list(values):
    """Build a singly linked list from a values list and return its head."""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def list_to_values(head):
    """Serialize a linked list back to a plain values list for value comparison."""
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values
