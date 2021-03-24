'''

-Hard-

Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the 
positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

 

Example 1:

Input: s1 = "ab", s2 = "ba"
Output: 1
Example 2:

Input: s1 = "abc", s2 = "bca"
Output: 2
Example 3:

Input: s1 = "abac", s2 = "baca"
Output: 2
Example 4:

Input: s1 = "aabc", s2 = "abca"
Output: 2
 

Constraints:

1 <= s1.length <= 20
s2.length == s1.length
s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
s2 is an anagram of s1.

'''

from collections import deque

class Solution(object):
    def kSimilarity(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        queue = deque([(s1, 0)])
        visited = set([s1])
        while queue:
            s, steps = queue.popleft()
            if s == s2: return steps
            i = 0
            while s[i] == s2[i]: i += 1            
            for j in range(i+1,len(s)):
                if s[j] == s2[j] or s[j] != s2[i]: continue
                sa = list(s)
                sa[i], sa[j] = sa[j], sa[i]
                nxt = ''.join(sa)
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps+1))
        return -1


if __name__ == "__main__":
    print(Solution().kSimilarity("abac", "baca"))
    print(Solution().kSimilarity("abccaacceecdeea","bcaacceeccdeaae"))