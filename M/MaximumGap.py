'''

-Hard-

*Bucket Sort*

Given an integer array nums, return the maximum difference between two successive 
elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^9

'''

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0
        INT_MIN, INT_MAX = -1, 10**9+1
        n, pre, res = len(nums), 0, 0
        mx, mn = max(nums), min(nums)
        size = (mx - mn) // n + 1
        cnt  = (mx - mn) // size + 1
        bucket_min = [INT_MAX]*cnt 
        bucket_max = [INT_MIN]*cnt
        for num in nums:
            idx = (num - mn) // size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
        #print(size, cnt, bucket_max, bucket_min)
        for i in range(1, cnt):
            if bucket_min[i] == INT_MAX or bucket_max[i] == INT_MIN: continue
            res = max(res, bucket_min[i] - bucket_max[pre])
            pre = i
        return res

if __name__ == "__main__":
    print(Solution().maximumGap([3,6,9,1]))  
    print(Solution().maximumGap([10, 6, 20, 176, 55, 999, 340, 567]))       