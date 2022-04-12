
// reverse the inoder
//           1
//         /   \
//        2     3
//       / \   / \
//      4   5 6   7
function invertTree(tree) {
    function inorder(root) {
        const opt = [];
        const stack = [root];
        var t = root;
        while (t !== undefined && stack.length > 0) {
            var left = t.left;
            while (left !== undefined) {
                stack.push(left);
                left = left.left;
            }
            const node = stack.pop();
            opt.push(node);
            
            var right = node.right;
            if (right !== undefined) {
                stack.push(right);
                t = right;
            } else {
                t = node;
            }

        }

        return opt;
    }

    function reverse(arr) {
        var l = 0;
        var r = arr.length - 1;

        while (l < r) {
            const temp = arr[l].val;
            arr[l].val = arr[r].val;
            arr[r].val = temp;
            l++;
            r--;
        }

        return arr;
    }


    return reverse(inorder(tree));
}

const root = {
    val: 1,
    left: {
        val: 2,
        left: {
            val: 4,
        },
        right: {
            val: 5,
        }
    },
    right: {
        val: 3,
        left: {
            val: 6,
        },
        right: {
            val: 7,
        }
    }
}

console.dir(invertTree(root));