'''

-Hard-
*Sorting*
*Subset*

You are given a 0-indexed integer array nums representing the strength of some heroes. The power of a group of heroes is defined as follows:

Let i0, i1, ... ,ik be the indices of the heroes in a group. Then, the power of this group is max(nums[i0], nums[i1], ... ,nums[ik])2 * min(nums[i0], nums[i1], ... ,nums[ik]).
Return the sum of the power of all non-empty groups of heroes possible. Since the sum could be very large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [2,1,4]
Output: 141
Explanation: 
1st group: [2] has power = 22 * 2 = 8.
2nd group: [1] has power = 12 * 1 = 1. 
3rd group: [4] has power = 42 * 4 = 64. 
4th group: [2,1] has power = 22 * 1 = 4. 
5th group: [2,4] has power = 42 * 2 = 32. 
6th group: [1,4] has power = 42 * 1 = 16. 
​​​​​​​7th group: [2,1,4] has power = 42​​​​​​​ * 1 = 16. 
The sum of powers of all groups is 8 + 1 + 64 + 4 + 32 + 16 + 16 = 141.

Example 2:

Input: nums = [1,1,1]
Output: 7
Explanation: A total of 7 groups are possible, and the power of each group will be 1. Therefore, the sum of the powers of all groups is 7.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109


'''

from typing import List

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        MOD = 10**9 + 7
        ans, sm = 0, nums[0]
        ans = nums[0]**3
        for a in nums[1:]:            
            sm0 = sm 
            sm += a
            ans = (ans + a**2*sm) % MOD
            sm = sm0 * 2 + a
        return ans

    def sumOfPower(self, nums: List[int]) -> int:
        # consider contribution of each number nums[i] to the final sum
        # for nums[i] to be part of the power, it has to be either min or max of the 
        # subset it is in. This indicates some kind of ordering will be helpful
        # so first sort the array
        nums.sort()
        MOD = 10**9 + 7
        # now consider each number starting from the smallest 
        ans, sm = 0, nums[0]
        ans = nums[0]**3 # this is the smallest number's contribution  
        # starting from nums[1], each number nums[i] can form a power 
        # with each smaller number nums[j] where j < i and the power
        # is nums[i]**2 * nums[j]; in the meantime, all numbers in between 
        # nums[j] and nums[i] can be used to form subsets with the same power
        # and there are 2**(i-j-1) such subsets, for example, suppose [1,2,4,6,8]
        # nums[i] = 8 where i = 4 and we consider j = 0, the subsets including 1 and 8
        # and have power 8**2*1 are:
        # [1, 8], [1,2,8], [1,4,8], [1,6,8], [1,2,4,8], [1,4,6,8], [1,2,6,8] and [1,2,4,6,8]
        # effectively we can form all subsets (power set) using [2,4,6] and include [1, 8] in 
        # each of them and all these have power = 8**2*1
        # so the total power contributed by nums[i] is 
        #     sum((nums[i]**2 * nums[j])*(2**(i-j-1)), j=0,i-1)
        # which is
        #    nums[i]**2 * sum(nums[j]*2**(i-j-1), j=0,i-1)
        # we use sm to maintain sum(nums[j]*2**(i-j-1), j=0,i-1)
        for a in nums[1:]:            
            sm0 = sm 
            sm += a
            ans = (ans + a**2*sm) % MOD
            sm = (sm0 * 2 + a) % MOD
        return ans





if __name__ == "__main__":
    print(Solution().sumOfPower(nums = [2,1,4]))
    print(Solution().sumOfPower(nums = [1,1,1]))