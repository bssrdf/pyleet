'''
-Medium-

Given a non negative integer number num. For every numbers i in the range 
0 ≤ i ≤ num calculate the number of 1's in their binary representation 
and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function 
like __builtin_popcount in c++ or in any other language.

'''

import math

class Solution(object):
    def countBitsDP(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0: return [0]                        
        res = [0,1]
        n = int(math.log2(num))
        for i in range(0, n-1):
            last = res[-2**i:]
            res.extend(last)
            res.extend([k+1 for k in last])                            
        if len(res) < num+1:
            last = res[-2**(n-1):]
            last += [k+1 for k in last]   
            res += last[:(num+1)-len(res)]
        return res

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            bits = bin(i)
            cnt = 0
            for b in bits[2:]:
                cnt += 1 if b == '1' else 0
            res.append(cnt)
        return res




if __name__ == "__main__":
    print(Solution().countBits(5))
    print(Solution().countBits(17))
    print(Solution().countBitsDP(17))