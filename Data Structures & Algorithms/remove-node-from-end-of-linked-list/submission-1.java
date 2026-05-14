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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int counter = 0;
        ListNode curr = head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        while (curr != null) {
            curr = curr.next;
            counter++;
        }

        int ourIndex = counter - n; //2 -1 = 1
        curr = dummy;
        while (ourIndex > 0) {
           ourIndex--;
           curr = curr.next;
        }

        curr.next = curr.next.next;

        return dummy.next;
    }
}
