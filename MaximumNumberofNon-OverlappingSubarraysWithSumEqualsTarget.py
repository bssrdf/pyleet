'''

-Medium-

*Prefix Sum*
*Greedy*

Given an array nums and an integer target.

Return the maximum number of non-empty non-overlapping subarrays such that the sum of values 
in each subarray is equal to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
Example 2:

Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
Example 3:

Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
Output: 3
Example 4:

Input: nums = [0,0,0], target = 0
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
0 <= target <= 10^6

'''

class Solution(object):

    def maxNonOverlappingOnepass(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 69%
        dp, sm  = {0:-1}, 0
        right, cnt = -1, 0
        for i in range(len(nums)):
            sm += nums[i]
            if sm-target in dp:
                left = dp[sm-target]
                if right <= left:
                    cnt += 1
                    right = i
                #print(i, left, right, sm, cnt)
            dp[sm] = i
        return cnt

    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 15.6%
        sm = [0]
        for i in nums:
            sm.append(sm[-1]+i)
        m, ij = {0:-1}, []
        for i, n in enumerate(sm[1:]):
            if n-target in m:
                ij.append((m[n-target]+1, i))
            m[n] = i
        i, res = 0, 0
        while i < len(ij):
            j = i+1
            while j < len(ij) and ij[i][1] >= ij[j][0]:
                j += 1
            i = j
            res += 1
        return res

if __name__ == "__main__":
    '''
    print(Solution().maxNonOverlapping([-1,3,5,1,4,2,-9], 6))
    print(Solution().maxNonOverlapping([1,1,1,1,1], 2))
    print(Solution().maxNonOverlapping([-2,6,6,3,5,4,1,2,8], 10))
    print(Solution().maxNonOverlapping([0,0,0], 0))
    print(Solution().maxNonOverlapping([2,2,3,-2,2,-3,3,-2,1,3], 2))
    '''
    print(Solution().maxNonOverlappingOnepass([2,2,3,-2,2,-3,3,-2,1,3], 2))