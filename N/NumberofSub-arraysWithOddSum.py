'''

-Medium-
*DP*
*Prefix Sum*

Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100



'''

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even, MOD, ans = 0, 0, 10**9+7, 0
        for a in arr:
            if a % 2 == 1: # a is odd
                ans = (ans + even + 1) % MOD 
                even, odd = odd, even + 1
            else:
                ans = (ans + odd) % MOD 
                even += 1
        return ans        
            


if __name__ == "__main__":
    print(Solution().numOfSubarrays(arr = [1,3,5]))
    print(Solution().numOfSubarrays(arr = [2,4,6]))
    print(Solution().numOfSubarrays(arr = [1,2,3,4,5,6,7]))
        