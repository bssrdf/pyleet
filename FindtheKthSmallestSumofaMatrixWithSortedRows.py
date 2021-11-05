'''
-Hard-

You are given an m * n matrix, mat, and an integer k, which has its rows sorted 
in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return 
the Kth smallest array sum among all possible arrays.

 

Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  
Example 2:

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
Example 3:

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
Example 4:

Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12
 

Constraints:

m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] is a non decreasing array.




'''
from typing import List
import heapq
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        sum_ = sum(row[0] for row in mat)
        pq = [(sum_, (0,)*m)] 
        s = {(0,)*m}
        cnt = 0
        while pq:
            res, index = heapq.heappop(pq)
            cnt += 1
            if cnt == k: return res
            for i in range(m):
                if index[i] < n-1:
                    index_ = index[:i] + (index[i]+1,)+index[i+1:]
                    if index_ not in s:
                        s.add(index_)
                        sum_ = res - mat[i][index[i]] + mat[i][index[i]+1] 
                        heapq.heappush(pq, (sum_, index_))
        return -1    



if __name__ == "__main__":
    print(Solution().kthSmallest(mat = [[1,3,11],[2,4,6]], k = 5))  
    print(Solution().kthSmallest(mat = [[1,3,11],[2,4,6]], k = 9))  
    print(Solution().kthSmallest(mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7))  
