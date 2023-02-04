'''

-Hard-
$$$

*Sliding Window*

You are given an integer array nums and a positive integer k.

The frequency score of an array is the sum of the distinct values in the array raised to the power of their frequencies, taking the sum modulo 109 + 7.

For example, the frequency score of the array [5,4,5,7,4,4] is (43 + 52 + 71) modulo (109 + 7) = 96.
Return the maximum frequency score of a subarray of size k in nums. You should maximize the value under the modulo and not the actual value.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,1,1,2,1,2], k = 3
Output: 5
Explanation: The subarray [2,1,2] has a frequency score equal to 5. It can be shown that it is the maximum frequency score we can have.
Example 2:

Input: nums = [1,1,1,1,1,1], k = 4
Output: 1
Explanation: All the subarrays of length 4 have a frequency score equal to 1.
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 106


'''

from typing import List
from collections import defaultdict, Counter


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n, MOD = len(nums), 10**9 + 7
        cur, below = defaultdict(int), defaultdict(int)
        ans, sums = 0, 0
        ones = 0
        for i,v in enumerate(nums):
            if v > 1:
                if v not in cur:
                    cur[v] = v
                else:
                    below[v] = cur[v] 
                    cur[v] *= v
            if v == 1: 
                if ones == 0:  sums += 1
                ones += 1
            else:  
                sums += cur[v] - below[v]
            if i >= k:
                j = i-k
                if nums[j] == 1:
                    ones -= 1
                    if ones == 0: sums -= 1
                else:    
                    sums -= cur[nums[j]] - below[nums[j]] 
                    cur[nums[j]] = below[nums[j]]
                    below[nums[j]] //= nums[j]
                    if below[nums[j]] == 1:
                        below[nums[j]] = 0
                    if cur[nums[j]] == 0:
                        del cur[nums[j]]
            if i >= k-1:
                ans = max(ans, sums%MOD)
        return ans
        
    def maxFrequencyScore2(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        cnt = Counter(nums[:k])
        ans = cur = sum(pow(k, v, mod) for k, v in cnt.items()) % mod
        i = k
        while i < len(nums):
            a, b = nums[i - k], nums[i]
            if a != b:
                cur += (b - 1) * pow(b, cnt[b], mod) if cnt[b] else b
                cur -= (a - 1) * pow(a, cnt[a] - 1, mod) if cnt[a] > 1 else a
                cur %= mod
                cnt[b] += 1
                cnt[a] -= 1
                ans = max(ans, cur)
            i += 1
        return ans






from random import randint

if __name__ == "__main__":
    print(Solution().maxFrequencyScore(nums = [1,1,1,2,1,2], k = 3))
    print(Solution().maxFrequencyScore(nums = [1,1,1,1,1,1], k = 4))
    n = 50000
    k = randint(1, n)
    nums = [randint(1, 10000) for i in range(n)] 
    print(Solution().maxFrequencyScore2(nums = nums, k = k))
    print(Solution().maxFrequencyScore(nums = nums, k = k))


