'''
-Hard-


Return the number of distinct non-empty substrings of text that can be written as 
the concatenation of some string with itself (i.e. it can be written as a + a where 
a is some string).

 

Example 1:

Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
Example 2:

Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
 

Constraints:

1 <= text.length <= 2000
text has only lowercase English letters.

'''

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        d, q = 29, 10**9+7
        h, p = [0]*(n+1), [0]*(n+1)
        p[0] = 1
        s = set()
        for i in range(1,n+1):
            h[i] = (h[i-1]*d+ord(text[i-1]))%q
            p[i] = (p[i-1]*d)%q
        for i in range(n):
            for l in range(2, n-i+1, 2):
                mid = i + l // 2
                h1 = (h[mid] - (h[i]*p[mid-i])%q + q)%q 
                h2 = (h[i+l] - (h[mid]*p[i+l-mid])%q + q)%q 
                if h1 == h2: s.add(h1)
        return len(s)

        

    
if __name__ == "__main__":
    print(Solution().distinctEchoSubstrings("abcabcabc"))