'''
-Medium-

*Union Find*

*Kruskal's Algorithm*
*Minimum Spanning Tree*

You are given an array points representing integer coordinates of some points on a 2D-plane, 
where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between 
them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is 
exactly one simple path between any two points.

 

Example 1:



Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
Example 3:

Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4
Example 4:

Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000
Example 5:

Input: points = [[0,0]]
Output: 0

'''


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        res = 0
        roots = [i for i in range(n)]        
        def find(i):
            while roots[i] != i:
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i        
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                edges.append((i,j,dist))
        edges.sort(key = lambda x: x[2])
        for i, j, d in edges:
            x, y = find(i), find(j) 
            if x != y:
                roots[x] = y
                res += d
        return res



if __name__ == "__main__":
    print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
        