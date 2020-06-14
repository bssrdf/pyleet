'''
Find the contiguous subarray within an array (containing at least one number) which has 
he largest sum less than or equal to K

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''
import sys
import bisect
class Solution(object):
    def maxSubArray(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0    
        if not nums:
            return res
        for i in range(len(nums)):
            su = [0]   
            cum = 0         
            for j in range(i, len(nums)):
               cum += nums[j]               
               bisect.insort(su, cum)
               l = bisect.bisect_left(su, cum-k) 
               res = max(res, cum-su[l])
        return res

if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4], 7))
    print(Solution().maxSubArray([10], 5))