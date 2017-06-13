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
    def solve(self, board, x, y, replacement):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        process = [False]*len(board[0])
        processed = [process]*len(board)
        def isvalid(x, y, target):
            return x>=0 and x<len(board) and y>=0 and y<len(board[0]) and board[x][y] == target and not processed[x][y] 
        row = [ -1, -1, -1,  0, 0,  1, 1, 1]
        col = [ -1,  0,  1, -1, 1, -1, 0, 1]
        q = Queue(len(board)*len(board[0]))    
        print 'queue size: ', len(board)*len(board[0])
        target = board[x][y]
        q.enqueue((x,y))
        while(not q.isEmpty()):
            (x1, y1) = q.dequeue()
            processed[x1][y1] = True
            board[x1][y1] = replacement
            for r,c in zip(row,col):
                print r,c,len(q)
                if isvalid(x1+r,y1+c,target):
                    q.enqueue((x1+r,y1+c))
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
    Solution().solve(board, 3, 9, 'C')
    print '============================='
    for l in board:
        print l
    #assert board == expected_board
