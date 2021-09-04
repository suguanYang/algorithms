import math

class Solution:
    def bulbSwitch(self, n):
        # bulbs = [0] * n
        # def inverseBit(bs, gap):
        #     for i in range(len(bs)):
        #         if (i + 1) % gap == 0:
        #             bs[i] = 0 if bs[i] == 1 else 1
        # for round in range(n):
        #     inverseBit(bulbs, round + 1)
        
        # return sum(bulbs)
        return int(math.sqrt(n))

print(Solution().bulbSwitch(1))
for i in range(20):
    print(str(i) + ': ', Solution().bulbSwitch(i))

