# Definition for singly-linked list.
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# use a minheap to store all nodes
# O(nlogn) time, O(n) space
def sortList1(head: Optional[ListNode]) -> Optional[ListNode]:
    minheap = []
    # build the heap
    while head:
        heapq.heappush(minheap, head.val)
        head = head.next
    # recreate the linked list
    dummy = ListNode()
    prev = dummy
    while minheap:
        curr = ListNode(heapq.heappop(minheap))
        prev.next = curr
        prev = curr
    return dummy.next

# refer to merge sort, recursively merge two lists
def merge(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or head.next:
        return head
    # find the middle 
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next # type: ignore
        fast = fast.next.next
    mid = slow.next # type: ignore
    slow.next = None # type: ignore
    left = sortList(head)
    right = sortList(mid)
    return merge(left, right)