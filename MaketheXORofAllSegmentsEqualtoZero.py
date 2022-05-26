'''

-Hard-
*DP*

You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].

Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.

 

Example 1:

Input: nums = [1,2,0,3,0], k = 1
Output: 3
Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].
Example 2:

Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
Output: 3
Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].
Example 3:

Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
Output: 3
Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].
 

Constraints:

1 <= k <= nums.length <= 2000
​​​​​​0 <= nums[i] < 2^10

'''

from typing import List
from collections import defaultdict

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # TLE
        dp = [[0]*1024 for _ in range(2000)]
        totalCnt = [0]*2000
        count = [[0]*1024 for _ in range(2000)]
        n = len(nums)
        for i in range(k):
            for j in range(i, n, k):
                totalCnt[i] += 1
                count[i][nums[j]] += 1
        for d in range(1024):
            dp[0][d] = totalCnt[0] - count[0][d]
        for i in range(1,k): 
            minCost = float('inf')            
            for d in range(1024):
                if dp[i-1][d] < minCost:
                    minCost =  dp[i-1][d]
                    minCostD = d                    
            for d in range(1024):
                dp[i][d] = minCost + totalCnt[i] - count[i][d^minCostD]
                for j in range(i, n, k):
                    dp[i][d] = min(dp[i][d], dp[i-1][d^nums[j]] + totalCnt[i] - count[i][nums[j]])

        return dp[k-1][0]

    def minChanges2(self, nums: List[int], k: int) -> int:
        LIMIT = 2**10
   
        mrr = [[0 for _ in range(LIMIT)] 
               for _ in range(k)]
        for i,x in enumerate(nums):
            mrr[i%k][x] += 1

        dp = [-2000 for _ in range(LIMIT)]
        dp[0] = 0
        for row in mrr:
            maxprev = max(dp)
            new_dp = [maxprev for _ in range(LIMIT)]
            for i,cnt in enumerate(row):
                if cnt > 0:
                    for j,prev in enumerate(dp):
                        new_dp[i^j] = max(new_dp[i^j], prev+cnt)
            dp = new_dp

        return len(nums) - new_dp[0]

    def minChanges3(self, nums: List[int], k: int) -> int:
        freq = [defaultdict(int) for _ in range(k)]
        for i,num in enumerate(nums):
            freq[i%k][num] += 1

        max_save = []
        for i in range(k):
            max_save.append(max(freq[i].values()))

        max_save_suffix = max_save[::]
        for i in range(k-2,-1,-1):
            max_save_suffix[i] += max_save_suffix[i+1]
		###case 1 : choose k-1 num
        self.save = max_save_suffix[0] - min(max_save)
        ###case 2 : choose k num
        def DFS(i,state,cur_save):
            if i == k:
                if state == 0:
                    self.save = max(self.save,cur_save)
            else:
                if cur_save + max_save_suffix[i] > self.save:  ### pruning
                    for num in freq[i]:
                        DFS(i+1,state^num,cur_save+freq[i][num])
                      
        DFS(0,0,0)
        return len(nums)-self.save 

    

    




if __name__ == "__main__":
    print(Solution().minChanges(nums = [1,2,0,3,0], k = 1))