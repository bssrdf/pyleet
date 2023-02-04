'''
-Medium-
*Sliding Window*
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.

 

Example 1:

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.
Example 2:

Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109




'''

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # wrong solution
        A, n = nums, len(nums)
        i, mask = 0, 0
        ans = 0
        for j in range(n):                        
            if A[j] & mask > 0:
                mask = A[j] 
                i = j
            else:
                mask |= A[j]
            # print(f'{mask:032b}', f'{A[j]:032b}')
            ans = max(ans, j-i+1)
            print(f'{mask:032b}', f'{A[j]:032b}', ans)
        return ans
    
    def longestNiceSubarray2(self, nums: List[int]) -> int:
        A, n = nums, len(nums)
        i, mask = 0, 0
        ans = 0
        for j in range(n):                        
            while A[j] & mask > 0:
                mask ^= A[i] 
                i += 1
            mask |= A[j]
            ans = max(ans, j-i+1)
        return ans

              


if __name__ == "__main__":
    # print(Solution().longestNiceSubarray(nums = [1,3,8,48,10]))
    # print(Solution().longestNiceSubarray(nums = [3,1,5,11,13]))
    print(Solution().longestNiceSubarray2(nums = [1,3,8,48,10]))
    print(Solution().longestNiceSubarray2(nums = [3,1,5,11,13]))
    nums = [84139415,693324769,614626365,497710833,615598711,264,65552,50331652,1,1048576,16384,544,270532608,151813349,221976871,678178917,845710321,751376227,331656525,739558112,267703680]
    print(Solution().longestNiceSubarray2(nums = nums))


        