// The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

// P   A   H   N
// A P L S I I G
// Y   I   R
// And then read line by line: "PAHNAPLSIIGYIR"

// Write the code that will take a string and make this conversion given a number of rows:

// string convert(string s, int numRows);

// Example 1:

// Input: s = "PAYPALISHIRING", numRows = 3
// Output: "PAHNAPLSIIGYIR"
// Example 2:

// Input: s = "PAYPALISHIRING", numRows = 4
// Output: "PINALSIGYAHRPI"
// Explanation:
// P     I    N
// A   L S  I G
// Y A   H R
// P     I
// Example 3:

// Input: s = "A", numRows = 1
// Output: "A"

// Constraints:

// 1 <= s.length <= 1000
// s consists of English letters (lower-case and upper-case), ',' and '.'.
// 1 <= numRows <= 1000

package main

import (
	"strconv"
)

func convert(s string, numRows int) string {
	row := 0
	col := 1
	dict := make(map[string]string)
	inc := true
	for _, c := range s {
		if inc {
			row += 1
		} else {
			col++
			row -= 1
		}

		if row == numRows {
			inc = false
		}

		if row == 1 {
			inc = true
		}
		dict[strconv.Itoa(row)+"-"+strconv.Itoa(col)] = string(c)

	}

	res := ""
	for i := 1; i <= numRows; i++ {
		for j := 1; j <= col; j++ {
			if val, ok := dict[strconv.Itoa(i)+"-"+strconv.Itoa(j)]; ok {
				res += val
			}
		}
	}
	return res
}

func main() {
	convert("AB", 1)
}
