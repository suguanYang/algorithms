class Solution:
    def twoSum(self, nums, target):
        """[summary]
        """
        if (not isinstance(nums, list)):
            raise Exception('the argument nums must be a list')
        if (not (isinstance(target, int) or isinstance(target, float))):
            raise Exception('the target nums must be a int or float')
        numsLen = len(nums)
        for i in range(numsLen):
            k = 0
            while k < numsLen:
                if (k == i):
                    pass   
                elif (nums[i] + nums[k] == target):
                    return [i, k]
                k+=1
            else:
                pass
        
        return None

tarArr = [2,7,11,15]
tarNum = 9
sol = Solution()

result = sol.twoSum(tarArr, tarNum)

print(result)