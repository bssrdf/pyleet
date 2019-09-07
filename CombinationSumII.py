
'''
Given a collection of candidate numbers (candidates) and a target number 
(target), find all unique combinations in candidates where the candidate 
numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''


class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if i > start and nums[i] == nums[i - 1]:
               continue

        # If the current element is bigger than the assigned target, there is 
        # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
               break

        # We set the start to `i+1` because one element could
        # only be used once
            self.dfs(nums, i+1, path + [nums[i]], 
                           result, target - nums[i])

print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))