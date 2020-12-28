'''
-Hard-
*DP*
*Divide & Conquer*

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number 
on it represented by array nums. You are asked to burst all the balloons. 
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] 
coins. Here left and right are adjacent indices of i. After the burst, the 
left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can 
not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

'''

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        for details, see
        https://www.cnblogs.com/grandyang/p/5006441.html
        """
        n = len(nums)        
        nums = [1]+nums+[1]
        # len(dp) is n+3 because of 1's added at both ends
        dp = [[0 for _ in range(n+3)] for _ in range(n+3)] 
        for length in range (1, n+1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                for k in range(i, j+1):
                    """
                    状态转移方程如下所示：
                    dp[i][j] 表示打爆区间[i,j]中的所有气球能得到的最多金币
                    dp[i][j] = max(dp[i][j], nums[i - 1] * nums[k] * nums[j + 1] 
                         + dp[i][k - 1] + dp[k + 1][j])     ( i ≤ k ≤ j )
                    """
                    dp[i][j] = max(dp[i][j], nums[i - 1] * nums[k] * nums[j + 1] + 
                                             dp[i][k - 1] + dp[k + 1][j])
        return dp[1][n]

if __name__ == "__main__":
    print(Solution().maxCoins([3,1,5,8]))