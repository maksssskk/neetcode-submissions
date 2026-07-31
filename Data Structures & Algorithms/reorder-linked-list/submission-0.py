# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        sec = s.next
        s.next = None
        
        prev = None
        curr = sec
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first = head
        second = prev
        while first and second:
            el1 = first.next
            el2 = second.next
            first.next = second
            second.next = el1
            first = el1
            second = el2
        
    


        
    