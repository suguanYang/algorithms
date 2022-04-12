# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
from audioop import reverse


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getRightNode(self, order, preSave):
        for i in (order):
            if i in preSave:
                return preSave.get(i)
    def getLeftNode(self, order, preSave):
        for i in (reversed(order)):
            if i in preSave:
                return preSave.get(i)

    def buildTree(self, preorder, inorder):
        root = TreeNode(preorder[0])
        preNode = root
        preSave = {
        }
        preSave[root.val] = root
        for idx in range(1, len(preorder)):
            valIdx = inorder.index(preorder[idx])
            preIdx = inorder.index(preNode.val)
            if valIdx < preIdx: # left case
                parentNode = self.getRightNode(inorder[valIdx:preIdx+1], preSave)
                parentNode.left = TreeNode(preorder[idx])
                preSave[parentNode.left.val] = parentNode.left
                preNode = parentNode.left
            else:
                parentNode = self.getLeftNode(inorder[preIdx:valIdx+1], preSave)
                parentNode.right = TreeNode(preorder[idx])
                preSave[parentNode.right.val] = parentNode.right
                preNode = parentNode.right

        return root

Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])