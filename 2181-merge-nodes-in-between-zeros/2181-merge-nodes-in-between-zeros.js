/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var mergeNodes = function(head) {
    
    let prevPtr = null;
    let nodePtr = head;
    while (nodePtr !== null){
        if(nodePtr.val === 0){
            if (prevPtr === null){
                prevPtr = nodePtr;
            } else if (nodePtr.next) {
                prevPtr = prevPtr.next;
                prevPtr.val = 0;
            }
        }  else  if (prevPtr !== null && nodePtr !== null){
            prevPtr.val += nodePtr.val;
        }
        nodePtr = nodePtr.next;
    }
    prevPtr.next = null;
    return head;
};