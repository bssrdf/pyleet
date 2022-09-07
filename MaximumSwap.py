'''

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108



'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        ss = sorted(s, reverse=True)
        i = 0
        for i in range(len(s)):
            if ss[i] != s[i]:
                break
        if i == len(s): return num
        idx = i
        a, b = -1, -1
        for i in range(len(s)):
            if s[i] == ss[idx]:
                a = i
            if s[i] == s[idx] and b == -1:
                b = i
        s[a], s[b] = s[b], s[a]
        return int(''.join(s))