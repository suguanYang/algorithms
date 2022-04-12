// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.

// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false

// Constraints:

// 1 <= s.length <= 104
// s consists of parentheses only '()[]{}'.
package main

func isValid(s string) bool {
	opposite := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}
	stack := make([]rune, 0)
	count := 0
	for _, char := range s {
		stack = append(stack, char)
		count++
		if count > 1 {
			lastOne := stack[len(stack)-1]
			lastTwo := stack[len(stack)-2]
			oppo := opposite[lastOne]
			if lastTwo == oppo {
				stack = stack[:len(stack)-2]
			}
		}
	}

	return len(stack) == 0
}
