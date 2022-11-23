'''

-Hard-
*DP*
*Prefix Sum*


You are given a string s that consists of the digits '1' to '9' and two integers k and minLength.

A partition of s is called beautiful if:

s is partitioned into k non-intersecting substrings.
Each substring has a length of at least minLength.
Each substring starts with a prime digit and ends with a non-prime digit. Prime digits are '2', '3', '5', and '7', and the rest of the digits are non-prime.
Return the number of beautiful partitions of s. Since the answer may be very large, return it modulo 109 + 7.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "23542185131", k = 3, minLength = 2
Output: 3
Explanation: There exists three ways to create a beautiful partition:
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"
Example 2:

Input: s = "23542185131", k = 3, minLength = 3
Output: 1
Explanation: There exists one way to create a beautiful partition: "2354 | 218 | 5131".
Example 3:

Input: s = "3312958", k = 3, minLength = 1
Output: 1
Explanation: There exists one way to create a beautiful partition: "331 | 29 | 58".
 

Constraints:

1 <= k, minLength <= s.length <= 1000
s consists of the digits '1' to '9'.



'''
import sys
sys.setrecursionlimit(10000)
from functools import lru_cache
import bisect
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        primes = {'2', '3', '5', '7'}
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(minLength, n+1):
            if s[i-1] not in primes: 
                for j in range(1, i-minLength+2):
                    if s[j-1] not in primes: continue
                    for l in range(1, k+1):                    
                        dp[i][l] = (dp[i][l] + dp[j-1][l-1]) % MOD
        return dp[n][k]
    

    def beautifulPartitions6(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        primes = {'2', '3', '5', '7'}
        if s[0] not in primes or s[-1] in primes: return 0
        dp = [[0]*(k+1) for _ in range(n+1)]
        preSum = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1
        preSum[0][0] = 1
        for i in range(1, n+1):
            if i >= minLength and s[i-1] not in primes and (i == n or s[i] in primes): 
                for l in range(1, k+1):                    
                    dp[i][l] = preSum[i-minLength][l-1]
            for l in range(k+1):                    
                preSum[i][l] = (preSum[i-1][l] + dp[i][l]) % MOD     
        return dp[n][k]
    
    def beautifulPartitions2(self, s: str, k: int, minLength: int) -> int:
        # TLE
        MOD = 10**9 + 7
        n = len(s)
        primes = {'2', '3', '5', '7'}
        # print('n=', n)
        if k * minLength > n or s[0] not in primes or s[-1] in primes:
            return 0        
        nonprimes = []
        for i in range(n-1):
            if s[i] not in primes and s[i+1] in primes:
            # if s[i] not in primes:
                nonprimes.append(i)   
        if s[n-1] not in primes:
            nonprimes.append(n-1)   
        M = len(nonprimes)    
        # print('nonprimes', len(nonprimes))
        @lru_cache(None)
        def dp(i, j):
            if i == n and j == 0: return 1
            if i < n and j == 1: 
                return 1 if n-i >= minLength else 0 
            if i == n or j == 0: return 0
            # print(s[i])
            if s[i] in primes:
                cnt = 0
                # print(i, j)
                # for l in range(i+minLength-1, n):
                m = i + minLength - 1 
                idx = bisect.bisect_left(nonprimes, m)
                # for l in nonprimes:                     
                for ll in range(idx, M):  
                    l = nonprimes[ll]  
                    if (n-l) < (j-1) * max(minLength,2): break
                    cnt = (cnt + dp(l+1, j-1)) % MOD 
                return cnt
            return 0
        return dp(0, k)

    def beautifulPartitions3(self, s: str, k: int, minLength: int) -> int:
        n, primes, mod = len(s), set('2357'), (10 ** 9) + 7
        @lru_cache(None)
        def dp(i, at_start, k):
            if i == n: return int(k == 0)
            if i > n or k == 0 or s[i] not in primes and at_start: return 0
            if s[i] in primes:
                if at_start: return dp(i + minLength - 1, False, k)
                else: return dp(i + 1, False, k)
            return (dp(i + 1, True, k - 1) + dp(i + 1, False, k)) % mod
        return dp(0, True, k)
    

    def beautifulPartitions4(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        MOD = 10**9 + 7
        primes = ['2', '3', '5', '7']
        
        # pruning
        if k * minLength > n or s[0] not in primes or s[-1] in primes:
            return 0
        
        # posible starting indexes of a new partition
        ids = [0]
        for i in range(n-1):
            if s[i] not in primes and s[i+1] in primes:
                ids.append(i+1)
        m = len(ids)

        @lru_cache(None)
        # dp(i, kk) means number of ways to partition s[ids[i]:n] into kk partitions
        def dp(i, kk):
            
            # kk==1: last remaining partition, needs to have length >= l
            if kk == 1:
                return 1 if ids[i]+minLength-1 <= n-1 else 0
            res = 0
            
            # iterate possible starting index of next partition
            for j in range(i+1, m-kk+2):
                if ids[j]-ids[i] >= minLength:
                    res = (res + dp(j, kk-1)) % MOD 
            
            return res
        
        return dp(0, k)

    def beautifulPartitions5(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        MOD = 10**9 + 7
        primes = set('2357')

        @lru_cache(None)
        def dp(i, j):
            if j == 0 and i <= n:
                return 1
            if i >= n:
                return 0

            ans = dp(i+1, j)  # Skip
            if s[i] in primes and s[i-1] not in primes:  # Split
                ans += dp(i+minLength, j-1)
            return ans % MOD

        if s[0] not in primes or s[-1] in primes: return 0

        return dp(minLength, k-1)
    
    



if __name__=="__main__":
    print(Solution().beautifulPartitions(s = "23542185131", k = 3, minLength = 2))
    print(Solution().beautifulPartitions2(s = "23542185131", k = 3, minLength = 2))
    print(Solution().beautifulPartitions6(s = "23542185131", k = 3, minLength = 2))
    print(Solution().beautifulPartitions(s = "23542185131", k = 3, minLength = 3))
    print(Solution().beautifulPartitions2(s = "23542185131", k = 3, minLength = 3))
    print(Solution().beautifulPartitions6(s = "23542185131", k = 3, minLength = 3))
    # print(Solution().beautifulPartitions2(s = "3312958", k = 3, minLength = 1))

    s = "5155478282545937968677617165631996468422164721323437519981446499152361954963331348923115716653185682542873276533677171776423333937123888899147277975961395649121398465651768244786466485243834762359217344839381811585594334236128116525334963947959335618699383111688831863874435384924219934665268346389432951615945663317943255837728218731853289674543626337914657641148738337625139163472521771814322464828841948684633589964788392533142421691317794485793329647654574888464938879543862867988458154467692789493227549139223733114791239715438977415795764626937889572188863637572214545999845994952572638187327776863887953736933992959678728458361285275718217778562478957554712112118391581537963499158785724741446626246644678951166714624383896197364797341168952736146545938293195831632267494379237556584545748242951743349374612743231843643968422249431823338785223562691223717599695964697431997677135492974582635557536563885726841193474961349394778361131719517648936781369277746876574482711574163694739183493417181"
    print(Solution().beautifulPartitions(s = s, k = 204, minLength = 2))
    print(Solution().beautifulPartitions6(s = s, k = 204, minLength = 2))
    print(Solution().beautifulPartitions2(s = s, k = 204, minLength = 2))
    print(Solution().beautifulPartitions5(s = s, k = 204, minLength = 2))

    s = "3939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939393939"
    print(Solution().beautifulPartitions(s = s, k = 500, minLength = 1))
    print(Solution().beautifulPartitions6(s = s, k = 500, minLength = 1))
    print(Solution().beautifulPartitions2(s = s, k = 500, minLength = 1))
    print(Solution().beautifulPartitions5(s = s, k = 500, minLength = 1))
    s = "2121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121"
    print(Solution().beautifulPartitions(s = s, k = 100, minLength = 4))
    print(Solution().beautifulPartitions6(s = s, k = 100, minLength = 4))
    print(Solution().beautifulPartitions2(s = s, k = 100, minLength = 4))
    print(Solution().beautifulPartitions5(s = s, k = 100, minLength = 4))

