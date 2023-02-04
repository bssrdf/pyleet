'''
-Medium-
*Sliding Window*
*Prefix Sum*

You are given an integer array nums and an integer x. In one operation, you 
can either remove the leftmost or the rightmost element from the array nums 
and subtract its value from x. Note that this modifies the array for future 
operations.

Return the minimum number of operations to reduce x to exactly 0 if it's 
possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to 
reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and 
the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9

'''

from itertools import accumulate

class Solution(object):
    '''
    The equivalent problem is to find a longest subarray with sum equal to
    sum(nums)-x. There two ways to solve this maximum length subarray sum problem:
    hashtable and sliding window
    '''
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """        
        cumsum = [0] + list(accumulate(nums))
        dic = {c:i for i,c in enumerate(cumsum)}
        goal = cumsum[-1] - x
        ans = -float("inf")

        if goal < 0: return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])

        return len(nums) - ans if ans != -float("inf") else -1
        

    def minOperationsSlidingWindow(self, nums, x):
        target, size, win_sum, lo, n = sum(nums) - x, -1, 0, -1, len(nums)
        for hi, num in enumerate(nums):
            win_sum += num # expand the window to the right
            while lo + 1 < n and win_sum > target:
                # shrink the window because sum in the window too big
                lo += 1
                win_sum -= nums[lo]
            if win_sum == target: # we found a subarray, check its length
                size = max(size, hi - lo)
        return -1 if size < 0 else n - size
                

if __name__ == "__main__":
    print(Solution().minOperations([1,1,4,2,3], 5))
    print(Solution().minOperations([5,6,7,8,9], 4))
    print(Solution().minOperations([3,2,20,1,1,3], 10))
    nums = [5207,5594,477,6938,8010,7606,2356,6349,3970,751,5997,6114,9903,3859,6900,7722,2378,1996,8902,228,4461,90,7321,7893,4879,9987,1146,8177,1073,7254,5088,402,4266,6443,3084,1403,5357,2565,3470,3639,9468,8932,3119,5839,8008,2712,2735,825,4236,3703,2711,530,9630,1521,2174,5027,4833,3483,445,8300,3194,8784,279,3097,1491,9864,4992,6164,2043,5364,9192,9649,9944,7230,7224,585,3722,5628,4833,8379,3967,5649,2554,5828,4331,3547,7847,5433,3394,4968,9983,3540,9224,6216,9665,8070,31,3555,4198,2626,9553,9724,4503,1951,9980,3975,6025,8928,2952,911,3674,6620,3745,6548,4985,5206,5777,1908,6029,2322,2626,2188,5639]
    print(Solution().minOperations(nums, 565610))