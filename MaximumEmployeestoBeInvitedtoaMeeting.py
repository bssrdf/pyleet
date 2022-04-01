'''
-Hard-
*DFS*
*Topological Sort*
A company is organizing a meeting and has a list of n employees, waiting to be invited. 
They have arranged for a large circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person 
and they will attend the meeting only if they can sit next to their favorite person 
at the table. The favorite person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite 
person of the ith employee, return the maximum number of employees that can be invited 
to the meeting.

 

Example 1:


Input: favorite = [2,2,1,2]
Output: 3
Explanation:
The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
The maximum number of employees that can be invited to the meeting is 3. 
Example 2:

Input: favorite = [1,2,0]
Output: 3
Explanation: 
Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
The seating arrangement will be the same as that in the figure given in example 1:
- Employee 0 will sit between employees 2 and 1.
- Employee 1 will sit between employees 0 and 2.
- Employee 2 will sit between employees 1 and 0.
The maximum number of employees that can be invited to the meeting is 3.
Example 3:


Input: favorite = [3,0,1,4,1]
Output: 4
Explanation:
The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
So the company leaves them out of the meeting.
The maximum number of employees that can be invited to the meeting is 4.
 

Constraints:

n == favorite.length
2 <= n <= 105
0 <= favorite[i] <= n - 1
favorite[i] != i


'''

from itertools import cycle
from typing import DefaultDict, List
from collections import Counter, defaultdict, deque

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        A = favorite
        n = len(favorite)
        occupied = [-1]*n
        graph = defaultdict(list)
        for i,f in enumerate(favorite):
            graph[f].append(i)
        def dfs(u):
            if occupied[u] != -1: return occupied[u]
            ans = 0
            for v in graph[u]:
                ans = max(ans, dfs(v))
            occupied[u] = ans + 1
            return occupied[u]
       
        ans, free = 0, 0
        for u in range(n):           
            if occupied[u] != -1: continue
            if A[A[u]] == u:
                occupied[u] = occupied[A[u]] = 0
                a, b = 0, 0
                for v in graph[u]:
                    if v == A[u]: continue 
                    a = max(a, dfs(v))
                for v in graph[A[u]]:
                    if v == u: continue 
                    b = max(b, dfs(v))
                free += a + b + 2
        print(free)
        def dfs2(u):
            if occupied[u] != -1:
                return u, occupied[u], False 
            occupied[u] = 0
            entryPoint, depth, cycleVisited = dfs2(A[u])
            if cycleVisited: # After the cycle being traversed, any other node in the backtracking process are outside of the cycle and should be ignored (by keeping m[u] as 0).
                return entryPoint, depth, True
            occupied[u] = 1 + depth # If we haven't met the entry point again, this is a node within the cycle, so we increment the depth.
            return entryPoint, occupied[u], u == entryPoint # When we visit the entry point again, we know what we've done traversing the c
        for i in range(n):
            if occupied[i] != -1: continue
            entryPoint, depth, cycleVisited = dfs2(i)
            if cycleVisited:
                ans = max(ans, depth)
        return max(ans, free)

    def maximumInvitations2(self, favorite: List[int]) -> int:
        A = favorite
        n = len(favorite)
        indeg, visited = [0]*n, [False]*n
        for f in A:
            indeg[f] += 1
        que = deque()
        for i in range(n):
            if indeg[i] == 0:
                visited[i] = True
                que.append(i)
        dp = [0]*n
        while que:
            u = que.popleft()
            v = A[u]
            dp[v] = max(dp[v], dp[u]+1)
            indeg[v] -= 1
            if indeg[v] == 0:
                visited[v] = True
                que.append(v)
        res, res2 = 0, 0
        print(visited, dp)
        for u in range(n):
            if not visited[u]:
                length = 0
                v = u
                while not visited[v]:
                    visited[v] = True
                    v = A[v]
                    length += 1
                if length == 2:
                    res2 += 2 + dp[u] + dp[A[u]]
                else:
                    res = max(res, length)
        return max(res, res2)











if __name__ == "__main__":
    # print(Solution().maximumInvitations(favorite = [2,2,1,2]))
    print(Solution().maximumInvitations(favorite = [1,2,3,0,3,4,0]))
    print(Solution().maximumInvitations2(favorite = [1,2,3,0,3,4,0]))
        