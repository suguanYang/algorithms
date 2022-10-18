// Count and Say

// The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

// countAndSay(1) = "1"
// countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
// To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

// For example, the saying and conversion for digit string "3322251":


// Given a positive integer n, return the nth term of the count-and-say sequence.

// Example 1:

// Input: n = 1
// Output: "1"
// Explanation: This is the base case.
// Example 2:

// Input: n = 4
// Output: "1211"
// Explanation:
// countAndSay(1) = "1"
// countAndSay(2) = say "1" = one 1 = "11"
// countAndSay(3) = say "11" = two 1's = "21"
// countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 

// Constraints:

// 1 <= n <= 30
// Accepted
// 707,851
// Submissions
// 1,400,204

package main

import (
	"fmt"
	"strconv"
)

func say(words string) string {
	count := make(map[rune]int)
	// sequence := make([]rune, 9)
	subStrings := make([]string, 1)
	subStrintIdx := -1
	var preW rune
	for _, w := range words {
		if (count[w] == 0) {
			subStrintIdx++
			subStrings = append(subStrings, "")
			if (preW != 0) {
				count[preW] = 0
			}
		}
		count[w]++
		subStrings[subStrintIdx] = subStrings[subStrintIdx] + string(w)
		preW = w
	}

	s := ""

	for _, str := range subStrings {
		l := len(str)
			if (l > 0) {
		s += strconv.Itoa(l) + string(str[0])
			}
	}
	return s;
}

func countAndSay(n int) string {
	if (n == 1) {
		return "1"
	}
	

	return say(countAndSay(n - 1));
}

func main() {
	fmt.Println(countAndSay(30))
}