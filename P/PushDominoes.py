'''

-Medium-
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, 
we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. 
Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the 
balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional 
force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:

n == dominoes.length
1 <= n <= 10^5
dominoes[i] is either 'L', 'R', or '.'.

'''

class Solution(object):
    def pushDominoesWrong(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = list(dominoes)
        n = len(dominoes)
        left, right = -2, -2
        for i in range(n):
            if dominoes[i] == 'L': right = i
            if dominoes[i] == 'R': left = i
            if left < right:
                l, r = left+1, right-1
                print('l,r', l, r)
                if l-1 < 0:
                    while r >= 0: 
                       dominoes[r] = dominoes[r+1]                       
                       r -= 1
                else:
                    while l < r:
                        dominoes[l] = dominoes[l-1]
                        dominoes[r] = dominoes[r+1]
                        l += 1
                        r -= 1
                left = right + 1
                right += 1
        print(dominoes)
        left, right = n+1, n+1
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L': right = i
            if dominoes[i] == 'R': left = i
            if left < right:
                l, r = left+1, right-1
                if r+1 >= n:
                    while l < n:
                        dominoes[l] = dominoes[l-1]
                        l += 1
                else:
                    while l < r:
                        dominoes[l] = dominoes[l-1]
                        dominoes[r] = dominoes[r+1]
                        l += 1
                        r -= 1
                right = left - 1
                left  -= 1

        return ''.join(dominoes)

    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        A = ['L']+list(dominoes)+['R']
        n = len(A)
        left, right = 0, -1        
        for i in range(n):
            if A[i] == '.': continue                   
            right = i
            if A[left] == A[right]:
                for j in range(left+1, right):
                    A[j] = A[left]
            elif A[left] == 'R' and A[right] == 'L':
                l, r = left+1, right-1
                while l < r:
                    A[l] = A[l-1]
                    A[r] = A[r+1]
                    l += 1
                    r -= 1
            left = right
        return ''.join(A[1:-1])

    def pushDominoesSlow(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        A = 'L'+dominoes+'R'
        n = len(A)
        res = ''
        left, right = 0, -1        
        for right in range(1, n):
            if A[right] == '.': continue                   
            mid = right-left-1
            if left > 0: res += A[left]
            if A[left] == A[right]:
                res += A[right]*mid
            elif A[left] == 'L' and A[right] == 'R':
                res += '.'*mid
            else:
                res += 'R'*(mid//2) + '.'*(mid%2)+'L'*(mid//2)
            left = right
        return res



                    
            


if __name__ == "__main__": 
    print(Solution().pushDominoes(".L.R...LR..L.."))
    #'''
    print(Solution().pushDominoes("RR.L"))
    print(Solution().pushDominoes("R."))
    print(Solution().pushDominoes(".L"))
    print(Solution().pushDominoes("..R.."))
    print(Solution().pushDominoes("R.R.L"))
    #'''
    print(Solution().pushDominoesSlow(".L.R...LR..L.."))