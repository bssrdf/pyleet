'''
-Medium-

*Bit Manipulation*

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you 
implement it using only constant extra space complexity?

'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)//2-sum(nums)

    def missingNumberXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, res = len(nums), 0
        for i in range(n+1):
            res ^= i
        for i in range(n):
            res ^= nums[i]
        return res
        

if __name__ == "__main__":
    print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
    print(Solution().missingNumber([3,0,1]))
    print(Solution().missingNumberXOR([9,6,4,2,3,5,7,0,1]))
    print(Solution().missingNumberXOR([3,0,1]))