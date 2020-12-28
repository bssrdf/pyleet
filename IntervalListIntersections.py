'''
-Medium-
*Interval*

Given two lists of closed intervals, each list of intervals is pairwise 
disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real 
numbers x with a <= x <= b.  The intersection of two closed intervals is a 
set of real numbers that is either empty, or can be represented as a 
closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9


'''

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B: return []                
        res = []
        na, nb = len(A), len(B)
        i, j = 0, 0
        while i < na and j < nb:
            if A[i][1] <= B[j][1]:
                if A[i][0] >= B[j][0]:
                    res.append(A[i])
                elif A[i][1] >= B[j][0]:
                    res.append([B[j][0],A[i][1]])
                i += 1
            else:
                if B[j][0] >= A[i][0]:
                    res.append(B[j])
                elif B[j][1] >= A[i][0]:
                    res.append([A[i][0], B[j][1]])
                j += 1
        return res
        
if __name__ == "__main__":
    print(Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]], 
                                          [[1,5],[8,12],[15,24],[25,26]]))