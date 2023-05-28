'''

-Hard-
*Union Find*
*Hash Table*
*Prime Factors*


You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

 

Example 1:

Input: nums = [2,3,6]
Output: true
Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
Example 2:

Input: nums = [3,9,5]
Output: false
Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
Example 3:

Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105

'''
from typing import List
from math import gcd
import math 
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # wrong
        n = len(nums)
        fa = [-1]*n
        g = [-1]*n
        conn = set()
        def find(x):
            while x != fa[x]:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x
        def union(x, y, gx, gy):
            fx, fy = find(x), find(y)
            if fx != fy:
                fa[fx] = fy
                g[fy] = min(gx, gy)
        for i in range(n):
            fa[i] = i             
            g[i] = nums[i]
            newconn = set()
            for j in conn:
                if gcd(g[i], g[j]) > 1:
                    # conn.remove(j)
                    union(i, j, g[i], g[j])
                else:
                    newconn.add(j)
            newconn.add(i)
            conn = newconn
            print(i, nums[i],fa, conn, g)
        st = set()    
        print(fa)
        for i in range(n):
            st.add(find(i))
        return len(st) == 1

    def canTraverseAllPairs2(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        fa = [i for i in range(n)]
        g = [1]*n
        def find(x):
            while x != fa[x]:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx == fy: return
            if g[fx] > g[fy]:
                fa[fy] = fx
                g[fx] += g[fy]
            else:
                fa[fx] = fy
                g[fy] += g[fx]
            
        conn = {}     
        for i in range(n):
            x = nums[i]             
            if x == 1 : return False
            d = 2
            while d * d <= x:
                if x % d == 0: 
                    if d in conn:
                        union(i, conn[d])
                    else:
                        conn[d] = i
                    while x % d == 0:
                        x //= d                  
                d += 1
            if x > 1:
                if x in conn:
                    union(i, conn[x])
                else:
                    conn[x] = i
        return g[find(0)] == n            
    

    def canTraverseAllPairs3(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        
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
        
        primes = sieve(int(math.sqrt(10**5))+1) 

        fa = [i for i in range(n)]
        g = [1]*n
        def find(x):
            while x != fa[x]:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx == fy: return
            if g[fx] > g[fy]:
                fa[fy] = fx
                g[fx] += g[fy]
            else:
                fa[fx] = fy
                g[fy] += g[fx]
            
        conn = {} # map of a prime to an index   
        for i in range(n):
            x = nums[i]             
            if x == 1 : return False
            for p in primes:            
                if x % p == 0: 
                    if p in conn:
                        union(i, conn[p])
                    else:
                        conn[p] = i
                    while x % p == 0:
                        x //= p                  
            if x > 1: # x is a big prime
                if x in conn:
                    union(i, conn[x])
                else:
                    conn[x] = i
        return g[find(0)] == n            
        

            
            



        

if __name__ == "__main__":
    # print(Solution().canTraverseAllPairs(nums = [2,3,6]))
    # print(Solution().canTraverseAllPairs(nums = [3,9,5]))
    # print(Solution().canTraverseAllPairs(nums = [4,3,12,8]))
    print(Solution().canTraverseAllPairs(nums = [40,22,15]))
    print(Solution().canTraverseAllPairs2(nums = [40,22,15]))