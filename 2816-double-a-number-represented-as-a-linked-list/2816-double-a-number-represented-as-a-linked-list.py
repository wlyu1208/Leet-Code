# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = self.reverse(head)

        carry = 0
        current, prev = reverse, None

        while current:
            new_val = current.val * 2 + carry
            carry = new_val // 10
            current.val = new_val % 10

            prev, current = current, current.next

        if carry:
            prev.next = ListNode(carry)
        
        result = self.reverse(reverse)

        return result

    
    def reverse(self, head: Optional[ListNode]):
        prev, current = None, head

        while current:
            _next = current.next
            current.next = prev
            prev, current = current, _next
        
        return prev
