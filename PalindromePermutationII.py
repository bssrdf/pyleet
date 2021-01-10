'''
-Medium-

Given a string s, return all the palindromic permutations (without duplicates)
 of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []

'''

from collections import defaultdict

class Solution(object):
    def generatePalindromes(self, s):
        m = defaultdict(int)
        res = set()
        for c in s:
            m[c] += 1
        t, mid = [], ''
        for c in m:
            if m[c] % 2 == 1: mid += c
            else: t.extend([c]*(m[c]//2))
            if len(mid) > 1: return []
        def permute(t, start):
            if start >= len(t):
                res.add(''.join(t) + mid + ''.join(t[::-1]))
                return
            for i in range(start, len(t)):
                if i != start and t[i] == t[start]: continue
                t[i], t[start] = t[start], t[i]
                permute(t, start+1)
                t[i], t[start] = t[start], t[i]
        permute(t, 0)
        return list(res)

if __name__ == "__main__":
    print(Solution().generatePalindromes("abba"))
    print(Solution().generatePalindromes("cabba"))