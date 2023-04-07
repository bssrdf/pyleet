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

class Solution:
    def beautifulPair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Divide and Conquer O(NlogN)
        n = len(nums1) 
        Pts = [(x,y,i) for i,(x,y) in enumerate(zip(nums1, nums2))]  
        XPts = [(x,y,i) for i,(x,y) in enumerate(zip(nums1, nums2))]  
        XPts.sort()
        YPts = [(x,y,i) for i,(x,y) in enumerate(zip(nums1, nums2))]  
        YPts.sort(key=lambda x: x[1])


        def helper(Z, X, Y):
            # print(Z, X, Y)
            if len(Z) <= 3:
                dmin = inf
                pair = [n,n]
                for i in range(len(Z)):
                    for j in range(i+1, len(Z)):
                        d = abs(Z[i][0]-Z[j][0]) + abs(Z[i][1]-Z[j][1]) 
                        if dmin > d:
                            dmin = d
                            pair = sorted([Z[i][2], Z[j][2]])
                        elif dmin == d:
                            pair = min(pair, sorted([Z[i][2], Z[j][2]]))
                return dmin, pair
            P, Q = X[:len(X)//2], X[len(X)//2:]           
            XL, XR = X[:len(X)//2], X[len(X)//2:]          
            IL = set(x[2] for x in X[:len(X)//2])
            YL, YR = [], []
            for i in range(len(Y)):
                if Y[i][2] in IL: 
                    YL.append(Y[i]) 
                else:
                    YR.append(Y[i])
            dp, pairP = helper(P, XL, YL)
            dq, pairQ = helper(Q, XR, YR)
            d = min(dp, dq)
            if dp == dq:
                d = dp
                pair = min(pairP, pairQ)
            elif dp < dq:
                d = dp
                pair = pairP
            else:
                d = dq
                pair = pairQ
            # print(dp, dq, pairP, pairQ)
            strip = []
            sep = (XL[-1][0] + XR[0][0]) // 2
            for i in range(len(Y)):
                if sep - d <= Y[i][0] <= sep + d:
                    strip.append(Y[i])
            for j in range(len(strip)-1):
                for k in range(j+1, min(j+10,len(strip))):
                    dd = abs(strip[j][0]-strip[k][0]) + abs(strip[j][1]-strip[k][1]) 
                    if d > dd:
                        d = dd
                        pair = sorted([strip[j][2],strip[k][2]])
                    elif d == dd:
                        pair = min(pair, sorted([strip[j][2],strip[k][2]]))
            # print('ret', d, pair)
            return d, pair                                 

        _, p = helper(Pts, XPts, YPts)
        return p    

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
    
    for _ in range(1000):
        n = 1000
        nums1 = [randint(0, n) for _ in range(n)]
        nums2 = [randint(0, n) for _ in range(n)]
        # print(nums1)
        # print(nums2)
        sol1 = Solution().beautifulPair(nums1 = nums1, nums2 = nums2)
        sol2 = Solution().beautifulPair2(nums1 = nums1, nums2 = nums2)
        assert sol1 == sol2






