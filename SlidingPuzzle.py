
from collections import deque

class Solution(object):

    
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        visited=set()
        q = deque()
        m = 2
        n = 3
        target = '123450'
        neighbor = ((1,3), 
                    (0,4,2),
                    (1,5),
                    (0,4),
                    (3,1,5),
                    (4,2))
        def board2string(board):
            return ''.join([str(b) for row in board for b in row])
        def swap(s, i, j):
            lst = list(s)
            lst[i], lst[j] = lst[j], lst[i]
            return ''.join(lst)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    cur = board2string(board)
                    q.append((0,cur))
                    visited.add(cur)
        while q:
            steps,cur = q.popleft()
            if cur == target:
                return steps
            i = cur.index('0')
            for n in neighbor[i]:
                nxt = swap(cur,i,n) 
                if nxt not in visited:
                   q.append((steps+1,nxt))
                   visited.add(nxt)
        return -1

if __name__ == "__main__":
    print(Solution().slidingPuzzle([[1,2,3],[4,0,5]]))
    print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))
    print(Solution().slidingPuzzle([[1,2,3],[5,4,0]]))
    print(Solution().slidingPuzzle([[3,2,4],[1,5,0]]))
            





