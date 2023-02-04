'''
-Hard-
*DP*
You are given an integer array nums.

You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, 
and average(A) == average(B).

Return true if it is possible to achieve that and false otherwise.

Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
Example 2:

Input: nums = [3,1]
Output: false
 

Constraints:

1 <= nums.length <= 30
0 <= nums[i] <= 10^4



'''
from typing import List
from functools import lru_cache

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        m, totalSum = n//2, sum(nums)
        # early pruning
        # if the array of size n can be splitted into group A and B with same mean, 
        # assuming A is the smaller group, then
        # totalSum/n = Asum/k = Bsum/(n-k), where k = A.size() and 1 <= k <= n/2;
        # Asum = totalSum*k/n, which is an integer. So we have totalSum*k%n == 0;
        isPossible = False
        for i in range(1, m+1): 
            if totalSum*i%n == 0:  
                isPossible = True
                break
        if not isPossible: return False
        # DP like knapsack
        # If there are still some k valid after early pruning by checking totalSum*k%n == 0,
        # we can generate all possible combination sum of k numbers from the array using DP, 
        # like knapsack problem. (Note: 1 <= k <= n/2)
        # Next, for each valid k, simply check whether the group sum, i.e. totalSum * k / n, exists 
        # in the kth combination sum hashset.

        # vector<vector<unordered_set<int>>> sums(n, vector<unordered_set<int>>(n/2+1));
        # sums[i][j] is all possible combination sum of j numbers from the subarray A[0, i];
        sums = [set() for _ in range(m+1)]
        sums[0].add(0)
        for num in nums:
            for i in range(m, 0, -1): 
                for t in sums[i-1]: 
                    sums[i].add(t + num)
            #for s in sums:
            #    print(s)
            #print('----')
        for i in range(1, m+1): 
            if totalSum*i%n == 0 and totalSum*i//n in sums[i]: return True
        return False

    def splitArraySameAverage2(self, nums: List[int]) -> bool:
        # correct but TLE without using cache
        n = len(nums)
        nums.sort()
        m, totalSum = n//2, sum(nums)
        @lru_cache(None)  # changing from brute-force to memoization can pass all test cases                  
        def combinationSum(start, target, k):
            # check if sum of combination of k numbers equals to target             
            if k == 0: return target == 0
            if target < k*nums[start]: return False            
            for j in range(start, n-k+1):
                if j > start and nums[j] == nums[j-1]: continue
                if nums[j] > target: break
                if combinationSum(j+1, target-nums[j], k-1):
                    return True                    
            return False
        '''
        # recursion function for Combination Sum problem 
        # aside from nums, path and result which are specific to Combination Sum
        # the same start and target are also used here, plus an additional k argument
        # 
        def dfs(self, nums, start, path, result, target):
            if not target:
                result.append(path)
                return   
            
            # NOTE the ending index is different in SplitArray
            # at each recursion level, the ending index is determined by the k arguments
              
            for i in range(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want 
            # to count the first element in this recursive step even if it is the same 
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
                #if i > start and nums[i] == nums[i - 1]:
                #   continue

            # If the current element is bigger than the assigned target, there is 
            # no need to keep searching, since all the numbers are positive
                if nums[i] > target:
                    break
            
            # same 2 optimizations are used
            #  
            # We set the start to `i` because one element could
            # be used more than once
            # NOTE the differece from SplitArray which starts at i+1
                self.dfs(nums, i, path + [nums[i]], 
                            result, target - nums[i])
        '''
    
        for i in range(1, m+1):
            if totalSum*i%n == 0 and combinationSum(0, totalSum*i//n, i):
                return True
        return False            
    
        
if __name__ == "__main__":
    print(Solution().splitArraySameAverage([1,2,3,4,5,6,7,8]))
    print(Solution().splitArraySameAverage2([1,2,3,4,5,6,7,8]))
    print(Solution().splitArraySameAverage([3,1,2]))
    print(Solution().splitArraySameAverage2([3,1,2]))
    print(Solution().splitArraySameAverage([0,13,13,7,5,0,10,19,5]))
    print(Solution().splitArraySameAverage2([0,13,13,7,5,0,10,19,5]))
    nums = [5000,5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5114,5115,5116,5117,5118,5119,5120,5121,5122,5123,5124,5125,5126,5127,6128,7724]
    print(Solution().splitArraySameAverage(nums))
    print(Solution().splitArraySameAverage2(nums))
    nums = [9990, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
    print(Solution().splitArraySameAverage(nums))
    print(Solution().splitArraySameAverage2(nums))
    nums = [120, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
    print(Solution().splitArraySameAverage(nums))
    print(Solution().splitArraySameAverage2(nums))