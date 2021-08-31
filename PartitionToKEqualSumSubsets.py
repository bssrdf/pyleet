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

    def canPartitionKSubsetsBackTrack(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        m = sum(nums) // k
        if sum(nums) % k != 0 or max(nums) > m: 
            return False 
        used = [False]*n 
        target = sum(nums) // k
        def backtrack(k, bucket, start):
            # base case
            if k == 0:
                # 所有桶都被装满了，而且 nums 一定全部用完了
                # 因为 target == sum / k
                return True
            if bucket == target :
                # 装满了当前桶，递归穷举下一个桶的选择
                # 让下一个桶从 nums[0] 开始选数字
                return backtrack(k - 1, 0, 0)

            # 从 start 开始向后探查有效的 nums[i] 装入当前桶
            for i in range(start, n):
                # 剪枝
                if used[i]:
                    # nums[i] 已经被装入别的桶中
                    continue
                if nums[i] + bucket > target:
                    # 当前桶装不下 nums[i]
                    continue
                # 做选择，将 nums[i] 装入当前桶中
                used[i] = True
                bucket += nums[i]
                #递归穷举下一个数字是否装入当前桶
                if backtrack(k, bucket, i + 1):
                    return True
                # 撤销选择
                used[i] = False
                bucket -= nums[i]
            # 穷举了所有数字，都无法装满当前桶    
            return False
        # k 号桶初始什么都没装，从 nums[0] 开始做选择        
        return backtrack(k, 0, 0)   

    def canPartitionKSubsetsWithPrune(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """     
        if len(nums) < k or sum(nums) % k != 0 or max(nums) > sum(nums) // k:
            return False
        target = sum(nums)//k

        nums.sort(reverse = True)
        edge = [0]*k

        def dfs(index):
            if index == len(nums):
                return True
            seen = [] # record the searched summ
            #seen = set()#  slower than using list??
            for i in range(k):
                if edge[i] in seen: continue
                if edge[i] + nums[index] <= target:
                    seen.append(edge[i])
                    #seen.add(edge[i])
                    edge[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    edge[i] -= nums[index]
            return False

        return dfs(0)   
         
if __name__ == "__main__":
    print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    print(Solution().canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3))
    print(Solution().canPartitionKSubsetsBackTrack([4, 3, 2, 3, 5, 2, 1], 4))
    print(Solution().canPartitionKSubsetsBackTrack([10,10,10,7,7,7,7,7,7,6,6,6], 3))