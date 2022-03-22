# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
 

# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dic = {}
        dic[(0, 0)] = True

        s_len = len(s)
        p_len = len(p)
        for i in range(1, p_len + 1):
            if p[i - 1] == '*':
                dic[(0, i)] = dic[(0, i - 2)]
            else:
                dic[(0, i)] = False
        for i in range(1, s_len + 1):
            dic[(i, 0)] = False

        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if s[i - 1] == p[j - 1]:
                    dic[(i, j)] = dic[(i - 1, j - 1)]
                elif p[j - 1] == '.':
                    dic[(i, j)] = dic[(i - 1, j - 1)]
                elif p[j - 1] == '*':
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dic[(i, j)] = dic[(i, j - 1)] or dic[(i - 1, j)] or dic[(i, j - 2)]
                    else:
                        dic[(i, j)] = dic[(i, j - 2)]
                else:
                    dic[(i, j)] = False
        return dic[(s_len, p_len)]


a = Solution()
print(a.isMatch("a", "c*a*"))