'''

-Medium-
*DP*

You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

 

Example 1:

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
Example 2:

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
 

Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 103
m <= n <= 105
-1000 <= nums[i], multipliers[i] <= 1000


'''
from typing import List
from functools import lru_cache
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def dp(s, i):
            if i == len(multipliers):
                return 0
            # some explanation to get e:

            # 0            s         e           nums.size()-1
            # |____________|_________|______________|
            # You could see that if current index is i, we have already 
            # chosen i elements from nums array, then:

            # (s - 0) + (nums.size() - 1 - e) = i
            #                  e = nums.size() - 1 - (i - s)
            e = len(nums) - (i - s) - 1
            pickStart = nums[s] * multipliers[i] + dp(s + 1, i + 1) # pick left as ith
            pickEnd = nums[e] * multipliers[i] + dp(s, i + 1) # pick right as ith
            return max(pickStart, pickEnd)

        return dp(0, 0)

    def maximumScore2(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0]*m for _ in range(m+1)]
        
        for i in reversed(range(m)):
            for j in range(i, m): 
                k = i + m - j - 1
                dp[i][j] = max(nums[i] * multipliers[k] + dp[i+1][j], nums[j-m+n] * multipliers[k] + dp[i][j-1])
        
        return dp[0][-1]


    
if __name__ == "__main__":
    print(Solution().maximumScore(nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]))