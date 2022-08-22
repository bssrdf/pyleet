
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
    

    def subsets2(self, nums):
        # iterative
        A = nums
        n = len(A)        
        res = [[], [A[0]]]
        for i in range(1,n):
            tmp = []
            for j in range(1<<(i-1)):
                tmp.append(res[-(j+1)][:-1]+[A[i]])
                tmp.append(res[-(j+1)]+[A[i]])
            res += tmp    
        return res



print(Solution().subsets([1,2,3]))
print(Solution().subsets2([1,2,3]))