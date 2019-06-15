/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    var next = head.next;
    var length = 1;
    // Count Length
    while (next != null) {
        length ++;
        next = next.next;
    }
    if (n > length){
        return head;
    }
    
    // Start Delete
    var target = length - n;
    var pre = null;
    var position = 0;
    var start = new ListNode(null);
    start.next = head;
    var current = head;
    
    // Handle Head
    if (target == 0) {
        return head.next;
    }
    
    while (current != null) {
        if (position != target){
            pre = current;
            current = current.next;
        } else {
            pre.next = current.next;
            break;
        }
        position ++;
    }
    
    return start.next;
};


/**
 * Method 2
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    var start = new ListNode(null);
    start.next = head;
    
    var left = start;
    var right = start;
    // Set Distance
    for (var i = 0; i < n + 1; i++){
        right = right.next;
    }
    
    // Move two pointers until right reach end
    while (right !== null) {
        left = left.next;
        right = right.next;
    }
    
    // Delete
    left.next = left.next.next;
    
    return start.next
};