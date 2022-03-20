'''

-Medium-


Given a string s, find two disjoint palindromic subsequences of s such that the 
product of their lengths is maximized. The two subsequences are disjoint if 
they do not both pick a character at the same index.

Return the maximum possible product of the lengths of the two palindromic subsequences.

A subsequence is a string that can be derived from another string by deleting 
some or no characters without changing the order of the remaining characters. 
A string is palindromic if it reads the same forward and backward.

 

Example 1:

example-1
Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.
Example 2:

Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.
Example 3:

Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.
 

Constraints:

2 <= s.length <= 12
s consists of lowercase English letters only.


'''

from typing import List

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        def isPalin(s):
            if not s: return False
            return s == s[::-1]
        palins = {}
        for mask1 in range(1<<n):
            s1 = []
            for i in range(n):
                if mask1 & (1<<i) > 0:                 
                    s1.append(s[i])  
            if isPalin(''.join(s1)):              
                palins[mask1] = bin(mask1).count('1')
        ans = 1 
        for mask1 in palins:            
            for mask2 in palins:
                if mask2 & mask1 == 0:
                    ans = max(ans, palins[mask1]*palins[mask2])
        return ans



        

if __name__ == "__main__":
    print(Solution().maxProduct("leetcodecom"))
    print(Solution().maxProduct("accbcaxxcxx"))
    print(Solution().maxProduct("fnkkfnkfkffk"))
    print(Solution().maxProduct("vfffvfvfvfvf"))
        