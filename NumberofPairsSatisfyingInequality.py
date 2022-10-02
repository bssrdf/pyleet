'''
-Hard-
*BIT*
*Fenwick Tree*


You are given two 0-indexed integer arrays nums1 and nums2, each of size n, and an integer diff. Find the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
Return the number of pairs that satisfy the conditions.

 

Example 1:

Input: nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
Output: 3
Explanation:
There are 3 pairs that satisfy the conditions:
1. i = 0, j = 1: 3 - 2 <= 2 - 2 + 1. Since i < j and 1 <= 1, this pair satisfies the conditions.
2. i = 0, j = 2: 3 - 5 <= 2 - 1 + 1. Since i < j and -2 <= 2, this pair satisfies the conditions.
3. i = 1, j = 2: 2 - 5 <= 2 - 1 + 1. Since i < j and -3 <= 2, this pair satisfies the conditions.
Therefore, we return 3.
Example 2:

Input: nums1 = [3,-1], nums2 = [-2,2], diff = -1
Output: 0
Explanation:
Since there does not exist any pair that satisfies the conditions, we return 0.
 

Constraints:

n == nums1.length == nums2.length
2 <= n <= 105
-104 <= nums1[i], nums2[i] <= 104
-104 <= diff <= 104

'''
from typing import List
import bisect
from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        A = [a-b for a,b in zip(nums1, nums2)]
        n = len(A)
        BIT = [0]*(n+1) 
        Asort = sorted(A)
        # print(A, Asort) 
        def update(x, val):
            while x <= n:
                BIT[x] += val 
                x += x & (-x)
        def query(x):
            sums = 0
            while x > 0:
                sums += BIT[x]
                x -= x & (-x)
            return sums                
        ans = 0
        for a in A:
            idx1 = bisect.bisect_right(Asort, a+diff)
            ans += query(idx1)
            # print(idx1, BIT)
            idx = bisect.bisect_right(Asort, a)
            update(idx, 1)
            # print(ans, a, idx, BIT)
        return ans


    def numberOfPairs2(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        A = [a-b for a,b in zip(nums1, nums2)]
        sl = SortedList()
        ans = 0
        for a in A:
            ans += sl.bisect_right(a+diff)
            sl.add(a)
        return ans     



if __name__ == "__main__":
    print(Solution().numberOfPairs(nums1 = [3,2,5], nums2 = [2,2,1], diff = 1))
    print(Solution().numberOfPairs(nums1 = [3,-1], nums2 = [-2,2], diff = -1))    
    print(Solution().numberOfPairs(nums1 = [5,-3,-4], nums2 = [1,-5,5], diff = 2))    
    print(Solution().numberOfPairs2(nums1 = [3,2,5], nums2 = [2,2,1], diff = 1))
    print(Solution().numberOfPairs2(nums1 = [3,-1], nums2 = [-2,2], diff = -1))    
    print(Solution().numberOfPairs2(nums1 = [5,-3,-4], nums2 = [1,-5,5], diff = 2))    
