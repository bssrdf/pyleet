

'''

-Medium-

*DFS*

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
 

Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000

'''

from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = nums
        def dfs(i, s):
            if i == n: return 1
            ret = dfs(i+1, s)
            if A[i]-k not in s and A[i]+k not in s:
                ret += dfs(i+1, s | {A[i]})
            return ret
        return dfs(0, set()) - 1
    

    # 在枚举 78. 子集 的基础上加个判断。

    # 代码实现时，可以用哈希表或者数组来记录选过的数，从而 

    #写法一：选或不选

    def beautifulSubsets2(self, nums: List[int], k: int) -> int:
        ans = -1  # 去掉空集
        cnt = [0] * (max(nums) + k * 2)  # 用数组实现比哈希表更快
        def dfs(i: int) -> None:
            if i == len(nums):
                nonlocal ans
                ans += 1
                return
            dfs(i + 1)  # 不选
            x = nums[i]
            if cnt[x - k] == 0 and cnt[x + k] == 0:
                cnt[x] += 1  # 选
                dfs(i + 1)
                cnt[x] -= 1  # 恢复现场
        dfs(0)
        return ans

    #写法二：枚举选哪个
    def beautifulSubsets3(self, nums: List[int], k: int) -> int:
        ans = -1  # 去掉空集
        cnt = [0] * (max(nums) + k * 2)  # 用数组实现比哈希表更快
        def dfs(i: int) -> None:  # 从 i 开始选
            nonlocal ans
            ans += 1
            if i == len(nums):
                return
            for j in range(i, len(nums)):  # 枚举选哪个
                x = nums[j]
                if cnt[x - k] == 0 and cnt[x + k] == 0:
                    cnt[x] += 1  # 选
                    dfs(j + 1)
                    cnt[x] -= 1  # 恢复现场
        dfs(0)
        return ans





    
if __name__ == '__main__':
    print(Solution().beautifulSubsets(nums = [2,4,6], k = 2))
    print(Solution().beautifulSubsets(nums = [1], k = 1))
        