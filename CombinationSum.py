'''
-Medium-

*DFS*
*Backtracking*

Given a set of candidate numbers (candidates) (without duplicates) and a 
target number (target), find all unique combinations in candidates where 
the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number 
of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, 0, [], res, target)
        return res
    
    def dfs(self, nums, start, path, result, target):
        if not target:
            result.append(path)
            return
    
    
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

        # We set the start to `i` because one element could
        # be used more than once
            self.dfs(nums, i, path + [nums[i]], 
                           result, target - nums[i])
    

print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([2,3,5], 8))