'''
-Hard-

A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents 
uninfected cells, and isInfected[i][j] == 1 represents cells contaminated with the virus. A wall 
(and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. 
Resources are limited. Each day, you can install walls around only one region (i.e., the affected area 
(continuous block of infected cells) that threatens the most uninfected cells the following night). 
There will never be a tie.

Return the number of walls used to quarantine all the infected regions. If the world will become fully 
infected, return the number of walls used.

 

Example 1:


Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
Output: 10
Explanation: There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

Example 2:


Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.
Example 3:

Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.
 

Constraints:

m == isInfected.length
n == isInfected[i].length
1 <= m, n <= 50
isInfected[i][j] is either 0 or 1.
There is always a contiguous viral region throughout the described process that will infect strictly more uncontaminated squares in the next round.


'''

from collections import deque

class Solution(object):
    def containVirus(self, isInfected):
        """
        :type isInfected: List[List[int]]
        :rtype: int
        """
        grid = isInfected
        res = 0
        self.aaaa = {}
    
        while True:
            lst = self.findRegions(grid)
            if not lst: return res
            
            for i, j in lst:
                for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if (i, j, ii, jj) not in self.aaaa and 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == 0:
                        res += 1
                        self.aaaa[(i, j, ii, jj)] = 1
                        self.aaaa[(ii, jj, i, j)] = 1
            for i, j in lst:
                grid[i][j] = 2

            self.spread(grid)
    
    def findRegions(self, grid):
        tmp = []
        num = -1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    lst, affect = self.findRegion(grid, i, j)
                    num1 = len(set(affect))
                    
                    if num1 > num:
                        tmp = lst
                        num = num1
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] %= 10
                
        return tmp
    
    def findRegion(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return [], []
        
        if grid[i][j] == 0: return [], [(i, j)]
        
        if grid[i][j] != 1: return [], []
        
        res = [(i, j)]
        affect = []
        grid[i][j] += 10
        
        for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if (i, j, ii, jj) not in self.aaaa:
                res1, a1 = self.findRegion(grid, ii, jj)
                res += res1
                affect += a1
        
        return res, affect
        
    
    def spread(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if (i, j, ii, jj) not in self.aaaa and 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == 0:
                            grid[ii][jj] = 11
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] %= 10

    def containVirusOfficial(self, grid):
        R, C = len(grid), len(grid[0])
        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def dfs(r, c):
            if (r, c) not in seen:
                seen.add((r, c))
                regions[-1].add((r, c))
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == 1:
                        dfs(nr, nc)
                    elif grid[nr][nc] == 0:
                        frontiers[-1].add((nr, nc))
                        perimeters[-1] += 1

        ans = 0
        while True:
            #Find all regions, with associated frontiers and perimeters.
            seen = set()
            regions = []
            frontiers = []
            perimeters = []
            for r, row in enumerate(grid):
                for c, val in enumerate(row):
                    if val == 1 and (r, c) not in seen:
                        regions.append(set())
                        frontiers.append(set())
                        perimeters.append(0)
                        dfs(r, c)

            #If there are no regions left, break.
            if not regions: break

            #Add the perimeter of the region which will infect the most squares.
            triage_index = frontiers.index(max(frontiers, key = len))
            ans += perimeters[triage_index]

            #Triage the most infectious region, and spread the rest of the regions.
            for i, reg in enumerate(regions):
                if i == triage_index:
                    for r, c in reg:
                        grid[r][c] = -1
                else:
                    for r, c in reg:
                        for nr, nc in neighbors(r, c):
                            if grid[nr][nc] == 0:
                                grid[nr][nc] = 1

        return ans
    """
    思路：BFS
        1. 获取感染区、扩散区和墙数：获取感染区中所有点、及每个区域的扩散点、墙数
        2. 建墙：选取扩散点数最多的区域，统计墙数，建墙后墙内节点设置为安全区
        3. 扩散：其他区域的扩散点设为感染区
        4. 重复以上过程，直至没有感染区        
    """
    def containVirusBFS(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 75%
        m,n = len(grid),len(grid[0])
        
        def adj(i,j):
            for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= ii < m and 0 <= jj< n:
                    yield ii,jj
        
        def get_virus_areas(grid):
            areas = []
            dangers = []
            walls = []
            color = [[0] * n for i in range(m)]
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and color[i][j] == 0:
                        area = [(i,j)]
                        danger = set()
                        wall = 0
                        Q = deque([(i,j)])
                        color[i][j] = 1
                        while Q:
                            s,t = Q.popleft()
                            for ii,jj in adj(s,t):
                                if grid[ii][jj] == 1 and color[ii][jj] == 0:
                                    color[ii][jj] = 1
                                    Q.append((ii,jj))
                                    area.append((ii,jj))
                                if grid[ii][jj] == 0:
                                    wall += 1
                                    danger.add((ii,jj))
                        areas.append(area)
                        dangers.append(danger)
                        walls.append(wall)
            return areas,dangers,walls
        
        def spread(dangers):
            for danger in dangers:
                for i,j in danger:
                    grid[i][j] = 1
        
        wall_count = 0
        areas,dangers,walls = get_virus_areas(grid)
        while areas:
            # 如果全是感染区，返回
            n_area = len(areas)
            if sum(len(area) for area in areas) == m * n:
                return wall_count
            
            # 获取危险点最多的区域
            dangerest_i = 0
            for i in range(n_area):
                if len(dangers[i]) > len(dangers[dangerest_i]):
                    dangerest_i = i
            
            # 建墙，统计墙数，将对应感染区变为安全区
            wall_count += walls[dangerest_i]
            for i,j in areas[dangerest_i]:
                grid[i][j] = -1
            
            # 其他感染区扩散
            spread(dangers[:dangerest_i] + dangers[dangerest_i+1:])
            
            # 重新获取感染区
            areas,dangers,walls = get_virus_areas(grid)
        
        return wall_count
        

if __name__=="__main__":
    isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
    print(Solution().containVirus(isInfected))