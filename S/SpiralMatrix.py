'''
-Medium-

Given a matrix of m x n elements (m rows, n columns), return all elements of the 
matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m,n = len(matrix), len(matrix[0])        
        ans = []
        upper, lower = 0, m-1
        left, right = 0, n-1
        while True:
            for n in range(left, right+1):
                ans.append(matrix[upper][n])
            upper += 1
            if upper > lower:
                break
            for n in range(upper, lower+1):
                ans.append(matrix[n][right])
            right -= 1
            if right < left:
                break                
            for n in range(right, left-1, -1):
                ans.append(matrix[lower][n])
            lower -= 1
            if lower < upper:
                break
            for n in range(lower, upper-1, -1):
                ans.append(matrix[n][left])
            left += 1
            if left > right:
                break
        return ans





a = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
  ]

print(Solution().spiralOrder(a))
