'''

-Medium-

*Binary Search*


'''

import bisect

class Solution:
    def medianRowwiseSortedMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        target = (m*n +1) // 2 
        l, r = float('inf'), -float('inf')
        for i in range(m):
            l = min(l, matrix[i][0])
            r = max(r, matrix[i][-1])
        while l < r:
            cnt = 0
            mid = l + (r-l)//2
            for i in range(m):
                idx = bisect.bisect_right(matrix[i], mid)
                cnt += idx 
            print(mid, l, r, cnt, target)
            if cnt < target:
                l = mid + 1
            else:
                r = mid
        return l




if __name__ == "__main__":
    mat = [ [2,  3,  3],
            [1,  5,  6],
            [6,  6,  9]]
    print(Solution().medianRowwiseSortedMatrix(matrix= mat))
    mat = [ [2,  3,  3],
            [1,  2,  6],
            [6,  6,  7]]
    print(Solution().medianRowwiseSortedMatrix(matrix= mat))
    mat = [ [2,  3,  3],
            [1,  2,  2],
            [6,  6,  7]]
    print(Solution().medianRowwiseSortedMatrix(matrix= mat))
