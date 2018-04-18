class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (not isinstance(x, int)):
            pass
        xStr = str(x)
        xStrRevers = str(x)[::-1]

        if (xStr == xStrRevers):
            return True
        
        return False

inputNum = 1121211

sol = Solution()

result = sol.isPalindrome(inputNum)

print(result)