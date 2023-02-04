'''
-Hard-
*Binary Search*
*Rolling Hash*
*Rabin Karp*

Given a string s, consider all duplicated substrings: (contiguous) substrings of s that 
occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not 
have a duplicated substring, the answer is "".

 

Example 1:

Input: s = "banana"
Output: "ana"
Example 2:

Input: s = "abcd"
Output: ""
 

Constraints:

2 <= s.length <= 3 * 104
s consists of lowercase English letters.

'''

from stree import STree, suffix_tree
from collections import deque

class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        A = [ord(c)-ord('a') for c in s]
        MOD = 2**63-1
        def test(L):
           # if L == 0: return None
            P = pow(26, L, MOD)
            cur = 0
            for i in range(L):
               cur = (cur*26+A[i])%MOD
            st = {cur}
            for i in range(L, len(s)):
                cur = (26*cur - P*A[i-L] + A[i]) % MOD
                if cur in st: return i-L+1
                st.add(cur)
        res, left, right = 0, 0, len(s)
        while left < right:
            mid = (left + right) // 2
            pos = test(mid)
            if pos:
                left = mid+1
                res = pos
            else:
                right = mid
        # print(left, right, res)
        return s[res:res+left-1]
    
    def longestDupSubstring2(self, s: str) -> str:
        st = suffix_tree(s+'$')
        
        que = deque([("", st.root)])
        res = ''
        # def update_max(lst, x):
        #     if not lst or len(lst[0]) < len(x):
        #         return [x]
        #     return lst 

        while que:
            s1, node = que.popleft()
            for _, (str_ref, tr) in node.children.items():
                if tr.children:
                    s2 = s1 + st.substr(str_ref)
                    que.append((s2, tr))
                    if len(s2) > len(res):
                       res = s2
        return res




if __name__ == "__main__":
    print(Solution().longestDupSubstring("banana"))
    print(Solution().longestDupSubstring("abcd"))
    print(Solution().longestDupSubstring("nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy"))
    print(Solution().longestDupSubstring2("banana"))
    print(Solution().longestDupSubstring2("abcd"))
    print(Solution().longestDupSubstring2("nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy"))

