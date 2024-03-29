'''
-Medium-


Given two integer arrays nums1 and nums2 of length n, count the pairs of indices (i, j) such 
that i < j and nums1[i] + nums1[j] > nums2[i] + nums2[j].

Return the number of pairs satisfying the condition.

Example 1:

Input: nums1 = [2,1,2,1], nums2 = [1,2,1,2]

Output: 1

Explanation: The pairs satisfying the condition are:

(0, 2) where 2 + 2 > 1 + 1.
Example 2:

Input: nums1 = [1,10,6,2], nums2 = [1,4,1,5]

Output: 5

Explanation: The pairs satisfying the condition are:

(0, 1) where 1 + 10 > 1 + 4.
(0, 2) where 1 + 6 > 1 + 1.
(1, 2) where 10 + 6 > 4 + 1.
(1, 3) where 10 + 2 > 4 + 5.
(2, 3) where 6 + 2 > 1 + 5.
Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
1 <= nums1[i], nums2[i] <= 10^5

'''

import bisect

class Solution:
    def countPairs(self, nums1, nums2):
        # O(Nlog(N))
        # Create an array differences with length n such that differences[i] = nums1[i] - nums2[i] for 
        # all 0 <= i < n. Sort differences. For each 0 <= i < n - 1, find the minimum index such that 
        # differences[index] + differences[i] > 0, or index = n if differences[n - 1] + differences[i] <= 0, 
        # and the number of j’s for the current i is n - index. In this way, the number of pairs of 
        # indices (i, j) can be calculated.
        n = len(nums1)
        diff = [nums1[i]-nums2[i] for i in range(n)]
        diff.sort()
        res = 0
        def binarySearch(target, startIndex): 
            low = startIndex
            high = n - 1
            if diff[high] < target:
                return n
            while low < high:
                mid = (high - low) // 2 + low
                if diff[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low
        for i in range(n-1):
            #target = nums2[i]-nums1[i]+1
            target = -diff[i]+1
            idx = bisect.bisect_left(diff, target, i+1)            
            res += n - idx
        return res

if __name__ == '__main__':
     nums1 = [2,1,2,1]; nums2 = [1,2,1,2]
     print(Solution().countPairs(nums1, nums2))
     nums1 = [1,10,6,2]; nums2 = [1,4,1,5]
     print(Solution().countPairs(nums1, nums2))


