'''
-Medium-

Given an array of integers nums and a positive integer k, find whether 
it's possible to divide this array into k non-empty subsets whose sums 
are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), 
(2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
Accepted

'''
from functools import lru_cache

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = sum(nums) // k
        if sum(nums) % k != 0 or max(nums) > m: 
            return False        
        
        n = len(nums)          
        """
        We can take it as a nested recursion. The graph below shows the 
        control flow (not accurate):

        Outer recursion on k subsets:
        Base case: k == 0
        Recursive case: k > 0 
				// Inner recursion on individual subset
				Base case: curSubsetSum == targetSubsetSum (return to outer 
                recursion)
				Recursive case: curSubsetSum < targetSubsetSum
        Since the order of numbers within a subset doesn't matter, we add 
        nextIndexToCheck for the inner recursion to avoid duplicate 
        calculations.
        """  
        @lru_cache(None)        
        def dfs(picked, nsubs, curSubsetSum, nextIndexToCheck):        
            if nsubs == 0: return True      
            if curSubsetSum == m:
                # once we are done with one subset, for the next subset we are 
                # starting again with index 0 and subsetSum 0). 
                return dfs(picked, nsubs-1, 0, 0)      
            
            for i in range(nextIndexToCheck, n):  
                if picked & (1<<i) == 0 and curSubsetSum + nums[i] <= m:
                    picked |= (1<<i)  
                    if dfs(picked, nsubs, curSubsetSum + nums[i], i+1):                
                        return True                
                    picked ^= (1<<i)   
            return False
        return dfs(0, k, 0, 0)

         
if __name__ == "__main__":
    print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    print(Solution().canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3))