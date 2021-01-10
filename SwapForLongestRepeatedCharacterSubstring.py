'''
-Medium-
*Sliding Window*

Given a string text, we are allowed to swap two of the characters in the string. 
Find the length of the longest substring with repeated characters.

 

Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with 
the first 'a'. Then, the longest repeated character substring is "aaa", which its 
length is 3.
Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest 
repeated character substring "aaaaaa", which its length is 6.
Example 3:

Input: text = "aaabbaaa"
Output: 4
Example 4:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", 
length is 5.
Example 5:

Input: text = "abcdef"
Output: 1
 

Constraints:

1 <= text.length <= 20000
text consist of lowercase English characters only.

'''
from collections import Counter
from collections import defaultdict
class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = Counter(text)
        n = len(text)
        m = defaultdict(int)
        left, right = 0, 0
        res = 0
        while right < n:            
            m[text[right]] += 1                        
            right += 1
            if len(m) == 1:
                res = max(res, list(m.values())[0])
            elif len(m) == 2:
                c1, c2 = list(m.keys())
                while m[c1] > 1 and m[c2] > 1:
                    m[text[left]] -= 1                        
                    left += 1                
                if m[c1] == 1 and count[c2]-m[c2]>=1:
                    res = max(res, m[c2]+1)
                elif m[c2] == 1 and count[c1]-m[c1]>=1:
                    res = max(res, m[c1]+1)
                #print(c1, c2, res)
            else:
                while len(m) > 2:
                    m[text[left]] -= 1
                    if m[text[left]] == 0:
                       m.pop(text[left])
                    left += 1
        return res
 
        
if __name__ == "__main__":
    print(Solution().maxRepOpt1("ababa"))
    print(Solution().maxRepOpt1("aaabaaa"))
    print(Solution().maxRepOpt1("aaabbaaa"))
    print(Solution().maxRepOpt1("abcdef"))
    print(Solution().maxRepOpt1("aaaaa"))
