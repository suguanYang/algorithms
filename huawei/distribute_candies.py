from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        n = 0
        while candies > 0:
            for i in range(num_people):
                if candies > n + (i + 1):
                    res[i] += n + (i + 1)
                    candies = candies - (n + (i + 1))
                else:
                    res[i] += candies
                    candies = 0
                    break
            n+=num_people
        return res

print(Solution().distributeCandies(10, 3))
        
                    