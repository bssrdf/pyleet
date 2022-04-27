'''
-Hard-
*Fenwick Tree*

You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are 
permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing order 
by position both in nums1 and nums2. In other words, if we consider pos1v as the 
index of the value v in nums1 and pos2v as the index of the value v in nums2, 
then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such 
that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

Return the total number of good triplets.

 

Example 1:

Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
Output: 1
Explanation: 
There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.
Example 2:

Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
Output: 4
Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).
 

Constraints:

n == nums1.length == nums2.length
3 <= n <= 105
0 <= nums1[i], nums2[i] <= n - 1
nums1 and nums2 are permutations of [0, 1, ..., n - 1].

'''
from typing import List
from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = nums1, nums2
        # Index of a (from A) in B.
        pos = [0] * len(A)               
        for idx, b in enumerate(B):
            pos[b] = idx
        
        # Build pre_a[i]: number of elements on a[i]'s left in both A and B.
        # pos_in_b: sorted indexes (in B) of all the visited elements in A.
        pos_in_b, pre_a = SortedList([pos[A[0]]]), [0]      
        for a in A[1:]:       
            pos_in_b.add(pos[a])
            pre_a.append(pos_in_b.bisect_left(pos[a]))
    
        # Build suf_a[i]: number of elements on a[i]'s right in both A and B.
        pos_in_b, suf_a = SortedList([pos[A[-1]]]), [0]
        for a in reversed(A[:len(A)-1]):
            idx = pos_in_b.bisect(pos[a])
            suf_a.append(len(pos_in_b) - idx)
            pos_in_b.add(pos[a])
        suf_a.reverse()
        
        # Sum up all unique triplets centered on A[i].
        ans = 0
        for x, y in zip(pre_a, suf_a):
            ans += x * y
        return ans

    def goodTriplets2(self, nums1: List[int], nums2: List[int]) -> int:
        A, B, n = nums1, nums2, len(nums1)
        # Index of a (from A) in B.
        pos = [0] * len(A)         
        BIT = [0]*(n+1) 
        def update(x, val):
            while x < n:
                BIT[x] += val 
                x += x & (-x)
        def query(x):
            sums = 0
            while x > 0:
                sums += BIT[x]
                x -= x & (-x)
            return sums                
        for idx, b in enumerate(B, start=1):
            pos[b] = idx
        pre_a = []        
        for a in A:                   
            pre_a.append(query(pos[a]))
            update(pos[a], 1)        
        BIT = [0]*(n+1) 
        suf_a = []
        pos = [0]*n         
        for idx, b in enumerate(B[::-1], start=1):
            pos[b] = idx
        for a in A[::-1]:                   
            suf_a.append(query(pos[a]))
            update(pos[a], 1)        
        # suf_a.reverse()
        ans = 0
        for x, y in zip(pre_a, suf_a[::-1]):
            ans += x * y
        return ans
        



if __name__ == "__main__":
    nums1 = [2,0,1,3]; nums2 = [0,1,2,3]
    # print(Solution().goodTriplets(nums1, nums2))
    print(Solution().goodTriplets2(nums1, nums2))
    nums1 = [4,0,1,3,2]; nums2 = [4,1,0,2,3]
    # print(Solution().goodTriplets(nums1, nums2))
    print(Solution().goodTriplets2(nums1, nums2))
