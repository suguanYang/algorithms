# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
# Constraints:

# 1 <= n <= 8
class Solution(object):
    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     res = []
    #     for i in range(n+1):
    #         res.append([])
    #     res[0] = ['']
    #     for i in range(1, n + 1):
    #         for l in range(0, i):
    #             left = res[l]
    #             right = res[i-l-1]
    #             for le in left:
    #                 for ri in right:
    #                     res[i].append(le + '(' + ri + ')')

    #     return res[n]
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        total = n * 2
        res = []
        def iter(t, open, close, str):
            if t == total:
                res.append(str)
                return

            if open < n:
                iter(t+1, open+1, close, str +'(')
            if close < open:
                iter(t+1, open, close+1, str +')')

        iter(0, 0, 0, '')

        return res;

sol = Solution()
print((sol.generateParenthesis(4)))