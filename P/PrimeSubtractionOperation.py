'''

-Medium-
*Greedy*
*Binary Search*

You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.

 

Example 1:

Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.
Example 2:

Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
Example 3:

Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
nums.length == n




'''
import math
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

from typing import List
import bisect

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = sieve(1000)
        # print(primes)
        ans = True
        idx = bisect.bisect_left(primes, nums[0])
        if idx > 0:
            nums[0] -= primes[idx-1]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                ans = False
                break
            idx = bisect.bisect_left(primes, nums[i])
            while idx-1 >= 0 and nums[i] - primes[idx-1] <= nums[i-1]:
                idx -= 1
            if idx > 0:
                nums[i] -= primes[idx-1]
        return ans

if __name__ == '__main__':
    print(Solution().primeSubOperation(nums = [4,9,6,10]))
    print(Solution().primeSubOperation(nums = [6,8,11,12]))
    print(Solution().primeSubOperation(nums = [5,8,3]))
    print(Solution().primeSubOperation(nums = [4,3,7,4]))