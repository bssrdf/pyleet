'''

-Medium-
*DP*
*Kadane's Algorithm*
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of 
the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4

'''
from typing import List

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n, sm, mx = len(arr), arr[0], arr[0]
        total = sum(arr)
        mod = 10**9+7
        for i in range(1, n * min(k, 2)):
            sm = max(arr[i % n], sm + arr[i % n])
            mx = max(mx, sm)            
        
        return max(0, mx, total * max(0, k - 2) + mx) % mod

    def kConcatenationMaxSum2(self, arr: List[int], k: int) -> int:
        # 1. all positive : [1,2,3], k = 3, array_sum = 6
        #     return array_sum*3
        # 2. all negative : [-1,-2], k = 2, array_sum = -3
        #     return 0
        # 3. hybrid, with array_sum <= 0, [2,1,-3], k = 4, array_sum = 0
        #     [ 2,  1, -3, 2, 1, -3, 2, 1, -3, 2, 1, -3]
        # max sum  2   3  0   2  3  0   2  3   0   2  3  0
        #     return max_subarray_sum between [2,1,-3,2,1,-3] which is twice of original array
        #     so, return max_subarray_sum = 3
        # 4. hybrid, with array_sum > 0, [2,-6,5], k =4, array_sum = 1
        #     [ 2, -6, 5, 2, -6, 5, 2, -6, 5, 2, -6, 5]
        # max sum  2   0  5  7   1  6  8   2  7  9   3  8
        # a. you can notice max subarray sum is getting bigger as k grows up.
        # b. with first 2 array, we can get max subarray sum is 8.
        # c. after that, with each new array, max_subarray_sum will increase by 1, which is array_sum
        # ==>return (max_subarray_sum when k=2) + array_sum*(k-2)
        mod = 10**9+7
        def Kadane(arr):
            res, cur = 0, 0
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res
        return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % mod if k > 1 else Kadane(arr) % mod

if __name__ == "__main__":
    print(Solution().kConcatenationMaxSum([1,-2,1], k = 5))
    print(Solution().kConcatenationMaxSum2([1,-2,1], k = 5))
        