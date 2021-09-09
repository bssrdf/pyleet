'''
-Medium-

*Sort*

A group of two or more people wants to meet and minimize the total 
travel distance. You are given a 2D grid of values 0 or 1, where each 
1 marks the home of someone in the group. The distance is calculated 
using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel
             distance of 2+2+2=6 is minimal. So return 6.

'''


class Solution(object):

    def shortestDistance(self, grid):
        m, n = len(grid), len(grid[0])
        rows, cols = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        #rows.sort()
        cols.sort()
        res, i, j = 0, 0, len(rows)-1
        while i < j:
            res += rows[j] - rows[i] + cols[j] - cols[i]
            i += 1
            j -= 1
        return res
    
    def minTotalDistance(self, grid):
        # Write your code here
        # x,y坐标分别去中位数（如果个数为偶数，则中间2个数之间任取一个）为最佳方案。
        # 时间复杂度 O(MN), O(MLogM), O(N*LogN) 三者取最大值
        # 空间复杂度 O(M+N)
        xLst,yLst = [],[]
        m,n = len(grid),len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    xLst.append(i)
                    yLst.append(j)
        
        xLst.sort()
        yLst.sort()

        x = xLst[len(xLst)//2]
        y = yLst[len(yLst)//2]

        return sum([abs(x-x1) for x1 in xLst]) + sum([abs(y-y1) for y1 in yLst])


s = Solution()
grid = [[1,0,0,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]]
print(s.shortestDistance(grid))
print(s.minTotalDistance(grid))


