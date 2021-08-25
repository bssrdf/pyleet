'''
-Medium-


Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] 
with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence seq is arithmetic 
if seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

 

Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: nums = [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
 

Constraints:

2 <= nums.length <= 1000
0 <= nums[i] <= 500

'''

from collections import defaultdict

class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = defaultdict(int)
        n = len(nums)
        res = 1
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                m[(i,diff)] = m[(j,diff)] + 1
                res = max(res, m[(i,diff)])
        return res + 1 
    def longestArithSeqLengthDP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0]*2000 for _ in range(n)]
        res = 1
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]+1000
                dp[i][diff] = dp[j][diff] + 1
                res = max(res, dp[i][diff])
        return res + 1 

if __name__ == '__main__':   
    print(Solution().longestArithSeqLength([3,6,9,12]))
    print(Solution().longestArithSeqLength([9,4,7,2,10]))
    print(Solution().longestArithSeqLength([20,1,15,3,10,5,8]))
    print(Solution().longestArithSeqLength([83,20,17,43,52,78,68,45]))
    print(Solution().longestArithSeqLength([24,13,1,100,0,94,3,0,3]))
    arr = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
    print(Solution().longestArithSeqLength(arr))

    print(Solution().longestArithSeqLengthDP([3,6,9,12]))
    print(Solution().longestArithSeqLengthDP([9,4,7,2,10]))
    print(Solution().longestArithSeqLengthDP([20,1,15,3,10,5,8]))
    print(Solution().longestArithSeqLengthDP([83,20,17,43,52,78,68,45]))
    print(Solution().longestArithSeqLengthDP([24,13,1,100,0,94,3,0,3]))
    arr = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
    print(Solution().longestArithSeqLengthDP(arr))