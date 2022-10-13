'''
-Medium-

*Greedy*

You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:

Operation 1: If the number contains the substring "00", you can replace it with "10".
For example, "00010" -> "10010"
Operation 2: If the number contains the substring "10", you can replace it with "01".
For example, "00010" -> "00001"
Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.

 

Example 1:

Input: binary = "000110"
Output: "111011"
Explanation: A valid transformation sequence can be:
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"
Example 2:

Input: binary = "01"
Output: "01"
Explanation: "01" cannot be transformed any further.
 

Constraints:

1 <= binary.length <= 105
binary consist of '0' and '1'.

'''
from collections import Counter

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        s = binary
        i, n = 0, len(s)
        while i < n and s[i] == '1':
            i += 1
        cnt = Counter(s[i:])
        return '1'*i + '1'*(cnt['0']-1)+ ('0' if cnt['0'] > 0 else '') +'1'*cnt['1']
        

    
if __name__ == "__main__":
    print(Solution().maximumBinaryString("1100"))