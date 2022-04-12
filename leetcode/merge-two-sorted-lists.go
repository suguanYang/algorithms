// You are given the heads of two sorted linked lists list1 and list2.

// Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

// Return the head of the merged linked list.

// Example 1:

// Input: list1 = [1,2,4], list2 = [1,3,4]
// Output: [1,1,2,3,4,4]
// Example 2:

// Input: list1 = [], list2 = []
// Output: []
// Example 3:

// Input: list1 = [], list2 = [0]
// Output: [0]

// Constraints:

// The number of nodes in both lists is in the range [0, 50].
// -100 <= Node.val <= 100
// Both list1 and list2 are sorted in non-decreasing order.
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	head1 := list1
	head2 := list2

	merged := &ListNode{}
	mergedHead := merged

	for head1 != nil && head2 != nil {
		if head1.Val < head2.Val {
			merged.Next = head1
			head1 = head1.Next
		} else {
			merged.Next = head2
			head2 = head2.Next
		}

		merged = merged.Next
	}

	for head1 != nil {
		merged.Next = head1
		head1 = head1.Next
		merged = merged.Next
	}
	for head2 != nil {
		merged.Next = head2
		head2 = head2.Next
		merged = merged.Next
	}
	return mergedHead.Next
}
