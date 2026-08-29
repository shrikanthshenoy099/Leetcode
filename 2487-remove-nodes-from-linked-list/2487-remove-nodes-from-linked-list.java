class Solution {
    public ListNode removeNodes(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

       
        head.next = removeNodes(head.next);

        
        if (head.next != null && head.val < head.next.val) {
            return head.next;
        }

        // Keep the current node
        return head;
    }
}