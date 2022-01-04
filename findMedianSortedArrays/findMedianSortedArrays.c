#include <stdlib.h>
#include <stdio.h>
// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

// The overall run time complexity should be O(log (m+n)).

// Example 1:

// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.
// Example 2:

// Input: nums1 = [1,2], nums2 = [3,4]
// Output: 2.50000
// Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

// Constraints:

// nums1.length == m
// nums2.length == n
// 0 <= m <= 1000
// 0 <= n <= 1000
// 1 <= m + n <= 2000
// -106 <= nums1[i], nums2[i] <= 106

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
    if (nums1Size == 0 || nums2Size == 0)
    {
        return 0;
    }
    int total_size = (nums1Size + nums2Size);
    int *arr = malloc(total_size * sizeof(int));

    int l_idx = 0, r_idx = 0;
    while (l_idx < nums1Size && r_idx < nums2Size) {
        if (nums1[l_idx] <= nums2[r_idx]) {
            arr[l_idx + r_idx] = nums1[l_idx];
            l_idx++;
        } else {
            arr[l_idx + r_idx] = nums2[r_idx];
            r_idx++;
        }
    }

    while (l_idx < nums1Size)
    {
        arr[l_idx + r_idx] = nums1[l_idx];
        l_idx++;
    }

    while (r_idx < nums2Size)
    {
        arr[l_idx + r_idx] = nums2[r_idx];
        r_idx++;
    }
    int middle = total_size / 2;
    if (total_size % 2 == 0)
    {
        return (arr[middle] + arr[middle - 1]) / 2.0;
    }
    
    return arr[middle];
}
