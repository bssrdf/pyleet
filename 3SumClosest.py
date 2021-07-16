'''

-Medium-

Given an array nums of n integers and an integer target, find three integers in nums such that the 
sum is closest to target. Return the sum of the three integers. You may assume that each input 
would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        res = target
        dm = float('inf')
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                sm = nums[left] + nums[right] + nums[i] 
                if sm == target: return sm
                if sm < target:                    
                    left += 1
                else:                    
                    right -= 1
                diff = abs(target-sm)    
                if dm > diff: 
                    dm = diff                
                    res = sm
        return res


        
if __name__ == "__main__":
    print(Solution().threeSumClosest([-1,2,1,-4], 1))