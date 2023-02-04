'''
-Medium-

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, 
it is the product of some integer with itself. For example, 1, 4, 9, and 16 are 
perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 10^4


'''

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(2, n+1):
            j = 1
            j2 = j*j
            while j2 <= i:
                #k = i//j2
                dp[i] = min(dp[i], dp[i-j2]+1)
                j += 1
                j2 = j*j
        #    print(i, dp)
        return dp[n]

    def numSquaresBFS(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt


        
if __name__ == "__main__":
    print(Solution().numSquares(12))
    print(Solution().numSquares(13))
    print(Solution().numSquares(8))
    print(Solution().numSquares(4))
    print(Solution().numSquares(3006))