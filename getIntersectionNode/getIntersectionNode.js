/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
 var getIntersectionNode = function(headA, headB) {
  let [a, b] = [headA, headB];
  
  while (a != b) {
      a = a === null ? headB : a.next;
      b = b === null ? headA : b.next;
  }
  
  return a;
};

// headA = l1 + L
// headB = l2 + L
// intersection = L
// 