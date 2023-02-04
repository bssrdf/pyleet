'''
-Medium-

*Greedy*

We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value 
in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted 
as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.

'''

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        ans = 0
        for i in range(m):
           if A[i][0] == 0:
               A[i][:] = [1-x for x in A[i]]
        for j in range(1,n):
            cnt = 0
            for i in range(m):
                cnt += 1 if A[i][j] == 1 else 0
            if cnt < m-cnt:
                for i in range(m):
                    A[i][j] = 1-A[i][j]
        for i in range(m):
            ans += int('0b'+''.join([str(x) for x in A[i]]), base=0)
        return ans




        

if __name__ == "__main__":
    A = [[0,0,1,1],
         [1,0,1,0],
         [1,1,0,0]]
    print(Solution().matrixScore(A))