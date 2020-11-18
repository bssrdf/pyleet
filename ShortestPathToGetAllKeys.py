'''
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the 
starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of 
the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  
If we walk over a key, we pick it up.  We can't walk over a lock unless we have the 
corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the 
first K letters of the English alphabet in the grid.  This means that there is exactly 
one key for each lock, and one lock for each key; and also that the letters used to 
represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

 

Example 1:

Input: ["@.a.#","###.#","b.A.B"]
Output: 8
Example 2:

Input: ["@..aA","..B#.","....b"]
Output: 6
 

Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly 
one lock.

'''
import string
from collections import deque

class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        '''
        When exploring a grid with BFS, we can 走回头路，by 
        putting a state which encodes keys or somthing else other than
        the grid cell index (i,j) in visited set.   

        '''
        m = len(grid)
        n = len(grid[0])
        start = (0, 0) 
        all_keys = []
        q = deque()
        visited = set()
        dirs = [(-1,0), (0, 1), (0, -1), (1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i,j)
                    visited.add((start, ''))
                    q.append((start, 0, ''))
                if grid[i][j] in string.ascii_lowercase:
                    all_keys.append(grid[i][j])
        
        while q:
            (cur, steps, keys) = q.popleft()                          
            if len(keys) == len(all_keys): return steps            
            for x,y in [(cur[0]+i, cur[1]+j) for (i,j) in dirs]:                                
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                    continue                
                if ord('A') <= ord(grid[x][y]) <= ord('F')  and grid[x][y].lower() not in keys:  
                    continue
                newkeys = keys[:]
                if  ord('a') <= ord(grid[x][y]) <= ord('f') and grid[x][y] not in keys:
                    newkeys = keys+grid[x][y]
                    # important: by sorting the key, we skipped visiting 
                    # many dulicated states (same set of keys but in different order)
                    # adding ust this line reduced runtime from 980ms to 508ms
                    newkeys = ''.join(sorted(newkeys))
                if ((x,y),newkeys) not in visited:
                    visited.add(((x,y),newkeys))                  
                    q.append(((x,y), steps+1, newkeys))              
            
        return -1
                     




if __name__ == '__main__':
    print(Solution().shortestPathAllKeys(["...#.",
                                          "a..@.",
                                          "#..#.",
                                          "b.#B.",
                                          ".##.A"]))
    #'''
    print(Solution().shortestPathAllKeys(["@...a",
                                          ".###A",
                                          "b.BCc"]))

    print(Solution().shortestPathAllKeys(["@.a.#","###.#","b.A.B"]))
    print(Solution().shortestPathAllKeys(["@..aA",
                                          "..B#.",
                                          "....b"]))
    #'''