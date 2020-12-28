'''
-Medium-

*Sort*

*Two Pointers*

Given an array nums of n integers and an integer target, are there elements 
a, b, c, and d in nums such that a + b + c + d = target? Find all unique 
quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
 

Constraints:

0 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n-3): # first num, index range [0, n-4]
            for j in range(i + 1, n-2): # 2nd num, index range [i+1, n-3]
                # get rid of duplicates
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                left = j + 1    # 3rd num
                right = n - 1   # 4th num
                while left < right:
                    sums = nums[i] + nums[j] + nums[left] + nums[right]
                    if sums == target:
                        out = (nums[i], nums[j], nums[left], nums[right])
                        res.add(out)
                        left += 1
                        right -= 1
                    elif sums < target: left += 1
                    else: right -= 1
        return list([list(s) for s in res])
        
if __name__ == "__main__":
    print(Solution().fourSum([1,0,-1,0,-2,2], 0))