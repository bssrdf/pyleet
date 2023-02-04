'''
-Hard-

*DP*

In a given array nums of positive integers, find three non-overlapping subarrays 
with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each 
interval (0-indexed). If there are multiple answers, return the lexicographically 
smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices 
[0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be 
lexicographically larger.
 

Note:

nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
 

'''

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """
        The question asks for three non-overlapping intervals with maximum sum of all 
        3 intervals. If the middle interval is [i, i+k-1], where k <= i <= n-2k, the 
        left interval has to be in subrange [0, i-1], and the right interval is from 
        subrange [i+k, n-1].

        So the following solution is based on DP.

        posLeft[i] is the starting index for the left interval in range [0, i];
        posRight[i] is the starting index for the right interval in range [i, n-1]; 
        Then we test every possible starting index of middle interval, i.e. 
        k <= i <= n-2k, and we can get the corresponding left and right max sum 
        intervals easily from DP. And the run time is O(n).

        Caution. In order to get lexicographical smallest order, when there are two 
        intervals with equal max sum, always select the left most one. So in the code, 
        the if condition is ">= tot" for right interval due to backward searching, 
        and "> tot" for left interval. Thanks to @lee215 for pointing this out!

        """
        n, maxsum = len(nums), 0
        sums = [0] 
        posLeft = [0] * n
        posRight = [n-k] * n 
        ans = [0]*3
        for i in nums: sums.append(sums[-1]+i)
        # DP for starting index of the left max sum interval
        tot = sums[k]-sums[0]
        for i in range(k, n):
            if sums[i+1]-sums[i+1-k] > tot: 
                posLeft[i] = i+1-k
                tot = sums[i+1]-sums[i+1-k]            
            else: 
                posLeft[i] = posLeft[i-1]
        # DP for starting index of the right max sum interval
        # caution: the condition is ">= tot" for right interval, 
        # and "> tot" for left interval
        tot = sums[n]-sums[n-k]
        for i in range(n-k-1, -1, -1):
            if sums[i+k]-sums[i] >= tot:
                posRight[i] = i
                tot = sums[i+k]-sums[i]
            else:
                posRight[i] = posRight[i+1]
        # test all possible middle interval
        for i in range(k, n-2*k+1):
            l = posLeft[i-1] 
            r = posRight[i+k]
            tot = (sums[i+k]-sums[i]) + (sums[l+k]-sums[l]) + (sums[r+k]-sums[r])
            if tot > maxsum: 
                maxsum = tot
                ans = [l, i, r]
        return ans
        

if __name__ == "__main__":
    print(Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))
