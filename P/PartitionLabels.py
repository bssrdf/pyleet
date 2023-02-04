'''

-Medium-
*Greedy*

A string S of lowercase letters is given. We want to partition this 
string into as many parts as possible so that each letter appears in 
at most one part, and return a list of integers representing the size 
of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because 
it splits S into less parts.

Example 2:

Input: s = "eccbbbbdec"
Output: [10]

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.



'''

from typing import List

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        '''
        Figure out the rightmost index first and use it to denote the start
        of the next section.

        Reset the left pointer at the start of each new section.

        Store the difference of right and left pointers + 1 as in the 
        result for each section.

        '''
        book={}
        for i,s in enumerate(S):
            book[s] = i
        print(book)
        lo = hi = 0
        res = []
        for i,s in enumerate(S):
            hi = max(hi, book[s])
            if hi == i:
                res.append(hi-lo+1)
                lo = hi + 1
        return res

    def partitionLabels3(self, s: str) -> List[int]:
        right = {}
        for i,c in enumerate(s):
            right[c] = i
        # print(book)
        res = []
        i = 0
        while i < len(s):
            hi, j = right[s[i]], i+1
            while j < hi:
                if right[s[j]] > hi:
                    hi = right[s[j]]
                j += 1    
            res.append(hi-i+1)
            i = hi + 1  
        return res

    
    def partitionLabels2(self, s: str) -> List[int]:
        n, left, right = len(s), [-1]*26, [-1]*26
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            if left[idx] == -1:
                left[idx] = i
            right[idx] = i
        ivs = [] 
        for i in range(26):
            l, r = left[i], right[i]
            if l >= 0:
                k, valid = l, True
                while k < r:
                    idx = ord(s[k])-ord('a')
                    if left[idx] < l:
                        valid = False 
                        break
                    r = max(r, right[idx])
                    k += 1
                if valid:                    
                    ivs.append([l, r])
        ivs.sort(key = lambda x: x[0])
        i, merge = 0, []
        while i < len(ivs):
            merge.append(ivs[i])
            j = i+1
            while j < len(ivs) and ivs[j][0] <= ivs[i][1]:
                j += 1
            i = j    
        return [b-a+1 for a,b in merge]
        

        
if __name__ == "__main__":
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
    print(Solution().partitionLabels2("ababcbacadefegdehijhklij"))
    print(Solution().partitionLabels2("qiejxqfnqceocmy"))
    print(Solution().partitionLabels3("qiejxqfnqceocmy"))
    print(Solution().partitionLabels2("befrppytljbvezqkjzkvmncnc"))
    print(Solution().partitionLabels3("befrppytljbvezqkjzkvmncnc"))

        