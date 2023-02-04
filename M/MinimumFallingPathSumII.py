'''
-Hard-
*DP*

Given a square grid of integers arr, a falling path with non-zero shifts is a choice of 
exactly one element from each row of arr, such that no two elements chosen in adjacent 
rows are in the same column.

Return the minimum sum of a falling path with non-zero shifts.

 

Example 1:

Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
 

Constraints:

1 <= arr.length == arr[i].length <= 200
-99 <= arr[i][j] <= 99
'''


class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        matrix = arr
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]
        min1, min2 = float('inf'), float('inf')
        min1_idx  = -1
        for j in range(n):
            dp[n-1][j] = matrix[n-1][j]
            if dp[n-1][j] < min1:
                min2 = min1
                min1 = dp[n-1][j]
                min1_idx = j
            elif dp[n-1][j] < min2:
                min2 = dp[n-1][j]
        for i in range(n-2, -1, -1):
            min1n, min2n = float('inf'), float('inf')
            min1_idxn = -1
            for j in range(n):
                dp[i][j] = matrix[i][j] + (min1 if j != min1_idx else min2)
                if dp[i][j] < min1n:
                    min2n = min1n
                    min1n = dp[i][j]
                    min1_idxn = j                    
                elif dp[i][j] < min2n:
                    min2n = dp[i][j]
            min1, min2 = min1n, min2n
            min1_idx = min1_idxn
        return min(dp[0][j] for j in range(n))

    def minFallingPathSumOnSpace(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        matrix = arr
        n = len(matrix)
        dp = [0 for _ in range(n)]
        min1, min2 = float('inf'), float('inf')
        min1_idx  = -1
        for j in range(n):
            dp[j] = matrix[n-1][j]
            if dp[j] < min1:
                min2 = min1
                min1 = dp[j]
                min1_idx = j
            elif dp[j] < min2:
                min2 = dp[j]
        for i in range(n-2, -1, -1):
            min1n, min2n = float('inf'), float('inf')
            min1_idxn = -1
            for j in range(n):
                dp[j] = matrix[i][j] + (min1 if j != min1_idx else min2)
                if dp[j] < min1n:
                    min2n = min1n
                    min1n = dp[j]
                    min1_idxn = j                    
                elif dp[j] < min2n:
                    min2n = dp[j]
            min1, min2 = min1n, min2n
            min1_idx = min1_idxn
        return min(dp)



        
if __name__ == "__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().minFallingPathSum(arr))
    print(Solution().minFallingPathSumOnSpace(arr))
    arr = [[50,-18,-38,39,-20,-37,-61,72,22,79],
           [82,26,30,-96,-1,28,87,94,34,-89], 
           [55,-50,20,76,-50,59,-58,85,83,-83],
           [39,65,-68,89,-62,-53,74,2,-70,-90],
           [1,57,-70,83,-91,-32,-13,49,-11,58],
           [-55,83,60,-12,-90,-37,-36,-27,-19,-6],
           [76,-53,78,90,70,62,-81,-94,-32,-57],
           [-32,-85,81,25,80,90,-24,10,27,-55],
           [39,54,39,34,-45,17,-2,-61,-81,85],
           [-77,65,76,92,21,68,78,-13,39,22]] 
    print(Solution().minFallingPathSum(arr))
    print(Solution().minFallingPathSumOnSpace(arr))