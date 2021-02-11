# -*- coding: utf-8 -*-
"""
-Medium-

*Divide & Conquer*
*Priority Queue*

Find the kth largest element in an unsorted array. Note that it is the kth 
largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
__author__ = 'Daniel'
import heapq

from random import randint

class Solution:
    def findKthLargest(self, nums, k):
        """
        Algorithm:
        * Partial quick sort average O(n), worst case O(n^2)        

        :rtype: int
        """
                    
        def partition(p, r):           
            x = nums[r]
            i = p-1
            for j in range(p,r):
                if nums[j] < x:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1],nums[r] = nums[r], nums[i+1]    
            return i+1     

        def random_partition(p,r):
            ri = randint(p,r)
            nums[ri], nums[r] = nums[r], nums[ri]
            return partition(p, r)     

        def select(p, r, k):
            # returns kth smallest
            if p == r:
                return nums[p]
            q = random_partition(p, r)
            i = q-p+1
            if i == k:
                return nums[q]
            elif k < i:
                return select(p, q-1, k)
            else:
                return select(q+1, r, k-i)
        n = len(nums)    
        return select(0, n-1, n-k+1)   


    def findKthLargestPQ(self, nums, k):
        """
        Algorithm:
        * Heap O(n lg k), kth largest element is the smallest one in the 
        k-size min-heap.

        :rtype: int
        """
        n = len(nums)
        pq = []
        for i in range(k):
            heapq.heappush(pq, nums[i])        
        for i in range(k, n):
            heapq.heappush(pq, nums[i])
            heapq.heappop(pq)
        return pq[0]



if __name__ == "__main__":
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(Solution().findKthLargestPQ([3, 2, 1, 5, 6, 4], 2))

