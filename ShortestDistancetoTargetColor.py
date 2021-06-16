'''
-Medium-
*DP*
*Binary Search*

You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest 

distance between the given index i and the target color c. If there is no solution return -1.

 

Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
Example 2:

Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.
 

Constraints:

1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3


'''
import bisect
class Solution:
    def shortestDistanceColor(self, colors, queries):
        n = len(colors)
        idx = [[] for _ in range(4)]
        for i,v in enumerate(colors):
            idx[v].append(i)
        res = []
        for k,c in queries:
            if not idx[c]: res.append(-1)
            else:
                q = bisect.bisect_left(idx[c],k)
                if q == 0: res.append(idx[c][q]-k)
                elif q == len(idx[c]): res.append(k-idx[c][q-1])
                else: res.append(min(idx[c][q]-k, k-idx[c][q-1]))
        return res

    def shortestDistanceColorDP(self, colors, queries):
        n = len(colors)
        dist = [[-1]*4 for _ in range(n)]
        idx = [-1]*4
        for i,c in enumerate(colors):
            idx[c] = i
            for j in range(1, 4):
                if idx[j] != -1:
                    dist[i][j] = i - idx[j]
        #for j in range(1, 4):
        #    for i in range(n):
        #       print(dist[i][j],',', end='')
        #    print()

        idx = [-1]*4       
        
        for i in range(n - 1, -1, -1):
            c = colors[i]
            idx[c] = i            
            for j in range(1, 4):
                if idx[j] != -1:
                    d = idx[j] - i
                    dist[i][j] = d if dist[i][j] == -1 else min(dist[i][j], d)
        #for j in range(1, 4):
        #    for i in range(n):
        #       print(dist[i][j],',', end='')
        #    print()
        
        return [dist[q[0]][q[1]] for q in queries]



if __name__ == "__main__":
    #print(Solution().shortestDistanceColor(colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]))
    print(Solution().shortestDistanceColorDP(colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]))
    #print(Solution().shortestDistanceColor(colors = [1,2], queries = [[0,3]]))