# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        current, _next = head, head.next

        while True:
            if current == _next:
                return True
            
            if _next is None or _next.next is None:
                return False
            
            current = current.next
            _next = _next.next.next
        