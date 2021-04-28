'''

Given an integer array nums, return the number of range sums that lie 
in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between
indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective 
sums are: -2, -1, 2.

'''
import bisect

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        """
        Recall "count smaller number after self" where we encountered the problem

        count[i] = count of nums[j] - nums[i] < 0 with j > i
        
        Here, after we preprocessed the array, we need to solve the problem

        count[i] = count of a <= S[j] - S[i] <= b with j > i
        ans = sum(count[:])
        """
        first = [0]
        for num in nums:
           first.append(first[-1] + num)
        def sort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            '''
            The merge sort based solution counts the answer while doing the merge.     
            During the merge stage, we have already sorted the left half 
            [start, mid) and right half [mid, end).    
            '''
            count = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            '''            
            We then iterate through the left half with index left. For each left, 
            we need to find two indices i and j in the right half where

            j is the first index satisfy sums[j] - sums[i] > upper and
            i is the first index satisfy sums[k] - sums[i] >= lower.

            Then the number of sums in [lower, upper] is j-k
            '''
            for left in first[lo:mid]:
                while i < hi and first[i] - left <  lower: i += 1
                while j < hi and first[j] - left <= upper: j += 1
                count += j - i
            first[lo:hi] = sorted(first[lo:hi])
            return count
        return sort(0, len(first))


    def countRangeSumBIT(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """    
        n = len(nums)
        Sum, BITree = [0] * (n + 1), [0] * (n + 2)
        
        def count(x):
            s = 0
            while x:
                s += BITree[x]
                x -= (x & -x)
            return s
        
        def update(x):
            while x <= n + 1:
                BITree[x] += 1
                x += (x & -x)
                
        for i in range(n):
            Sum[i + 1] = Sum[i] + nums[i]
        sortSum, res = sorted(Sum), 0
        for sum_j in Sum:
            sum_i_count = count(bisect.bisect_right(sortSum, sum_j - lower)) - count(bisect.bisect_left(sortSum, sum_j - upper))
            res += sum_i_count
            update(bisect.bisect_left(sortSum, sum_j) + 1)
        return res

print(Solution().countRangeSum([-2,5,-1], -2, 2))
print(Solution().countRangeSumBIT([-2,5,-1], -2, 2))