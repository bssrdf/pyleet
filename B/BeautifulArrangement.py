'''
-Medium-
*Backtracking*
*DFS*

Suppose you have n integers from 1 to n. We define a beautiful arrangement 
as an array that is constructed by these n numbers successfully if one of 
the following is true for the ith position (1 <= i <= n) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Given an integer n, return the number of the beautiful arrangements that 
you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 15

'''

class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """

        visited = [0]*(n+1)
        self.res = 0
        def dfs(i): # i is the position         
            if i > n: 
                self.res += 1 
                return
            for j in range(1, n+1): # j is the number put on position i
                if visited[j] == 0 and (i % j == 0 or j % i == 0):
                    visited[j] = 1
                    dfs(i+1)
                    visited[j] = 0
        dfs(1)
        return self.res   
        
        


if __name__ == "__main__":
    print(Solution().countArrangement(4))