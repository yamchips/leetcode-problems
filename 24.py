from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def swapPairs( head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    curr = head
    next = head.next
    
    while prev and next:
        curr.next = next.next
        next.next = curr
        prev.next = next

        prev = curr
        curr = prev.next
        if curr is None:
            break
        next = curr.next
        if next is None:
            break

    return dummy.next


def swapPairs( head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    curr = head
    
    
    while curr and curr.next:
        next = curr.next
        curr.next = next.next
        next.next = curr
        prev.next = next

        prev = curr
        curr = prev.next

    return dummy.next     

if __name__=='__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print(swapPairs(head))