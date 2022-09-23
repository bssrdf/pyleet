'''
-Medium-
*Two Pointers*
*Binary Search*
*Sliding Window*

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
import bisect
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
    
    def minSubArrayLenNlogN(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        preSum = [0]*(n+1)
        for i in range(1,n+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        res = n
        for i in range(1,n+1):
            target = s + preSum[i-1]
            l = bisect.bisect_left(preSum, target)
            if l < n+1:
                res = min(res, l - i + 1)
        return 0 if res == n+1 else res    






if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
    print(Solution().minSubArrayLenNlogN(7, [2,3,1,2,4,3]))
    print(Solution().minSubArrayLenNlogN(4, [1,4,4]))