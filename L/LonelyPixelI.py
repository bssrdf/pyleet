'''
-Medium-
*Matrix*

Given a picture consisting of black and white pixels, find the number of 
black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', 
which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position 
where the same row and same column don't have any other black pixels.

Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]
Output: 3
Explanation: All the three 'B's are black lonely pixels.


Note:
The range of width and height of the input 2D array is [1,500].

'''

class Solution(object):
    def findLonelyPixel(self, picture):
        '''
        :type picture: List[List[str]]        
        :rtype: int
        '''
        m = len(picture)
        n = len(picture[0])
        colCnts, rowCnts = [0]*n, [0]*m
        res = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    colCnts[j] += 1
                    rowCnts[i] += 1
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    if colCnts[j] == 1 and rowCnts[i] == 1:
                        res += 1
        return res

if __name__ == "__main__":

    print(Solution().findLonelyPixel([['W', 'W', 'B'],
                                      ['W', 'B', 'W'],
                                      ['B', 'W', 'W']]))