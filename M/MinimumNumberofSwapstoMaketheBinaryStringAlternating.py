'''

-Medium-

Given a binary string s, return the minimum number of character swaps to 
make it alternating, or -1 if it is impossible.

The string is called alternating if no two adjacent characters are equal. 
For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Any two characters may be swapped, even if they are not adjacent.

 

Example 1:

Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
Example 3:

Input: s = "1110"
Output: -1
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.

'''

from collections import Counter

class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        cnt = Counter(s)
        def swaps(pos):
            swap = 0
            for i in range(n):
                c = '1' if i % 2 == pos else '0'
                swap += 1 if c != s[i] else 0
            return swap
        if n % 2 == 1:
            if abs(cnt['1'] - cnt['0']) != 1:
                return -1 
            if cnt['1'] > cnt['0']:
                return swaps(0)//2
            else:
                return swaps(1)//2
        else:
            if cnt['1'] != cnt['0']:
                return -1 
            return min(swaps(0)//2, swaps(1)//2)    


if __name__ == "__main__":
    print(Solution().minSwaps("111000"))    
    print(Solution().minSwaps("010"))    
    print(Solution().minSwaps("1110"))    