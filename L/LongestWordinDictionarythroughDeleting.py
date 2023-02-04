'''
-Medium-

Given a string and a string dictionary, find the longest string in the 
dictionary that can be formed by deleting some characters of the given string. 
If there are more than one possible results, return the longest word with 
the smallest lexicographical order. If there is no possible result, return 
the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.


'''

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def match(s1, s2):
            if len(s2) > len(s1): return False
            l1, l2 = 0, 0
            r1, r2 = len(s1)-1, len(s2)-1
            while l1 <= r1:
                if s1[l1] == s2[l2]:
                    l2 += 1
                    if l2 > r2: return True
                l1 += 1
                if s1[r1] == s2[r2]:
                    r2 -= 1
                    if l2 > r2: return True
                r1 -= 1
            return False
        d.sort(key=lambda x: (-len(x),x))
        for t in d:
            if match(s, t): return t
        return ""

        
if __name__ == "__main__":
    print(Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))
    #Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"])