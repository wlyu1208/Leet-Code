# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_1, l_2 = list(), list()

        while l1:
            l_1.append(l1.val)
            l1 = l1.next

        while l2:
            l_2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None
        while l_1 or l_2:
            val1 = l_1.pop() if l_1 else 0
            val2 = l_2.pop() if l_2 else 0
            _sum = val1 + val2 + carry
            carry, v = divmod(_sum, 10)
            temp = head
            head = ListNode(v)
            head.next = temp
        if carry:
            temp = head
            head = ListNode(carry)
            head.next = temp
        return head
            
