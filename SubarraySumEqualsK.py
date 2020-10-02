'''

Given an array of integers and an integer k, you need to find the 
total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range 
of the integer k is [-1e7, 1e7].


'''
from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = defaultdict(int)
        n = len(nums)
        S = [0]*(n+1)
        ans = 0        
        for i,num in enumerate(nums):
            S[i+1] = S[i]+num        
        m[S[0]]+=1
        for s in S[1:]:
            if s-k in m:
                ans += m[s-k]
            m[s] += 1
        return ans
        



if __name__ == "__main__":
    print(Solution().subarraySum([1,1,1], 2))
    print(Solution().subarraySum([0,0,0,0,0,0,0,0,0,0],0))