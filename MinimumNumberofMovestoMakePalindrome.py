'''
-Hard-
*Greedy*
*Fenwick Tree*

You are given a string s consisting only of lowercase English letters.

In one move, you can select any two adjacent characters of s and swap them.

Return the minimum number of moves needed to make s a palindrome.

Note that the input will be generated such that s can always be converted to a palindrome.

 

Example 1:

Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab". 
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.
Example 2:

Input: s = "letelt"
Output: 2
Explanation:
One of the palindromes we can obtain from s in 2 moves is "lettel".
One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
Other palindromes such as "tleelt" can also be obtained in 2 moves.
It can be shown that it is not possible to obtain a palindrome in less than 2 moves.
 

Constraints:

1 <= s.length <= 2000
s consists only of lowercase English letters.
s can be converted to a palindrome using a finite number of moves.


'''
from collections import Counter, defaultdict

class BIT:
    def __init__(self, n):
        self.sums = [0] * (n+1)
    
    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        def helper(s):
            # print(s)
            if len(s) <= 1: return 0
            ret1, ret2 = 0, 0
            j = len(s)-1
            while j > 0 and s[j] != s[0]:
                ret1 += 1
                j -= 1
            i = 0    
            while i < len(s)-1 and s[i] != s[-1]:
                ret2 += 1
                i += 1
            
            if ret1 < ret2:
                return ret1 + helper(s[1:j]+s[j+1:])
            else:
                return ret2 + helper(s[:i]+s[i+1:-1])
        return helper(s)

    
    def minMovesToMakePalindrome2(self, s: str) -> int:
        s = list(s)
        res = 0
        while s:
            i = s.index(s[-1])
            if i == len(s) - 1:
                res += i // 2
            else:
                res += i
                s.pop(i)
            s.pop()
        return res
    
    def minMovesToMakePalindrome3(self, s):
        n = len(s)
        s = [ord(x) - 95 for x in s]
        ans, bit = 0, BIT(n)
        if sum(x % 2 == 1 for x in Counter(s).values()) > 1: return -1

        idx = defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)

        B, P = [0] * n, []
        for c, I in idx.items():
            cnt = len(I)
            if cnt % 2:
                B[I[cnt//2]] = n//2 + 1
            for i in range((cnt)//2):
                P += [(I[i], I[~i])]

        for i, (l, r) in enumerate(sorted(P)):
            B[l], B[r] = i + 1, n - i
        
        for i, b in enumerate(B):
            ans += i - bit.query(b)
            bit.update(b, 1)
        
        return ans
        
if __name__ == "__main__":
    print(Solution().minMovesToMakePalindrome(s = "letelt"))
    print(Solution().minMovesToMakePalindrome(s = "aabb"))

