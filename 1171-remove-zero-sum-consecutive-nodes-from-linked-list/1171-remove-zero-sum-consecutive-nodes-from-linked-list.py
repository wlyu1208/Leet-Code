# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head

        prefix = 0
        prefix_dict = {0: temp}
        current = head

        while current:
            prefix += current.val
            if prefix in prefix_dict:
                to_delete = prefix_dict[prefix].next
                temp_sum = prefix + to_delete.val

                while to_delete != current:
                    del prefix_dict[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_dict[prefix].next = current.next
            else:
                prefix_dict[prefix] = current
            current = current.next
        return temp.next