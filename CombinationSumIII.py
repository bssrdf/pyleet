'''
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be 
a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = range(1,10)
        self.dfs(candidates, 0, [], res, k, n)
        return res
    
    def dfs(self, nums, start, path, result, n, target):
        if not target and len(path) == n:
            result.append(path)
            return    
    
        for i in range(start, len(nums)):       

        # If the current element is bigger than the assigned target, there is 
        # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
               break

        # We set the start to `i+1` because one element could
        # only be used once
            self.dfs(nums, i+1, path + [nums[i]], 
                           result, n, target - nums[i])

print(Solution().combinationSum3(3, 9))
print(Solution().combinationSum3(3, 7))