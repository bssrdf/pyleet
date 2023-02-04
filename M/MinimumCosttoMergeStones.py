'''
-Hard-

There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

A move consists of merging exactly k consecutive piles into one pile, and the cost of this move 
is equal to the total number of stones in these k piles.

Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

 

Example 1:

Input: stones = [3,2,4,1], k = 2
Output: 20
Explanation: We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], k = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the 
task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], k = 3
Output: 25
Explanation: We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
 

Constraints:

n == stones.length
1 <= n <= 30
1 <= stones[i] <= 100
2 <= k <= 30

'''

from functools import lru_cache
class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        INT_MAX = 3001
        def helper(arr, cur):
            if len(arr) == 1:
                return cur
            elif len(arr) < k:
                return -1
            n = len(arr)
            moves = INT_MAX
            cnt = 0            
            for j in range(k-1):
                cnt += arr[j]
            for i in range(n-k+1):                               
                cnt += arr[i+k-1]
                moves = min(moves, helper(arr[:i]+[cnt]+arr[i+k:], cur+cnt))
                cnt -= arr[i]
            return moves 
        return helper(stones, 0)   

    def mergeStones2(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        INT_MAX = 2**31-1
        self.res = INT_MAX
        def helper(arr, cur):
            if len(arr) == 1:
                self.res = min(self.res, cur)
                return             
            elif len(arr) < k:
                return 
            elif cur > self.res:
                return
            n = len(arr)
            cnt = 0            
            for j in range(k-1):
                cnt += arr[j]
            for i in range(n-k+1):                               
                cnt += arr[i+k-1]
                helper(arr[:i]+[cnt]+arr[i+k:], cur+cnt)
                cnt -= arr[i]
            return 
        helper(stones, 0)   
        return -1 if self.res == INT_MAX else self.res

    def mergeStones3(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        INT_MAX = 2**31-1
        self.res = INT_MAX
        if (len(stones) - 1) % (k - 1) != 0: 
            return -1
        @lru_cache(None)
        def helper(arr, cur):
            if len(arr) == 1:
                self.res = min(self.res, cur)
                return             
            elif len(arr) < k:
                return 
            elif cur > self.res:
                return
            n = len(arr)
            cnt = 0            
            for j in range(k-1):
                cnt += arr[j]
            for i in range(n-k+1):                               
                cnt += arr[i+k-1]
                helper(arr[:i]+(cnt,)+arr[i+k:], cur+cnt)
                cnt -= arr[i]
            return 
        helper(tuple(stones), 0)   
        return -1 if self.res == INT_MAX else self.res
    
    def mergeStonesDP(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        n = len(stones)
        if (len(stones) - 1) % (k - 1) != 0: 
            return -1
        INT_MAX = 2**31-1
        sums = [0]*(n + 1)
        dp = [[0]*n for _ in range(n)]
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + stones[i - 1]
        for length in range(k, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                dp[i][j] = INT_MAX
                for t in range(i,j,k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][t] + dp[t + 1][j])
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += sums[j + 1] - sums[i]
        return dp[0][n - 1]
        

if __name__ == "__main__":
    print(Solution().mergeStones2([3,2,4,1], 2))
    print(Solution().mergeStones2([3,2,4,1], 3))
    print(Solution().mergeStones2([3,5,1,2,6], 3))
    #print(Solution().mergeStones2([69,39,79,78,16,6,36,97,79,27,14,31,4], 2))
    print(Solution().mergeStones3([3,2,4,1], 2))
    print(Solution().mergeStones3([3,2,4,1], 3))
    print(Solution().mergeStones3([3,5,1,2,6], 3))
    print(Solution().mergeStones3([69,39,79,78,16,6,36,97,79,27,14,31,4], 2))
    print(Solution().mergeStones3([29,59,31,7,51,99,47,40,24,20,98,41,42,81,92,55],2))
    print(Solution().mergeStonesDP([69,39,79,78,16,6,36,97,79,27,14,31,4], 2))
    print(Solution().mergeStonesDP([29,59,31,7,51,99,47,40,24,20,98,41,42,81,92,55],2))
