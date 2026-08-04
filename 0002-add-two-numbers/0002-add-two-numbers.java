
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Dummy head to simplify result list construction
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;
        int carry = 0;

        // Traverse both lists until both are null
        while (l1 != null || l2 != null) {
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;

            int sum = carry + x + y;
            carry = sum / 10;

            // Create new node with digit value
            current.next = new ListNode(sum % 10);
            current = current.next;

            // Move forward in lists
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        // If carry remains, add new node
        if (carry > 0) {
            current.next = new ListNode(carry);
        }

        return dummyHead.next;
    }
}