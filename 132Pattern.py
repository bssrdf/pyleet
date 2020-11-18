'''
-Medium-

*Monotonic Queue*

Given an array of n integers nums, a 132 pattern is a subsequence of three 
integers nums[i], nums[j] and nums[k] such that i < j < k and 
nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or 
the O(n) solution?

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: 
[-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109

'''

from collections import deque

class Solution(object):

    def find132patternN2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)                
        mn = 10**10
        for j in range(n):            
            mn = min(mn, nums[j])
            if mn == nums[j]: continue
            for k in range(n-1, j, -1):
                if nums[k] > mn and nums[k] < nums[j]:
                    return True                            
        return False

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)        
        st = []
        third = -10**10
        for i in range(n-1, -1, -1):
            if nums[i] < third: # we found an i element, return
                return True
            # the monotonic stack contains all the j elements that 
            # are larger than third (k element)
            while st and nums[st[-1]] < nums[i]:
                third = nums[st.pop()]                               
            st.append(i)           
        return False

if __name__ == "__main__":
    #'''
    print(Solution().find132pattern([1,2,3,4]))
    print(Solution().find132pattern([3,1,4,2]))
    print(Solution().find132pattern([-1,3,2,0]))
    print(Solution().find132pattern([1,0,1,-4,-3]))
    #'''
    print(Solution().find132pattern([3,5,0,3,4]))

    print(Solution().find132patternN2([1,2,3,4]))
    print(Solution().find132patternN2([3,1,4,2]))
    print(Solution().find132patternN2([-1,3,2,0]))
    print(Solution().find132patternN2([1,0,1,-4,-3]))
    #'''
    print(Solution().find132patternN2([3,5,0,3,4]))