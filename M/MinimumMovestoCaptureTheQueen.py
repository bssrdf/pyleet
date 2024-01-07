'''
-Medium-

*Dijkstra's Algorithm"
*Shortest Path*

There is a 1-indexed 8 x 8 chessboard containing 3 pieces.

You are given 6 integers a, b, c, d, e, and f where:

(a, b) denotes the position of the white rook.
(c, d) denotes the position of the white bishop.
(e, f) denotes the position of the black queen.
Given that you can only move the white pieces, return the minimum number of moves required to capture the black queen.

Note that:

Rooks can move any number of squares either vertically or horizontally, but cannot jump over other pieces.
Bishops can move any number of squares diagonally, but cannot jump over other pieces.
A rook or a bishop can capture the queen if it is located in a square that they can move to.
The queen does not move.
 

Example 1:


Input: a = 1, b = 1, c = 8, d = 8, e = 2, f = 3
Output: 2
Explanation: We can capture the black queen in two moves by moving the white rook to (1, 3) then to (2, 3).
It is impossible to capture the black queen in less than two moves since it is not being attacked by any of the pieces at the beginning.
Example 2:


Input: a = 5, b = 3, c = 3, d = 4, e = 5, f = 2
Output: 1
Explanation: We can capture the black queen in a single move by doing one of the following: 
- Move the white rook to (5, 2).
- Move the white bishop to (5, 2).
 

Constraints:

1 <= a, b, c, d, e, f <= 8
No two pieces are on the same square.


'''

from collections import deque
import heapq
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        n = 8
        def bfs1():
            visited = [[False]*n for i in range(n)]
            que = deque([(a-1,b-1,0)])
            visited[a-1][b-1] = True
            while que:
                x, y, t = que.popleft()
                if x == e-1 and y == f-1:
                    return t
                for i in range(x-1, -1, -1):
                    if i == c-1 and y == d-1:
                        break
                    if not visited[i][y]:
                        visited[i][y] = True
                        que.append((i,y,t+1))
                for i in range(x+1, n):
                    if i == c-1 and y == d-1:
                        break
                    if not visited[i][y]:
                        visited[i][y] = True
                        que.append((i,y,t+1))
                for j in range(y-1, -1, -1):
                    if x == c-1 and j == d-1:
                        break
                    if not visited[x][j]:
                        visited[x][j] = True
                        que.append((x,j,t+1))
                for j in range(y+1, n):
                    if x == c-1 and j == d-1:
                        break
                    if not visited[x][j]:
                        visited[x][j] = True
                        que.append((x,j,t+1))
            return n*n
        def bfs2():
            visited = [[False]*n for i in range(n)]
            que = deque([(c-1,d-1,0)])
            visited[c-1][d-1] = True
            while que:
                x, y, t = que.popleft()
                if x == e-1 and y == f-1:
                    return t
                k = 1
                while x-k >= 0 and y-k >= 0: 
                    if x-k == a-1 and y-k == b-1:
                        break
                    if not visited[x-k][y-k]:
                        visited[x-k][y-k] = True
                        que.append((x-k, y-k, t+1))
                    k += 1
                k = 1
                while x+k < n and y+k < n: 
                    if x+k == a-1 and y+k == b-1:
                        break
                    if not visited[x+k][y+k]:
                        visited[x+k][y+k] = True
                        que.append((x+k, y+k, t+1))
                    k += 1   
                k = 1
                while x-k >= 0 and y+k < n: 
                    if x-k == a-1 and y+k == b-1:
                        break
                    if not visited[x-k][y+k]:
                        visited[x-k][y+k] = True
                        que.append((x-k, y+k, t+1))
                    k += 1
                k = 1
                while x+k < n and y-k >= 0: 
                    if x+k == a-1 and y-k == b-1:
                        break
                    if not visited[x+k][y-k]:
                        visited[x+k][y-k] = True
                        que.append((x+k, y-k, t+1))
                    k += 1   
            return n*n
        x,y = bfs1(), bfs2()        
        # print(x,y)
        return min(x, y)
    
    def minMovesToCaptureTheQueen2(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        n = 8
        def bfs1():
            visited = [[False]*n for i in range(n)]
            que = deque([(a-1,b-1,0)])
            visited[a-1][b-1] = True
            while que:
                x, y, t = que.popleft()
                if x == e-1 and y == f-1:
                    return t
                t1 = t
                for i in range(x-1, -1, -1):
                    if i == c-1 and y == d-1:
                        t1 += 1
                    if not visited[i][y]:
                        visited[i][y] = True
                        que.append((i,y,t1+1))
                t1 = t
                for i in range(x+1, n):
                    if i == c-1 and y == d-1:
                        t1 += 1
                    if not visited[i][y]:
                        visited[i][y] = True
                        que.append((i,y,t1+1))
                t1 = t
                for j in range(y-1, -1, -1):
                    if x == c-1 and j == d-1:
                        t1 += 1
                    if not visited[x][j]:
                        visited[x][j] = True
                        que.append((x,j,t1+1))
                t1 = t
                for j in range(y+1, n):
                    if x == c-1 and j == d-1:
                        t1 += 1
                    if not visited[x][j]:
                        visited[x][j] = True
                        que.append((x,j,t1+1))
            return n*n
        def bfs2():
            visited = [[False]*n for i in range(n)]
            que = deque([(c-1,d-1,0)])
            visited[c-1][d-1] = True
            while que:
                x, y, t = que.popleft()
                if x == e-1 and y == f-1:
                    return t
                k, t1 = 1, t
                while x-k >= 0 and y-k >= 0: 
                    if x-k == a-1 and y-k == b-1:
                        t1 += 1
                    if not visited[x-k][y-k]:
                        visited[x-k][y-k] = True
                        que.append((x-k, y-k, t1+1))
                    k += 1
                # k = 1
                k, t1 = 1, t
                while x+k < n and y+k < n: 
                    if x+k == a-1 and y+k == b-1:
                        # break
                        t1 += 1
                    if not visited[x+k][y+k]:
                        visited[x+k][y+k] = True
                        que.append((x+k, y+k, t1+1))
                    k += 1   
                # k = 1
                k, t1 = 1, t
                while x-k >= 0 and y+k < n: 
                    if x-k == a-1 and y+k == b-1:
                        # break
                        t1 += 1
                    if not visited[x-k][y+k]:
                        visited[x-k][y+k] = True
                        que.append((x-k, y+k, t1+1))
                    k += 1
                # k = 1
                k, t1 = 1, t
                while x+k < n and y-k >= 0: 
                    if x+k == a-1 and y-k == b-1:
                        # break
                        t1 += 1
                    if not visited[x+k][y-k]:
                        visited[x+k][y-k] = True
                        que.append((x+k, y-k, t1+1))
                    k += 1   
            return n*n
        x,y = bfs1(), bfs2()        
        print(x,y)
        return min(x, y)
    
    def minMovesToCaptureTheQueen3(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        n = 8
        def bfs1():
            dist = [[n*n]*n for _ in range(n)]
            que = [(0,a-1,b-1)]
            dist[a-1][b-1] = 0
            while que:
                t, x, y = heapq.heappop(que)
                if x == e-1 and y == f-1:
                    return t
                t1 = t
                for i in range(x-1, -1, -1):
                    if i == c-1 and y == d-1:
                        t1 += 1
                    if dist[i][y] > t1+1:
                        dist[i][y] = t1+1
                        heapq.heappush(que, (t1+1,i,y))
                t1 = t
                for i in range(x+1, n):
                    if i == c-1 and y == d-1:
                        t1 += 1
                    if dist[i][y] > t1+1:
                        dist[i][y] = t1+1                    
                        heapq.heappush(que, (t1+1,i,y))    
                t1 = t
                for j in range(y-1, -1, -1):
                    if x == c-1 and j == d-1:
                        t1 += 1
                    if dist[x][j] > t1+1:
                        dist[x][j] = t1+1                    
                        heapq.heappush(que, (t1+1,x,j))    
                t1 = t
                for j in range(y+1, n):
                    if x == c-1 and j == d-1:
                        t1 += 1
                    if dist[x][j] > t1+1:
                        dist[x][j] = t1+1                    
                        heapq.heappush(que, (t1+1,x,j))                            
            return n*n
        def bfs2():
            dist = [[n*n]*n for _ in range(n)]
            que = [(0,c-1,d-1)]
            dist[c-1][d-1] = 0
            while que:                
                t, x, y = heapq.heappop(que)
                if x == e-1 and y == f-1:
                    return t
                k, t1 = 1, t
                while x-k >= 0 and y-k >= 0: 
                    if x-k == a-1 and y-k == b-1:
                        t1 += 1
                    if dist[x-k][y-k] > t1+1:
                        dist[x-k][y-k] = t1+1
                        heapq.heappush(que, (t1+1,x-k,y-k))                              
                    k += 1
                k, t1 = 1, t
                while x+k < n and y+k < n: 
                    if x+k == a-1 and y+k == b-1:
                        t1 += 1
                    if dist[x+k][y+k] > t1+1:
                        dist[x+k][y+k] = t1+1
                        heapq.heappush(que, (t1+1,x+k,y+k))                                                  
                    k += 1   
                k, t1 = 1, t
                while x-k >= 0 and y+k < n: 
                    if x-k == a-1 and y+k == b-1:
                        t1 += 1
                    if dist[x-k][y+k] > t1+1:
                        dist[x-k][y+k] = t1+1
                        heapq.heappush(que, (t1+1,x-k,y+k))                    
                    k += 1
                k, t1 = 1, t
                while x+k < n and y-k >= 0: 
                    if x+k == a-1 and y-k == b-1:
                        t1 += 1
                    if dist[x+k][y-k] > t1+1:
                        dist[x+k][y-k] = t1+1
                        heapq.heappush(que, (t1+1,x+k,y-k))                    
                    k += 1   
            return n*n
        x = bfs1()
        y = bfs2()        
        # print(x,y)
        return min(x, y)


        

if __name__ == "__main__":
    # print(Solution().minMovesToCaptureTheQueen2(a = 1, b = 1, c = 8, d = 8, e = 2, f = 3))
    # print(Solution().minMovesToCaptureTheQueen2(a = 5, b = 3, c = 3, d = 4, e = 5, f = 2))    
    # print(Solution().minMovesToCaptureTheQueen2(a = 6, b = 8, c = 6, d = 6, e = 6, f = 3))
    # print(Solution().minMovesToCaptureTheQueen2(a = 3, b = 1, c = 1, d = 1, e = 2, f = 5))

    print(Solution().minMovesToCaptureTheQueen3(a = 1, b = 1, c = 8, d = 8, e = 2, f = 3))
    print(Solution().minMovesToCaptureTheQueen3(a = 5, b = 3, c = 3, d = 4, e = 5, f = 2))    
    print(Solution().minMovesToCaptureTheQueen3(a = 6, b = 8, c = 6, d = 6, e = 6, f = 3))
    print(Solution().minMovesToCaptureTheQueen3(a = 3, b = 1, c = 1, d = 1, e = 2, f = 5))
    print(Solution().minMovesToCaptureTheQueen3(a = 7, b = 3, c = 6, d = 4, e = 6, f = 7))
                  
