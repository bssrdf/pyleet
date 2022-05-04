'''
-Medium-

You are given a 0-indexed string text and another 0-indexed string pattern of length 2, both of which consist of only lowercase English letters.

You can add either pattern[0] or pattern[1] anywhere in text exactly once. Note that the character can be added even at the beginning or at the end of text.

Return the maximum number of times pattern can occur as a subsequence of the modified text.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

Example 1:

Input: text = "abdcdbc", pattern = "ac"
Output: 4
Explanation:
If we add pattern[0] = 'a' in between text[1] and text[2], we get "abadcdbc". Now, the number of times "ac" occurs as a subsequence is 4.
Some other strings which have 4 subsequences "ac" after adding a character to text are "aabdcdbc" and "abdacdbc".
However, strings such as "abdcadbc", "abdccdbc", and "abdcdbcc", although obtainable, have only 3 subsequences "ac" and are thus suboptimal.
It can be shown that it is not possible to get more than 4 subsequences "ac" by adding only one character.
Example 2:

Input: text = "aabb", pattern = "ab"
Output: 6
Explanation:
Some of the strings which can be obtained from text and have 6 subsequences "ab" are "aaabb", "aaabb", and "aabbb".
 

Constraints:

1 <= text.length <= 105
pattern.length == 2
text and pattern consist only of lowercase English letters.

'''


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        (t1, t2), n = pattern, len(text)
        c1, c2 = [0]*n, [0]*(n+1)
        cnt = 0
        for i in range(n-1,-1, -1):
            if text[i] == t2: cnt += 1            
            c2[i] = cnt            
        cnt = 0            
        for i in range(n):
            if text[i] == t1: cnt += 1
            c1[i] = cnt  
        cnt = 0
        for i in range(n):
            cnt += c2[i+1] if text[i] == t1 else 0
        ans = 0
        for i in range(n):
            ans = max(ans, c2[i], c1[i])
        # print(c1, c2, ans, cnt)
        return ans + cnt
    
    def maximumSubsequenceCount2(self, text: str, pattern: str) -> int:
        t1, t2 = pattern
        def count(s):
            c2 = [0]*(len(s)+1)
            cnt = 0
            for i in range(len(s)-1,-1, -1):
                if s[i] == t2: cnt += 1            
                c2[i] = cnt  
            cnt = 0
            for i in range(len(s)):
                if s[i] == t1: cnt += c2[i+1]
            return cnt
        if t1 != t2:
            return count(text) + max(text.count(t1), text.count(t2))
        else:
            count = text.count(t1) + 1
            return count * (count - 1) >> 1

    
    def maximumSubsequenceCount3(self, text: str, pattern: str) -> int:
        x, y = pattern
        if x != y:
            cur = 0
            ycount = text.count(y)
            for c in text:
                if c == x:
                    cur += ycount
                if c == y:
                    ycount -= 1

            return cur + max(text.count(x), text.count(y))
        
        else:
            count = text.count(x) + 1
            return count * (count - 1) >> 1
            





if __name__ == "__main__":
    print(Solution().maximumSubsequenceCount(text = "abdcdbc", pattern = "ac"))        
    print(Solution().maximumSubsequenceCount(text = "aabb", pattern = "ab"))
    print(Solution().maximumSubsequenceCount(text = "zigfj", pattern = "ju"))
    print(Solution().maximumSubsequenceCount("fwymvreuftzgrcrxczjacqovduqaiig", "yy"))
    print(Solution().maximumSubsequenceCount("k", "jk"))
    print(Solution().maximumSubsequenceCount2(text = "abdcdbc", pattern = "ac"))        
    print(Solution().maximumSubsequenceCount2(text = "aabb", pattern = "ab"))
    print(Solution().maximumSubsequenceCount2(text = "zigfj", pattern = "ju"))
    print(Solution().maximumSubsequenceCount2("fwymvreuftzgrcrxczjacqovduqaiig", "yy"))
    print(Solution().maximumSubsequenceCount2("k", "jk"))