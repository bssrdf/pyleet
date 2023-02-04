'''
-Medium-
*Binary Search*

A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors 
to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element 
mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

Example 1:



Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
Example 2:



Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
No two adjacent cells are equal.

'''

class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        startCol, endCol = 0, len(mat[0])-1
        startRow, endRow = 0, len(mat)-1
        if len(mat[0]) > len(mat):
            while startCol <= endCol:
                midCol = (endCol+startCol)//2
                maxRow = 0
                for i in range(len(mat)):
                    maxRow = i if mat[i][midCol] >= mat[maxRow][midCol] else maxRow
                leftBig = midCol-1 >= startCol and mat[maxRow][midCol-1] > mat[maxRow][midCol]
                rightBig = midCol+1 <= endCol and mat[maxRow][midCol+1] > mat[maxRow][midCol]
                if (not leftBig) and (not rightBig):
                    return [maxRow, midCol]
                elif leftBig:
                    endCol = midCol - 1
                else:
                    startCol = midCol + 1
        else:
            while startRow <= endRow:
                midRow = (endRow+startRow)//2
                maxCol = 0
                for j in range(len(mat[0])):
                    maxCol = j if mat[midRow][j] >= mat[midRow][maxCol] else maxCol
                upBig = midRow-1 >= startRow and mat[midRow-1][maxCol] > mat[midRow][maxCol]
                bottomBig = midRow+1 <= endRow and mat[midRow+1][maxCol] > mat[midRow][maxCol]
                if (not upBig) and (not bottomBig):
                    return [midRow, maxCol]
                elif upBig:
                    endRow = midRow - 1
                else:
                    startRow = midRow + 1
        return [] 



if __name__ == "__main__":
    #mat = [[10,20,15],[21,30,14],[7,16,32]]
    #print(Solution().findPeakGrid(mat))
    mat = [[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11]]
    print(Solution().findPeakGrid(mat))