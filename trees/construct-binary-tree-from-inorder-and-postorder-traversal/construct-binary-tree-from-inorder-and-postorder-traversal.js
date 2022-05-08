// Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

// Example 1:

//                  3
//              9       20
//                  15       7
// Input: inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3]
// Output: [3,9,20,null,null,15,7]
// Example 2:

// Input: inorder = [-1], postorder = [-1]
// Output: [-1]
 

// Constraints:

// 1 <= inorder.length <= 3000
// postorder.length == inorder.length
// -3000 <= inorder[i], postorder[i] <= 3000
// inorder and postorder consist of unique values.
// Each value of postorder also appears in inorder.
// inorder is guaranteed to be the inorder traversal of the tree.
// postorder is guaranteed to be the postorder traversal of the tree.

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    const root = postorder[postorder.length - 1];

    const get_sub_r = (left, right) => {
        let max = 0;
        for (let i = left; i < (right + 1); i++) {
            const node = inorder[i];
            const post_idx = postorder.findIndex(it => it === node);

            if (post_idx > max) {
                max = post_idx;
            }
        }

        return postorder[max];
    }
    
    const iter = (left, right, r) => {
        if (left > right) {
            return;
        };
        const sub_r = get_sub_r(left, right);
        r.val = sub_r;
        const sub_r_idx = inorder.findIndex(it => it === sub_r);
        if (left <= sub_r_idx - 1) {
            r.left = new TreeNode();
            iter(left, sub_r_idx - 1, r.left);
        }
        if (sub_r_idx + 1 <= right) {
            r.right = new TreeNode();
            iter(sub_r_idx + 1, right, r.right);
        }

        return r;
    }

    const rootNode = new TreeNode(root);
    iter(0, inorder.length - 1, rootNode);

    return rootNode;
};

var buildTreeIter = function(inorder, postorder) {
    const inorderVal2IdxMap = inorder.reduce((prev, curr, idx) => ({
        ...prev,
        [curr]: idx
    }), {});

    const stack = [];
    const nodeStack = [];
    let sp = 0;
    stack[sp++] = 0;
    stack[sp++] = postorder.length - 1;
    stack[sp++] = 'no';
    stack[sp++] = null;

    let root = null;
    while (sp > 0) {
        const pi = stack[--sp];
        const dir = stack[--sp];
        const end = stack[--sp];
        const start = stack[--sp];

        if (start > end) {
            continue;
        }

        const node = new TreeNode(postorder.pop());
        nodeStack.push(node);

        if (dir === 'no') {
            root = node;
        }
        
        if (dir === 'right') {
            pi.right = node;
        }

        if (dir === 'left') {
            pi.left = node;
        }

        const mid = inorderVal2IdxMap[node.val];

        stack[sp++] = (start);
        stack[sp++] = (mid - 1);
        stack[sp++] = 'left';
        stack[sp++] = node;

        stack[sp++] = (mid + 1);
        stack[sp++] = (end);
        stack[sp++] = 'right';
        stack[sp++] = node;
    }
    return root;
}
//                  3
//              9       20
//                  15       7
console.log(buildTreeIter([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]));