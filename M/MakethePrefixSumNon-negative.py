'''

-Medium-
$$$
*Greedy*
*Priority Queue*
You are given a 0-indexed integer array nums. You can apply the following operation any number of times:

Pick any element from nums and put it at the end of nums.
The prefix sum array of nums is an array prefix of the same length as nums such that prefix[i] is the sum of all the integers nums[j] where j is in the inclusive range [0, i].

Return the minimum number of operations such that the prefix sum array does not contain negative integers. The test cases are generated such that it is always possible to make the prefix sum array non-negative.

 

Example 1:

Input: nums = [2,3,-5,4]
Output: 0
Explanation: we do not need to do any operations.
The array is [2,3,-5,4]. The prefix sum array is [2, 5, 0, 4].
Example 2:

Input: nums = [3,-5,-2,6]
Output: 1
Explanation: we can do one operation on index 1.
The array after the operation is [3,-2,6,-5]. The prefix sum array is [3, 1, 7, 2].
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


'''

from typing import List
from collections import deque
from heapq import heappop, heappush
class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        # Wrong
        ans, stack = 0, deque()
        A, n, t = nums, len(nums), 0
        for i in range(n):
            t += A[i]
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            stack.append(i)
            while t < 0 and stack:
                t -= A[stack.popleft()]                
                ans += 1
        return ans
    
    def makePrefSumNonNegative2(self, nums: List[int]) -> int:
        h = []
        ans = s = 0
        for x in nums:
            s += x
            if x < 0:
                heappush(h, x)
            while s < 0:
                s -= heappop(h)
                ans += 1
        return ans

import random
if __name__ == '__main__':
    # print(Solution().makePrefSumNonNegative(nums = [2,3,-5,4]))
    # print(Solution().makePrefSumNonNegative(nums = [3,-5,-2,6]))
    # print(Solution().makePrefSumNonNegative(nums = [3,-5,-7, 10, 18, -17, 26, -2,6]))
    # print(Solution().makePrefSumNonNegative2(nums = [3,-5,-7, 10, 18, -17, 26, -2,6]))
    nums = [20, -6, -9, 40, 62, -54, -86, 95, -97, -62, -23, -68, -34, -55, -42, 98, 1, -83, 33, -82]
    print(Solution().makePrefSumNonNegative(nums = nums))
    print(Solution().makePrefSumNonNegative2(nums = nums))
    # n, M = 20, 100
    # for _ in range(1000): 
    #     nums = [ random.randint(-M, M) for i in range(n) ]
    #     sol1 = Solution().makePrefSumNonNegative(nums = nums)
    #     sol2 = Solution().makePrefSumNonNegative2(nums = nums)
    #     if sol1 != sol2:
    #         print(nums, sol1, sol2)
    #         break

