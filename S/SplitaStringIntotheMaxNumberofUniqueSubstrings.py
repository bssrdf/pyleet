'''

-Medium-
*Backtracking*

Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.


'''

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # wrong
        def helper(s):
            if not s: return [ set() ]
            l, ret = 0, []
            for i in range(len(s)):
                spt = helper(s[i+1:])
                # print(s, i, s[:i+1], s[i+1:], spt)
                for sp in spt:
                    if sp and s[:i+1] not in sp:                            
                            ret.append(sp | {s[:i+1]}) 
                        # print('x', s, i, spt, ret)
            if not ret:
                ret = [ {s} ]
            # print(s, ret)
            # if len(s) > sum(len(r) for r in ret):
            #     print(s, ret)                
            return ret
        return max(len(r) for r in helper(s))
    
    def maxUniqueSplit2(self, s: str) -> int:
        seen = set()
        def helper(s, seen):
            ans = 0
            if s:
                for i in range(1, len(s) + 1):
                    candidate = s[:i]
                    if candidate not in seen:
                        seen.add(candidate)
                        ans = max(ans, 1 + helper(s[i:], seen))
                        seen.remove(candidate)
            return ans
        return helper(s, seen)

        
    
if __name__ == "__main__":
    print(Solution().maxUniqueSplit(s = "ccc"))
    print(Solution().maxUniqueSplit(s = "ababccc"))
    print(Solution().maxUniqueSplit(s = "aba"))
    print(Solution().maxUniqueSplit(s = "aa"))
    print(Solution().maxUniqueSplit(s = "ww"))
    print(Solution().maxUniqueSplit(s = "sww"))
    print(Solution().maxUniqueSplit(s = "wwwzfvedwfvhsww"))
    print(Solution().maxUniqueSplit(s = "bbgmgp"))
    print(Solution().maxUniqueSplit(s = "nfbbgmgp"))
    print(Solution().maxUniqueSplit(s = "mbaejekebbb"))
    print(Solution().maxUniqueSplit(s = "aapmihbdabknhebd"))


    print(Solution().maxUniqueSplit2(s = "ccc"))
    print(Solution().maxUniqueSplit2(s = "ababccc"))
    print(Solution().maxUniqueSplit2(s = "aba"))
    print(Solution().maxUniqueSplit2(s = "aa"))
    print(Solution().maxUniqueSplit2(s = "ww"))
    print(Solution().maxUniqueSplit2(s = "sww"))
    print(Solution().maxUniqueSplit2(s = "wwwzfvedwfvhsww"))
    print(Solution().maxUniqueSplit2(s = "bbgmgp"))
    print(Solution().maxUniqueSplit2(s = "nfbbgmgp"))
    print(Solution().maxUniqueSplit2(s = "mbaejekebbb"))
    print(Solution().maxUniqueSplit2(s = "aapmihbdabknhebd"))
