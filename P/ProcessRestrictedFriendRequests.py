'''
-Hard-
*Union Find*

You are given an integer n indicating the number of people in a network. 
Each person is labeled from 0 to n - 1.

You are also given a 0-indexed 2D integer array restrictions, where 
restrictions[i] = [xi, yi] means that person xi and person yi cannot 
become friends, either directly or indirectly through other people.

Initially, no one is friends with each other. You are given a list of 
friend requests as a 0-indexed 2D integer array requests, where 
requests[j] = [uj, vj] is a friend request between person uj and person vj.

A friend request is successful if uj and vj can be friends. Each friend 
request is processed in the given order (i.e., requests[j] occurs before 
requests[j + 1]), and upon a successful request, uj and vj become direct 
friends for all future friend requests.

Return a boolean array result, where each result[j] is true if the jth 
friend request is successful or false if it is not.

Note: If uj and vj are already direct friends, the request is still successful.

 

Example 1:

Input: n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]
Output: [true,false]
Explanation:
Request 0: Person 0 and person 2 can be friends, so they become direct friends. 
Request 1: Person 2 and person 1 cannot be friends since person 0 and person 1 would be indirect friends (1--2--0).
Example 2:

Input: n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]]
Output: [true,false]
Explanation:
Request 0: Person 1 and person 2 can be friends, so they become direct friends.
Request 1: Person 0 and person 2 cannot be friends since person 0 and person 1 would be indirect friends (0--2--1).
Example 3:

Input: n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3,4]]
Output: [true,false,true,false]
Explanation:
Request 0: Person 0 and person 4 can be friends, so they become direct friends.
Request 1: Person 1 and person 2 cannot be friends since they are directly restricted.
Request 2: Person 3 and person 1 can be friends, so they become direct friends.
Request 3: Person 3 and person 4 cannot be friends since person 0 and person 1 would be indirect friends (0--4--3--1).
 

Constraints:

2 <= n <= 1000
0 <= restrictions.length <= 1000
restrictions[i].length == 2
0 <= xi, yi <= n - 1
xi != yi
1 <= requests.length <= 1000
requests[j].length == 2
0 <= uj, vj <= n - 1
uj != vj


'''
from typing import List
from collections import defaultdict

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        roots = [i for i in range(n)]
        excludes = [set() for _ in range(n)]
        def find(x):
            while x != roots[x]:
                roots[x] = roots[roots[x]]
                x = roots[x]
            return x
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx < fy:
                roots[fy] = fx
                excludes[fx] |= excludes[fy]
                for v in excludes[fy]:
                    excludes[find(v)].add(fx)
                excludes[fy].clear()
            elif fx > fy:
                roots[fx] = fy
                excludes[fy] |= excludes[fx]
                for v in excludes[fx]:
                    excludes[find(v)].add(fy)
                excludes[fx].clear()
        for r in restrictions:
            excludes[r[0]].add(r[1])
            excludes[r[1]].add(r[0])
        ans = []
        for i, (u,v) in enumerate(requests):
            fu, fv = find(u), find(v)
            if fu in excludes[fv] or fv in excludes[fu]:
                ans.append(False)
            else:
                ans.append(True)
                union(u, v)
        return ans






if __name__ == "__main__":
    true, false = True, False
    print(Solution().friendRequests(n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3,4]]))
    n = 8
    restrictions = [[6,4],[7,5],[2,6],[1,5],[6,7],[6,5],[0,3],[5,4],[0,4],
                  [2,7],[0,2]]
    requests = [[6,3],[0,2],[0,5],[0,3],[6,4],[2,4],[1,0],[2,1],[2,5],
                [6,7],[7,0],[3,2],[3,5],[2,1],[1,6],[7,4],[6,3],[1,3],
                [6,5],[3,7],[7,0],[6,5],[0,5],[0,4],[7,5],[7,0],[7,0],[1,3]]
    sol = Solution().friendRequests(n, restrictions, requests)
    ans = [true,false,true,false,false,true,false,true,false,false,false,false,false,true,false,false,true,false,false,false,false,false,true,false,false,false,false,false]
    for i, (s, a) in enumerate(zip(sol, ans)):
        if s != a:
            print(i, s, a)
