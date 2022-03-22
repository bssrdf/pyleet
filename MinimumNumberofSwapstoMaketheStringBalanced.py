'''

-Medium-
*Greedy*
*Stack*

ou are given a 0-indexed string s of even length n. The string consists of 
exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

 

Example 1:

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".
Example 2:

Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".
Example 3:

Input: s = "[]"
Output: 0
Explanation: The string is already balanced.
 

Constraints:

n == s.length
2 <= n <= 106
n is even.
s[i] is either '[' or ']'.
The number of opening brackets '[' equals n / 2, 
and the number of closing brackets ']' equals n / 2.

'''


class Solution:

    def minSwaps(self, s: str) -> int:
        res, bal = 0, 0
        for ch in s:
            bal += 1 if ch == '[' else -1
            if bal == -1:
                res += 1
                bal = 1
        return res
    
    def minSwaps2(self, s: str) -> int:        
        bal, r = 0, len(s)-1        
        i, ans = 0, 0
        while i < r:
            if s[i] == '[': bal += 1
            else: bal -= 1
            if bal < 0:
                while i < r and s[r] != '[':
                    r -= 1  
                ans += 1
                bal = 1
            i += 1
        return ans

   

    
                       
if __name__ == "__main__":
    print(Solution().minSwaps("][]["))
    print(Solution().minSwaps("]]][[["))
    print(Solution().minSwaps2("][]["))
    print(Solution().minSwaps2("]]][[["))
