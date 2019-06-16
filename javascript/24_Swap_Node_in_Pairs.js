/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    var start = new ListNode(null);
    start.next = head;
    
    var prev = start;
    
    while (head != null && head.next != null){
        var first = head;
        var second = head.next;
        var after = head.next.next;
        
        prev.next = second;
        
        head = second;
        head.next = first;
        
        head.next.next = after;
        head = head.next.next;
        prev = prev.next.next;
    }
    
    return start.next;
};