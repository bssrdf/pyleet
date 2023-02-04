'''

-Medium-

$$$



A subsequence of a string is good if it is not empty and the frequency of each one of its characters is the same.

Given a string s, return the number of good subsequences of s. Since the answer may be too large, return it modulo 109 + 7.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

Example 1:

Input: s = "aabb"
Output: 11
Explanation: The total number of subsequences is 24. There are five subsequences which are not good: "aabb", "aabb", "aabb", "aabb", and the empty subsequence. Hence, the number of good subsequences is 24-5 = 11.
Example 2:

Input: s = "leet"
Output: 12
Explanation: There are four subsequences which are not good: "leet", "leet", "leet", and the empty subsequence. Hence, the number of good subsequences is 24-4 = 12.
Example 3:

Input: s = "abcd"
Output: 15
Explanation: All of the non-empty subsequences are good subsequences. Hence, the number of good subsequences is 24-1 = 15.
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.



'''

from collections import Counter

N = 10001

MOD = 10**9 + 7
f = [1] * N
g = [1] * N
for i in range(1, N):
    f[i] = f[i - 1] * i % MOD
    g[i] = pow(f[i], MOD - 2, MOD)


def comb(n, k):
    return f[n] * g[k] * g[n - k] % MOD


class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        '''
        由于题目说的是子序列中字母出现的次数，因此，我们可以先用一个数组 cnt 统计字符串 s 中每个字母
        出现的次数，记最大的次数为 mx。

        接下来，我们在[1,2,..mx]范围内枚举子序列中字母出现的次数i，然后枚举所有出现过的字母，
        如果该字母c的出现次数cnt[c]大于等于i，那么我们可以从这cnt[c]个相同字母中选择其中i个，
        也可以一个都不选，那么当前字母的可选方案数就是comb(cnt[c],i)+1，将所有可选方案数相乘，
        可以得到当前次数的所有子序列次数，将次数减去1累加到答案中。

        那么问题的关键在于如何快速求出comb(n,k)，我们可以用逆元来求解，具体实现见代码。

        时间复杂度O(nC)，空间复杂度O(n)。其中n为字符串s的长度，而C是字符集的大小，本题中C=26。
        '''


        cnt = Counter(s)
        ans = 0
        for i in range(1, max(cnt.values()) + 1): # iterating over each frequency i
            x = 1
            for v in cnt.values():
                if v >= i: # only letters with frequency >= i can contribute  
                    x = x * (comb(v, i) + 1) % MOD
            ans = (ans + x - 1) % MOD
        return ans


    
if __name__ == '__main__':
    print(Solution().countGoodSubsequences(s = "aabb"))
    print(Solution().countGoodSubsequences(s = 'leet'))
