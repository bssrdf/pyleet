'''

-Medium-


Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= nums1 < nums2 <= right .
nums1 and nums2 are both prime numbers.
nums2 - nums1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [nums1, nums2]. If there are multiple pairs satisfying these conditions, return the one with the minimum nums1 value or [-1, -1] if such numbers do not exist.

A number greater than 1 is called prime if it is only divisible by 1 and itself.

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Constraints:

1 <= left <= right <= 106


'''

from typing import List
import math
import bisect

def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for divisor in range(2, math.floor(math.sqrt(num)) + 1):
        if num % divisor == 0:
            return False
    return True

def sieve(n):
    A = [i for i in range(n+1)]
    A[1] = 0
    for p in range(2, math.floor(math.sqrt(n))+1):
        if A[p]:
            j = p*p
            while j <= n:
                A[j] = 0
                j += p
    L = []
    for p in range(2, n+1):
        if A[p]:
            L.append(A[p])
    return L

primes = sieve(1000000)  

class Solution:


    def closestPrimes(self, left: int, right: int) -> List[int]:
        # TLE
        # need to precompute all primes in range[left, right]
        # to avoid TLE
        def sieve(n, m):
            A = [i for i in range(n+1)]
            for p in range(2, math.floor(math.sqrt(n))+1):
                if A[p]:
                    j = p*p
                    while j <= n:
                        A[j] = 0
                        j += p
            # print('A', A)
            L = []
            for p in range(max(2,m), n+1):
                if A[p]:
                    L.append(A[p])
            return L
        
        primes = sieve(right, left)
        # print(len(primes))
        # print(primes)
        mx = right - left + 1
        ans = [-1, -1]
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i-1]            
            if diff < mx:
                mx = diff
                ans = [primes[i-1], primes[i]]
            if diff < 3:
                break
        return ans
    

    def closestPrimes2(self, left: int, right: int) -> List[int]:
        #TLE
        def sieve(n, m):
            mx = right - left + 1
            A = [i for i in range(n+1)]
            A[1] = 0
            for p in range(2, math.floor(math.sqrt(n))+1):
                if A[p]:
                    for j in range(p*p, n+1, p):  
                        A[j] = 0
            L = [-1, -1]
            start = 0
            for p in range(m, n+1):
                if A[p]: 
                    if start and A[p]-start < mx:
                       mx = A[p]-start
                       L = [start, A[p]]
                    start = A[p]
            return L
        
        return sieve(right, left)
    
    def closestPrimes3(self, left: int, right: int) -> list[int]:
        primes = []
        for candidate in range(left, right + 1):
            if is_prime(candidate):
                if primes and candidate <= primes[-1] + 2:
                    return [primes[-1], candidate]  # twin or [2, 3]
                primes.append(candidate)
        
        gaps = ([primes[i - 1], primes[i]]
                for i in range(1, len(primes)))

        return min(gaps,
                   key=lambda gap: (gap[1] - gap[0], gap[0]),
                   default=[-1, -1])
    

    def closestPrimes4(self, left: int, right: int) -> List[int]:

        i = bisect.bisect_left(primes, left)
        n1, n2 = -1, -1 
        while i + 1 < len(primes) and primes[i+1] <= right:
            if n1 == -1 or primes[i+1] - primes[i] < n2 - n1:
                n1, n2 = primes[i], primes[i+1]
                if n2 - n1 < 3:
                    break
            i += 1
        return [n1, n2]





if __name__ == "__main__":
    # print(Solution().closestPrimes(left = 10, right = 19))
    # print(Solution().closestPrimes(left = 4, right = 6))
    # print(Solution().closestPrimes(left = 84084, right = 407043))
    # print(Solution().closestPrimes(left = 1, right = 1000000))
    print(Solution().closestPrimes(left = 710119, right = 710189))
    print(Solution().closestPrimes2(left = 710119, right = 710189))
    print(Solution().closestPrimes4(left = 710119, right = 710189))
    print(Solution().closestPrimes(left = 313, right = 742467))
    print(Solution().closestPrimes2(left = 313, right = 742467))
    print(Solution().closestPrimes4(left = 313, right = 742467))





