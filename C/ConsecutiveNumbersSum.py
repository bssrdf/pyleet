'''
-Hard-

Given an integer n, return the number of ways you can write n as the sum of 
consecutive positive integers.

 

Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 2 + 3
Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
 

Constraints:

1 <= n <= 10^9


'''
import math
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 1 # the N itself is also counted as one way
        for k in range(2, int(math.sqrt(2*n))+1):
            if (n - k*(k-1)//2) % k == 0:
                count += 1
        return count 


if __name__ == "__main__":
    print(Solution().consecutiveNumbersSum(15))
        
