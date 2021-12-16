'''
-Hard-
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. 
Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, a = 2, b = 3
Output: 2
Example 2:

Input: n = 4, a = 2, b = 3
Output: 6
Example 3:

Input: n = 5, a = 2, b = 4
Output: 10
Example 4:

Input: n = 3, a = 6, b = 4
Output: 8
 

Constraints:

1 <= n <= 10^9
2 <= a, b <= 4 * 10^4


'''
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(a, b):
            return a if b == 0  else gcd(b, a % b)
    
        lcm = a * b // gcd(a, b); left = 2; right = 10**14; M = 10**9 + 7
        while left < right:
            mid = left + (right - left) // 2
            if mid // a + mid // b - mid // lcm < n: left = mid + 1
            else: right = mid
        return right % M
        

if __name__ == "__main__":
    print(Solution().nthMagicalNumber(n = 3, a = 6, b = 4))
