'''
-Medium-

Given an integer array nums, return all the different possible increasing subsequences of the given 
array with at least two elements. You may return the answer in any order.

The given array may contain duplicates, and two equal integers should also be considered a special 
case of increasing sequence.

 

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]
 

Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100

'''

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(nums, start, path):
            if len(path) >= 2:
                res.append(path[:]) 
            s = set()
            for i in range(start, len(nums)):
                # Very important here! We don't use `i > 0` because we always want 
                # to count the first element in this recursive step even if it is the same 
                # as one before. To avoid overcounting, we just ignore the duplicates
                # after the first element.
                #if i > start and nums[i] == nums[i - 1]:
                #    continue       

            # We set the start to `i+1` because one element could
            # only be used once
                if path and nums[i] < path[-1]: continue
                if nums[i] in s: continue
                s.add(nums[i])
                dfs(nums, i+1, path + [nums[i]])
        dfs(nums, 0, [])
        return res

if __name__ == "__main__":
    print(Solution().findSubsequences([4,6,7,7]))
    #print(Solution().findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]))