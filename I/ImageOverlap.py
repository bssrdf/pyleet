'''
Two images A and B are given, represented as binary, square matrices of the 
same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or 
down any number of units), and place it on top of the other image.  After, 
the overlap of this translation is the number of positions that have a 1 in 
both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1


'''
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        la = []
        lb = []
        d =  {}
        # use lists to record coordinates of pixels of interest (here 1's)
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    la.append((i,j))
                if B[i][j] == 1:
                    lb.append((i,j))    
        for a in la:
            for b in lb:
                # take vector difference (or displacement vector) and convert 
                # them to strings so they can be put into a dict 
                s = str(a[0]-b[0])+" "+str(a[1]-b[1])                
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1
        ans = 0
        for m in d.values():
            ans = max(ans, m)
        return ans




if __name__ == "__main__":
    A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
    B = [[0,0,0],
            [0,1,1],
            [0,1,0]]
    print(Solution().largestOverlap(A,B))

