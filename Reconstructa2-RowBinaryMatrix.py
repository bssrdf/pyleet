'''
-Medium-


Given the following details of a matrix with n columns and 2 rows :

The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
The sum of elements of the 0-th(upper) row is given as upper.
The sum of elements of the 1-st(lower) row is given as lower.
The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is 
given as an integer array with length n.
Your task is to reconstruct the matrix with upper, lower and colsum.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.

 

Example 1:

Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]
Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
Example 2:

Input: upper = 2, lower = 3, colsum = [2,2,1,1]
Output: []
Example 3:

Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
 

Constraints:

1 <= colsum.length <= 10^5
0 <= upper, lower <= colsum.length
0 <= colsum[i] <= 2


'''

from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        ans = [[0]*n for _ in range(2)]
        total = sum(colsum)
        if total != upper + lower: return []
        for j,c in enumerate(colsum):
            if c == 2:
                ans[0][j] = ans[1][j] = 1
                upper -= 1
                lower -= 1
                total -= 2
                if upper < 0 or lower < 0:
                    return []       
        for j,c in enumerate(colsum):
            if c == 1:
                if upper > 0:
                    ans[0][j] = 1
                    upper -= 1
                else:
                    ans[1][j] = 1
                    lower -= 1
        return ans

        

                

if __name__ == "__main__":
    #print(Solution().reconstructMatrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]))
    #print(Solution().reconstructMatrix(upper = 2, lower = 3, colsum = [2,2,1,1]))
    #print(Solution().reconstructMatrix(upper = 2, lower = 1, colsum = [1,1,1]))
    mat = Solution().reconstructMatrix(upper = 9, lower = 2, colsum = [0,1,2,0,0,0,0,0,2,1,2,1,2])
    for r in mat:
        print(r)