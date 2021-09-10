'''
-Medium-

You are given an integer n. You have an n x n binary grid grid with all values initially 1's 
except for some indices given in the array mines. The ith element of the array mines is defined 
as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four 
arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there 
could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

 

Example 1:


Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
Example 2:


Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.
 

Constraints:

1 <= n <= 500
1 <= mines.length <= 5000
0 <= xi, yi < n
All the pairs (xi, yi) are unique.


'''

class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mines = {(x,y) for x,y in mines}
        lall, rall = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
        uall, dall = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
        for i in range(n):
            cnt = 0
            for j in range(n):
                if (i,j) not in mines: cnt += 1
                else: cnt = 0
                lall[i][j] = cnt
            cnt = 0
            for j in range(n-1,-1,-1):
                if (i,j) not in mines: cnt += 1
                else: cnt = 0
                rall[i][j] = cnt
        for j in range(n):
            cnt = 0
            for i in range(n):
                if (i,j) not in mines: cnt += 1
                else: cnt = 0
                uall[i][j] = cnt
            cnt = 0
            for i in range(n-1,-1,-1):
                if (i,j) not in mines: cnt += 1
                else: cnt = 0
                dall[i][j] = cnt
        res = 0
        for i in range(n):
            for j in range(n):
                if (i,j) not in mines:
                    res = max(res, min(lall[i][j], rall[i][j], uall[i][j], dall[i][j]))
        return res

    def orderOfLargestPlusSignOptSpace(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mines = {(x,y) for x,y in mines}
        #lall, rall = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
        res, rall = 0, [0]*n
        uall, dall = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
        for j in range(n):
            cnt = 0
            for i in range(n):
                if (i,j) not in mines: cnt += 1
                else: cnt = 0
                uall[i][j] = cnt
            cnt = 0
            for i in range(n-1,-1,-1):
                if (i,j) not in mines: cnt += 1
                else: cnt = 0
                dall[i][j] = cnt
        for i in range(n):
            cnt = 0
            for j in range(n-1,-1,-1):
                if (i,j) not in mines: cnt += 1
                else: cnt = 0
                rall[j] = cnt
            cnt = 0
            for j in range(n):
                if (i,j) not in mines: cnt += 1
                else: cnt = 0
                res = max(res, min(cnt, rall[j], uall[i][j], dall[i][j]))
        return res
    
    def orderOfLargestPlusSignOptSpace2(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mines = {(x,y) for x,y in mines}
        res, rall, uall = 0, [0]*n, [0]*n
        dall = [[0]*n for _ in range(n)]
        for j in range(n):
            cnt = 0
            for i in range(n-1,-1,-1):
                if (i,j) not in mines: cnt += 1
                else: cnt = 0
                dall[i][j] = cnt
        for i in range(n):
            cnt = 0
            for j in range(n-1,-1,-1):
                if (i,j) not in mines: 
                    cnt += 1
                    uall[j] += 1
                else: 
                    cnt = 0
                    uall[j] = 0
                rall[j] = cnt
            cnt = 0
            for j in range(n):
                if (i,j) not in mines: cnt += 1
                else: cnt = 0
                res = max(res, min(cnt, rall[j], uall[j], dall[i][j]))
        return res

    def orderOfLargestPlusSignOptSpace3(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        #mines = {(x,y) for x,y in mines}
        grid = [[1]*n for _ in range(n)]
        for i,j in mines:
            grid[i][j] = 0
        res, rall, uall = 0, [0]*n, [0]*n
        dall = [[0]*n for _ in range(n)]
        for j in range(n):
            cnt = 0
            for i in range(n-1,-1,-1):
                if grid[i][j]: cnt += 1
                else: cnt = 0
                dall[i][j] = cnt
        for i in range(n):
            cnt = 0
            for j in range(n-1,-1,-1):
                if grid[i][j]: 
                    cnt += 1
                    uall[j] += 1
                else: 
                    cnt = 0
                    uall[j] = 0
                rall[j] = cnt
            cnt = 0
            for j in range(n):
                if grid[i][j]: cnt += 1
                else: cnt = 0
                res = max(res, min(cnt, rall[j], uall[j], dall[i][j]))
        return res
            


 

if __name__ == "__main__":
    print(Solution().orderOfLargestPlusSign(n = 5, mines = [[4,2]]))
    print(Solution().orderOfLargestPlusSign(n = 1, mines = [[0,0]]))
    print(Solution().orderOfLargestPlusSignOptSpace(n = 5, mines = [[4,2]]))
    print(Solution().orderOfLargestPlusSignOptSpace(n = 1, mines = [[0,0]]))
    print(Solution().orderOfLargestPlusSignOptSpace2(n = 5, mines = [[4,2]]))
    print(Solution().orderOfLargestPlusSignOptSpace2(n = 1, mines = [[0,0]]))
    print(Solution().orderOfLargestPlusSignOptSpace3(n = 5, mines = [[4,2]]))
    print(Solution().orderOfLargestPlusSignOptSpace3(n = 1, mines = [[0,0]]))

