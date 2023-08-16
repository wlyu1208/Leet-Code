# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = start = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                answer.next = list1
                tmp = list1
                list1 = list1.next
                answer = tmp
            else:
                answer.next = list2
                tmp = list2
                list2 = list2.next
                answer = tmp
        
        if list1 or list2:
            answer.next = list1 if list1 else list2
        
        return start.next
