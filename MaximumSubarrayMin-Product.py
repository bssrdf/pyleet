'''
-Medium-
*Monotonic Stack*


The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. 
Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. Testcases are 
generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
Example 2:

Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.
Example 3:

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^7


'''

from RangeMinimumQuery import RMQ

class Solution(object):
    def maxSumMinProductTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        preSum = [0]*(n+1)
        for i in range(1,n+1):
            preSum[i] = preSum[i-1]+nums[i-1]
        res = 1
        rmq = RMQ(nums)
        for i in range(n):
            for j in range(i, n):                
                res = max(res, nums[rmq.minRange(i,j)]*(preSum[j+1]-preSum[i]))
                #print(i, j, nums[rmq.minRange(i,j)], preSum[j+1]-preSum[i], res)
        return res

    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        preSum = [0]*(n+1)
        for i in range(1,n+1):
            preSum[i] = preSum[i-1]+nums[i-1]
        res = 1
        leftGreat = [-1]*n
        rightGreat = [-1]*n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop() 
            if stack:
                leftGreat[i] = stack[-1]+1
            else:
                leftGreat[i] = 0    
            stack.append(i) 
        #print(leftGreat)    
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop() 
            if stack:
                rightGreat[i] = stack[-1]-1
            else:
                rightGreat[i] = n-1    
            stack.append(i) 
        for i in range(n):
            l = leftGreat[i]
            r = rightGreat[i] 
            res = max(res, nums[i]*(preSum[r+1]-preSum[l]))
        return res%(10**9+7)

        

if __name__ == "__main__":
    #print(Solution().maxSumMinProduct([1,2,3,2]))
    print(Solution().maxSumMinProduct([2,3,3,1,2]))
    #print(Solution().maxSumMinProduct([3,1,5,6,4,2]))