'''
-Medium-

Given a set of distinct positive integers nums, return the largest subset answer 
such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 10^9
All the integers in nums are unique.


'''

from typing import List
from collections import defaultdict, Counter

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        # dp[i]表示到数字nums[i]位置最大可整除的子集合的长度
        # parent[i]，来保存上一个能整除nums[i]的数字的位置
        dp, parent = [0]*n, [0]*n
        mx, mx_idx = 0, 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if nums[j] % nums[i] == 0 and dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if mx < dp[i]:
                        mx, mx_idx = dp[i], i
                    
        for i in range(mx):
            res.append(nums[mx_idx])
            mx_idx = parent[mx_idx]
        return res         
                    




        return []            

if __name__ == "__main__":
    print(Solution().largestDivisibleSubset([1,2,4,8]))
    print(Solution().largestDivisibleSubset([1,2,3]))
    print(Solution().largestDivisibleSubset([2, 3, 4, 5, 7, 10, 12]))