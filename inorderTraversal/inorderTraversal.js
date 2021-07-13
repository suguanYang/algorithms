/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
 var inorderTraversal = function(root) {
  let left = [];
  const inOrderIter = (node) => {
      
      if (node === null) {
          return;
      }
      inOrderIter(node.left);
      left.push(node.val);
      inOrderIter(node.right)
  }
  
  inOrderIter(root);
  
  return left;
};