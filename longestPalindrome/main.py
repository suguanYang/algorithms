class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def getSupStrMaxLen(ss, maxLen, paliList):
            # maxLen = 0
            currStr = ''
            if (ss == ''):
                return paliList
            for i, item in enumerate(ss):
                currStr = currStr + item
                sameIndex = currStr.find(item)
                if (sameIndex == 0 and currStr == currStr[::-1]):
                    # paliList.append(currStr)
                    thisLen = len(currStr)
                    if (maxLen < thisLen):
                        maxLen = thisLen
                        paliList = currStr
            return getSupStrMaxLen(ss[1::], maxLen, paliList)
        return getSupStrMaxLen(s, 0, '')
target = "eabcb"
sol = Solution()

print(sol.longestPalindrome(target))