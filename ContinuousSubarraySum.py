'''

-Medium-
*Hash Table*

Given a list of non-negative numbers and a target integer k, write a 
function to check if the array has a continuous subarray of size at 
least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and 
sums up to 6.

Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of 
size 5 and sums up to 42.
 

Constraints:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a 
signed 32-bit integer.
'''

from collections import defaultdict

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = set()
        p = defaultdict(int)
        n = len(nums)
        S = [0]*(n+1)        
        for i,num in enumerate(nums):
            S[i+1] = S[i]+num             
        m.add(S[0])
        p[S[0]] = 0               
        for i in range(1,n+1):
            t = S[i]%k if k != 0 else S[i]
            if t in m and t in p and i-p[t]>=2:              
                return True
            m.add(t)
            if t in p:
                p[t] = min(p[t], i) 
            else:
                p[t] = i

        return False

    def checkSubarraySum2(self, nums, k):
        p = defaultdict(int)
        n = len(nums)
        S = 0
        p[S] = 0 
        
        for i in range(1,n+1):
            S += nums[i-1]
            t = S%k if k != 0 else S
            if t in p and i-p[t]>=2:              
                return True
            if t in p:
                p[t] = min(p[t], i) 
            else:
                p[t] = i
        return False


if __name__ == "__main__":
    print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(Solution().checkSubarraySum2([23, 2, 4, 6, 7], 6))
    print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 0))
    print(Solution().checkSubarraySum2([23, 2, 4, 6, 7], 0))
    print(Solution().checkSubarraySum([0,0], 0))
    print(Solution().checkSubarraySum2([0,0], 0))
    print(Solution().checkSubarraySum([0,1,0,3,0,4,0,4,0], 5))
    print(Solution().checkSubarraySum2([0,1,0,3,0,4,0,4,0], 5))
    


