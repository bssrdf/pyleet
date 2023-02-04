'''
-Hard-

Given an array A of non-negative integers, the array is squareful if for every pair of 
adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 
differ if and only if there is some index i such that A1[i] != A2[i].

 

Example 1:

Input: [1,17,8]
Output: 2
Explanation: 
[1,8,17] and [17,8,1] are the valid permutations.
Example 2:

Input: [2,2,2]
Output: 1
 

Note:

1 <= A.length <= 12
0 <= A[i] <= 1e9

'''

class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = set()        
        def isSquare(n):
            k = int(n**(0.5))
            return k*k == n 
        def dfs(seq, current): 
            if not seq:
                res.add(tuple(current))
                return
            for i,v in enumerate(seq): 
                if i-1>=0 and v==seq[i-1]: continue           
                if not current or isSquare(current[-1]+v):
                    dfs(seq[:i]+seq[i+1:], current+[v])        
        dfs(A, [])
        return len(res)

    def numSquarefulPermsFast(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 78%
        res = [0]
        A.sort()
        def isSquare(n):
            k = int(n**(0.5))
            return k*k == n 
        def dfs(seq, current): 
            if not seq:
                res[0] += 1
                return
            for i,v in enumerate(seq):   
                if i-1>=0 and v==seq[i-1]: continue  
                if not current or isSquare(current[-1]+v):
                    dfs(seq[:i]+seq[i+1:], current+[v])        
        dfs(A, [])
        return res[0]
        
if __name__ == "__main__":
    print(Solution().numSquarefulPerms([1,17,8]))
    print(Solution().numSquarefulPerms([2,2,2]))
    print(Solution().numSquarefulPerms([2,2,2,2,2,2,2,2,2,2,2]))