'''

-Medium-

Given three integers a, b, and n, return the maximum value of (a XOR x) * (b XOR x) where 0 <= x < 2n.

Since the answer may be too large, return it modulo 109 + 7.

Note that XOR is the bitwise XOR operation.

 

Example 1:

Input: a = 12, b = 5, n = 4
Output: 98
Explanation: For x = 2, (a XOR x) = 14 and (b XOR x) = 7. Hence, (a XOR x) * (b XOR x) = 98. 
It can be shown that 98 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2n.
Example 2:

Input: a = 6, b = 7 , n = 5
Output: 930
Explanation: For x = 25, (a XOR x) = 31 and (b XOR x) = 30. Hence, (a XOR x) * (b XOR x) = 930.
It can be shown that 930 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2n.
Example 3:

Input: a = 1, b = 6, n = 3
Output: 12
Explanation: For x = 5, (a XOR x) = 4 and (b XOR x) = 3. Hence, (a XOR x) * (b XOR x) = 12.
It can be shown that 12 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2n.
 

Constraints:

0 <= a, b < 2^50
0 <= n <= 50

'''


class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        A = format(a, '0'+str(n)+'b')
        A = A[::-1]
        B = format(b, '0'+str(n)+'b')
        B = B[::-1]
        if n == 0: return (a^0)*(b^0)
        # print(A, B)
        seen = False   
        def helper(i, x):
            nonlocal seen
            # if i < n:
            #     print(i, A[i], B[i])
            if i == n:
                # print(seen, x, int(x,2)) 
                return ((a^int(x, 2))*(b^int(x,2))) % MOD 
            if A[i] == '1' and B[i] == '0' or A[i] == '0' and B[i] == '1':
                # seen = True
                return max(helper(i+1, '1'+x),helper(i+1, '0'+x))
                
            elif A[i] == '1' and B[i] == '1':
                # seen = True
                return helper(i+1, '0'+x)
            else:
                # if not seen:
                return max(helper(i+1, '1'+x),helper(i+1, '0'+x))
                # else:
                #     return helper(i+1, x+'1')
        return helper(0, '')

    def maximumXorProduct2(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        for i in reversed(range(n)):
            mask = 1 << i
            if (a & mask) and (b & mask):
                continue
            elif (a & mask):
                if a > b:
                    a ^= mask
                    b |= mask
            elif (b & mask):
                if a < b:
                    a |= mask
                    b ^= mask
            else:
                a |= mask
                b |= mask
        a %= MOD
        b %= MOD
        return (a * b) % MOD     

                           

if __name__ == "__main__":
    # print(Solution().maximumXorProduct(a = 12, b = 5, n = 4))        
    # print(Solution().maximumXorProduct(a = 6, b = 7, n = 5))        
    # print(Solution().maximumXorProduct(a = 1, b = 6, n = 3))   
    # print(Solution().maximumXorProduct(a = 0, b = 4, n = 0))    
    # print(Solution().maximumXorProduct(a = 2, b = 8, n = 1))       
    print(Solution().maximumXorProduct2(a = 53449611838892, b = 712958946092406, n = 6))           