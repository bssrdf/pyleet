'''

-Medium-

Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

 

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
Example 2:

Input: num = 123
Output: [5,25]
Example 3:

Input: num = 999
Output: [40,25]
 

Constraints:

1 <= num <= 10^9

'''

from typing import List
from math import sqrt
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        ans = []
        diff = float('inf')
        k = num + 1
        for i in range(1, int(sqrt(k))+1):
            if k % i == 0:
                d = abs(i - k//i)    
                if diff > d:
                    diff = d
                    ans = [i, k//i]
        k = num + 2
        for i in range(1, int(sqrt(k))+1):
            if k % i == 0:
                d = abs(i - k//i)    
                if diff > d:
                    diff = d
                    ans = [i, k//i]
        return ans 


if __name__ == '__main__':   
    print(Solution().closestDivisors(8))
       
    print(Solution().closestDivisors(123))
    print(Solution().closestDivisors(999))