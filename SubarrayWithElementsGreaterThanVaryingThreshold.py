'''
-Hard-

You are given an integer array nums and an integer threshold.

Find any subarray of nums of length k such that every element in the subarray is greater than threshold / k.

Return the size of any such subarray. If there is no such subarray, return -1.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,4,3,1], threshold = 6
Output: 3
Explanation: The subarray [3,4,3] has a size of 3, and every element is greater than 6 / 3 = 2.
Note that this is the only valid subarray.
Example 2:

Input: nums = [6,5,6,5,8], threshold = 7
Output: 1
Explanation: The subarray [8] has a size of 1, and 8 > 7 / 1 = 7. So 1 is returned.
Note that the subarray [6,5] has a size of 2, and every element is greater than 7 / 2 = 3.5. 
Similarly, the subarrays [6,5,6], [6,5,6,5], [6,5,6,5,8] also satisfy the given conditions.
Therefore, 2, 3, 4, or 5 may also be returned.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], threshold <= 109


'''

from typing import List

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        # HINT: For all elements to be greater than the threshold/length, 
        # the minimum element in the subarray must be greater than the 
        # threshold/length.
        A, n = nums, len(nums)
        smallerLeft = [-1]*n
        smallerRight = [n]*n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                smallerRight[stack[-1]] = i 
                stack.pop()            
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] > A[i]:
                smallerLeft[stack[-1]] = i
                stack.pop()
            stack.append(i)
        print(smallerLeft)
        print(smallerRight)
        for i in range(n):
            k = smallerRight[i] - smallerLeft[i] - 1
            if A[i] > threshold / k:
                return k 
        return -1        




if __name__ == "__main__":
    print(Solution().validSubarraySize(nums = [1,3,4,3,1], threshold = 6))
        
    print(Solution().validSubarraySize(nums = [6,5,6,5,8], threshold = 7))