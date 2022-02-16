// Given an array of integers nums and an integer k, return the number of contiguous
// subarrays where the product of all the elements in the subarray is strictly less than k.


// Example 1:

// Input: nums = [10,5,2,6], k = 100
// Output: 8
// Explanation: The 8 subarrays that have product less than 100 are:
// [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
// Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
// Example 2:

// Input: nums = [1,2,3], k = 0
// Output: 0
 

// Constraints:

// 1 <= nums.length <= 3 * 104
// 1 <= nums[i] <= 1000
// 0 <= k <= 106
// Accepted
// 137,090
// Sub

// for i to size(nums):
//      while j > 0

int rowCol2Idx(int row, int col, int base)
{
    return (
        (row * base - ((row - 1) * row) / 2) - (base - row + 1) + col
    );
}

int numSubarrayProductLessThanK(int* nums, int numsSize, int k) {
    int count = 0;
    int max_size = 10000;
    int arr1[max_size];

    for(int i = 0; i < numsSize; i++)
    {
        if (nums[i] < k)
        {
            count++;
            arr1[rowCol2Idx(1, i + 1, numsSize)] = nums[i];
        } else {
            arr1[rowCol2Idx(1, i + 1, numsSize)] = k;
        }
    }

    for (int interval = 2; interval <= numsSize; interval++)
    {
        int j = 0;
        while(j <= (numsSize - interval))
        {
            int sum = arr1[rowCol2Idx(interval - 2 + 1, j + 1, numsSize)] * nums[j + interval - 1];
            if (sum < k)
            {
                count++;
                arr1[rowCol2Idx(interval - 1 + 1, j + 1, numsSize)] = sum;
            } else {
                arr1[rowCol2Idx(interval - 1 + 1, j + 1, numsSize)] = k;
            }
            j += 1;
        }
    }

    return count;
}

int main()
{
    int arr[4] = {10,5,2,6};
    int out = numSubarrayProductLessThanK(arr, 4, 100);
    return 0;
}