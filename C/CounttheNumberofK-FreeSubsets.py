'''

-Medium-
$$$
*Sorting*
*Modular*
*DP*

You are given an integer array nums, which contains distinct elements and an integer k.

A subset is called a k-Free subset if it contains no two elements with an absolute difference equal to k. Notice that the empty set is a k-Free subset.

Return the number of k-Free subsets of nums.

A subset of an array is a selection of elements (possibly none) of the array.

 

Example 1:

Input: nums = [5,4,6], k = 1
Output: 5
Explanation: There are 5 valid subsets: {}, {5}, {4}, {6} and {4, 6}.
Example 2:

Input: nums = [2,3,5,8], k = 5
Output: 12
Explanation: There are 12 valid subsets: {}, {2}, {3}, {5}, {8}, {2, 3}, {2, 3, 5}, {2, 5}, {2, 5, 8}, {2, 8}, {3, 5} and {5, 8}.
Example 3:

Input: nums = [10,5,9,11], k = 20
Output: 16
Explanation: All subsets are valid. Since the total count of subsets is 24 = 16, so the answer is 16. 
 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 1000
1 <= k <= 1000
Solutions



'''

from typing import List
from functools import lru_cache
from collections import defaultdict

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        #wrong 
        A, n = nums, len(nums)
        A.sort()
        mask = [False]*1001
        @lru_cache(None)
        def dfs(i):
            if i == n: return 1
            ret = dfs(i+1)
            if not mask[A[i]-k]:
                mask[A[i]] = True
                ret += dfs(i+1)
                mask[A[i]] = False
            return ret
        return dfs(0)
    
    def countTheNumOfKFreeSubsets2(self, nums: List[int], k: int) -> int:
        #  方法：分组 + 动态规划
        #  我们先将数组按照升序排序，然后将数组中的元素按照 mod k 分组，即 nums[i] mod k
        #  相同的元素放在同一组中。那么对于任意两个不同组的元素，它们的差值的绝对值一定不等于 
        #  因此，我们可以求出每一组的子集个数，然后将每一组的子集个数相乘即可得到答案。

        # 对于每一组 arr，我们可以使用动态规划求出子集个数。设 f[i] 表示前 i 个元素的子集个数，
        # 初始时 f[0] = 1 ，而 f[1] = 2 。当 i >= 2 时，如果 arr[i-1]-arr[i-2] = k，如果我们选择 
        # arr[i-1],那么 f[i] = f[i-2]; 如果我们不选择 arr[i-1]，那么 f[i] = f[i-1]。因此，当 
        # arr[i-1] -arr[i-2] = k 时，有 f[i] = f[i-1] + f[i-2] ；否则 f[i] = f[i-1]*2 。
        # 这一组的子集个数即为 f[m]，其中 m 为数组 arr 的长度。

        # 最后，我们将每一组的子集个数相乘即可得到答案。

        # 时间复杂度 O(nlogn)，空间复杂度 O(n)。
        nums.sort()
        g = defaultdict(list)
        for x in nums:
            g[x % k].append(x)
        ans = 1
        for arr in g.values():
            m = len(arr)
            f = [0] * (m + 1)
            f[0] = 1
            f[1] = 2
            for i in range(2, m + 1):
                if arr[i - 1] - arr[i - 2] == k:
                    f[i] = f[i - 1] + f[i - 2]
                else:
                    f[i] = f[i - 1] * 2
            ans *= f[m]
        return ans

    
import random 

if __name__ == '__main__':
    print(Solution().countTheNumOfKFreeSubsets(nums = [5,4,6], k = 1))
    print(Solution().countTheNumOfKFreeSubsets(nums = [2,3,5,8], k = 5))
    print(Solution().countTheNumOfKFreeSubsets(nums = [10,5,9,11], k = 20))
    N = 45
    nums = [random.randint(1, 1000) for _ in range(N)]
    k = random.randint(1, 1000)
    print(nums, k)
    print(Solution().countTheNumOfKFreeSubsets(nums = nums, k = k))
    print(Solution().countTheNumOfKFreeSubsets2(nums = nums, k = k))