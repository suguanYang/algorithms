class Solution:
    def twoSum(self, nums, target):
        if (not isinstance(nums, list)):
            raise Exception('the argument nums must be a list')
        if (not (isinstance(target, int) or isinstance(target, float))):
            raise Exception('the target nums must be a int or float')
        numsLen = len(nums)
        for i in range(numsLen):
            k = 0
            while k < numsLen:
                if ( k!= i and nums[i] + nums[k] == target):
                    return [i, k]
                k+=1

        return None
    
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            print(num)
            if target - num in lookup:
                print(lookup)
                return [lookup[target - num], i]
            if (not num in lookup):
                lookup[num] = i
    
    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = 0
        for i in nums:
            j = target - i
            k += 1
            tmp_nums = nums[k:]
            if j in tmp_nums:
                return [k - 1, tmp_nums.index(j) + k]

numarrr = [2,2,11,15]
targetnum = 17

sol = Solution()

result = sol.twoSum3(numarrr, targetnum)

print(result)
