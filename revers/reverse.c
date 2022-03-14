// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

// Example 1:

// Input: x = 123
// Output: 321
// Example 2:

// Input: x = -123
// Output: -321
// Example 3:

// Input: x = 120
// Output: 21

#include <limits.h>

int reverse(int x)
{
    int isNegative = x < 0 ? 1 : -1;
    if (isNegative > 0 && x == -0x7FFFFFFF)
    {
        return 0;
    }
    x = isNegative > 0 ? -x : x;
    int reversed = x % 10;
    x = x / 10;
    while (x > 0)
    {
        int r = x % 10;
        if ((0x7FFFFFFF / 10) < reversed)
        {
            return 0;
        }
        reversed = reversed * 10 + r;
        x = x / 10;
    }
    if (isNegative > 0 && 0x7FFFFFFF == reversed)
    {
        return 0;
    }
    return isNegative > 0 ? -reversed : reversed;
}

int main()
{
    int a = 1646324359;
    int reverseA = reverse(a);
    return 0;
}