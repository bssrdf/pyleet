'''
-Medium-
*DP*

Given an integer array nums, return the number of longest increasing 
subsequences.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] 
and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, 
and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

0 <= nums.length <= 2000
-106 <= nums[i] <= 106

'''
from collections import defaultdict

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        # length of increasing subsequence ending at nums[i]
        F = [1]*len(nums)        
        # number of increasing subsequence ending at nums[i]
        cnt = [1]*len(nums)          
        mx, res = 0, 0               
        for i in range(0, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if F[i] == F[j]+1:                 
                        cnt[i] += cnt[j]
                    elif F[i] < F[j]+1:                
                        F[i] = F[j]+1
                        cnt[i] = cnt[j]
            if mx == F[i]:
                res += cnt[i]
            elif mx < F[i]:
                mx = F[i]
                res = cnt[i]                       
        return res       

if __name__ == "__main__":
    print(Solution().findNumberOfLIS([1,3,5,4,7]))
    print(Solution().findNumberOfLIS([2,2,2,2,2]))
    print(Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]))