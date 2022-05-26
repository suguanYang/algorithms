// Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

// Example 1:


// Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
// Output: 6
// Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
// Example 2:

// Input: height = [4,2,0,3,2,5]
// Output: 9
 

// Constraints:

// n == height.length
// 1 <= n <= 2 * 104
// 0 <= height[i] <= 105

// construct Metrix M(m, n), where m = height.length, n = max(height)
// for a given col j, assign item 1 if item was less than height[j] otherwise 0
// subproblemm: for any given row j, what's the total gap in M(m, j)?
// related: M(m, n) = for j in n:
//                      acculamate(M(m, j))
// Topology: increas or decrease j
// base: no base
// origin: M(m, n)
// 

/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    const m = height.length;

    let peek = 0;
    let draftPool = 0;
    let res = 0;
    const dp = {};

    for (let i = 0; i < m; i++) {
        const gap = height[peek] - height[i];
        if (gap <= 0) {
            dp[i] = draftPool;
            res += draftPool;
            draftPool = 0;
            peek = i;
        } else {
            draftPool += gap
            if (i === (m - 1) && draftPool > 0) {
                draftPool = 0;
                i = peek
                height[peek] -= 1
            }
        }
    }
    return res
};

console.log(trap([4,2,0,3,2,5]))