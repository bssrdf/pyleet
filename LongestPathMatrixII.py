# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 23:56:08 2017

@author: merli
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        distance = [[0 for _ in xrange(N)] for _ in xrange(M)]          
        paths = [[[] for _ in xrange(N)] for _ in xrange(M)]          
        #distance[ball[0]][ball[1]] = 0
        dirs=((-1,0), (1,0), (0,-1), (0,1))
        def dfs(i, j, distance, paths):
            localpath = []
            for direct in dirs:
                x=i+direct[0]
                y=j+direct[1]
                if x >= 0 and y >= 0 and x < M and y < N and matrix[x][y] > matrix[i][j]:
                #print x, y, count, direct[0], direct[1]
                    dfs(x, y, distance, paths)
                    if distance[i][j] < distance[x][y]+1:
                        distance[i][j] = distance[x][y]+1
                        if localpath:
                            del localpath[:]
                        localpath.extend(paths[x][y])
            paths[i][j].append((i,j))
            if localpath:
                paths[i][j].extend(localpath)
        #for i in xrange(M):
         #   for j in xrange(N):
#        #        print 'processing: ',i,j
         #       dfs(i,j,distance,paths)
        dfs(0,0,distance,paths)
        #for d in distance:
         #   print d
        print paths[0][0]
        return distance[0][1] 
        
if __name__ == "__main__":
    """
    matrix=[
     [9,9,4],
     [6,6,8],
     [2,1,1]
      ]
    """
    matrix=[
     [2,1,1],
     [6,7,8],
     [9,9,4]
      ]
    for m in matrix:    
        print m 
    print '================='
    print Solution().longestIncreasingPath(matrix)
