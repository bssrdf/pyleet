'''

-Hard-

You are given a 0-indexed integer array nums of length n. The number of ways to 
partition nums is the number of pivot indices that satisfy both conditions:

1 <= pivot < n
nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
You are also given an integer k. You can choose to change the value of one element of 
nums to k, or to leave the array unchanged.

Return the maximum possible number of ways to partition nums to satisfy both conditions 
after changing at most one element.

 

Example 1:

Input: nums = [2,-1,2], k = 3
Output: 1
Explanation: One optimal approach is to change nums[0] to k. The array becomes [3,-1,2].
There is one way to partition the array:
- For pivot = 2, we have the partition [3,-1 | 2]: 3 + -1 == 2.
Example 2:

Input: nums = [0,0,0], k = 1
Output: 2
Explanation: The optimal approach is to leave the array unchanged.
There are two ways to partition the array:
- For pivot = 1, we have the partition [0 | 0,0]: 0 == 0 + 0.
- For pivot = 2, we have the partition [0,0 | 0]: 0 + 0 == 0.
Example 3:

Input: nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
Output: 4
Explanation: One optimal approach is to change nums[2] to k. The array becomes [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14].
There are four ways to partition the array.
 

Constraints:

n == nums.length
2 <= n <= 10^5
-10^5 <= k, nums[i] <= 10^5

'''
from collections import defaultdict
from typing import List

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = nums       
        sum_ = sum(A)
        L, R = defaultdict(int), defaultdict(int)
        left = 0
        for i in range(n - 1):
            left += A[i]
            right = sum_ - left
            R[left - right] += 1
        ans = R[0] #  If we don't do any replacement, answer is the number of `0`s in 
                   #  the frequency map
        left = 0
        for i in range(n):
            left += A[i]
            right = sum_ - left
            d = k - A[i]
            ans = max(ans, L[d] + R[-d]) # If we replace `A[i]` with `k`, 
                                         # we will get `L[d] + R[-d]` pivots
            R[left - right] -= 1 # transfer the frequency from `R` to `L`.
            L[left - right] += 1
        return ans

    def waysToPartition2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = nums       
        sum_ = sum(A)
        L, R = defaultdict(int), defaultdict(int)
        left = 0
        for i in range(n - 1):
            left += A[i]
            R[left] += 1
        ans = R[sum_//2] if sum_ % 2 == 0 else 0 #  If we don't do any replacement, answer is the number of `0`s in 
                                           #  the frequency map
        left = 0
        for i in range(n):
            left += A[i]
            d = k - A[i]
            if (sum_ + d) % 2 == 0:
                newSum = (sum_ + d) // 2
                ans = max(ans,  L[newSum] + R[newSum-d]) # If we replace `A[i]` with `k`,             
            R[left] -= 1 # transfer the frequency from `R` to `L`.
            L[left] += 1
        return ans


if __name__ == "__main__":
    print(Solution().waysToPartition(nums = [2,-1,2], k = 3))
    print(Solution().waysToPartition(nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33))
    print(Solution().waysToPartition2(nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33))
    arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30827,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(Solution().waysToPartition2(arr,0))
    arr = [0,0,0,1077,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,70590,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(Solution().waysToPartition2(arr,1077))
        