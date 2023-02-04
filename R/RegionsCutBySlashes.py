'''
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists 
of a /, \, or blank space.  These characters divide the square into 
contiguous regions.

(Note that backslash characters are escaped, so a \ is represented 
as "\\".)

Return the number of regions.

 

Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers 
to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers 
to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

 

Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.

'''

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        res = 0
        visited = [[[False for _ in range(4)] for _ in range(n)] for _ in range(n)]
        def dfs(i, j, k):
            if i < 0 or i >= n or j < 0 or j >= n or visited[i][j][k]:
                return  
            visited[i][j][k] = True
            if grid[i][j] == '\\':
                if k == 0: 
                    dfs(i,j,1)
                    dfs(i,j+1,2)
                elif k == 1:
                    dfs(i,j,0)
                    dfs(i-1,j,3)
                elif k == 2:
                    dfs(i,j,3)
                    dfs(i,j-1,0)
                elif k == 3:
                    dfs(i,j,2)
                    dfs(i+1,j,1)
            elif grid[i][j] == '/':
                if k == 0: 
                    dfs(i,j,3)
                    dfs(i,j+1,2)
                elif k == 1:
                    dfs(i,j,2)
                    dfs(i-1,j,3)
                elif k == 2:
                    dfs(i,j,1)
                    dfs(i,j-1,0)
                elif k == 3:
                    dfs(i,j,0)
                    dfs(i+1,j,1)     
            else:
                if k == 0: 
                    dfs(i,j,3)
                    dfs(i,j,1)
                    dfs(i,j+1,2)
                elif k == 1:
                    dfs(i,j,2)
                    dfs(i,j,0)
                    dfs(i-1,j,3)
                elif k == 2:
                    dfs(i,j,1)
                    dfs(i,j,3)
                    dfs(i,j-1,0)
                elif k == 3:
                    dfs(i,j,0)
                    dfs(i,j,2)
                    dfs(i+1,j,1)

        for i in range(n):            
            for j in range(n):
                for k in range(4):
                    if not visited[i][j][k]:  
                        dfs(i, j, k) 
                        res += 1
                        #for l in range(n):
                        #    print(visited[l][:][:])
                        #print('===============================')
        return res



if __name__ == "__main__":
    #'''
    region = [
           "\\/",
           "/\\"
           ]
    print(Solution().regionsBySlashes(region))
    #'''
    region = [
           "/\\",
           "\\/"
            ]
    print(Solution().regionsBySlashes(region))
    region = [
             "//",
             "/ "
            ]
    print(Solution().regionsBySlashes(region))
    
    region = [
             " /",
             "/ "
            ]
    print(Solution().regionsBySlashes(region))

    region =  [
             " /",
             "  "
             ]
    print(Solution().regionsBySlashes(region))         
    #'''