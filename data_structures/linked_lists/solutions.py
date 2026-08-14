"""Linked List — Essential Problem Solutions."""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly linked list in O(1) space."""
    prev: Optional[ListNode] = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def has_cycle(head: Optional[ListNode]) -> bool:
    """Floyd's Cycle-Finding Algorithm (Tortoise and Hare)."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def merge_two_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """Merge two sorted linked lists using a dummy head sentinel."""
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Remove N-th node from end using two-pointer offset sweep."""
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def get_intersection_node(
    head_a: Optional[ListNode], head_b: Optional[ListNode]
) -> Optional[ListNode]:
    """Find intersection node via dual pointer alignment. O(n) time, O(1) space."""
    if not head_a or not head_b:
        return None
    a, b = head_a, head_b
    while a is not b:
        a = a.next if a else head_b
        b = b.next if b else head_a
    return a
