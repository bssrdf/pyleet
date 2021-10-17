'''
-Easy-

Given a list of points, find the nearest points that shares either an x or a y coordinate 
with the queried point.

The distance is denoted on a Euclidean plane: the difference in x plus the difference in y.

Input

numOfPoints, an integer representing the number of points;

points, a list of strings representing the names of each point [i];

xCoordinates, a list of integers representing the X coordinates of each point[i];

yCoordinates, a list of integers representing the Y coordinates of each point[i];

numOfQueriedPoints, an integer representing the number of points queried;

queriedPoints, a list of strings representing the names of the queried points.

Output

Return a list of strings representing the name of the nearest points that shares either 
an x or a y coordinate with the queried point.

Example 1:

Input:

numOfPoints = 3

points = ["p1","p2","p3"]

xCoordinates = [30, 20, 10]

yCoordinates = [30, 20, 30]

numOfQueriedPoints = 3

queriedPoints = ["p3", "p2", "p1"]

Output:

["p1", NONE, "p3"]

Example 2:

Input:

numOfPoints = 5

points = ["p1", "p2","p3", "p4", "p5"]

xCoordinates = [10, 20, 30, 40, 50]

yCoordinates = [10, 20, 30, 40, 50]

numOfQueriedPoints = 5

queriedPoints = ["p1", "p2", "p3", "p4", "p5"]

Output

[NONE, NONE, NONE, NONE, NONE]


'''

from collections import defaultdict
import bisect

from random import randint, seed

class Solution(object):
    def closest(self, numOfPoints,points,x,y,numQueried,queries):
        mapping = {}
        ans = []
        for i in range(numOfPoints):
            mapping[points[i]] = (x[i],y[i]) 

        for n in queries:            
            xtarget = mapping[n][0]
            ytarget = mapping[n][1]
            mindist = float('inf')
            c = None
            for k,(xo,yo) in mapping.items():
                if k != n and (xo == xtarget or yo == ytarget):
                    if abs(ytarget - yo) + abs(xtarget - xo) < mindist:
                        mindist = abs(ytarget - yo) + abs(xtarget - xo)
                        c = k
            ans.append(c)
        return ans

    def closestBinarySearch(self, numOfPoints,points,x,y,numQueried,queries):
        mapping = {}
        ans = []
        xCities, yCities = defaultdict(list), defaultdict(list)
        for i in range(numOfPoints):
            mapping[points[i]] = (x[i],y[i]) 
            xCities[x[i]].append((y[i],points[i])) 
            yCities[y[i]].append((x[i],points[i])) 

        for v in xCities.values():
            v.sort()
        for v in yCities.values():
            v.sort()
        def getMin(arr, x, y):
            idx = bisect.bisect_left(arr[x], (y,n))
            if idx == 0: 
                dx = arr[x][idx+1][0]-y
                cx = arr[x][idx+1][1]
            elif idx == len(arr[x])-1:
                dx = y - arr[x][idx-1][0]
                cx = arr[x][idx-1][1]
            else:
                d1 = y - arr[x][idx-1][0]
                d2 = arr[x][idx+1][0]-y
                if d1 < d2:
                    dx, cx = d1, arr[x][idx-1][1]
                else:
                    dx, cx = d2, arr[x][idx+1][1]
            return cx, dx 

        for n in queries:            
            xtarget = mapping[n][0]
            ytarget = mapping[n][1]
            if len(xCities[xtarget]) > 1:
                cx, dx = getMin(xCities, xtarget, ytarget)
            else:
                cx, dx = None, float('inf')
            if len(yCities[ytarget]) > 1:
                cy, dy = getMin(yCities, ytarget, xtarget)
            else:
                cy, dy = None, float('inf')
            if dx < dy: ans.append(cx)
            else: ans.append(cy)
        return ans

import time

if __name__ == "__main__":
    numOfPoints = 3
    points = ["p1","p2","p3"]
    xCoordinates = [30, 20, 10]
    yCoordinates = [30, 20, 30]
    numOfQueriedPoints = 3
    queriedPoints = ["p3", "p2", "p1"]
    print(Solution().closest(
        numOfPoints,points,xCoordinates,yCoordinates,numOfQueriedPoints,queriedPoints
    ))
    print(Solution().closestBinarySearch(
        numOfPoints,points,xCoordinates,yCoordinates,numOfQueriedPoints,queriedPoints
    ))
    numOfPoints = 5
    points = ["p1","p2","p3", "p4", "p5"]
    xCoordinates = [10, 20, 30, 40, 50]
    yCoordinates = [10, 20, 30, 40, 50]
    numOfQueriedPoints = 5
    queriedPoints = ["p1", "p2", "p3", "p4", "p5"]
    print(Solution().closest(
        numOfPoints,points,xCoordinates,yCoordinates,numOfQueriedPoints,queriedPoints
    ))
    print(Solution().closestBinarySearch(
        numOfPoints,points,xCoordinates,yCoordinates,numOfQueriedPoints,queriedPoints
    ))

    seed(41)
    pts = set()
    N = 10**5
    M = 10**5
    for i in range(N):
        x, y = randint(1, M), randint(1, M)
        pts.add((x, y))
    pts = list(pts)
    n = len(pts)
    print("total points ",n)
    numOfPoints = n
    points = []    
    xCoordinates = []
    yCoordinates = []
    for i in range(1,n+1):
        points.append('p'+str(i))
        xCoordinates.append(pts[i-1][0])
        yCoordinates.append(pts[i-1][1])
    nQ = 5000
    numOfQueriedPoints = nQ
    for i in range(nQ):
        queriedPoints.append('p'+str(randint(1,n)))
    starttime = time.time()
    sol2 = Solution().closestBinarySearch(numOfPoints,points,xCoordinates,yCoordinates,numOfQueriedPoints,queriedPoints)
    print("elapsed {}s".format(time.time()-starttime))
    starttime = time.time()
    sol1 = Solution().closest(numOfPoints,points,xCoordinates,yCoordinates,numOfQueriedPoints,queriedPoints)
    print("elapsed {}s".format(time.time()-starttime))
    assert sol1 == sol2
    #for q, s1, s2 in zip(queriedPoints, sol1, sol2):
    #    if s1 != s2: 
    #        print(q, s1, s2)
            


    


    

