'''
-Easy-




'''

from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cnt, sm = 0, 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        i1 = i + di
                        j1 = j + dj
                        if 0 <= i1 < m and 0 <= j1 < n:
                            cnt += 1
                            sm  += img[i1][j1]
                ans[i][j] = sm // cnt
        return ans
                