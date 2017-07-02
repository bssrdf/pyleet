"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in
the matrix.

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
    def kthSmallest(self, matrix, k):
        """
        Heap of list
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo,hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi)/2
            loc = self.countLower(matrix, mid)
            print mid, loc
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def countLower(self, matrix, num):
        i, j = len(matrix)-1, 0
        cnt = 0
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j] <= num:
                cnt += i+1
                j += 1
            else:
                i -= 1
            print i, j, cnt
        return cnt

if __name__ == "__main__":
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    #print Solution().kthSmallest(matrix, k)
    Solution().countLower(matrix, 8)
