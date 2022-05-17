'''
-Medium-
*Greedy*
*Two Pointers*


You are given two strings word1 and word2. You want to construct a string merge in the following way: while either word1 or word2 are non-empty, choose one of the following options:

If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
For example, if word1 = "abc" and merge = "dv", then after choosing this operation, word1 = "bc" and merge = "dva".
If word2 is non-empty, append the first character in word2 to merge and delete it from word2.
For example, if word2 = "abc" and merge = "", then after choosing this operation, word2 = "bc" and merge = "a".
Return the lexicographically largest merge you can construct.

A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b. For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.

 

Example 1:

Input: word1 = "cabaa", word2 = "bcaaa"
Output: "cbcabaaaaa"
Explanation: One way to get the lexicographically largest merge is:
- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
- Append the remaining 5 a's from word1 and word2 at the end of merge.
Example 2:

Input: word1 = "abcabc", word2 = "abdcaba"
Output: "abdcabcabcaba"
 

Constraints:

1 <= word1.length, word2.length <= 3000
word1 and word2 consist only of lowercase English letters.



'''


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i, j = 0, 0
        ans = ''
        while i < n and j < m:
            if word1[i] < word2[j]:
                ans += word2[j]
                j += 1
            elif word1[i] > word2[j]: 
                ans += word1[i]
                i += 1
            else:
                i1, j1 = i, j
                while i1 < n and j1 < m and word1[i1] == word2[j1]:
                    i1 += 1
                    j1 += 1
                if i1 < n and j1 < m:
                    if word1[i1] > word2[j1]: 
                        ans += word1[i]
                        i += 1
                    else:
                        ans += word2[j]
                        j += 1
                elif i1 < n:
                    ans += word1[i]
                    i += 1
                else:
                    ans += word2[j]
                    j += 1
        while i < n:
            ans += word1[i]
            i += 1
        while j < m:
            ans += word2[j]
            j += 1
        return ans 
    
    def largestMerge2(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i, j = 0, 0
        ans = []
        while i < n and j < m:
            if word1[i] < word2[j]:
                ans.append(word2[j])
                j += 1
            elif word1[i] > word2[j]: 
                ans.append(word1[i])
                i += 1
            else:
                i1, j1 = i, j
                while i1 < n and j1 < m and word1[i1] == word2[j1]:
                    i1 += 1
                    j1 += 1
                if i1 < n and j1 < m:
                    if word1[i1] > word2[j1]: 
                        ans.append(word1[i])
                        i += 1
                    else:
                        ans.append(word2[j])
                        j += 1
                elif i1 < n:
                    ans.append(word1[i])
                    i += 1
                else:
                    ans.append(word2[j])
                    j += 1
        while i < n:
            ans.append(word1[i])
            i += 1
        while j < m:
            ans.append(word2[j])
            j += 1
        return ''.join(ans)
    
    def largestMerge3(self, word1: str, word2: str) -> str:
        ans = ''
        while word1 and word2:
            if word1>word2:
                ans += word1[0]
                word1 = word1[1:]
            else:
                ans += word2[0]
                word2 = word2[1:]
        ans += word1
        ans += word2
        return ans
        


if __name__ == "__main__":
    print(Solution().largestMerge(word1 = "cabaa", word2 = "bcaaa"))        
    print(Solution().largestMerge(word1 = "abcabc", word2 = "abdcaba"))        