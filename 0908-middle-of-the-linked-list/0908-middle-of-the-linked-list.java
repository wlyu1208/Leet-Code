/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode find_len = head;
        ListNode ans = head;

        int len = 0;
        while (find_len.next != null) {
            find_len = find_len.next;
            len++;
        }
        int mid = 0;
        if (len % 2 == 1) {
            mid = len / 2 + 1;
        }
        else {
            mid = len / 2;
        }

        int start = 0;
        while (start < mid) {
            ans = ans.next;
            start++;
        }
        return ans;
    }
}