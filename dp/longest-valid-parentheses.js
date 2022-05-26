/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses_NonDP = function(s) {
    const stack = [];
    const validIdx = {};
    const len = s.length;
    for (let i = 0; i < len; i++) {
        const c = s[i];
        if (c === '(') {
            stack.push(i);
        } else if (stack.length > 0) {
            validIdx[stack.pop()] = true;
            validIdx[i] = true;
        }

        
    }

    let gap = 0;
    let max = 0;
    for (let i = 0; i < len; i++) {
        if (validIdx[i]) {
            gap++;
        } else {
            max = Math.max(max, gap);
            gap = 0;
        }
    }
    max = Math.max(max, gap);
    return max;
};

// subproblems: for a given index, what is the longest sub valid partentheses? s[:i]
// related probles: 
// dp(i) = {
//  if i = 0 return 0
//  if i = '(' return dp(i - 1) 
//  if s[i-1] + s[i] = '()' return dp(i - 1) + 2
//  p = i - dp[i - 1] - 1
//  if s[p] = '(' return dp(i - 1) + dp(p - 1) + 2
//  return dp(i - 1)       
// }

var longestValidParentheses = (s) => {
    if (s === '') return 0
    const dp = {
        [-1]: 0,
    }
    let max = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            dp[i] = 0
            continue
        }
        if ((s[i - 1] + s[i]) === '()') {
            dp[i] = dp[i - 2] + 2
            max = Math.max(max, dp[i])
            continue
        }
        const pre = i - dp[i - 1] - 1;
        if (s[pre] === '(') {
            dp[i] = dp[i - 1] + dp[pre - 1] + 2
            max = Math.max(max, dp[i])
            continue
        }

        dp[i] = 0
    }

    return max
}
