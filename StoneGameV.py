'''
-Hard-

There are several stones arranged in a row, and each stone has an associated value which is an 
integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right 
row), then Bob calculates the value of each row which is the sum of the values of all the stones 
in this row. Bob throws away the row which has the maximum value, and Alice's score increases by 
the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which 
row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's is initially zero.

Return the maximum score that Alice can obtain.

 

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28
Example 3:

Input: stoneValue = [4]
Output: 0
 

Constraints:

1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6


'''

from itertools import accumulate

class Solution(object):
    def stoneGameVTLE(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        sm = sum(stoneValue)
        #preSum = [0] + list(accumulate(stoneValue))
        memo = [[0 for _ in range(n)] for _ in range(n)]
        def helper(left, right, sm):
            if left == right: return 0
            if memo[left][right] > 0: return memo[left][right]
            lSum = res = 0
            for i in range(left, right):
                lSum += stoneValue[i]
                rSum = sm - lSum
                if lSum < rSum: res = max(res, lSum+helper(left, i, lSum))
                elif lSum > rSum: res = max(res, rSum+helper(i+1,right, rSum))
                else:
                    res = max(res, lSum+helper(left, i, lSum))
                    res = max(res, rSum+helper(i+1,right, rSum))
            memo[left][right] = res
            return memo[left][right]
        return helper(0, n-1, sm)

    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        """
        In the intuitive O(N^3) DP, to calculate the maximum score h[i][j], we need to iterate through 
        any k that i <= k < j. But if we examine the relationship among h[i][j], h[i][j+1] and h[i-1][j], 
        it's possible to derive an optimized O(N^2) solution.

        Let's split the candidates of h[i][j] into 2 groups, depending on whether picking the left or right 
        row:

        picking the left row [i,k], score = sum(stoneValue[i], ..., stoneValue[k]) + h[i][k], iff 
        sum(stoneValue[i], ..., stoneValue[k]) <= sum(stoneValue[k+1],..., stoneValue[j])
        
        picking the right row [k+1,j], score = sum(stoneValue[k+1],..., stoneValue[j]) + h[k+1][j], 
        iff sum(stoneValue[k+1],..., stoneValue[j]) <= sum(stoneValue[i],..., stoneValue[k])

        Now, what if we need to calculate h[i][j+1]? The left row candidates for h[i][j] are also candidates 
        for h[i][j+1], since sum(stoneValue[i], ..., stoneValue[k]) <= sum(stoneValue[k+1],..., stoneValue[j]) 
        and stoneValue[j+1] > 0.

        So when we calculate all of h[i][i], h[i][i+1],...h[i][n], each left row candidate with 
        score = sum(stoneValue[i], ..., stoneValue[k]) + h[i][k] (i <= k < n) only needs to calculate once.

        The same trick also holds when we need to calculate h[i-1][j]. The right row candidates for h[i][j] 
        are also candidates for h[i-1][j].

        So when we calculate all of h[j][j], h[j-1][j], ... h[1][j], each right row candidate with 
        score = sum(stoneValue[k+1],..., stoneValue[j]) + h[k+1][j] (1 <= k < j) only needs to calculate once.

        To keep the calculation of both left row and right row candidates in order respectively, the first 
        loop should iterate through the row length from 1 to n, then the second loop simply enumates all 
        possible rows with that length.

        Time: O(N^2)
        Space: O(N^2)
        
        """

        n = len(stoneValue)
        preSum = [0]
        for x in stoneValue:
            preSum.append(preSum[-1] + x)
            
        dp = [[0] * (n+1) for _ in range(n+1)]
        left, right = [0] * (n+1), [0] * (n+1)
        x, y = [0] * (n+1), [0] * (n+1)
        
        for i in range(1,n+1):
            x[i], y[i] = i, i - 1
        
        for l in range(2, n + 1): # length start from 2 (2 non-empty rows; each needs to at least 1)
            for i in range(1, n+1):
                j = i + l - 1
                if j > n:
                    break

                half = (preSum[j] - preSum[i-1]) // 2
                
                while x[i] < j and preSum[x[i]] - preSum[i-1] <= half:
                    left[i] = max(left[i], preSum[x[i]] - preSum[i-1] + dp[i][x[i]])
                    x[i] += 1
                    
                while y[j] >= i and preSum[j] - preSum[y[j]] <= half:
                    right[j] = max(right[j], preSum[j] - preSum[y[j]] + dp[y[j]+1][j])
                    y[j] -= 1
                    
                dp[i][j] = max(left[i], right[j])

        return dp[1][n]
        
        


if __name__ == "__main__":
    print(Solution().stoneGameV([6,2,3,4,5,5]))