'''

-Hard-

Given an m x n matrix matrix and an integer k, return the max sum of a 
rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

 

Example 1:


Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, 
and 2 is the max number no larger than k (k = 2).
Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 3000
1 <= m * n <= 5 * 104
-100 <= matrix[i][j] <= 100
-105 <= k <= 105
 

Follow up: What if the number of rows is much larger than the number of columns?

'''

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:  return 0
        
        res = float('-inf')
        rows, columns = len(matrix), len(matrix[0])
        for i in range(columns):
            sums = [0 for _ in range(rows)]
            for j in range(i, columns):
                for r in range(rows):
                    sums[r] += matrix[r][j]

                # find the largest sum of a subarray which is no more than K
                import bisect
                cum_sum = [0]
                cum, max_sum = 0, float('-inf')
                for item in sums:
                    cum += item
                    left = bisect.bisect_left(cum_sum, cum - k)
                    if left < len(cum_sum):
                        max_sum = max(max_sum, cum - cum_sum[left])
                    bisect.insort(cum_sum, cum)

                res = max(res, max_sum)

        return res

if __name__ == "__main__":
    print(Solution().maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))

