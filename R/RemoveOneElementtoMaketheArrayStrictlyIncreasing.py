'''

-Easy-

Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

 

Example 1:

Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.
Example 2:

Input: nums = [2,3,1,2]
Output: false
Explanation:
[3,1,2] is the result of removing the element at index 0.
[2,1,2] is the result of removing the element at index 1.
[2,3,2] is the result of removing the element at index 2.
[2,3,1] is the result of removing the element at index 3.
No resulting array is strictly increasing, so return false.
Example 3:

Input: nums = [1,1,1]
Output: false
Explanation: The result of removing any element is [1,1].
[1,1] is not strictly increasing, so return false.
 

Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 1000




'''

from typing import List

class Solution:
    '''
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n, A = len(nums), nums
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            stack.append(i)
        return True if len(stack) >= n-1 else False
    '''
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # o(N)
        A = [0] + nums + [1001]
        cnt = 0
        for i in range(2, len(A)-1):
            if A[i] <= A[i-1]:
                if A[i] > A[i-2] or A[i+1] > A[i-1]: 
                   cnt += 1
                else:
                    return False
        return True if cnt <= 1 else False
    
    def canBeIncreasing2(self, nums: List[int]) -> bool:
        # O(N2)
        n, A = len(nums), nums
        F = [1]*len(nums)
        maxa = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if A[i] > A[j] and F[i] < 1+F[j]:                    
                    F[i] = 1 + F[j]    
            maxa = max(maxa, F[i])
        return True if maxa >= n-1 else False
            
                
if __name__ == "__main__":
    print(Solution().canBeIncreasing(nums = [1,2,10,5,7]))
    print(Solution().canBeIncreasing(nums = [2,3,1,2]))
    print(Solution().canBeIncreasing(nums = [1,1,1]))
    print(Solution().canBeIncreasing(nums = [105,924,32,968]))
