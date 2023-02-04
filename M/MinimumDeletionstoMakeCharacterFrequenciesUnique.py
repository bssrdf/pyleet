'''
-Medium-

A string s is called good if there are no two different characters in s that have the same 
frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. 
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end 
(i.e. frequency of 0 is ignored).
 

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.

'''
from sortedcontainers import SortedSet
from collections import Counter
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = Counter(s)

        s = SortedSet([_ for _ in range(1, max(cnt.values())+1)], key= lambda x: -x)
        s -= SortedSet(list(cnt.values()))        
        res = 0
        cnts = sorted(cnt.values(), reverse=True)
        f = -1
       # print(cnts,s )
        for i in range(len(cnts)):
            while s and s[0] >= cnts[i]:
                s.pop(0) 
            if cnts[i] == f:
                if s:
                    res += (cnts[i]-s[0])
                    s.pop(0)
                else:
                    res += cnts[i]
            f = cnts[i]
        return res
    def minDeletions2(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = Counter(s)
        s = SortedSet([_ for _ in range(1, max(cnt.values())+1)], key= lambda x: -x)
        s -= SortedSet(list(cnt.values()))        
        res = 0
        cnts = Counter(cnt.values())
        for i in sorted(cnts.keys(), reverse=True):
            if cnts[i] > 1:
                k = cnts[i]
                while s and s[0] >= i:
                   s.pop(0) 
                while s and k > 1:
                    res += i-s[0]
                    s.pop(0)
                    k -= 1
                if k > 1:
                    while k > 1:
                        res += i
                        k -= 1
        return res            

    def minDeletionsFaster(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = Counter(s)
        cnts = set()
        res = 0
        for k in sorted(cnt.values(), reverse=True):
            i = k
            while i in cnts:
                i -= 1  
            res += (k-i) if i >= 0 else k
            cnts.add(i)
        return res 

    def minDeletionsFastest(self, s):
        """
        :type s: str
        :rtype: int
        """           
        cnt, res, used = Counter(s), 0, set()
        for ch, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res

    def minDeletions3(self, s: str) -> int:
        prev, keep = float('inf'), 0
        for freq in sorted(Counter(s).values(), reverse=True):
            freq = min(prev - 1, freq)
            if freq == 0:
                break
            keep += freq
            prev = freq
        return len(s) - keep

                    
         
if __name__ == "__main__":
    #print(Solution().minDeletions(s = "aaabbbcc"))
    #print(Solution().minDeletions(s = "ceabaacb"))
    #print(Solution().minDeletions(s = "aab"))
    #print(Solution().minDeletions(s = "accdcdadddbaadbc"))
    #print(Solution().minDeletionsFaster(s = "accdcdadddbaadbc"))
    print(Solution().minDeletions(s = "bbcebab"))
    print(Solution().minDeletionsFaster(s = "bbcebab"))