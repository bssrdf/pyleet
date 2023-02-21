'''

-Medium-
*DP*
*Bitmask*


You are given a positive integer 0-indexed array nums.

A subset of the array nums is square-free if the product of its elements is a square-free integer.

A square-free integer is an integer that is divisible by no square number other than 1.

Return the number of square-free non-empty subsets of the array nums. Since the answer may be too large, return it modulo 109 + 7.

A non-empty subset of nums is an array that can be obtained by deleting some (possibly none but not all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [3,4,4,5]
Output: 3
Explanation: There are 3 square-free subsets in this example:
- The subset consisting of the 0th element [3]. The product of its elements is 3, which is a square-free integer.
- The subset consisting of the 3rd element [5]. The product of its elements is 5, which is a square-free integer.
- The subset consisting of 0th and 3rd elements [3,5]. The product of its elements is 15, which is a square-free integer.
It can be proven that there are no more than 3 square-free subsets in the given array.
Example 2:

Input: nums = [1]
Output: 1
Explanation: There is 1 square-free subset in this example:
- The subset consisting of the 0th element [1]. The product of its elements is 1, which is a square-free integer.
It can be proven that there is no more than 1 square-free subset in the given array.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 30


'''

from typing import List, Counter
from functools import lru_cache
import sys
sys.setrecursionlimit(3000)
import math
def primes_set(m):
    for i in range(2, int(math.sqrt(m))+1):
        if m % i == 0:
            return primes_set(m//i) | set([i])
    return set([m])

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        # print(nums)
        ans, MOD = 0, 10**9+7
        n = len(nums)
        sqs = {4, 8, 9, 12, 16, 20, 24, 28, 18, 27, 25}
        masks = [0]*31
        for i in range(1,31):
            st = primes_set(i)
            for k in st:
                masks[i] |= 1 << (k-1)
            # print(i, st, f'{masks[i]:030b}') 
        masks[1] = 0    
        @lru_cache(None)
        def dfs(i, bmask, amask):
            # if (i == 4 or i == 1) and bmask == 0:
            # if bmask == masks[6]:    
                # print('got 6', i)
            # nonlocal ans
            if i == n:
                # tmp = []
                # for j in range(1,31):
                #     if (1<<j) & amask > 0:
                #         tmp.append(j)
                # print(f'{amask:030b}', tmp)
                # ans += 1
                return 1
            
            ret = dfs(i+1, bmask, amask)
            # if nums[i] in sqs or ((1 << nums[i]) & bmask) > 0:
            #     dfs(i+1, bmask)
            if nums[i] not in sqs and  (masks[nums[i]] & bmask) == 0:
            # if masks[nums[i]] & bmask == 0:
                ret += dfs(i+1, bmask | masks[nums[i]], amask | (1 << nums[i]))
            return ret    
        return dfs(0, 0, 0) % MOD - 1
        return ans % (MOD) - 1
    
    def squareFreeSubsets2(self, nums: List[int]) -> int:
        #TLE
        MOD = 10**9+7
        n = len(nums)
        sqs = {4, 8, 9, 12, 16, 20, 24, 28, 18, 27, 25}
        masks = [0]*31
        for i in range(1,31):
            st = primes_set(i)
            for k in st:
                masks[i] |= 1 << (k-1)
            # print(i, st, f'{masks[i]:030b}') 
        masks[1] = 0    
        @lru_cache(None)
        def dfs(i, bmask):
            # if (i == 4 or i == 1) and bmask == 0:
            # if bmask == masks[6]:    
                # print('got 6', i)
            # nonlocal ans
            if i == n:
                # tmp = []
                # for j in range(1,31):
                #     if (1<<j) & amask > 0:
                #         tmp.append(j)
                # print(f'{amask:030b}', tmp)
                # ans += 1
                return 1
            
            ret = dfs(i+1, bmask)
            # if nums[i] in sqs or ((1 << nums[i]) & bmask) > 0:
            #     dfs(i+1, bmask)
            if nums[i] not in sqs and  (masks[nums[i]] & bmask) == 0:
            # if masks[nums[i]] & bmask == 0:
                ret += dfs(i+1, bmask | masks[nums[i]])
            return ret    
        return dfs(0, 0) % MOD - 1
    
    def squareFreeSubsets3(self, nums: List[int]) -> int:
        # TLE
        MOD = 10**9+7
        sqs = {4, 8, 9, 12, 16, 20, 24, 28, 18, 27, 25}
        A = [i for i in nums if i not in sqs]
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mp = {p:i for i,p in enumerate(primes)}
        n = len(A)
        # print('n=', n)
        masks = [0]*31
        for i in range(2,31):
            # st = primes_set(i)
            st = set()
            for k in mp:
                if i % k == 0:
                    st.add(k)
                    masks[i] |= 1 << (mp[k]) 
            # print(i, st, f'{masks[i]:010b}') 
        # masks[1] = 0    
        @lru_cache(None)
        def dfs(i, bmask):
            if i == n: return 1
            ret = dfs(i+1, bmask)
            if (masks[A[i]] & bmask) == 0:
                ret += dfs(i+1, bmask | masks[A[i]])
            return ret % MOD    
        return dfs(0, 0) - 1    
    
    def squareFreeSubsets6(self, nums: List[int]) -> int:
        # AC
        # almost the same as squareFreeSubsets3 but managing cache
        # manually, instead of relying on built-in lru_cache
        MOD = 10**9+7
        sqs = {4, 8, 9, 12, 16, 20, 24, 28, 18, 27, 25}
        A = [i for i in nums if i not in sqs]
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mp = {p:i for i,p in enumerate(primes)}
        n = len(A)
        # Added
        self.dp = [[-1 for _ in range(1024)] for _ in range(n)]
        masks = [0]*31
        for i in range(2,31):
            st = set()
            for k in mp:
                if i % k == 0:
                    st.add(k)
                    masks[i] |= 1 << (mp[k]) 
        def dfs(i, bmask):
            if i == n: return 1
            # Added
            if self.dp[i][bmask] != -1: return self.dp[i][bmask]
            ret = dfs(i+1, bmask)
            if (masks[A[i]] & bmask) == 0:
                ret += dfs(i+1, bmask | masks[A[i]])
            # Added
            self.dp[i][bmask] = ret
            return ret
        return (dfs(0, 0) - 1) % MOD   
    
    def squareFreeSubsets4(self, nums: List[int]) -> int:
        MOD = 10**9+7
        sqs = {4, 8, 9, 12, 16, 20, 24, 28, 18, 27, 25}
        A = [i for i in nums if i not in sqs]
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mp = {p:i for i,p in enumerate(primes)}
        n = len(A)
        masks = [0]*31
        for i in range(2,31):
            for k in mp:
                if i % k == 0:
                    masks[i] |= 1 << (mp[k]) 
        dp = [0]*(1<<10)
        dp[0] = 1
        for i in range(n):
            for j in range(1<<10):
                if j & masks[A[i]] == 0:
                    dp[j | masks[A[i]]] += dp[j]
        return sum(dp)%MOD - 1
    
    def squareFreeSubsets5(self, nums: List[int]) -> int:
        # 
        MOD = 10**9+7
        sqs = {4, 8, 9, 12, 16, 20, 24, 28, 18, 27, 25}
        A = Counter([i for i in nums if i not in sqs])
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mp = {p:i for i,p in enumerate(primes)}
        B = [(k,v) for k,v in A.items()]
        n = len(B)
        # print('n=', n)
        masks = [0]*31
        for i in range(2,31):
            for k in mp:
                if i % k == 0:
                    masks[i] |= 1 << (mp[k]) 
        # masks[1] = 0    
        @lru_cache(None)
        def dfs(i, bmask):
            if i == n: return 1
            # ret = B[i][1] * dfs(i+1, bmask)
            ret = dfs(i+1, bmask)
            if (masks[B[i][0]] & bmask) == 0:
                if B[i][0] == 1:
                    '''
                    Edge case is when 1 is present.

                    For example, [3, 5]. The square-free subsets are {[], [3], [5], [3, 5]}. 
                    We need to remove the empty subset [], but we keep it here for now.

                    When we add one 1. The nubmer of square-free sbusets are original solutions 
                    doubles, because we must add add one 1 to each of original subsets, 
                    such as {[], [3], [5], [3, 5], [1], [1, 3], [1, 5], [1, 3, 5]}, therefore, 
                    the count doubled when including empty subset [].

                    When we add two 1s. The number of square-free subsets doubles again. 
                    The solution becomes: {[], [3], [5], [3, 5], [1], [1, 3], [1, 5], [1, 3, 5], 
                    [1], [1, 3], [1, 5], [1, 3, 5], [1,1], [1, 1, 3], [1, 1, 5], [1, 1, 3, 5]}. 
                    Notice that what the solution require are subsets, but not unique subsets, 
                    so that there are some duplicated subsets.
                    '''
                    ret += (2**B[i][1]-1) * dfs(i+1, bmask | masks[B[i][0]])
                else:
                    ret += B[i][1] * dfs(i+1, bmask | masks[B[i][0]])    
            return ret % MOD    
        return dfs(0, 0) - 1    
        


if __name__ == '__main__':
    # print(Solution().squareFreeSubsets(nums = [3,4,4,5]))

    # print(Solution().squareFreeSubsets(nums = [1]))
    print(Solution().squareFreeSubsets3(nums = [11,2,19,7,9,27]))
    print(Solution().squareFreeSubsets4(nums = [11,2,19,7,9,27]))
    print(Solution().squareFreeSubsets5(nums = [11,2,19,7,9,27]))
    # print(Solution().squareFreeSubsets3(nums =[8,11,17,2,25,29,21,20,4,22]))
    # print(Solution().squareFreeSubsets2(nums =[8,11,17,2,25,29,21,20,4,22]))
    # print(Solution().squareFreeSubsets(nums = [26,6,4,27,6,18]))
    # print(Solution().squareFreeSubsets2(nums = [26,6,4,27,6,18]))

    # print(Solution().squareFreeSubsets(nums = [1,2,6,15,7,19,6,29,28,24,21,25,25,18,9,6,20,21,8,24,14,19,24,28,30,27,13,21,1,23,13,29,24,29,18,7]))
    # print(Solution().squareFreeSubsets2(nums = [1,2,6,15,7,19,6,29,28,24,21,25,25,18,9,6,20,21,8,24,14,19,24,28,30,27,13,21,1,23,13,29,24,29,18,7]))
    nums = [20,14,7,23,25,24,2,16,8,2,26,29,24,18,26,13,25,7,25,30,16,1,6,26,5,30,18,25,7,9,24,22,16,9,8,4,18,18,21,30,20,25,4,25,20,21,5,6,5,19,15,12,30,5,2,6,14,2,25,13,5,30,9,14,30,24,11,15,24,20,24,22,20,29,25,3,20,19,4,30,4,13,28,29,14,6,3,22,19,18,8,2,23,3,3,14,2,15,24,3,14,19,20,17,3,24,28,15,23,20,2,8,2,7,11,21,1,19,26,26,28,19,5,27,9,8,15,20,1,3,17,14,15,6,8,19,21,25,9,12,10,20,30,6,1,1,10,3,17,25,17,26,15,1,28,22,1,12,4,2,27,16,5,19,6,22,22,5,5,30,29,25,16,27,17,29,20,21,3,16,7,6,11,24,19,15,16,29,11,3,15,21,4,10,17,10,13,15,1,2,19,18,30,6,17,29,26,26,15,6,3,26,18,23,11,10,6,15,30,18,20,13,30,6,27,16,26,7,4,4,14,18,2,22,2,3,2,15,30,24,14,28,9,14,9,18,27,11,4,17,7,28,30,20,1,30,15,9,29,7,5,22,22,21,25,13,3,21,23,8,13,26,23,8,25,26,12,4,19,8,10,24,4,24,9,10,3,14,14,2,15,21,27,18,3,17,25,28,8,17,7,14,6,7,8,15,8,20,15,4,27,23,30,25,27,15,14,23,9,29,12,19,1,29,10,12,11,16,19,29,20,28,25,15,7,23,29,2,30,25,20,15,25,27,1,4,28,13,14,7,13,26,29,11,28,11,11,19,28,10,11,29,16,25,17,23,19,12,23,10,13,15,17,18,5,29,6,18,23,8,9,8,27,8,7,19,4,12,6,30,18,14,1,24,20,20,23,26,27,8,8,11,19,17,20,29,26,6,8,4,24,18,8,30,26,4,1,21,7,15,6,29,11,7,1,2,23,15,4,4,6,27,21,6,20,15,23,26,2,13,2,11,29,13,23,30,1,22,4,25,27,13,17,25,19,22,20,27,9,9,14,29,2,6,20,3,29,2,7,17,1,10,20,21,12,5,27,5,18,19,20,20,17,3,17,29,2,10,4,23,3,19,29,17,14,25,18,30,19,28,28,9,19,6,6,23,6,20,28,30,9,11,29,4,11,11,28,28,11,15,18,18,4,27,7,29,4,27,13,5,5,30,11,14,12,27,3,8,12,27,29,8,30,5,21,27,15,24,11,2,13,6,16,26,9,26,2,12,6,19,7,12,22,10,15,28,20,10,14,24,9,9,28,2,17,2,15,22,12,26,14,15,2,22,27,18,19,19,9,7,18,1,30,21,16,23,20,21,22,12,30,15,20,22,4,23,19,17,8,18,11,8,13,19,3,13,30,7,21,3,20,29,6,10,4,3,8,27,17,28,20,2,11,3,22,16,5,2,26,23,6,9,17,24,26,23,27,17,16,26,29,20,22,15,18,19,23,26,13,16,14,13,12,17,30,4,21,21,9,26,16,7,11,25,24,17,27,7,3,7,20,19,15,19,21,14,15,19,10,17,3,7,21,8,10,24,7,3,30,30,25,12,22,14,28,3,12,6,30,19,6,16,21,29,19,16,2,11,4,18,6,16,10,28,25,29,10,23,30,2,11,15,1,14,13,8,30,22,18,1,15,18,24,9,18,7,20,7,25,28,2,8,2,9,19,21,4,9,5,4,2,5,6,4,30,18,20,13,6,5,14,12,4,1,13,9,20,17,19,28,24,2,15,9,3,12,4,24,8,19,10,9,28,26,27,7,5,15,15,19,21,28,18,11,3,14,6,14,14,5,12,12,12,7,10,5,8,14,10,26,15,8,8,7,26,19,18,13,6,18,30,16,25,5,6,11,3,21,9,15,29,18,11,16,26,28,6,21,11,8,25,19,20,12,18,11,19,25,17,24,11,9,2,2,2,2,28,19,5,8,20,4,3,20,11,8,18,18,6,30,17,3,5,3,24,10,11,13,25,26,25,18,6,29,17,2,27,16,24,22,5,25,30,24,30,23,18,29,27,21,17,27,13,2,28,15,22,17,4,3,29,4,28,7,9,5,28,23,23,30,4,21,8,12,22,22,1,23,18,22,25,22,10,6,5,10,4,8,6,18,14,24,8,7,6,2,21,6,4,12,22,28,25,14,4,22,10,8,8,8,28,28,4,26,21,23,23,29,25,27,3,13,15,23,12,6,3,16,10,3,14,25,4,28,15,28,20,13,24,27]
    print(Solution().squareFreeSubsets3(nums = nums))
    print(Solution().squareFreeSubsets4(nums = nums))
    print(Solution().squareFreeSubsets5(nums = nums))
    nums = [26,22,14,1,12,23,25,3,6,23,12,2,30,11,30,22,20,22,4,12,19,5,21,14,22,16,22,11,7,6,6,20,9,3,18,10,13,16,14,25,12,7,21,16,24,3,15,18,26,6,2,4,4,24,27,12,17,8,1,20,28,4,20,29,12,17,14,21,15,25,7,12,17,12,25,20,27,17,23,2,19,12,23,18,21,15,16,30,6,26,28,16,24,16,1,13,14,18,8,21,29,24,5,17,3,19,24,11,21,17,21,2,16,11,6,18,7,21,11,14,27,14,25,6,18,16,16,21,19,22,14,5,26,9,30,5,11,29,23,9,2,6,22,14,16,22,14,29,5,2,27,15,11,18,27,28,10,11,30,30,22,30,23,2,4,18,12,22,3,19,3,12,6,21,12,29,30,8,10,19,14,21,13,18,2,13,7,1,17,7,29,28,5,30,14,11,6,28,28,27,24,1,8,25,8,20,7,11,5,10,2,10,9,17,10,1,20,3,10,25,7,30,28,14,29,23,20,3,18,24,29,27,14,8,9,5,9,10,2,21,3,24,16,21,30,6,4,21,12,17,20,28,6,20,22,10,14,2,25,7,4,17,28,5,9,1,3,20,8,16,17,23,8,13,28,3,11,10,17,17,19,13,12,17,1,26,20,23,6,24,4,10,26,1,27,28,2,10,22,17,1,21,20,6,3,15,19,30,23,20,18,3,16,25,9,25,23,14,8,11,11,28,26,5,13,24,23,24,18,3,8,4,9,18,3,13,18,16,29,13,23,3,23,5,15,2,2,6,19,7,16,8,14,13,27,23,21,9,21,16,29,24,22,9,3,15,9,28,18,13,25,16,4,27,3,28,15,3,3,7,10,11,14,21,5,25,29,18,21,27,27,17,9,14,7,23,16,22,3,27,25,17,4,18,9,5,28,27,6,22,21,26,10,28,13,6,21,27,5,15,18,25,30,12,5,20,13,12,26,13,5,13,6,11,12,16,22,1,1,13,9,26,13,1,28,22,28,20,7,15,6,17,21,9,13,14,26,22,14,2,28,24,3,14,28,12,15,7,26,2,10,28,21,2,21,11,18,24,14,20,1,25,14,5,14,28,3,25,1,12,24,5,26,3,19,26,2,28,30,16,6,27,15,19,11,24,26,2,10,22,18,28,19,3,23,25,22,8,28,14,7,13,13,19,29,30,26,25,4,28,6,9,13,11,3,19,1,16,16,27,26,6,1,20,10,26,30,2,5,6,23,11,5,7,17,15,18,30,25,2,2,13,6,19,26,29,4,18,18,12,26,10,4,10,26,30,12,6,22,2,25,10,29,11,3,26,25,26,21,30,29,11,22,9,13,17,29,1,13,23,16,22,14,13,23,17,10,29,26,25,15,4,6,10,16,26,13,26,26,14,6,21,20,4,6,23,25,2,30,19,24,28,14,12,19,2,5,3,1,18,2,10,14,2,15,5,26,7,23,19,20,14,13,21,24,26,18,23,14,13,21,18,1,10,5,16,22,24,7,7,17,10,20,4,15,20,4,9,19,6,23,25,11,3,17,21,22,12,13,4,5,22,23,8,3,4,1,25,4,13,17,1,20,9,6,23,10,20,13,16,12,20,9,25,21,18,16,16,17,29,30,16,16,22,19,29,22,22,6,24,20,27,4,1,10,20,20,10,26,9,4,21,5,12,7,20,26,9,24,16,16,30,17,2,14,26,15,1,15,30,2,2,25,19,26,17,26,16,21,23,1,13,22,3,12,23,12,4,8,21,23,21,14,25,2,27,6,28,3,5,15,14,30,14,30,7,26,10,6,29,17,16,21,16,4,29,19,13,21,17,21,23,26,20,18,13,26,29,22,13,30,2,12,15,26,22,1,5,3,25,3,2,12,24,26,13,25,8,15,20,21,3,24,1,23,14,21,6,28,13,12,13,18,18,6,5,17,19,7,25,7,12,16,25,26,26,19,21,26,25,10,24,28,21,11,17,28,15,27,12,24,3,6,8,18,1,29,25,18,23,24,20,13,20,24,15,15,5,17,17,9,15,18,17,9,12,17,23,17,11,7,22,23,22,5,3,6,5,19,12,4,24,22,23,14,12,20,12,23,3,29,11,13,30,18,14,21,7,9,14,25,4,28,22,7,18,10,8,14,18,21,12,13,29,8,26,21,12,27,7,20,7,12,23,1,3,28,27,10,2,3,24,17,24,5,27,29,25,19,6,15,12,3,3,20,6,26,3,28,28,29,19,3,16,17,7,25,12,19,1]
    print(Solution().squareFreeSubsets3(nums = nums))
    print(Solution().squareFreeSubsets4(nums = nums))
    print(Solution().squareFreeSubsets5(nums = nums))