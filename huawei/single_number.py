from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            if counter.get(n) == None:
                counter[n] = 1
            else:
                counter[n] += 1
        
        for key in counter:
            if counter[key] == 1:
                return key
        return None
    
    def singleNumber2(self, nums: List[int]) -> int:
        res = None
        for n in nums:
            if res == None:
                res = n
                continue
            if res == n:
                res = None

        return res

print(Solution().singleNumber2([2,2,3,2]))