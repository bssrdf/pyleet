'''

Given a positive integer n, generate a square matrix filled with elements 
from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """        
        
        upper, lower = 0, n-1
        left, right = 0, n-1
        matrix = [ [0 for _ in range(n)] for _ in range(n)]
        val = 1
        while True:
            for n in range(left, right+1):
                matrix[upper][n] = val
                val += 1
            upper += 1
            if upper > lower:
                break
            for n in range(upper, lower+1):
                matrix[n][right] = val
                val += 1
            right -= 1
            if right < left:
                break                
            for n in range(right, left-1, -1):
                matrix[lower][n] = val
                val += 1
            lower -= 1
            if lower < upper:
                break
            for n in range(lower, upper-1, -1):
                matrix[n][left] = val
                val += 1
            left += 1
            if left > right:
                break
        return matrix



a= Solution().generateMatrix(3)
for i in a:
    print(i)