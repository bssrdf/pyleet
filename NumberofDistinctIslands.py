'''
-Medium-

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) You 
may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same 
as another if and only if one island can be translated (and not rotated or 
reflected) to equal the other.

Example 1:

11000
11000
00011
00011
Given the above grid map, return 1.

 

Example 2:

11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:

11
1
and

 1
11
are considered different island shapes, because we do not consider 
reflection / rotation.

 

Note: The length of each dimension in the given grid does not exceed 50.

'''

class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        '''
        :type grid: List[List[str]]
        :rtype: int
        '''
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        def helper(i0, j0, i, j, st):
            if i < 0 or i > m-1 or j < 0 or j > n-1: return
            if grid[i][j] != '1': return
            grid[i][j] = '#'
            st.add(str(i-i0)+'_'+str(j-j0))
            for di, dj in dirs:
                x, y = i+di, j+dj
                helper(i0, j0, x, y, st)
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    locations = set()
                    helper(i, j, i, j, locations)
                    t = ''
                    for loc in locations:
                        t += loc + '_'
                    res.add(t)
        return len(res)


if __name__=="__main__":
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '1', '1'],
            ['0', '0', '0', '1', '1']]
    print(Solution().numberofDistinctIslands(grid))
    grid = [['1', '1', '0', '1', '1'],
            ['1', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '1'],
            ['1', '1', '0', '1', '1']]
    print(Solution().numberofDistinctIslands(grid))