package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(node *TreeNode, depth int, max *int) {
	if node == nil {
		if depth > *max {
			*max = depth
		}
		return
	}
	dfs(node.Left, depth+1, max)
	dfs(node.Right, depth+1, max)
}

func maxDepth(root *TreeNode) int {
	var d int = 0
	var max *int = &d

	dfs(root, 0, max)

	return *max
}
