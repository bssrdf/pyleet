'''
-Medium-

Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive numbers 
strictly alternate between positive and negative. The first difference (if one exists) 
may be either positive or negative. A sequence with fewer than two elements is 
trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences 
(6, -3, 5, -7, 3) are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, 
the first because its first two differences are positive and the second because 
its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) 
from the original sequence, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One 
is [1,17,10,13,10,16,8].
Example 3:

Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000

Follow up: Could you solve this in O(n) time?

'''

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(down, up)

    def wiggleMaxLengthDP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        # 0: up, 1: down
        dp[0][0], dp[0][1] = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i][0] = dp[i-1][1] + 1
                dp[i][1] = dp[i-1][1]
            elif nums[i] < nums[i-1]:
                dp[i][1] = dp[i-1][0] + 1
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
        print(nums)
        print([dp[i][0] for i in range(len(nums))])
        print([dp[i][1] for i in range(len(nums))])
        return max(dp[-1][:])
             
                

if __name__ == "__main__":
    #print(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    #print(Solution().wiggleMaxLengthDP([1,17,5,10,13,15,10,5,16,8]))
    print(Solution().wiggleMaxLengthDP([3, 10, 11, 10, 12, 11]))