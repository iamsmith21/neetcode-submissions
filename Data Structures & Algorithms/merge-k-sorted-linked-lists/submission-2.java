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

    public ListNode mergeTwoLists(ListNode first, ListNode second) {
            ListNode dummy = new ListNode(0);
            ListNode curr = dummy;

            while (first != null && second != null) {
                if (first.val <= second.val ) {
                    curr.next = first;
                    first = first.next;
                } else {
                    curr.next = second;
                    second = second.next;
                }

                curr = curr.next;
            }

            curr.next = (first != null) ? first : second;
            return dummy.next;
    }

    public ListNode mergeKLists(ListNode[] lists) {

        if (lists == null || lists.length == 0) return null;
        for (int i = 1; i < lists.length; i++) {
            lists[i] = mergeTwoLists(lists[i], lists[i-1]);
        }

        return lists[lists.length - 1];
    }
}
