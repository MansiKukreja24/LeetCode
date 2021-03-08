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
    public boolean isPalindrome(ListNode head) {
        ListNode reversedp = reverse(head);
        return isEqual(head,reversedp);
    }
    ListNode reverse(ListNode node){
        ListNode head=null;
        while(node!=null){
            ListNode n= new ListNode(node.val);
            n.next=head;
            head=n;
            node=node.next;
            }
        return head;
        }
    boolean isEqual(ListNode a,ListNode b){        
        while(a!=null && b!=null){
        if(a.val!=b.val)
                return false;
            a=a.next;
            b=b.next;
        }
        return (a==null && b==null);
        }
                
}
