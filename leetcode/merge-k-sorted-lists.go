// You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.

// Example 1:

// Input: lists = [[1,4,5],[1,3,4],[2,6]]
// Output: [1,1,2,3,4,4,5,6]
// Explanation: The linked-lists are:
// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// merging them into one sorted list:
// 1->1->2->3->4->4->5->6
// Example 2:

// Input: lists = []
// Output: []
// Example 3:

// Input: lists = [[]]
// Output: []

// Constraints:

// k == lists.length
// 0 <= k <= 104
// 0 <= lists[i].length <= 500
// -104 <= lists[i][j] <= 104
// lists[i] is sorted in ascending order.
// The sum of lists[i].length will not exceed 104.
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func merge(list1 *ListNode, list2 *ListNode) *ListNode {
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

func mergeKLists(lists []*ListNode) *ListNode {
	var res *ListNode = nil
	for len(lists) > 0 {
		first := lists[0]
		lists = lists[1:]

		res = merge(res, first)
	}

	return res
}
