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

int numSubarrayProductLessThanK(int* nums, int numsSize, int k) {
    int count = 0;
    int arr[numsSize][numsSize];

    for(int i = 0; i < numsSize; i++)
    {
        if (nums[i] < k)
        {
            count++;
            arr[0][i] = nums[i];
        } else {
            arr[0][i] = k;
        }
    }

    for (int interval = 2; interval <= numsSize; interval++)
    {
        int j = 0;
        while(j <= (numsSize - interval))
        {
            int sum = (arr[interval - 2][j] * nums[j + interval - 1]);
            if (sum < k)
            {
                count++;
                arr[interval - 1][j] = sum;
            } else {
                arr[interval - 1][j] = k;
            }
            j += 1;
        }
    }

    return count;
}

int main()
{
    int arr[4] = {1, 2, 3, 4};
    int out = numSubarrayProductLessThanK(arr, 4, 100);
    return 0;
}