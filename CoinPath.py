'''
-Hard-

*DP*

Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. 
The integer B denotes that from any place (suppose the index is i) in the array A, you can jump to 
any one of the place in the array A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, 
if you step on the index i, you have to pay Ai coins. If Ai is -1, it means you can’t jump to the 
place indexed i in the array.

Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed 
N using the minimum coins. You need to return the path of indexes (starting from 1 to N) in the 
array you should take to get to the place indexed N using minimum coins.

If there are multiple paths with the same cost, return the lexicographically smallest such path.

If it's not possible to reach the place indexed N then you need to return an empty array.

Example 1:

Input: [1,2,4,-1,2], 2
Output: [1,3,5]
 

Example 2:

Input: [1,2,4,-1,2], 1
Output: []
 

Note:

Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm, if and only if 
at the first i where Pai and Pbi differ, Pai < Pbi; when no such i exists, then n < m.
A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
Length of A is in the range of [1, 1000].
B is in the range of [1, 100].

'''


class Solution:
    """
    @param A: a list of integer
    @param B: an integer
    @return: return a list of integer
    """
    def cheapestJump(self, A, B):
        # write your code here
        if A[-1] == -1: return []
        n = len(A)
        res, pos, dp = [], [-1]*n, [float('inf')]*n 
        dp[-1] = A[-1]
        for i in range(n-2, -1, -1): # jump from back to front
            if A[i] == -1: continue # can not jump to this position
            for j in range(i+1, min(i+B+1, n)):
                if dp[j] == float('inf'): continue # can not jump from j to i
                if dp[i] > dp[j]+A[i]:
                   dp[i] = dp[j]+A[i] # min coins jumping from end to i
                   pos[i] = j
        if dp[0] == float('inf'): return []
        cur = 0
        while cur != -1:            
            res.append(cur+1)
            cur = pos[cur]
        return res



if __name__ == "__main__":
    print(Solution().cheapestJump([1,2,4,-1,2], 2))