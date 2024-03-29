'''
-Hard-

*Union Find*

You are given an integer array nums, and you can perform the following operation any 
number of times on nums:

Swap the positions of two elements nums[i] and nums[j] if gcd(nums[i], nums[j]) > 1 
where gcd(nums[i], nums[j]) is the greatest common divisor of nums[i] and nums[j].
Return true if it is possible to sort nums in non-decreasing order using the 
above swap method, or false otherwise.

 

Example 1:

Input: nums = [7,21,3]
Output: true
Explanation: We can sort [7,21,3] by performing the following operations:
- Swap 7 and 21 because gcd(7,21) = 7. nums = [21,7,3]
- Swap 21 and 3 because gcd(21,3) = 3. nums = [3,7,21]
Example 2:

Input: nums = [5,2,6,2]
Output: false
Explanation: It is impossible to sort the array because 5 cannot be swapped with any other element.
Example 3:

Input: nums = [10,5,9,3,15]
Output: true
We can sort [10,5,9,3,15] by performing the following operations:
- Swap 10 and 15 because gcd(10,15) = 5. nums = [15,5,9,3,10]
- Swap 15 and 3 because gcd(15,3) = 3. nums = [3,5,9,15,10]
- Swap 10 and 15 because gcd(10,15) = 5. nums = [3,5,9,10,15]
 

Constraints:

1 <= nums.length <= 3 * 104
2 <= nums[i] <= 105


'''
from typing import List
from collections import defaultdict, Counter
import math

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u != self.parent.setdefault(u, u):
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv: self.parent[pu] = pv


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)
        graph = defaultdict(list)
        sortIndex = sorted([i for i,_ in enumerate(nums)], key=lambda x: nums[x])
        def sieve(n):
            A = [i for i in range(n+1)]
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
        def primes_set(m):
            for i in range(2, int(math.sqrt(m))+1):
                if m % i == 0:
                    return primes_set(m//i) | set([i])
            return set([m])
        roots = [i for i in range(n)]
        ranks = [0]*n
        def find(x):
            while x != roots[x]:
                roots[x] = roots[roots[x]]
                x = roots[x]
            return x
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                if ranks[fx] > ranks[fy]:
                    roots[fy] = fx
                else:
                    roots[fx] = fy
                    if ranks[fx] == ranks[fy]:
                        ranks[fy] += 1
        #L = set(sieve(10**5))
        for i in range(n):
            L = primes_set(nums[i])
            for j in L:
                graph[j].append(i)
        for k in graph:
            idx = graph[k]
            for i in range(len(idx)-1):
                union(idx[i], idx[i+1])
        for i in range(n):
            if find(i) != find(sortIndex[i]):
                return False
        # cnt = defaultdict(list)
        # for i in range(n):
        #     cnt[find(i)].append(i)        
        # for r in cnt:
        #     match = set()
        #     for j in cnt[r]:
        #         match.add(sortIndex[j])
        #     if match != set(cnt[r]):
        #         return False
        return True

    def gcdSort(self, nums: List[int]) -> bool:
        def sieve(n):  # O(N*log(logN)) ~ O(N)
            spf = [i for i in range(n)]
            for i in range(2, n):
                if spf[i] != i: continue  # Skip if it's a not prime number
                for j in range(i * i, n, i):
                    if spf[j] > i:  # update to the smallest prime factor of j
                        spf[j] = i
            return spf

        def getPrimeFactors(num, spf):  # O(logNum)
            while num > 1:
                yield spf[num]
                num //= spf[num]

        spf = sieve(max(nums) + 1)
        uf = UnionFind()
        for x in nums:
            for f in getPrimeFactors(x, spf):
                uf.union(x, f)

        for x, y in zip(nums, sorted(nums)):
            if uf.find(x) != uf.find(y):
                return False

        return True






if __name__ == "__main__":
    # print(Solution().gcdSort([7,21,3]))
    # print(Solution().gcdSort([5,2,6,2]))
    # print(Solution().gcdSort([10,5,9,3,15]))
    print(Solution().gcdSort([8,9,4,2,3]))