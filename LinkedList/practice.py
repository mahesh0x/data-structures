# Definition for singly-linked list.
from typing import List, Optional

import linked_list_helper


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a Node with a random pointer (Copy List with Random Pointer).
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # 1. Reverse Linked List
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

    # 2. Merge Two Sorted Lists
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass

    # 3. Linked List Cycle
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass

    # 4. Reorder List
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Do not return anything, modify head in-place instead."""
        pass

    # 5. Remove Nth Node From End of List
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        pass

    # 6. Copy List with Random Pointer
    def copyRandomList(self, head: Optional["Node"]) -> Optional["Node"]:
        pass

    # 7. Add Two Numbers
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass

    # 8. Find the Duplicate Number
    def findDuplicate(self, nums: List[int]) -> int:
        pass

    # 10. Merge k Sorted Lists
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        pass

    # 11. Reverse Nodes in k-Group
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        pass


# 9. LRU Cache
class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


def list_to_values(head):
    """Serialize a linked list back to a plain values list so list-returning methods
    can be compared against an expected list instead of by object identity."""
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values


def build_cyclic(values, pos):
    """Build a list and connect the tail's next to the node at index `pos`
    (pos = -1 means no cycle), so hasCycle can be tested both ways."""
    helper = linked_list_helper.LinkedListHelper()
    head = helper.build_list(values)
    if pos < 0 or not head:
        return head
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    nodes[-1].next = nodes[pos]
    return head


def run_tests():
    helper = linked_list_helper.LinkedListHelper()
    sl = Solution()
    tests = []

    def test_reverse_list():
        head = helper.build_list([1, 2, 3, 4, 5])
        assert list_to_values(sl.reverseList(head)) == [5, 4, 3, 2, 1]
    tests.append(("1. reverseList", test_reverse_list))

    def test_merge_two_lists():
        a = helper.build_list([1, 2, 4])
        b = helper.build_list([1, 3, 4])
        assert list_to_values(sl.mergeTwoLists(a, b)) == [1, 1, 2, 3, 4, 4]
    tests.append(("2. mergeTwoLists", test_merge_two_lists))

    def test_has_cycle_true():
        head = build_cyclic([3, 2, 0, -4], pos=1)
        assert sl.hasCycle(head) is True
    tests.append(("3. hasCycle (cycle)", test_has_cycle_true))

    def test_has_cycle_false():
        head = build_cyclic([1, 2], pos=-1)
        assert sl.hasCycle(head) is False
    tests.append(("3. hasCycle (no cycle)", test_has_cycle_false))

    def test_reorder_list():
        head = helper.build_list([1, 2, 3, 4, 5])
        sl.reorderList(head)  # in-place
        assert list_to_values(head) == [1, 5, 2, 4, 3]
    tests.append(("4. reorderList", test_reorder_list))

    def test_remove_nth():
        head = helper.build_list([1, 2, 3, 4, 5])
        assert list_to_values(sl.removeNthFromEnd(head, 2)) == [1, 2, 3, 5]
    tests.append(("5. removeNthFromEnd", test_remove_nth))

    def test_copy_random_list():
        # 1 -> 2, with 1.random -> 2 and 2.random -> 2
        a, b = Node(1), Node(2)
        a.next = b
        a.random = b
        b.random = b
        copy = sl.copyRandomList(a)
        # deep copy: distinct objects, same values and same random topology
        assert copy is not a
        assert copy.val == 1 and copy.next.val == 2
        assert copy.random is copy.next
        assert copy.next.random is copy.next
    tests.append(("6. copyRandomList", test_copy_random_list))

    def test_add_two_numbers():
        l1 = helper.build_list([2, 4, 3])  # 342
        l2 = helper.build_list([5, 6, 4])  # 465
        assert list_to_values(sl.addTwoNumbers(l1, l2)) == [7, 0, 8]  # 807
    tests.append(("7. addTwoNumbers", test_add_two_numbers))

    def test_find_duplicate():
        assert sl.findDuplicate([1, 3, 4, 2, 2]) == 2
    tests.append(("8. findDuplicate", test_find_duplicate))

    def test_lru_cache():
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1
        cache.put(3, 3)          # evicts key 2
        assert cache.get(2) == -1
        cache.put(4, 4)          # evicts key 1
        assert cache.get(1) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4
    tests.append(("9. LRUCache", test_lru_cache))

    def test_merge_k_lists():
        lists = [
            helper.build_list([1, 4, 5]),
            helper.build_list([1, 3, 4]),
            helper.build_list([2, 6]),
        ]
        assert list_to_values(sl.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    tests.append(("10. mergeKLists", test_merge_k_lists))

    def test_reverse_k_group():
        head = helper.build_list([1, 2, 3, 4, 5])
        assert list_to_values(sl.reverseKGroup(head, 2)) == [2, 1, 4, 3, 5]
    tests.append(("11. reverseKGroup", test_reverse_k_group))

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
    values = [1, 2, 3, 4, 5]
    helper = linked_list_helper.LinkedListHelper()
    head = helper.build_list(values)
    helper.print_list(head)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(list_to_values(sl.reverseList(head)))

    print()
    run_tests()
