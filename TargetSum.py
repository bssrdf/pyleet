'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, 
S. Now you have 2 symbols + and -. For each integer, you should choose one 
from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to 
target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
 

Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

'''
from functools import lru_cache

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        #dp = [{} for i in range(n)]   
        @lru_cache(None)      
        def dfs(i, s):
            if i == n:
                return 1 if s == 0 else 0              
            #if s in dp[i]: return dp[i][s]            
            l1 = dfs(i+1, s+nums[i])
            l2 = dfs(i+1, s-nums[i])
            #dp[i][s] = l1 + l2  
            #return dp[i][s]
            return l1+l2

        return dfs(0, S)

if __name__ == "__main__":
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))