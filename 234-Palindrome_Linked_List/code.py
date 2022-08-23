# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindrome = list()
        while True:
            if head.next == None:
                palindrome.append(head.val)
                break
            palindrome.append(head.val)
            head = head.next
        if palindrome == palindrome[::-1]:
            return True
        else:
            return False
