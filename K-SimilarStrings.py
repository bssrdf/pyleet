'''

-Hard-
*BFS*

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
            # find the first index where s differs from s2
            # we'd like to swap s[i] with s[j] where j > i such that s gets closer to s2 
            while s[i] == s2[i]: i += 1            
            for j in range(i+1,len(s)):
                # if s[j] is the same as s2[j], we don't want to change s[j] 
                # by swapping with s[i], which will get s further ways from s2
                # if s[j] != s2[i], swapping with s[i] will not get s closer to s2
                if s[j] == s2[j] or s[j] != s2[i]: continue
                # now we find a s[j] such that swapping it with s[i] will 
                # make s[i] = s2[i], one step closer to s2
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