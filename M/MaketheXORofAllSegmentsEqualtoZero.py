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
from collections import defaultdict, Counter
from functools import reduce
from itertools import accumulate

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
    
    def minChanges4(self, nums: List[int], k: int) -> int:
        # special cases when k < 3 or k== len(nums)
        if k == 1:
            return len(nums) - nums.count(0)
        if k == 2:
            return len(nums) - Counter(nums).most_common(1)[0][1]
        if len(nums) == k:
            return 0 if reduce(lambda x, y: x ^ y, nums, 0) == 0 else 1

        # get the Counter for each position in [0 ... k-1]
        # sort it based on the length so that we can reduce the combinations since the order doesn't matter
        counters = sorted([Counter(nums[i::k]).most_common() for i in range(k)], key=lambda x:len(x))

        # If the full solution requires one position to have all its values changed, that position will be
        # one that minimizes the maximum frequency of its elements, and should be the final checked counter
        minMaxFreq = min(cc[0][1] for cc in counters)
        for i in range(k-1,-1,-1):
            if counters[i][0][1] == minMaxFreq:
                final_counter = Counter(dict(counters.pop(i)))
                break

        # cache the accumulated max possible sum of counts for the rest of the columns
        maxRemainingVal = list(accumulate([cc[0][1] for cc in reversed(counters)], initial=minMaxFreq))[::-1]

        self._max = 0

        # pos: position in [0:k]; val: previous XOR; running_tot: previous total counts
        def countXOR(pos=0, val=0, running_tot=0):
            if pos == k - 1:
                self._max = max(self._max, final_counter[val] + running_tot)
            else:
                best_score_remaining = maxRemainingVal[pos+1] + running_tot
                for elem, freq in counters[pos]:
                    if freq + best_score_remaining > self._max:
                        countXOR(pos+1, val^elem, running_tot+freq)
                    else:
                        break

        countXOR()
        return len(nums) - self._max


    

    




if __name__ == "__main__":
    print(Solution().minChanges(nums = [1,2,0,3,0], k = 1))