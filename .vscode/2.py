# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    current = dummy
    add = 0
    
    while l1 or l2 or add:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        res = val1 + val2 + add
        
        if res >= 10:
            res = res - 10
            add = 1
        else:
            add = 0

        current.next = ListNode(res)
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
   
    return dummy.next

if __name__=='__main__':
    l1 = ListNode(9, ListNode(9, ListNode(1)))
    l2 = ListNode(1)
    node1 = addTwoNumbers(l1, l2)
    while node1:
        print(node1.val)
        node1 = node1.next
    
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    node1 = addTwoNumbers(l1, l2)
    while node1:
        print(node1.val)
        node1 = node1.next

    l1 = ListNode(0)
    l2 = ListNode(0)
    node1 = addTwoNumbers(l1, l2)
    while node1:
        print(node1.val)
        node1 = node1.next

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    node1 = addTwoNumbers(l1, l2)
    while node1:
        print(node1.val)
        node1 = node1.next
    