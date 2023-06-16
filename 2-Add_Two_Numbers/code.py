class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        answer = list()

        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            _sum = n1 + n2 + carry
            carry = _sum // 10
            digit = _sum % 10

            current.next = ListNode(digit)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
