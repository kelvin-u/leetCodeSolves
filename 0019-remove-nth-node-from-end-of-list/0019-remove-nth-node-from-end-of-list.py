# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        slow = head
        
        # move the fast pointer n step ahead of slow
        for i in range(n):
            fast = fast.next
        
        #edge case for only one node
        if not fast:
            return head.next
        
        # move both the pointers now so slow is one before the nth node
        # fast will be null and slow will be one node before the nth node
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # delete the next node
        slow.next = slow.next.next
        return head
    