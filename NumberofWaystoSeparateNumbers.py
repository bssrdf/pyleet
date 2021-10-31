'''

-Hard-

You wrote down many positive integers in a string called num. However, you realized 
that you forgot to add commas to seperate the different numbers. You remember 
that the list of integers was non-decreasing and that no integer had leading zeros.

Return the number of possible lists of integers that you could have written down to 
get the string num. Since the answer may be large, return it modulo 10**9 + 7.

 

Example 1:

Input: num = "327"
Output: 2
Explanation: You could have written down the numbers:
3, 27
327
Example 2:

Input: num = "094"
Output: 0
Explanation: No numbers can have leading zeros and all numbers must be positive.
Example 3:

Input: num = "0"
Output: 0
Explanation: No numbers can have leading zeros and all numbers must be positive.
Example 4:

Input: num = "9999999999999"
Output: 101
 

Constraints:

1 <= num.length <= 3500
num consists of digits '0' through '9'.


Really hard problem!!!

'''

from functools import lru_cache
from itertools import zip_longest, islice
from math import floor, log2
import numpy as np

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        def ranks(l):
            index = {v: i for i, v in enumerate(sorted(set(l)))}
            return [index[v] for v in l]

        def suffixArray(s):
            line = ranks(s)
            n, k, ans, sa = len(s), 1, [line], [0]*len(s)
            while k < n - 1:
                line = ranks(list(zip_longest(line, islice(line, k, None), fillvalue=-1)))
                ans, k = ans + [line], k << 1
            for i, k in enumerate(ans[-1]): sa[k] = i
            return ans, sa

        def compare(i, j, l, k):
            a = (c[k][i], c[k][(i+l-(1<<k))%n])
            b = (c[k][j], c[k][(j+l-(1<<k))%n])
            return 0 if a == b else 1 if a < b else -1

        s = num 
        c, sa = suffixArray([int(i) for i in s])

        n, M = len(s), 10**9 + 7
        dp = np.zeros([n+1, n+1], dtype = int) #[[0]*(n+1) for _ in range(n+1)]
        mp = np.zeros([n+1, n+1], dtype = int) #[[0]*(n+1) for _ in range(n+1)]

        for k in range(n+1):
            dp[0][k] = 1
            mp[0][k] = 1

        logs = [0] + [floor(log2(k)) for k in range(1, n+1)]

        s_zero = np.array([i != "0" for i in s], dtype = int)

        for i in range(1, n+1):
            dp[i][1:i+1] = mp[range(i-1,-1,-1), range(i)] * s_zero[i-1::-1]

            check1 = dp[range(i-1, (i-1)//2, -1), range(1, i//2 + 1)]
            f = lambda k: compare(i-2*k, i-k, k, logs[k]) >= 0
            check2 = np.array([f(i) for i in range(1, i//2+1)])

            dp[i][1:i//2+1] = dp[i][1:i//2+1] + check1*check2
            dp[i][1:i//2+1] = [x % M for x in dp[i][1:i//2+1]]

            mp[i] = np.cumsum(dp[i])

        return mp[-1][-1] % M
    
    def numberOfCombinations2(self, num: str) -> int:
        """
        If previous number is num[i:j], in order to count number of combs in num[j:],
        then count(i, j) = sum(count(j, k) for k that num[j:k] >= num[i:j] and without leading zero).
        
        Fix j, and increment i. Decrement k to match i.
        Goal: sum count(0, j) for all 1 <= j <= n.
        Initial: When j == n, count = 1 if no leading zeros, or else 0.
        """
        n = len(num)
        MOD = 10**9 +7
        counts = [[0] * (n+1) for _ in range(n)]
        # If all characters in num are the same, set this flag to save time in partial_compare
        all_same_flag = True if num.count(num[0]) == len(num) else False
        for i in range(n):
            counts[i][n] = 1 if num[i] != '0' else 0
        
        @lru_cache(None)
        def partial_compare(i, j) -> int:
            """Return
			0: num[i:j] == num[j:2*j-i]
			>0: num[i:j] > num[j:2*j-i], and the value is the first position (1-indexed) where they're different
			<0: num[i:j] < num[j:2*j-i], and the absolute value is the first position (1-indexed) where they're different
			"""
            if i == j or all_same_flag:
                return 0
            elif num[i] != num[j]:
                return i+1 if num[i] > num[j] else -(i+1)
            elif 2*j - i == n or 2*j - i == n-1:
                for k in range(j-i):
                    if num[i+k] != num[j+k]:
                        return i+k if num[i+k] > num[j+k] else -(i+k+1)
                return 0
            else:
                idx = partial_compare(i+1, j+1)
                return 0 if idx == 0 or abs(idx)-1 >= j else idx
            
        ans = counts[0][n]
        for j in range(n-1, 0, -1):
            k, total = n, 0
            for i in range(j):
                if num[i] != '0':
                    while k-j > j-i or (k-j == j-i and partial_compare(i, j) <= 0):
                        total = (total + counts[j][k]) % MOD
                        k -= 1
                    counts[i][j] = total
            ans = (ans + counts[0][j]) % MOD
            # No longer used
            del counts[j]
        return ans

    def numberOfCombinations3(self, num: str) -> int:
        N, n = 3501, len(num)
        dp, dpp, pf, M = [0]*N, [0]*N, [0]*N, 1000000007
        for l in range(1, n+1):
            dpp[0] = 1
            for i in range(n, l, -1):
                pf[i - 1] = pf[i]+1 if num[i - 1 - l] == num[i - 1] else 0
            for i in range(n):
                dp[i + 1] = dpp[i + 1]
                if l <= i + 1 and num[i + 1 - l] != '0':
                    if (i + 1 - 2 * l >= 0 and (pf[i + 1 - l] >= l or num[i + 1 - l + pf[i + 1 - l]] > num[i + 1 - 2 * l + pf[i + 1 - l]])):                    
                        dp[i + 1] = (dp[i + 1] + dp[i + 1 - l]) % M
                    else:
                        dp[i + 1] = (dp[i + 1] + dpp[i + 1 - l]) % M
            dp, dpp = dpp, dp   
        return dpp[n]

    def numberOfCombinations4(self, num: str) -> int:

        mod = 10**9+7
        def ad(a,  b):
            return (a+b+mod)%mod
        def compare(i, j, l, s):
        # returns true if s[i: i+len-1] <= s[i+len,i+2*len-1] 
            common = same[i][j]   
            if common >= l: return 1              #equal substrings
            if s[i+common] < s[j+common]: return 1  #first substring is smaller
            else: return 0

        n = len(num)
        if num[0] == '0': return 0

        same = [[0]*(n+1) for _ in range(n+1)]
        # same[i][j] = largest common prefix of num.substr(i) and num.substr(j)
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if num[i]==num[j]:
                    same[i][j] = same[i+1][j+1]+1
        
        pref = [[0]*n for _ in range(n)]

        #base case
        for j in range(n): pref[0][j] = 1
 
        for i in range(1, n):
            if num[i] == '0' :
                pref[i] = pref[i-1]
                continue 
            
            for j in range(i, n):
                len_ = j-i+1 
                prevStart = i-1-(len_-1) 
                count = 0
                
                # second last number cant have length = len
                if prevStart < 0: 
                    count = pref[i-1][i-1]; #= dp[0][i-1] + dp[1][i-1] ... dp[i-1][i-1]
                
                else:
                    
                    #when length of second last number < len
                    count = ad(pref[i-1][i-1], -pref[prevStart][i-1]) #= dp[prevStart+1][i-1] ... dp[i-1][i-1]
                    
                    #length of second last number == len
                    if compare(prevStart, i, len_, num):
                        cnt = (pref[prevStart][i-1] if prevStart == 0 else 
                                  ad(pref[prevStart][i-1], -pref[prevStart-1][i-1]))
                        count = ad(count, cnt)
                
                pref[i][j] = ad(pref[i-1][j], count)   #updating prefix sum

        return pref[n-1][n-1]
       
if __name__ == "__main__":
    print(Solution().numberOfCombinations("327"))
    print(Solution().numberOfCombinations2("327"))
    print(Solution().numberOfCombinations4("327"))