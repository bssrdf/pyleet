'''

-Medium-

*Hash Table*

You are given a 0-indexed array nums consisting of positive integers, representing targets on a number line. You are also given an integer space.

You have a machine which can destroy targets. Seeding the machine with some nums[i] allows it to destroy all targets with values that can be represented as nums[i] + c * space, where c is any non-negative integer. You want to destroy the maximum number of targets in nums.

Return the minimum value of nums[i] you can seed the machine with to destroy the maximum number of targets.

 

Example 1:

Input: nums = [3,7,8,1,1,5], space = 2
Output: 1
Explanation: If we seed the machine with nums[3], then we destroy all targets equal to 1,3,5,7,9,... 
In this case, we would destroy 5 total targets (all except for nums[2]). 
It is impossible to destroy more than 5 targets, so we return nums[3].
Example 2:

Input: nums = [1,3,5,2,4,6], space = 2
Output: 1
Explanation: Seeding the machine with nums[0], or nums[3] destroys 3 targets. 
It is not possible to destroy more than 3 targets.
Since nums[0] is the minimal integer that can destroy 3 targets, we return 1.
Example 3:

Input: nums = [6,2,5], space = 100
Output: 2
Explanation: Whatever initial seed we select, we can only destroy 1 target. The minimal seed is nums[1].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= space <= 109


'''


from typing import List

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        A = list(sorted(nums))
        k = space
        n = len(A)
        dp = {A[0]%k:1}
        for i in range(1,n):
            if A[i] == A[i-1]:
                dp[A[i]%k] += 1
                continue
            if A[i]%k in dp:
                dp[A[i]%k] += 1
            else:
                dp[A[i]%k] = 1  
        # print(A)  
        # print(dp)  
        mxf, vals = 0, []
        for i in dp:
            if mxf < dp[i]:
                mxf = dp[i]
                vals = [i]
            elif mxf == dp[i]:
                vals.append(i)
        # print(vals)
        for a in A:
            for v in vals:
                if a%k == v:
                    return a 
        return 0        
    
    def destroyTargets2(self, nums: List[int], space: int) -> int:
        A, k, n, = nums, space, len(nums)
        ans, dp = 10**9, {}
        for i in range(n):            
            if A[i]%k in dp:
                dp[A[i]%k] += 1
            else:
                dp[A[i]%k] = 1  
        mxf, vals = 0, set()
        for i in dp:
            if mxf < dp[i]:
                mxf = dp[i]
                vals = {i}
            elif mxf == dp[i]:
                vals.add(i)
        for a in A:
            if a%k in vals:
                ans = min(ans, a)
        return ans
        
        

if __name__ == "__main__":   
    print(Solution().destroyTargets(nums = [3,7,8,1,1,5], space = 2))
    print(Solution().destroyTargets(nums = [1,3,5,2,4,6], space = 2))
    print(Solution().destroyTargets(nums = [6,2,5], space = 100))
    nums = [625879766,235326233,250224393,501422042,683823101,948619719,680305710,733191937,182186779,353350082]
    print(Solution().destroyTargets(nums = nums, space = 4))
    