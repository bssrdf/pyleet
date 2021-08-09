'''
-Hard-

*DFS*


Given a 2D array of characters grid of size m x n, you need to find if there exists any 
cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. 
From a given cell, you can move to one of the cells adjacent to it - in one of the four 
directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the 
cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which 
was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.

 

Example 1:



Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:



Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:



Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 500
1 <= n <= 500
grid consists only of lowercase English letters.


'''
import collections
class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
       
        m, n = len(grid), len(grid[0])
        #print(m,n)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(cur, pre, visited, mark):
            visited[cur[0]][cur[1]] = True
            for dx, dy in dirs:
                i, j = cur[0]+dx, cur[1]+dy
                if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != mark:
                    continue 
                if (i,j) != pre:
                    if visited[i][j]: return True
                    if dfs((i,j), cur, visited, mark):
                       return True 
            return False
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs((i,j), (-1,-1), visited, grid[i][j]):
                       return True
        return False

    def containsCycleUF(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """    
        def find(pos):
            if parents[pos] != pos:
                parents[pos] = find(parents[pos])
            return parents[pos]

        def union(pos1, pos2):
            parent1, parent2 = find(pos1), find(pos2)
            if parent1 != parent2:
                if ranks[parent2] > ranks[parent1]:
                    parents[parent1] = parent2
                else:
                    parents[parent2] = parent1
                    if ranks[parent1] == ranks[parent2]:
                        ranks[parent1] += 1

        rows, cols = len(grid), len(grid[0])
        parents = {(i, j): (i, j) for i in range(rows) for j in range(cols)}
        ranks = collections.Counter()
        for i, row in enumerate(grid):
            for j, letter in enumerate(row):
                if i > 0 and j > 0 and grid[i-1][j] == grid[i][j-1] == letter and find((i-1, j)) == find((i, j-1)):
                    return True
                for r, c in (i - 1, j), (i, j - 1):
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == letter:
                        union((i, j), (r, c))
        return False

    
    def containsCycleTLE(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        # TLE 68 / 74 test cases passed.
        m, n = len(grid), len(grid[0])
        #print(m,n)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(cur, visited, target, mark, k):
            visited[cur[0]][cur[1]] = True
            for dx, dy in dirs:
                i, j = cur[0]+dx, cur[1]+dy
                if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != mark:
                    continue 
                if k >= 4 and (i,j) == target: return True
                if visited[i][j]: continue          
                if dfs((i,j), visited, target, mark, k+1):
                    return True 
            return False
        for i in range(m):
            for j in range(n):
                visited = [[False]*n for _ in range(m)]
                #visited[i][j] = True
                if dfs((i,j), visited, (i,j), grid[i][j], 1):
                    return True
        return False


if __name__ == "__main__":
    #'''
    grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
    print(Solution().containsCycle(grid))
    grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
    print(Solution().containsCycle(grid))
    grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
    print(Solution().containsCycle(grid))
    grid = [["l","d","x","y","r","a","r","v","i","i","j","w","r","d","o","e","l","g","a","a","c","e","v","k","o","x","a","a","r","p","k","q","q","m","c","v","c","l","c","b","m","s","a","l","m","v","u","x","u","o","l","u","f","d","a","n","k","a","l","b","i","j","x","d","n","z","i","u","q","u","l","x","y","m","a","l","h","w","k","z","g","j","s","u"],["p","h","u","u","f","v","l","b","j","a","b","f","d","e","t","o","l","y","k","i","h","o","n","i","a","k","l","w","p","n","z","f","h","v","p","h","t","c","p","t","v","t","g","g","z","x","n","k","j","v","e","g","q","j","z","l","n","f","b","t","a","c","b","t","d","f","r","r","y","f","x","a","d","c","f","a","i","g","c","t","s","m","j","r"],["u","l","y","b","k","a","m","i","a","w","g","e","l","i","y","d","k","i","p","g","u","x","r","r","k","t","c","g","w","s","t","a","p","h","f","s","k","u","v","n","j","b","y","b","g","v","s","e","e","y","t","j","z","j","v","n","h","w","l","r","z","h","h","m","a","s","a","x","p","x","w","h","p","s","g","j","j","v","s","z","c","d","q","w"],["j","k","y","w","x","s","b","t","a","s","j","s","v","b","k","d","c","j","e","w","z","m","j","w","s","y","k","s","w","t","g","i","f","o","m","v","s","s","b","e","z","e","f","b","b","x","o","w","e","d","f","u","y","g","y","j","k","c","b","r","n","r","s","t","b","d","z","v","n","u","c","d","j","g","g","k","v","t","u","g","a","g","i","a"],["a","z","d","m","u","a","g","m","h","a","o","g","p","d","e","g","o","u","n","j","t","i","q","u","f","w","a","y","y","h","s","e","y","i","d","h","w","s","t","k","k","v","v","b","t","z","a","b","e","b","m","q","o","m","r","q","z","k","r","w","o","m","e","w","j","x","n","u","i","s","q","a","k","t","i","s","q","a","e","h","w","s","a","l"],["h","z","z","i","o","v","m","h","l","d","l","e","f","x","o","w","j","t","g","g","x","q","r","k","j","c","w","r","e","s","h","g","u","p","h","z","s","s","u","t","y","l","h","d","j","k","c","s","t","u","z","h","g","a","o","q","x","e","i","h","b","z","j","h","x","d","g","j","l","g","s","a","r","r","k","d","i","j","w","f","a","l","t","f"],["l","m","m","u","h","t","x","b","l","k","m","a","u","b","v","x","h","v","m","x","r","f","z","p","r","c","x","y","n","b","o","y","z","d","g","i","n","g","h","v","l","f","z","v","k","l","u","h","w","j","b","b","e","q","p","h","g","p","s","n","j","f","p","x","z","u","r","i","l","u","k","g","q","o","p","e","w","b","x","m","u","t","u","r"],["e","o","r","n","o","a","n","a","w","n","v","p","o","u","l","p","k","k","p","y","b","z","r","v","i","g","b","f","z","n","k","d","k","k","b","r","z","w","g","f","k","b","s","s","m","n","z","a","r","d","h","e","d","h","e","z","w","v","r","n","w","t","q","o","w","j","n","y","m","h","n","v","n","i","l","l","z","k","b","c","m","y","i","c"],["v","q","f","g","m","m","h","x","m","d","g","v","e","v","s","d","u","z","d","d","l","h","t","m","y","c","l","p","j","h","g","i","e","m","w","z","u","v","k","w","a","w","o","r","b","z","s","q","c","t","n","c","s","k","s","n","d","b","f","h","n","r","v","h","p","c","h","p","m","b","w","k","u","t","r","y","x","m","m","d","t","m","j","z"],["b","y","m","x","f","t","m","r","i","h","i","y","q","x","e","h","c","x","o","r","z","w","z","f","f","f","q","x","k","w","f","w","r","q","z","n","p","z","y","g","v","d","z","s","p","h","v","e","u","n","e","y","k","r","v","v","n","p","n","a","a","x","y","n","b","i","z","c","g","l","b","q","n","w","m","p","t","a","r","t","x","p","q","p"],["e","a","h","g","j","s","t","a","l","q","b","o","l","a","p","r","n","b","g","d","o","o","a","t","q","z","y","n","s","a","c","l","t","t","i","a","h","b","m","v","f","t","p","p","s","q","c","o","y","m","x","p","s","n","z","r","k","i","n","d","t","b","x","f","n","a","h","j","a","y","q","x","h","i","x","l","m","e","n","x","z","h","k","c"],["t","c","b","p","z","h","l","k","p","p","h","d","o","u","e","w","i","o","l","d","g","g","v","x","u","h","q","d","x","n","r","w","w","a","o","p","w","i","e","g","d","r","i","p","n","v","s","k","h","y","o","h","h","l","n","m","y","y","t","a","x","f","e","j","g","q","r","h","i","n","e","m","b","n","q","p","d","g","f","y","f","h","m","g"],["k","e","a","b","d","a","l","b","g","a","z","f","y","k","j","p","z","i","s","t","l","z","t","b","n","b","b","k","x","t","l","q","p","r","a","d","j","m","d","u","f","v","h","l","d","n","v","c","f","b","o","c","u","f","g","v","b","z","e","m","o","l","b","e","u","v","x","c","s","q","a","r","s","c","n","l","x","z","n","b","z","b","b","s"],["c","n","q","s","p","d","t","y","w","c","l","j","g","m","n","s","y","i","p","k","z","b","j","r","l","r","w","z","a","q","r","n","a","a","u","b","i","x","w","s","p","r","e","j","b","f","w","o","q","c","i","l","d","k","m","x","y","o","u","m","b","c","w","e","n","k","j","w","k","v","m","b","d","d","j","z","j","n","j","e","p","s","k","n"],["t","r","u","d","b","p","j","a","r","j","e","k","t","t","v","a","n","t","n","s","i","u","r","w","d","e","b","s","r","u","i","o","k","v","d","s","y","n","x","l","b","y","w","s","j","e","z","h","m","z","w","o","m","p","h","r","a","q","q","q","p","c","m","h","s","b","a","p","h","p","x","d","t","n","z","c","k","g","t","r","y","q","c","z"],["l","f","w","a","v","u","d","l","j","y","i","z","e","w","n","j","u","m","s","g","f","d","p","o","d","q","o","v","u","x","i","s","m","l","y","s","n","y","h","l","m","r","a","z","q","d","p","o","b","h","s","u","o","e","n","z","u","z","a","p","h","g","l","e","f","x","g","i","g","c","t","i","k","c","t","j","o","p","o","s","e","p","l","z"],["k","i","w","m","n","x","c","q","o","t","i","w","r","t","d","o","c","m","x","a","p","h","n","m","j","a","s","l","g","f","v","p","x","a","h","e","l","g","l","i","t","n","e","i","y","z","h","i","d","y","i","t","t","d","z","g","u","m","f","e","w","q","y","h","w","m","n","u","e","z","n","k","d","v","l","a","k","n","k","b","v","c","y","k"],["g","a","c","w","n","w","q","a","f","n","o","p","k","n","u","y","b","j","d","o","m","t","d","h","f","g","a","z","s","b","z","n","f","i","w","q","v","b","h","y","y","f","y","f","b","d","n","m","c","p","t","x","v","f","m","d","s","l","d","a","y","w","t","q","e","o","z","c","y","l","e","d","w","f","k","c","w","y","n","t","g","d","e","x"],["r","z","y","n","m","w","g","t","c","u","e","q","t","j","e","g","t","m","e","o","l","b","d","a","i","s","t","z","x","e","p","p","d","b","e","b","z","y","c","g","i","n","x","i","e","u","n","o","a","b","m","y","f","p","q","s","z","d","p","p","p","r","u","c","t","i","d","z","d","n","b","k","w","y","i","l","v","l","z","z","b","a","z","x"],["b","e","b","n","b","h","o","y","b","a","k","t","y","k","t","c","x","m","x","t","c","w","p","g","i","e","x","a","p","c","m","n","k","p","k","w","z","o","p","z","n","c","k","d","n","k","u","e","o","j","f","z","c","u","i","z","l","i","x","s","r","n","u","x","h","d","g","q","g","j","o","s","k","n","e","t","d","e","f","a","m","t","t","j"],["h","d","i","x","c","k","s","q","y","y","s","q","j","y","h","r","m","m","u","n","i","f","o","o","b","m","c","c","b","p","v","b","z","c","x","o","z","n","y","b","j","l","e","m","e","k","u","o","n","l","s","r","t","n","s","s","e","p","m","f","q","j","g","v","x","o","h","g","v","p","z","g","g","z","o","e","e","u","e","t","l","t","b","b"],["d","x","u","v","u","l","a","f","y","b","k","u","x","k","k","t","s","u","l","v","z","i","k","s","r","z","i","c","f","u","r","v","o","m","t","d","e","l","r","z","q","c","b","d","o","e","u","h","l","c","e","t","y","s","v","m","q","g","t","n","h","g","t","m","x","b","z","r","a","u","n","s","h","u","j","t","w","m","y","t","x","c","a","p"],["g","t","m","d","u","e","v","q","z","d","f","m","v","z","r","m","d","u","e","u","t","m","y","u","y","n","c","x","l","z","j","b","w","k","h","b","x","v","f","o","z","h","f","h","b","m","c","j","s","e","l","j","l","z","a","o","a","m","o","o","w","m","l","m","m","z","r","r","a","u","i","u","g","f","u","l","j","e","r","m","g","r","z","e"],["j","w","l","b","r","e","j","m","m","l","s","w","a","w","k","s","w","r","j","k","d","f","z","k","f","q","y","t","n","z","o","y","t","o","j","l","l","d","f","h","u","o","c","g","r","k","l","c","n","m","g","a","y","b","v","u","j","n","u","h","i","u","z","r","m","q","k","f","s","x","f","l","i","o","g","z","g","n","z","r","k","o","w","y"],["z","x","v","c","n","i","f","p","k","g","x","s","k","d","m","a","b","t","m","u","g","o","j","x","s","l","m","e","o","m","j","m","f","b","t","n","l","r","m","s","a","x","e","d","z","o","p","t","k","x","z","m","i","j","s","o","n","i","m","x","g","s","x","x","g","b","y","j","s","t","m","d","y","j","d","y","t","t","t","i","h","q","j","s"],["j","x","h","i","q","s","w","z","w","k","m","v","q","y","b","e","j","u","t","q","m","a","v","m","o","j","r","f","v","e","b","p","v","m","i","h","q","v","g","o","p","c","l","g","v","g","z","r","u","e","s","k","z","h","v","v","q","w","p","d","g","m","t","f","a","n","u","p","j","k","d","h","p","t","i","o","z","t","t","j","a","p","q","b"],["l","t","u","m","s","g","u","w","z","h","n","t","u","h","t","y","c","b","o","k","y","p","v","j","u","d","g","j","l","u","c","p","z","g","t","f","n","v","d","i","y","x","l","a","h","u","q","z","u","k","h","t","z","k","f","a","u","j","m","h","n","g","c","g","x","v","s","p","i","p","s","b","d","b","r","o","o","p","c","r","x","h","d","l"],["d","t","h","v","t","z","b","x","o","r","x","z","n","b","j","w","w","b","v","p","g","k","l","y","z","g","u","q","g","a","v","h","q","p","r","u","z","h","c","d","x","y","o","g","k","x","s","l","j","i","f","e","a","q","m","o","f","d","z","x","z","n","f","r","j","k","b","z","g","c","o","e","w","u","h","n","y","h","m","e","a","z","n","u"],["v","e","r","e","t","u","u","d","p","q","j","h","a","n","c","g","i","b","q","f","v","h","j","c","b","f","q","q","o","n","g","d","n","v","c","o","v","h","a","j","t","i","u","g","l","h","m","f","v","n","w","u","x","g","l","c","g","b","p","o","u","s","n","a","u","g","y","s","b","j","a","e","t","g","p","f","i","z","i","c","q","j","a","s"],["k","f","i","c","b","p","s","l","i","k","c","v","y","j","q","r","p","b","c","i","e","c","t","m","m","o","e","k","d","y","o","s","z","l","t","i","g","x","w","o","d","s","w","s","w","s","f","l","z","e","h","j","d","v","y","x","y","g","y","u","j","b","w","x","o","d","x","z","z","n","b","u","l","f","k","o","v","k","p","a","i","u","l","o"],["y","o","u","w","q","l","y","m","d","k","e","c","d","c","t","b","a","r","o","z","b","j","n","d","e","o","g","y","s","m","w","k","x","b","d","i","t","t","w","t","f","q","a","u","u","v","x","w","g","n","h","m","h","e","w","l","y","h","z","y","r","m","h","u","s","o","p","e","y","b","f","x","a","v","i","p","f","w","k","z","b","t","r","a"],["e","u","x","t","k","l","c","a","y","k","t","r","s","t","u","j","k","l","n","s","c","i","i","j","f","q","f","q","u","u","n","e","s","g","j","v","l","i","w","y","c","a","n","e","e","f","k","o","i","e","o","s","m","s","t","f","x","d","s","z","p","a","v","j","u","y","i","w","j","s","s","v","m","k","v","k","x","b","u","p","o","s","v","k"],["s","v","b","r","t","z","p","y","j","s","n","v","q","j","f","y","i","q","x","r","u","h","p","e","m","q","a","f","q","f","j","p","s","z","w","s","t","r","k","a","v","h","k","i","r","b","b","d","n","s","z","l","j","u","q","o","i","p","n","a","p","g","n","o","s","p","i","a","a","a","u","w","j","l","u","y","x","z","v","f","a","p","x","b"],["j","z","n","k","v","n","k","r","y","b","e","j","f","x","d","r","w","v","f","b","h","u","z","w","t","s","a","n","f","e","z","u","a","n","h","w","n","w","m","i","x","l","w","c","r","z","c","a","f","n","p","v","e","i","j","n","g","n","p","p","m","w","q","t","p","c","n","h","s","n","v","p","t","x","m","b","d","k","a","j","k","l","u","i"],["f","o","c","k","s","q","m","x","q","s","q","d","f","p","q","c","o","a","w","j","y","a","q","q","i","b","t","f","a","b","l","y","j","f","a","d","c","q","e","q","j","p","b","j","r","q","z","u","c","u","u","h","f","d","d","k","g","g","v","z","o","x","a","s","h","q","i","r","e","p","e","p","p","q","t","d","f","e","v","r","t","y","c","d"],["m","k","f","x","r","p","w","t","w","d","w","p","u","c","n","r","b","u","h","u","y","e","i","a","w","h","m","g","d","w","a","a","u","t","w","c","i","p","z","n","x","b","o","j","k","h","a","a","l","j","j","c","t","q","s","t","c","k","s","j","n","n","s","l","h","e","k","d","h","y","s","o","l","b","d","m","l","l","b","u","t","x","p","f"],["h","d","x","t","m","f","l","k","n","a","u","r","f","j","l","t","s","v","s","v","s","z","i","e","z","z","l","v","v","k","y","o","i","q","w","p","q","s","r","e","a","a","s","u","z","c","z","y","o","m","c","n","l","m","z","s","m","j","t","v","q","j","f","g","z","s","o","t","q","g","c","a","q","k","h","m","c","q","b","c","r","k","c","a"],["z","k","u","h","l","p","f","w","g","e","r","y","r","z","d","y","i","n","t","d","y","x","s","h","w","q","w","k","w","y","d","v","q","u","d","u","o","r","v","n","w","h","g","s","m","r","w","k","q","p","g","l","t","w","s","m","d","j","i","y","r","z","n","w","m","n","i","r","i","a","u","c","a","i","c","n","n","t","l","x","x","g","r","d"],["x","d","b","o","l","u","h","r","f","r","p","w","q","w","n","z","i","l","c","p","c","f","o","m","o","m","r","o","a","l","z","r","x","k","p","u","p","c","c","m","z","h","e","f","f","b","y","f","e","q","f","i","s","k","e","s","e","g","y","z","m","d","a","v","o","e","y","n","b","v","j","y","o","o","d","u","u","v","v","u","j","o","h","s"],["r","a","u","a","j","s","q","t","u","q","r","f","r","l","p","q","s","r","f","p","z","q","k","v","m","b","g","d","u","j","j","n","p","t","l","p","h","w","i","u","v","e","i","h","n","t","y","e","d","v","i","t","p","q","x","t","l","n","i","g","w","x","g","u","t","b","k","p","m","p","z","p","g","g","h","u","v","h","u","e","e","y","s","g"],["g","j","r","k","c","f","m","o","f","m","c","w","y","x","b","c","j","h","j","u","s","h","o","p","f","z","l","v","y","r","v","t","c","m","x","w","u","u","e","l","q","l","t","h","u","s","a","v","a","k","v","p","x","l","v","q","i","y","j","p","w","j","f","h","i","m","q","m","a","j","n","n","v","l","r","z","f","k","y","q","e","x","w","m"],["h","j","l","s","z","m","g","p","x","f","p","g","i","y","c","e","f","d","w","m","g","y","h","q","a","j","p","m","j","v","t","j","i","s","d","w","d","s","h","w","y","f","a","f","p","e","h","x","o","a","w","f","i","e","q","j","x","k","c","r","n","g","k","g","f","g","p","q","x","r","u","k","f","b","s","w","w","a","t","i","i","g","k","i"],["n","e","j","c","x","u","s","q","t","t","e","v","d","v","w","q","a","j","g","q","d","h","b","a","s","j","o","f","m","j","h","p","s","i","e","g","t","k","r","x","c","h","k","w","x","s","o","i","x","j","m","d","d","u","p","c","v","g","a","a","p","m","t","d","d","g","c","l","a","x","b","g","w","z","o","g","d","v","b","u","r","b","u","w"],["e","e","u","e","b","k","n","y","f","f","l","q","x","n","j","h","c","m","l","r","o","w","b","l","l","g","g","g","g","i","v","w","n","g","r","l","j","i","e","d","k","m","a","j","r","u","t","q","f","q","e","t","s","h","p","e","o","u","e","b","q","r","u","f","r","q","t","h","t","m","j","u","d","w","d","i","x","x","q","j","s","n","x","k"],["e","u","n","y","z","g","f","x","k","t","e","b","k","a","g","m","m","t","l","d","o","t","b","d","v","x","n","j","q","v","r","k","r","t","b","y","a","h","z","a","t","r","x","a","u","e","p","p","x","j","q","t","l","k","g","c","h","u","c","d","q","x","w","e","i","x","b","l","d","a","w","z","s","l","y","t","h","j","k","p","i","j","f","v"],["f","j","h","d","b","e","t","z","u","e","k","j","g","l","w","n","v","b","s","i","v","x","i","v","x","e","k","h","j","b","e","v","l","f","w","l","l","p","j","m","v","p","r","o","g","p","x","n","o","s","m","l","e","j","d","v","b","w","v","w","n","p","v","i","n","b","d","l","t","a","q","q","c","l","t","r","f","k","c","c","o","e","w","s"],["f","l","w","w","v","k","p","a","d","o","o","f","g","u","z","m","k","k","b","a","v","x","d","g","e","c","r","l","w","i","w","q","c","g","a","c","k","y","b","z","e","t","t","i","y","p","i","y","r","m","v","p","d","d","w","g","j","o","l","p","c","c","d","u","w","u","h","h","d","q","i","t","l","b","b","u","t","v","x","u","e","g","t","w"],["y","e","x","d","u","r","s","v","f","h","y","l","p","e","i","r","c","y","l","v","d","y","u","u","a","y","i","d","j","d","d","e","i","w","z","u","v","b","y","z","a","m","q","f","k","v","x","z","l","v","b","w","k","l","u","q","n","r","z","q","a","l","b","u","x","o","y","z","d","r","v","b","a","l","z","v","g","v","u","a","g","t","r","a"],["l","q","c","d","w","y","v","l","q","k","v","x","h","y","d","c","i","v","y","h","y","w","m","t","b","z","b","n","a","p","p","e","r","t","y","t","v","b","q","u","v","m","l","j","n","n","l","n","d","x","z","e","u","g","q","s","d","i","u","q","v","b","n","r","p","n","s","c","a","v","g","s","x","l","r","x","h","x","z","t","r","b","h","o"],["d","z","i","s","p","x","t","l","t","r","b","e","e","g","j","n","h","p","g","l","s","k","t","h","c","p","m","q","d","n","h","e","e","n","t","l","l","r","h","x","k","x","e","u","n","v","k","c","o","u","e","v","n","f","p","u","k","t","h","y","f","n","c","m","n","l","a","t","i","b","n","x","q","m","l","n","q","z","j","x","t","w","a","m"],["k","y","c","m","y","o","o","e","h","o","t","t","x","a","k","b","e","f","i","h","j","c","x","z","e","e","d","b","q","t","t","j","e","l","z","m","c","c","s","e","p","n","z","h","n","b","d","e","b","n","g","c","k","e","w","w","g","j","f","v","w","q","h","x","u","o","y","a","z","f","u","v","q","s","o","w","w","b","w","c","v","l","d","v"],["v","g","s","l","q","e","o","c","z","t","p","w","z","z","a","f","r","e","r","n","e","r","s","l","t","v","r","q","z","z","h","m","d","c","g","q","t","j","q","g","q","l","w","m","d","i","s","j","f","p","n","r","c","n","y","k","r","y","a","h","n","x","k","y","q","k","d","h","v","a","f","u","r","u","z","e","k","l","m","a","g","u","r","j"],["h","d","v","o","n","i","k","q","l","c","x","t","e","u","f","g","x","u","j","l","y","y","o","i","c","w","r","c","d","s","a","w","i","h","u","l","w","h","b","z","n","h","z","i","i","l","y","f","o","o","y","l","u","o","w","v","q","a","a","u","z","j","a","r","y","g","d","y","d","f","i","a","i","u","h","x","a","w","c","a","x","e","y","r"],["o","w","d","e","k","a","b","d","b","h","d","x","b","u","p","x","k","s","b","e","u","l","t","j","y","g","o","y","a","p","h","b","w","x","k","d","y","t","u","x","j","o","m","i","t","w","l","h","g","t","d","q","y","j","k","n","b","g","h","w","n","l","c","x","x","c","q","h","y","p","d","x","x","s","j","r","w","h","g","j","p","u","h","e"],["b","y","e","l","g","z","g","c","g","s","i","m","p","w","l","q","e","s","u","m","q","t","u","n","k","m","d","w","a","o","t","r","i","t","t","b","e","l","a","g","d","k","b","i","c","t","r","g","q","a","z","d","d","x","k","w","b","q","q","f","k","t","y","r","o","k","x","n","d","n","u","b","y","x","u","b","e","w","s","p","e","m","j","m"],["v","n","z","x","m","n","u","b","h","y","p","w","e","q","n","s","r","t","g","k","m","a","x","k","m","p","h","z","w","n","q","m","m","e","z","f","f","r","h","g","w","r","o","m","h","z","d","p","b","e","x","a","i","j","p","h","q","c","f","r","v","m","j","q","w","v","d","f","x","w","h","g","n","t","g","u","q","o","h","l","j","x","s","g"],["y","f","y","p","z","l","h","e","t","r","m","p","a","c","r","b","v","z","r","s","c","w","j","q","f","w","r","q","f","l","g","m","s","l","g","a","x","s","l","s","w","o","r","v","i","d","z","s","j","d","o","u","x","v","i","q","e","a","v","m","z","y","j","n","g","g","x","f","c","k","n","a","t","u","t","z","k","r","g","o","i","i","i","y"],["z","p","f","p","t","t","x","d","i","r","o","o","j","i","c","z","w","f","b","c","r","x","b","l","e","j","l","r","i","i","p","o","l","f","t","f","n","j","z","w","s","l","m","u","q","z","c","l","b","z","y","q","j","e","r","v","o","b","h","g","a","z","q","q","c","k","j","o","o","q","a","l","o","k","p","c","d","t","i","h","v","y","j","j"],["l","x","j","h","b","x","h","k","c","m","s","a","l","y","s","g","p","o","z","y","j","u","r","v","x","e","i","b","u","g","e","x","r","d","t","t","q","e","j","j","w","e","y","i","w","p","p","e","s","l","z","k","c","v","t","v","y","k","v","v","i","h","i","r","f","v","h","f","h","n","r","u","o","j","y","k","r","i","e","j","h","j","u","x"],["r","t","i","m","f","u","b","x","k","o","m","p","p","n","f","w","f","t","i","m","j","w","x","n","b","g","v","l","e","b","w","n","m","h","q","z","u","r","u","o","v","r","n","w","t","l","z","k","f","x","v","o","t","h","c","w","j","o","b","y","d","h","e","c","m","n","d","n","c","n","n","o","i","h","t","c","y","g","h","n","p","l","y","k"],["n","n","r","z","n","q","t","t","z","p","o","l","w","z","z","e","x","a","n","x","b","n","n","r","l","l","x","y","a","m","u","w","x","r","e","q","w","u","z","e","h","i","k","k","i","k","q","q","b","h","q","m","k","o","y","p","u","d","f","z","m","i","b","h","k","l","b","h","o","g","e","y","t","m","b","a","l","i","b","g","g","f","r","s"],["l","v","r","s","f","t","z","r","g","t","t","k","l","l","y","o","z","b","q","u","t","s","d","w","i","a","b","y","c","t","u","g","z","u","i","g","c","v","w","s","a","a","h","j","v","x","n","d","c","x","w","k","c","t","g","t","g","q","w","t","u","d","v","z","u","c","g","o","a","b","n","l","b","n","h","h","p","q","w","x","l","i","l","k"],["h","g","i","y","u","u","b","z","q","u","r","o","q","l","m","c","x","k","f","d","x","p","l","m","y","n","q","u","e","h","r","n","q","r","t","w","e","l","i","a","w","t","c","c","b","i","b","j","k","r","x","q","q","v","c","d","g","y","j","u","j","s","n","q","a","o","q","j","y","p","o","c","n","o","v","x","d","j","c","h","f","w","v","i"],["n","t","a","z","q","y","r","b","r","f","h","r","z","u","b","i","m","e","h","t","g","g","u","x","n","s","h","c","m","c","p","c","u","l","i","b","e","o","c","q","y","m","b","u","o","t","n","d","l","q","w","t","a","e","q","s","e","u","s","w","l","p","v","g","d","w","r","t","f","y","w","r","t","r","c","k","z","n","g","o","i","o","p","l"],["u","y","o","v","p","u","n","y","w","c","e","s","x","o","l","b","r","k","k","s","w","f","b","l","f","n","u","a","h","i","j","g","k","k","s","b","i","b","t","x","e","u","y","u","h","t","i","w","j","b","l","b","d","o","z","h","u","o","q","m","b","w","u","j","a","p","c","x","t","i","c","e","p","e","k","u","f","f","x","e","x","w","h","d"],["u","v","w","t","d","z","p","n","j","q","s","j","h","r","z","u","f","v","c","n","k","x","j","z","t","e","p","u","t","o","c","d","d","z","x","x","l","b","y","j","u","j","g","n","o","w","h","d","l","r","j","y","q","n","j","m","p","x","c","u","z","t","g","d","g","m","h","g","d","j","v","i","l","t","f","n","y","d","i","k","w","x","y","t"],["r","m","u","n","k","e","x","x","k","q","e","e","g","v","c","g","o","h","q","w","t","v","p","j","v","u","p","k","n","s","h","h","r","t","o","x","o","l","n","e","j","d","i","w","v","a","u","b","q","d","h","m","c","n","d","f","k","o","i","q","a","q","z","f","k","s","s","p","o","w","g","e","f","m","i","s","d","g","z","e","m","d","f","z"],["j","t","s","z","d","j","g","e","p","b","u","b","c","o","f","n","r","a","a","r","y","s","a","p","u","r","f","r","j","h","j","u","i","v","n","x","w","j","i","r","w","a","g","o","e","z","d","a","l","n","r","z","i","m","f","s","r","q","i","c","e","e","p","r","n","n","p","z","d","k","l","j","w","j","m","z","n","z","u","y","t","m","r","h"]]
    print(Solution().containsCycle(grid))
    #'''

    grid = [["c","a","d"],
            ["a","a","a"],
            ["a","a","d"],
            ["a","c","d"],
            ["a","b","c"]]
    print(Solution().containsCycle(grid))