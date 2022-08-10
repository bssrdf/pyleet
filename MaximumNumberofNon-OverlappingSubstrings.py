'''


-Hard-
*Hash Table*
*Greedy*
*Sorting*


Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.


'''

from typing import List
from collections import defaultdict

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        ans = []
        invs = defaultdict(list)
        # We can start by finding the starting and ending index for each character.
        for i,c in enumerate(s):
            if not invs[c]:
                invs[c].append(i)
        for i in range(len(s)-1, -1, -1):
            if len(invs[s[i]]) == 1:
                invs[s[i]].append(i)            
        subs = set()        
        def expand(a, b):
            while True:
                a1, b1 = a, b
                for c in set(s[a:b+1]):
                    a1 = min(a1, invs[c][0])
                    b1 = max(b1, invs[c][1])
                if a1 == a and b1 == b: 
                    return (a1, b1)
                a, b = a1, b1

        for c in invs:
            a, b = invs[c]
            # From these indices, we can form the substrings by expanding each character's range 
            # if necessary (if another character exists in the range with smaller/larger 
            # starting/ending index).
            a1, b1 = expand(a,b)
            subs.add((a1,b1))
        
        # Sort the valid substrings by length 
        subs = sorted(subs, key=lambda x: x[1]-x[0])
        def overlap(inv, invs):
            for a, b in invs:
                if not (inv[0] > b or inv[1] < a):                    
                    return True
            return False

        for sub in subs:
            if not ans or not overlap(sub, ans): #  greedily take those with the smallest length, 
                                                 #  discarding the ones that overlap those we took.
                ans.append(sub)
        return [s[a:b+1] for a,b in ans]   
    
    def maxNumOfSubstrings2(self, s: str) -> List[str]:

        ans = []
        invs = defaultdict(list)
        # We can start by finding the starting and ending index for each character.
        for i,c in enumerate(s):
            if not invs[c]:
                invs[c].append(i)
        for i in range(len(s)-1, -1, -1):
            if len(invs[s[i]]) == 1:
                invs[s[i]].append(i)            

        subs = []
        for c in invs:
            a, b = invs[c]
            valid = True
            k = a
            while k <= b:
                if invs[s[k]][0] < a: # if a character to the right of a has starting position
                                      # before a, that means 'c' can not form a valid substring
                    valid = False
                    break
                b = max(b, invs[s[k]][1]) # only needs to expand to the right
                k += 1
            if valid: 
                subs.append((a, b))
        # print(subs)
        # Sort the valid substrings by length 
        subs = sorted(subs, key=lambda x: x[1]-x[0])
        def overlap(inv, invs):
            for a, b in invs:
                if not (inv[0] > b or inv[1] < a):                    
                    return True
            return False

        for sub in subs:
            if not ans or not overlap(sub, ans): #  greedily take those with the smallest length, 
                                                 #  discarding the ones that overlap those we took.
                ans.append(sub)
        return [s[a:b+1] for a,b in ans]   
    

    def maxNumOfSubstrings3(self, s: str) -> List[str]:
        ans = []
        invs = defaultdict(list)
        # We can start by finding the starting and ending index for each character.
        for i,c in enumerate(s):
            if not invs[c]:
                invs[c].append(i)
        for i in range(len(s)-1, -1, -1):
            if len(invs[s[i]]) == 1:
                invs[s[i]].append(i)            
        subs = set()        
        def expand(a, b):
            while True:
                a1, b1 = a, b
                for c in set(s[a:b+1]):
                    a1 = min(a1, invs[c][0])
                    b1 = max(b1, invs[c][1])
                if a1 == a and b1 == b: 
                    return (a1, b1)
                a, b = a1, b1

        for c in invs:
            a, b = invs[c]
            # From these indices, we can form the substrings by expanding each character's range 
            # if necessary (if another character exists in the range with smaller/larger 
            # starting/ending index).
            a1, b1 = expand(a,b)
            subs.add((a1,b1))
        
        # Sort the valid substrings by end
        intervals = sorted(subs, key=lambda x: x[1])
        i = 0
        while i < len(intervals):
            ans.append(intervals[i])
            j = i+1
            while j < len(intervals) and intervals[j][0] < intervals[i][1]:
                j += 1
            i = j        
        return [s[a:b+1] for a,b in ans]   

        

if __name__ == "__main__":
    print(Solution().maxNumOfSubstrings(s = "adefaddaccc"))
    print(Solution().maxNumOfSubstrings(s = "abbaccd"))
    print(Solution().maxNumOfSubstrings(s = "abab"))
    print(Solution().maxNumOfSubstrings(s = "zyz"))
    print(Solution().maxNumOfSubstrings(s = "cabcccbaa"))
    print(Solution().maxNumOfSubstrings(s = "bbcacbaba"))

    print(Solution().maxNumOfSubstrings2(s = "adefaddaccc"))
    print(Solution().maxNumOfSubstrings2(s = "abbaccd"))
    print(Solution().maxNumOfSubstrings2(s = "abab"))
    print(Solution().maxNumOfSubstrings2(s = "zyz"))
    print(Solution().maxNumOfSubstrings2(s = "cabcccbaa"))
    print(Solution().maxNumOfSubstrings2(s = "bbcacbaba"))


    print(Solution().maxNumOfSubstrings3(s = "adefaddaccc"))
    print(Solution().maxNumOfSubstrings3(s = "abbaccd"))
    print(Solution().maxNumOfSubstrings3(s = "abab"))
    print(Solution().maxNumOfSubstrings3(s = "zyz"))
    print(Solution().maxNumOfSubstrings3(s = "cabcccbaa"))
    print(Solution().maxNumOfSubstrings3(s = "bbcacbaba"))