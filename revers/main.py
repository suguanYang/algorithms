class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (not isinstance(x, int)):
            raise Exception('x must be an int')

        if (x < 0):
            str_x = str(abs(x))[::-1]
            rx = -int(str_x)
        else:
            str_x = str(x)[::-1]
            rx = int(str_x)

        if (rx > (2 ** 31 - 1) or rx < -2 ** 31):
            return 0
        
        return rx

newSol = Solution()
inputA = -12412412

result = newSol.reverse(inputA)

print(result)