'''
-Medium-
*Matrix*


Given a picture consisting of black and white pixels, and a positive integer N, 
find the number of black pixels located at some specific row R and column C 
that align with all the following rules:

Row R and column C both contain exactly N black pixels.
For all rows that have a black pixel at column C, they should be exactly the 
same as row R
The picture is represented by a 2D char array consisting of 'B' and 'W', which 
means black and white pixels respectively.

Example:
Input:                                            
[['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'W', 'B', 'W', 'B', 'W']]
N = 3
Output: 6
Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 
1 and 3).
0 1 2 3 4 5 column index

0 [['W', 'B', 'W', 'B', 'B', 'W'],

1 ['W', 'B', 'W', 'B', 'B', 'W'],

2 ['W', 'B', 'W', 'B', 'B', 'W'],

3 ['W', 'W', 'B', 'W', 'B', 'W']]

row index


Take 'B' at row R = 0 and column C = 1 as an example:
Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels.
Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. 
They are exactly the same as row R = 0.


Note:
The range of width and height of the input 2D array is [1,200].

'''

class Solution(object):
    def findLonelyPixel(self, picture, N):
        '''
        :type picture: List[List[str]]        
        :rtype: int
        '''
        m = len(picture)
        n = len(picture[0])
        colCnts, rowCnts = [0]*n, [0]*m
        res = 0
        rows = []
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    colCnts[j] += 1
                    rowCnts[i] += 1
            rows.append(''.join(picture[i]))
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    if colCnts[j] == N and rowCnts[i] == N:
                        for k in range(m):
                            if picture[k][j] == 'B'and \
                               rows[k] != rows[i]: 
                               break
                        else:
                            res += colCnts[j]
                            colCnts[j] = 0
        return res

if __name__ == "__main__":
    pixels = [['W', 'B', 'W', 'B', 'B', 'W'],    
              ['W', 'B', 'W', 'B', 'B', 'W'],    
              ['W', 'B', 'W', 'B', 'B', 'W'],    
              ['W', 'W', 'B', 'W', 'B', 'W']]

    print(Solution().findLonelyPixel(pixels, 3))