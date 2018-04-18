class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        
        if (not isinstance(J, str)):
            return count
        if (not isinstance(S, str)):
            return count
        
        Jlen = len(J)
        Slen = len(S)

        if (Jlen > 50 or Slen > 50):
            return count
        
        for i in range(Jlen):
            for k in range(Slen):
                if (J[i] == S[k]):
                    count = 1 + count
        
        return count

jewels = 'gsda'
stones = 'asfasfwefasdasdaf'

sol = Solution()
result = sol.numJewelsInStones(jewels, stones)

print(result)
