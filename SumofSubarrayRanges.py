'''

-Medium-

You are given an integer array nums. The range of a subarray of nums 
is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9


'''

from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res, inf = 0, float('inf')
        A = [-inf] + nums + [-inf]
        stack = []
        for i,x in enumerate(A):
            while stack and A[stack[-1]] > x:
                j = stack.pop()
                k = stack[-1]
                res -= A[j] * (i-j) * (j-k) 
            stack.append(i)
        stack = []
        A = [inf] + nums + [inf]
        for i,x in enumerate(A):
            while stack and A[stack[-1]] < x:
                j = stack.pop()
                k = stack[-1]
                res += A[j] * (i-j) * (j-k) 
            stack.append(i)
        return res



        
if __name__ == "__main__":
    print(Solution().subArrayRanges([4,-2,-3,4,1]))