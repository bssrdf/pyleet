'''

-Medium-

$$$


You are given an integer array nums.

Return the length of the longest semi-decreasing subarray of nums, and 0 if there are no such subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.
A non-empty array is semi-decreasing if its first element is strictly greater than its last element.
 

Example 1:

Input: nums = [7,6,5,4,3,2,1,6,10,11]
Output: 8
Explanation: Take the subarray [7,6,5,4,3,2,1,6].
The first element is 7 and the last one is 6 so the condition is met.
Hence, the answer would be the length of the subarray or 8.
It can be shown that there aren't any subarrays with the given condition with a length greater than 8.
Example 2:

Input: nums = [57,55,50,60,61,58,63,59,64,60,63]
Output: 6
Explanation: Take the subarray [61,58,63,59,64,60].
The first element is 61 and the last one is 60 so the condition is met.
Hence, the answer would be the length of the subarray or 6.
It can be shown that there aren't any subarrays with the given condition with a length greater than 6.
Example 3:

Input: nums = [1,2,3,4]
Output: 0
Explanation: Since there are no semi-decreasing subarrays in the given array, the answer is 0.
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109



'''

from typing import List
import bisect
class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        # Wrong
        A, n = nums, len(nums)
        stk = []
        nextGreater = [-1] * n
        for i in range(n):
            while stk and A[stk[-1]] <= A[i]:
                nextGreater[stk[-1]] = i     
                stk.pop()                
            stk.append(i)
        print(nextGreater)

        return max(v-i for i,v in enumerate(nextGreater) if v != -1)
    
    def maxSubarrayLength2(self, nums: List[int]) -> int:
        def rightFurthestSmaller(nums):
            n = len(nums)    
            indx = [-1]*n 
            stack, stackv = [], []
            for i in range(n-1, -1, -1):
                if not stack or nums[stack[-1]] > nums[i]:
                    stack.append(i) 
                    stackv.append(-nums[i])
                else:
                    idx = bisect.bisect_right(stackv, -nums[i])
                    indx[i] = stack[idx]
            return indx
        idx = rightFurthestSmaller(nums)
        # print(idx)
        return max((v-i+1 for i,v in enumerate(idx) if v != -1), default=0)

if __name__ == "__main__":
    print(Solution().maxSubarrayLength2(nums = [7,6,5,4,3,2,1,6,10,11]))
    print(Solution().maxSubarrayLength2(nums = [57,55,50,60,61,58,63,59,64,60,63]))
    print(Solution().maxSubarrayLength2(nums = [1,2,3,4]))