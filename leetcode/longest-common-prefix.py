# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
# Accepted
# 1,486,620
# Submissions
# 3,797,841

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        idx = 0
        prefix = ''
        prefixCount = 0
        strsLen = len(strs)

        while len(strs[idx]) >= prefixCount:
            if prefix != strs[idx][:prefixCount]:
                return prefix[:-1]
            
            idx += 1
            if idx == strsLen:
                prefixCount += 1
                if prefixCount > len(strs[0]):
                    return prefix
                prefix = strs[0][:prefixCount]
                idx = 0
        
        return prefix[:-1]