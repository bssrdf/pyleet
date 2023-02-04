"""
-Medium-
*Heap*
*Binary Search*

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find 
the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 <= k <= n2.
"""
import heapq


__author__ = 'Daniel'


class Solution(object):
    def kthSmallestHeap(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        ans = None
        for _ in range(k):
            ans, i, j = heapq.heappop(q)            
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
            if j == 0 and i+1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
        return ans
    
    def kthSmallest(self, matrix, k):
        """
        Heap of list
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo,hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi)//2
            loc = self.countLower(matrix, mid)
            #print(mid, loc)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def countLower(self, matrix, num):
        """ count how many elements in the matrix <= num """
        i, j = len(matrix)-1, 0
        #print(i,j)
        cnt = 0
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j] <= num:
                cnt += i+1
                j += 1
            else:
                i -= 1
        #   print(i, j, cnt)
        return cnt

if __name__ == "__main__":
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    #print Solution().kthSmallest(matrix, k)
    print(Solution().kthSmallestHeap(matrix, k))
    matrix = [[1,3,5],
              [6,7,12],
              [11,14,14]]
    print(Solution().kthSmallestHeap(matrix, 6))
