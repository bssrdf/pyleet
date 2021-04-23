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
    def waysToSplitBinarySearch(self, nums):
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
            rSum = preSum[n] - preSum[k]
            l, r = 1, k
            while l < r:
                m = l + (r-l) // 2
                if k==4: print(l, r, m, preSum[k] - preSum[m+1], rSum)
                if preSum[k] - preSum[m+1] >= rSum:
                    l = m + 1
                else:
                    r = m 
            n1 = l+1
            l, r = 1, k
            while l < r:                
                m = l + (r-l) // 2
                #if k==4: print(l, r, m, preSum[k] - preSum[m+1], preSum[m+1])
                if preSum[k] - preSum[m+1] >= preSum[m+1] - preSum[0]:
                    l = m+1
                else:
                    r = m
            n2 = l
            print(k, rSum, n1, n2)
            res += max(n2-n1+1, 0)
        return res

        

if __name__ == "__main__":
    #print(Solution().waysToSplit([1,2,2,2,5,0]))
    print(Solution().waysToSplitBinarySearch([1,2,2,2,5,0]))
    print(Solution().waysToSplitBinarySearch([1,1,1]))