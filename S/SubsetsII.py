
'''
Given a collection of integers that might contain duplicates, 
nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''


class Solution(object):
    def subsets(self, nums):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = [] 
        nums.sort()       
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, start, path, result):

        result.append(path)     
        
        for i in range(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want 
            # to count the first element in this recursive step even if it is the same 
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
               continue       

        # We set the start to `i+1` because one element could
        # only be used once
            self.dfs(nums, i+1, path + [nums[i]], 
                           result)


print(Solution().subsets([1,2,2]))