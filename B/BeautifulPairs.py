'''
-Hard-
$$$

*Divide and Conquer*


Description
You are given two 0-indexed integer arrays nums1 and nums2 of the same length. A pair of indices (i,j) is called beautiful if|nums1[i] - nums1[j]| + |nums2[i] - nums2[j]| is the smallest amongst all possible indices pairs where i < j.

Return the beautiful pair. In the case that there are multiple beautiful pairs, return the lexicographically smallest pair.

Note that

|x| denotes the absolute value of x.
A pair of indices (i1, j1) is lexicographically smaller than (i2, j2) if i1 < i2 or i1 == i2 and j1 < j2.
 

Example 1:

Input: nums1 = [1,2,3,2,4], nums2 = [2,3,1,2,3]
Output: [0,3]
Explanation: Consider index 0 and index 3. The value of |nums1[i]-nums1[j]| + |nums2[i]-nums2[j]| is 1, which is the smallest value we can achieve.
Example 2:

Input: nums1 = [1,2,4,3,2,5], nums2 = [1,4,2,3,5,1]
Output: [1,4]
Explanation: Consider index 1 and index 4. The value of |nums1[i]-nums1[j]| + |nums2[i]-nums2[j]| is 1, which is the smallest value we can achieve.
 

Constraints:

2 <= nums1.length, nums2.length <= 105
nums1.length == nums2.length
0 <= nums1i <= nums1.length
0 <= nums2i <= nums2.length



'''

from typing import List
from math import inf
from collections import defaultdict

class Solution:
    def beautifulPair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Divide and Conquer O(NlogN)
        n = len(nums1) 
        Pts = [(x,y,i) for i,(x,y) in enumerate(zip(nums1, nums2))]  
        XPts = sorted(list(Pts))
        YPts = sorted(list(Pts), key=lambda x: x[1])

        def dist(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)

        def helper(Z, X, Y):
            # print(Z, X, Y)
            if len(Z) <= 3:
                dmin = inf
                pair = [n,n]
                for i in range(len(Z)):
                    for j in range(i+1, len(Z)):
                        d = dist(Z[i][0], Z[i][1], Z[j][0], Z[j][1])
                        if dmin > d:
                            dmin = d
                            pair = sorted([Z[i][2], Z[j][2]])
                        elif dmin == d:
                            pair = min(pair, sorted([Z[i][2], Z[j][2]]))
                return dmin, pair            
            XL, XR = X[:len(X)//2], X[len(X)//2:]          
            IL = set(x[2] for x in X[:len(X)//2])
            # P, Q = [], []
            # YL, YR = [], []
            # for i in range(len(Y)):
            #     if Y[i][2] in IL:
            #         YL.append(Y[i]) 
            #     else:
            #         YR.append(Y[i])
            YL = [y for y in Y if y[2] in IL]
            YR = [y for y in Y if y[2] not in IL]
            P =  [z for z in Z if z[2] in IL]
            Q =  [z for z in Z if z[2] not in IL]

            dp, pairP = helper(P, XL, YL)
            dq, pairQ = helper(Q, XR, YR)
            if dp == dq:
                d = dp
                pair = min(pairP, pairQ)
            elif dp < dq:
                d = dp
                pair = pairP
            else:
                d = dq
                pair = pairQ
            sep = (XL[-1][0] + XR[0][0]) // 2
            strip = [y for y in Y if abs(y[0]-sep) <= d]
            for j in range(len(strip)-1):
                for k in range(j+1, min(j+10,len(strip))):
                    dd = dist(strip[j][0], strip[j][1], strip[k][0], strip[k][1])
                    if d > dd:
                        d = dd
                        pair = sorted([strip[j][2],strip[k][2]])
                    elif d == dd:
                        pair = min(pair, sorted([strip[j][2],strip[k][2]]))
            return d, pair                                 

        _, p = helper(Pts, XPts, YPts)
        return p    
    
    def beautifulPair4(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Divide and Conquer O(NlogN)
        n = len(nums1) 
        Pts = [(x,y,i) for i,(x,y) in enumerate(zip(nums1, nums2))]  
        XPts = sorted(list(Pts))
        YPts = sorted(list(Pts), key=lambda x: x[1])

        def dist(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)

        def helper(X, Y):
            # print(Z, X, Y)
            if len(X) <= 3:
                dmin = inf
                pair = [n,n]
                for i in range(len(X)):
                    for j in range(i+1, len(X)):
                        d = dist(X[i][0], X[i][1], X[j][0], X[j][1])
                        if dmin > d:
                            dmin = d
                            pair = sorted([X[i][2], X[j][2]])
                        elif dmin == d:
                            pair = min(pair, sorted([X[i][2], X[j][2]]))
                return dmin, pair            
            XL, XR = X[:len(X)//2], X[len(X)//2:]          
            IL = set(x[2] for x in XL)
            YL = [y for y in Y if y[2] in IL]
            YR = [y for y in Y if y[2] not in IL]
            dp, pairP = helper(XL, YL)
            dq, pairQ = helper(XR, YR)
            if dp == dq:
                d = dp
                pair = min(pairP, pairQ)
            elif dp < dq:
                d = dp
                pair = pairP
            else:
                d = dq
                pair = pairQ
            sep = (XL[-1][0] + XR[0][0]) // 2
            strip = [y for y in Y if abs(y[0]-sep) <= d]
            for j in range(len(strip)-1):
                for k in range(j+1, min(j+10,len(strip))):
                    dd = dist(strip[j][0], strip[j][1], strip[k][0], strip[k][1])
                    if d > dd:
                        d = dd
                        pair = sorted([strip[j][2],strip[k][2]])
                    elif d == dd:
                        pair = min(pair, sorted([strip[j][2],strip[k][2]]))
            return d, pair                                 

        _, p = helper(XPts, YPts)
        return p    
    
    def beautifulPair3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def dist(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)

        def dfs(l: int, r: int):
            if l >= r:
                return inf, -1, -1
            m = (l + r) >> 1
            x = points[m][0]
            d1, pi1, pj1 = dfs(l, m)
            d2, pi2, pj2 = dfs(m + 1, r)
            if d1 > d2 or (d1 == d2 and (pi1 > pi2 or (pi1 == pi2 and pj1 > pj2))):
                d1, pi1, pj1 = d2, pi2, pj2
            t = [p for p in points[l: r + 1] if abs(p[0] - x) <= d1]
            t.sort(key=lambda x: x[1])
            for i in range(len(t)):
                for j in range(i + 1, len(t)):
                    if t[j][1] - t[i][1] > d1:
                        break
                    pi, pj = sorted([t[i][2], t[j][2]])
                    d = dist(t[i][0], t[i][1], t[j][0], t[j][1])
                    if d < d1 or (d == d1 and (pi < pi1 or (pi == pi1 and pj < pj1))):
                        d1, pi1, pj1 = d, pi, pj
            return d1, pi1, pj1

        pl = defaultdict(list)
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            pl[(x, y)].append(i)
        points = []
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if len(pl[(x, y)]) > 1:
                return [i, pl[(x, y)][1]]
            points.append((x, y, i))
        points.sort()
        _, pi, pj = dfs(0, len(points) - 1)
        return [pi, pj]


    def beautifulPair2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute Force O(N^2)
        n = len(nums1)
        ans = [-1, -1]
        mi = inf
        for i in range(n):
            for j in range(i+1, n):
                k = abs(nums1[i]-nums1[j]) + abs(nums2[i]-nums2[j])
                if mi > k:
                    mi = k
                    ans = [i,j]
        # print(ans, mi)
        return ans


from random import randint
import time
if __name__ == '__main__':
    print(Solution().beautifulPair(nums1 = [1,2,3,2,4], nums2 = [2,3,1,2,3]))
    print(Solution().beautifulPair(nums1 = [1,2,4,3,2,5], nums2 = [1,4,2,3,5,1]))
    
    nums1 = [11, 8, 1, 5, 17, 14, 11, 8, 2, 18, 0, 17, 14, 17, 6, 11, 8, 10, 11, 16]
    nums2 = [17, 5, 12, 9, 20, 10, 7, 7, 1, 6, 17, 14, 16, 6, 2, 0, 15, 7, 14, 19]
    print(Solution().beautifulPair(nums1 = nums1, nums2 = nums2))
    print(Solution().beautifulPair2(nums1 = nums1, nums2 = nums2))
    nums1 = [15, 4, 2, 12, 7, 18, 13, 0, 16, 20, 20, 14, 16, 5, 20, 9, 14, 10, 5, 16]
    nums2 =  [8, 19, 19, 14, 1, 1, 14, 4, 14, 20, 10, 3, 5, 9, 18, 17, 18, 3, 6, 3]
    print(Solution().beautifulPair(nums1 = nums1, nums2 = nums2))
    print(Solution().beautifulPair2(nums1 = nums1, nums2 = nums2))
    nums1 = [7, 17, 3, 11, 19, 19, 10, 4, 19, 6, 6, 15, 7, 15, 18, 10, 8, 20, 6, 15]
    nums2 = [19, 7, 7, 6, 20, 19, 14, 18, 6, 4, 5, 11, 16, 14, 13, 11, 8, 10, 15, 10]
    print(Solution().beautifulPair(nums1 = nums1, nums2 = nums2))
    print(Solution().beautifulPair2(nums1 = nums1, nums2 = nums2))
    
    t1, t2 = 0., 0.
    for _ in range(100):
        n = 10000
        nums1 = [randint(0, n) for _ in range(n)]
        nums2 = [randint(0, n) for _ in range(n)]
        sets = set((x,y) for x,y in zip(nums1, nums2))
        nums1, nums2 = [], []
        for x,y in sets:
            nums1.append(x)
            nums2.append(y)
        # print(nums1)
        # print(nums2)
        start = time.time()
        sol1 = Solution().beautifulPair3(nums1 = nums1, nums2 = nums2)
        end = time.time()
        t1 += end-start 
        start = time.time()
        sol2 = Solution().beautifulPair4(nums1 = nums1, nums2 = nums2)
        end = time.time()
        t2 += end-start 
        assert sol1 == sol2
    print(t1, t2)






