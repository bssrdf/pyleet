'''
-Medium-

*Greedy*
*Priority Queue*

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of 
indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
 

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9

'''
import heapq

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        n = len(A)
        res, pq = [0] * n, []
        l, r = 0, n-1
        for i,b in enumerate(B):
            heapq.heappush(pq, (-b, i))
        while pq:
            num, idx = heapq.heappop(pq)
            if A[r] > (-num):
                res[idx] = A[r]
                r -= 1
            else:
                res[idx] = A[l]
                l += 1
        return res



if __name__ == "__main__":
    print(Solution().advantageCount([2,7,11,15], [1,10,4,11]))
    print(Solution().advantageCount([12,24,8,32], [13,25,32,11]))