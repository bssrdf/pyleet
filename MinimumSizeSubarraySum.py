'''
-Medium-

Given an array of n positive integers and a positive integer s, find the 
minimal length of a contiguous subarray of which the sum ≥ s. If there isn't 
one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem 
constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of 
which the time complexity is O(n log n). 

'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = n+1
        left, right, win_sum = 0, 0, 0
        while right < n:
            win_sum += nums[right]
            right += 1
            while win_sum >= s:
                ans = min(ans, right-left)
                win_sum -= nums[left]
                left += 1
        return ans if ans != n+1 else 0

if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))