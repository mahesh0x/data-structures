class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListHelper:
    def build_list(self, values):
        """Build a singly linked list from a values list and return its head.
        Empty list (or [None]) returns None, mirroring build_tree's shape."""
        if not values or values[0] is None:
            return None

        head = ListNode(values[0])
        curr = head
        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def print_list(self, head):
        """Render the list readably as 1 -> 2 -> 3 -> None."""
        parts = []
        curr = head
        while curr:
            parts.append(str(curr.val))
            curr = curr.next
        parts.append("None")
        print(" -> ".join(parts))
