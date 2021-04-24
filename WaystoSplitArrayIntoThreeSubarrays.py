'''

-Medium-

A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively 
from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the 
sum of the elements in mid is less than or equal to the sum of the elements in right.

Given nums, an array of non-negative integers, return the number of good ways to split nums. 
As the number may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.
 

Constraints:

3 <= nums.length <= 10^5
0 <= nums[i] <= 10^4

'''

class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        preSum = [0]
        res = 0
        for i in nums:
            preSum.append(preSum[-1]+i)
        for k in range(n-1, 1, -1):
            for j in range(0, k-1):
               lSum = preSum[j+1] - preSum[0]
               mSum = preSum[k] - preSum[j+1] 
               rSum = preSum[n] - preSum[k]
               print(k, j, lSum, mSum, rSum)
               if lSum <= mSum <= rSum: res += 1
        return res

    def waysToSplitO_N(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        ans = j = k = 0 
        for i in range(1, len(nums)): 
            j = max(j, i+1)
            while j < len(nums) and 2*prefix[i] > prefix[j]: j += 1
            k = max(k, j)
            while k < len(nums) and 2*prefix[k] <= prefix[i] + prefix[-1]: k += 1
            ans += k - j 
        return ans % 1_000_000_007

    def waysToSplitBinarySearch(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        preSum = [0]*n
        preSum[0] = nums[0]
        res = 0
        MOD = 10**9+7
        for i in range(1, n):
            preSum[i] = preSum[i-1]+nums[i]
        for k in range(1, n-1):
            if preSum[k - 1] > (preSum[n - 1] - preSum[i - 1]) // 2: break # early termination
            lSum = preSum[k-1]
            def helper(i, searchLeft):
                ret = -1
                l, r = i, n-2
                while l <= r:
                    m = l + (r-l) // 2
                    mSum = preSum[m] - preSum[i-1]
                    rSum = preSum[n-1] - preSum[m]
                    if lSum <= mSum <= rSum:
                        ret = m
                        if searchLeft: r = m-1
                        else: l = m+1
                    elif lSum > mSum:
                        l = m+1
                    else:
                        r = m-1
                return ret
            left = helper(k, True)
            right = helper(k, False)
            if left == -1 and right == -1: continue
            res = (res + (right - left + 1) % MOD) % MOD
        return res

        

if __name__ == "__main__":
    #print(Solution().waysToSplit([1,2,2,2,5,0]))
    print(Solution().waysToSplitBinarySearch([1,2,2,2,5,0]))
    print(Solution().waysToSplitBinarySearch([1,1,1]))