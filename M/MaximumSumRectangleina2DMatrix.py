'''
-Hard-

Given a 2D array, find the maximum sum subarray in it. For example, 
in the following 2D array, the maximum sum subarray is highlighted with 
blue rectangle and sum of this subarray is 29.


'''

class Solution(object):
    def maxSumSubmatrix(self, matrix):
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
                # Kadane's Algorithm    
                cur_sum = 0
                max_sum = 0
                for item in sums:
                    cur_sum = max(0, cur_sum+item)
                    max_sum = max(max_sum, cur_sum)
                res = max(res, max_sum)

        return res

if __name__ == "__main__":
    matrix= [[6, -5, -7, 4, -4],
             [-9,  3, -6, 5, 2],
             [-10, 4, 7, -6, 3],
             [-8, 9, -3, 3, -7]]
    print(Solution().maxSumSubmatrix(matrix))

