

#Count Servers that Communicate


class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        if not m:
            return 0
        count = 0
        points = []
        nums_in_rows = [0] * m
        nums_in_cols = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    points.append((i,j))
                    nums_in_rows[i] += 1
                    nums_in_cols[j] += 1
        for p in points:
            if nums_in_rows[p[0]] > 1 or nums_in_cols[p[1]] > 1:
                count += 1
        return count        
        
print(Solution().countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))



    