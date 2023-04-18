'''

-Medium-

You are given an array of strings of the same length words.

In one move, you can swap any two even indexed characters or any two odd indexed characters of a string words[i].

Two strings words[i] and words[j] are special-equivalent if after any number of moves, words[i] == words[j].

For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz".
A group of special-equivalent strings from words is a non-empty subset of words such that:

Every pair of strings in the group are special equivalent, and
The group is the largest size possible (i.e., there is not a string words[i] not in the group such that words[i] is special-equivalent to every string in the group).
Return the number of groups of special-equivalent strings from words.

 

Example 1:

Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation: 
One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings is all pairwise special equivalent to these.
The other two groups are ["xyzz", "zzxy"] and ["zzyx"].
Note that in particular, "zzxy" is not special equivalent to "zzyx".
Example 2:

Input: words = ["abc","acb","bac","bca","cab","cba"]
Output: 3
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 20
words[i] consist of lowercase English letters.
All the strings are of the same length.



'''

from typing import List
from collections import Counter
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        m, n = len(words), len(words[0]) 
        cnt0 = [[0]*26 for _ in range(m)]
        cnt1 = [[0]*26 for _ in range(m)]
        for i in range(m):
            for j in range(n):
                c = words[i][j]
                if j % 2 == 0:
                    cnt0[i][ord(c)-ord('a')] += 1
                else:
                    cnt1[i][ord(c)-ord('a')] += 1
        mp = set()
        # print(cnt0)
        for i in range(m):
            mark = ':'.join([str(j)+'_'+str(v) for j,v in enumerate(cnt0[i])])  
            mark1 = ':'.join([str(j)+'_'+str(v) for j,v in enumerate(cnt1[i])])  
            mp.add(mark+mark1)
        return len(mp)          




if __name__ == '__main__':
    print(Solution().numSpecialEquivGroups(words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))
