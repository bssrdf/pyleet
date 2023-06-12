'''


'''

from typing import List

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        for i in range(n):
            nums[i] += d if s[i] == 'R' else -d
        nums.sort()
        ans = 0 
        preSum = list(nums)
        for i in range(1,n):
            preSum[i] += preSum[i-1]
            preSum[i] %= MOD
        for i in range(1, n):
            ans += i*nums[i] - preSum[i-1]
            ans %= MOD
        return ans

if __name__ == "__main__":
    print(Solution().sumDistance(nums = [-2,0,2], s = "RLL", d = 3))