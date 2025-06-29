from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    curr = head.next
    head.next = None
    while curr:
        next = curr.next
        if head.val >= curr.val:
            dummy.next = curr
            curr.next = head
            curr = head
        else:
            prev = None
            while head and head.val < curr.val:
                prev = head
                head = head.next
            prev.next = curr
            curr.next = head
        curr = next
        head = dummy.next
    return dummy.next

if __name__=='__main__':
    node1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    node1 = (insertionSortList(node1))
    while node1:
        print(node1.val)
        node1 = node1.next

    node1 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4,ListNode(0)))))
    node1 = (insertionSortList(node1))
    while node1:
        print(node1.val)
        node1 = node1.next
    
    node1 = ListNode(-1, ListNode(5, ListNode(-1, ListNode(4,ListNode(0)))))
    node1 = (insertionSortList(node1))
    while node1:
        print(node1.val)
        node1 = node1.next

    node1 = ListNode(-100)
    node1 = (insertionSortList(node1))
    while node1:
        print(node1.val)
        node1 = node1.next

    node1 = ListNode(-1, ListNode(-1, ListNode(-1, ListNode(-1,ListNode(-1)))))
    node1 = (insertionSortList(node1))
    while node1:
        print(node1.val)
        node1 = node1.next