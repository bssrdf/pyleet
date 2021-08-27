'''
-Medium-

You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that 
result[i] is equal to the summation of absolute differences between nums[i] and 
all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) 
where 0 <= j < nums.length and j != i (0-indexed).

 

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]
 

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] <= nums[i + 1] <= 10^4

'''

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left, right = [0]*(n+1), [0]*(n+1)
        for i in range(1, n+1):
            left[i] = left[i-1]+nums[i-1]
        for i in range(n-1, -1, -1):
            right[i] = right[i+1] + nums[i] 
        #print(left, right)
        
        res = [0]*n
        for i in range(n):
            res[i] = nums[i]*(2*i-n+1) - left[i] + right[i+1]
        return res

    def getSumAbsoluteDifferencesLessSpace(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        right = [0]*(n+1)
        for i in range(n-1, -1, -1):
            right[i] = right[i+1] + nums[i] 
        res = [0]*n
        preSum = 0
        for i in range(n):
            res[i] = nums[i]*(2*i-n+1) - preSum + right[i+1]
            preSum += nums[i]
        return res





if __name__ == "__main__":
    print(Solution().getSumAbsoluteDifferences([2,3,5]))
    print(Solution().getSumAbsoluteDifferences([2,3,4,5]))
    print(Solution().getSumAbsoluteDifferences([1,4,6,8,10]))
    
