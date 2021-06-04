'''

-Medium-

描述
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". 
We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the 
same shifting sequence.

You don't need to care about the order of the result.

样例
Example 1:

input:["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
output: [["a","z"],["abc","bcd","xyz"],["acef"],["az","ba"]]
Example 2:

input:["a"]
output:[["a"]]


'''

from itertools import groupby
from collections import defaultdict
class Solution:
    """
    @param strings: a string array
    @return: return a list of string array
    """
    def groupStrings(self, strings):
        # write your code here
               
        #strings.sort(key=len)
        groups = defaultdict(list)
        ans = []
        for s in strings:
            t = ''
            for c in s:
                t += str((ord(c)+26-ord(s[0]))%26)+','
            groups[t].append(s)
         
        return list(groups.values())

if __name__=="__main__":
    print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))