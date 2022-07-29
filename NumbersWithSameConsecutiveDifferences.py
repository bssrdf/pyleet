'''

-Medium-

Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

 

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Constraints:

2 <= n <= 9
0 <= k <= 9


'''

from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        tmp = list('123456789')
        for i in range(1,n):
            tmp1 = []
            for t in tmp:
                for j in range(10):
                    if abs(j-int(t[-1])) == k:
                        tmp1.append(t+str(j))
            tmp = tmp1
        return [int(x) for x in tmp]         

if __name__ == "__main__":
    print(Solution().numsSameConsecDiff(n = 3, k = 7))
    print(Solution().numsSameConsecDiff(n = 2, k = 1))
        