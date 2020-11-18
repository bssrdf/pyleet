'''
-Medium-
*Greedy*

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith 
domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the 
tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, 
or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:


Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row 
equal to 2, as indicated by the second figure.

Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= A.length == B.length <= 2 * 104
1 <= A[i], B[i] <= 6

'''
import sys
import heapq
from collections import defaultdict 

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        res = sys.maxsize
        def stats(L):
            ma = defaultdict(int)
            qa = []
            for a in L:
                ma[a] += 1
            for i in ma:
                heapq.heappush(qa, (-ma[i],i))
            return qa
        qa = stats(A)
        qb = stats(B)        
        while qa or qb:
            C, D = None, None
            if (qa and qb and qa[0] < qb[0]) or (not qb):
                _, m = heapq.heappop(qa)
                C, D = A, B
            else:
                _, m = heapq.heappop(qb)
                C, D = B, A
            count = 0
            match = True
            for i in range(n):
                if C[i] == m: continue
                if D[i] == m: 
                    count += 1                        
                else:
                    match = False
                    break
            if match:
                res = min(res, count)
        return -1 if res ==sys.maxsize else res





if __name__ == "__main__":
    print(Solution().minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
    print(Solution().minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))