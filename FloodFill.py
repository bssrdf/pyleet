'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''
from queue import Queue

class Solution(object):
    
#    def isvalid(self, i, j, board, processed, target):
#        if i>=0 and i<len(board) and j>=0 and j<len(board[0]):
#            print 'isvalid: ', i, j, board[i][j], processed[i][j] 
#        return i>=0 and i<len(board) and j>=0 and j<len(board[0]) and board[i][j] == target and (not processed[i][j])
    row = [ -1, -1, -1,  0, 0,  1, 1, 1]
    col = [ -1,  0,  1, -1, 1, -1, 0, 1]
        
    def BFS(self, board, x, y, replacement):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        process = [False for l in board[0]]
        processed = [process[:] for l in board]        
        q = Queue(len(board)*len(board[0]))           
        target = board[x][y]
        q.enqueue((x,y))
        print 'target = ', target        
        processed[x][y] = True        
        while(not q.isEmpty()):
            (x1, y1) = q.dequeue()            
            board[x1][y1] = replacement
            for r,c in zip(self.row, self.col):
                #print r,c,len(q)
                #if isvalid(self, x1+r,y1+c, board, processed, target):                    
                i=x1+r
                j=y1+c
                if i>=0 and i<len(board) and j>=0 and j<len(board[0]) and board[i][j] == target and (not processed[i][j]):        
                    q.enqueue((i,j))
                   # print r,c, i, j, board[i][j], processed[i][j], len(q)
                    processed[i][j] = True
                    
        return

    def DFS(self, board, x, y, target, replacement):
        board[x][y] = replacement
        for r,c in zip(self.row, self.col):
            i=x+r
            j=y+c
            if i>=0 and i<len(board) and j>=0 and j<len(board[0]) and board[i][j] == target:        
                self.DFS(board, i, j, target, replacement)
        return
    
    def DFSIter(self, board, x, y, target, replacement):
        stack = []
        #board[x][y] = replacement
        stack.append((x,y))
        while stack:
            (x1, y1)=stack.pop() 
            board[x1][y1] = replacement
            for r,c in zip(self.row, self.col):
                i=x1+r
                j=y1+c
                if i>=0 and i<len(board) and j>=0 and j<len(board[0]) and board[i][j] == target:        
                    stack.append((i,j))
        return        
        

if __name__ == "__main__":
    board = [
        [ 'Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G' ],
        [ 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X' ],
        [ 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X' ],
        [ 'W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X' ],
        [ 'W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X' ],
        [ 'W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X' ],
        [ 'W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X' ],
        [ 'W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X' ],
        [ 'W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X' ],
        [ 'W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X' ]
    ]
    for l in board:
        print l
    #Solution().BFS(board, 3, 9, 'C')
    #Solution().DFS(board, 3, 9, 'X', 'C')
    Solution().DFSIter(board, 3, 9, 'X', 'C')
    print '============================='
    for l in board:
        print l
    #assert board == expected_board
