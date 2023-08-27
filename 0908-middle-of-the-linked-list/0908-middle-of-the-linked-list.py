# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        start = head
        while head:
            cnt += 1
            head = head.next
        mid = cnt // 2
        
        while mid:
            start = start.next
            mid -= 1
        
        return start