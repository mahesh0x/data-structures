# Linked Lists

Linked lists are the section where a small number of pointer moves, done carefully, solve almost everything. Unlike trees, there's no recursion-heavy theory here — the whole game is *manipulating `next` pointers without losing track of the list*. Once you're comfortable with three or four core maneuvers (reverse, two-pointer, dummy head, fast/slow), every problem in this section becomes a recombination of them. Let me walk you through the maneuvers first, then map them to the actual problems.

## The core structure

A singly linked list node is just:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

That's it — a value and a pointer to the next node. Everything you do comes down to reading `node.next`, saving it before you overwrite it, and relinking. The entire difficulty of linked list problems is *not losing a pointer you still need*.

## The single most important mental habit: draw the pointers and save before you overwrite

Before writing any linked list code, draw three or four nodes as boxes with arrows, and physically trace what each pointer points to *after* every line. The number one bug in this section is `a.next = b` clobbering the only reference you had to the old `a.next`. So the reflex to build is:

```python
nxt = curr.next   # save what you're about to lose
curr.next = prev  # now it's safe to overwrite
prev = curr       # walk forward
curr = nxt
```

That four-line dance *is* list reversal, and it's the most reused block in the whole section. If you can write it without thinking, half the problems fall.

## The 30-second mental check (do this before writing anything)

When a linked list problem lands in front of you, ask three quick questions to pick your maneuvers:

1. **Can the head itself change, move, or get removed? →** allocate a **dummy head** in front so you never special-case the first node (maneuver #2). Merges and removals almost always want this.
2. **Do I need the middle, a position relative to the end, or to detect a cycle? →** reach for **two pointers** — fast/slow for middle and cycles, or a fixed-gap leader/follower for "nth from the end" (maneuvers #3 and #4).
3. **Am I about to overwrite a `next` I still need? →** **save it first** (`nxt = curr.next`) before relinking — this is the reversal dance and the source of nearly every bug in the section.

These three cover most of what you'll see; the maneuvers below are the deeper version of each.

## The maneuvers — know these cold

**1. Reverse (in-place pointer flip)** — the four-line dance above. Returns the new head (`prev`).

```python
def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

**2. Dummy head** — when the head itself might change or get removed, allocate a fake node in front so you never special-case "what if it's the first node." Return `dummy.next` at the end. Essential for merges and removals.

```python
dummy = ListNode(0, head)
# ... build off `dummy` ...
return dummy.next
```

**3. Fast & slow pointers (Floyd's)** — advance one pointer two steps for every one step of the other. Fast reaches the end when slow is at the middle; and if there's a cycle, fast eventually laps slow and they meet. This one trick powers cycle detection, finding the middle, and the duplicate-number problem.

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is now at the middle; if fast/slow ever equal → cycle
```

**4. Two-pointer gap** — advance one pointer `n` steps ahead, then move both together; when the leader hits the end, the follower sits exactly `n` from the end. This is how you remove the nth node from the end in one pass.

## Pattern groups in NeetCode 150's linked list section

1. **Pure pointer surgery** — Reverse Linked List, Merge Two Sorted Lists. The foundational maneuvers: the reversal dance, and weaving two lists with a dummy head. Everything else builds on these.
2. **Fast & slow pointer** — Linked List Cycle, Find the Duplicate Number. Floyd's tortoise-and-hare: detect a cycle in a list, or (cleverly) treat an array as a linked list to find its repeated value in O(1) space.
3. **Multi-maneuver combos** — Reorder List, Remove Nth Node From End of List. These chain the primitives: Reorder = find middle (fast/slow) + reverse second half + merge; Remove Nth = two-pointer gap + dummy head. If you can decompose them into "find middle, then reverse, then merge," they stop being scary.
4. **Rebuild while traversing** — Add Two Numbers, Copy List with Random Pointer. You walk the input(s) and construct a brand-new list as you go. Add Two Numbers carries digits with a dummy head; Copy with Random Pointer needs a hashmap from old node → new node (or the clever interleaving trick) so the `random` pointers land right.
5. **Hard / composite** — Merge K Sorted Lists, Reverse Nodes in K-Group, LRU Cache. The boss fights. Merge K Sorted uses a heap (or divide-and-conquer over pattern-1 merges); Reverse in K-Group applies the reversal dance to fixed-size windows with careful reconnection; LRU Cache combines a hashmap with a doubly linked list for O(1) get/put.

## Suggested order to attack them

1. Reverse Linked List (drill the four-line dance until it's automatic)
2. Merge Two Sorted Lists (learn the dummy head)
3. Linked List Cycle (learn fast & slow)
4. Reorder List (first combo: middle + reverse + merge)
5. Remove Nth Node From End of List (two-pointer gap + dummy)
6. Copy List with Random Pointer (hashmap old→new)
7. Add Two Numbers (build-as-you-go with carry)
8. Find the Duplicate Number (Floyd's applied to an array — the sneaky one)
9. Merge K Sorted Lists (heap, or divide-and-conquer over #2)
10. Reverse Nodes in K-Group (reversal dance on windows)
11. LRU Cache (hashmap + doubly linked list — a mini design problem)

By the time you reach #9-11, the reversal dance and the dummy-head reflex from the first two problems will make the "boss fights" feel like assembly rather than invention.

One practical tip: when you're stuck, **draw the list on paper with 4-5 nodes and step a real pen through your pointer moves, one line at a time**. Linked list bugs are almost never logic errors — they're a pointer you overwrote before you were done with it, and you'll see it instantly on paper long before a debugger would show you.
