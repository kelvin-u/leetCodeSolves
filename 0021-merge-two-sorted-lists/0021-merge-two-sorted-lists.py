# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val: # take the list one node and put it in the dummy node since it's smaller
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2 # take the list two node and put it in the dummy node
                list2 = list2.next
            tail = tail.next # update it no matter wat
        
        # one is empty either is not
        if list1:
            tail.next = list1 #
        elif list2:
            tail.next = list2
        
        return dummy.next