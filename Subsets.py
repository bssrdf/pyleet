
'''
Given a set of distinct integers, nums, return all possible subsets 
(the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
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
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, start, path, result):

        result.append(path[:])     
        
        for i in range(start, len(nums)):       

        # We set the start to `i+1` because one element could
        # only be used once
            path.append(nums[i])
            self.dfs(nums, i+1, path, 
                           result)
            path.pop()

print(Solution().subsets([1,2,3]))