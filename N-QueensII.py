'''


'''

'''
The n-queens puzzle is the problem of placing n queens on an n×n 
chessboard such that no two queens attack each other.

'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        occupiedCols = set()
        occupiedDiag1s = set()
        occupiedDiag2s = set()
        
        count = [0]
        def backtrack(row):            
            for j in range(n):                
                if j in occupiedCols:                
                    continue 
                if row-j in occupiedDiag1s:
                    continue
                if row+j in occupiedDiag2s:
                    continue
                if row == n-1:
                    count[0] += 1
                else:
                    occupiedCols.add(j)
                    occupiedDiag1s.add(row-j)
                    occupiedDiag2s.add(row+j)
                    backtrack(row+1)
                    occupiedCols.remove(j)
                    occupiedDiag1s.remove(row-j)
                    occupiedDiag2s.remove(row+j)
            #return count
            return
                
        backtrack(0)
        return count[0]
        


if __name__ == "__main__":
    print(Solution().solveNQueens(4))
    