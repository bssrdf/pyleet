'''
-Medium-

*Binary Search*

Given an array nums which consists of non-negative integers and an integer m, 
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)

'''

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canSplit(target):
            sm = 0
            cnt = 0
            for n in nums:
                if sm + n > target:
                   sm = n
                   cnt += 1
                else: 
                   sm += n
            cnt += 1
            return cnt <= m
        l = 1
        r = 0
        for i in nums:
            l = max(l, i)
            r += i
        while l+1 < r:
            mid = l + (r-l)//2
            if canSplit(mid):
                r = mid 
            else:
                l = mid+1
        if canSplit(l): return l
        else: return r

if __name__ == "__main__":
    print(Solution().splitArray([7,2,5,10,8], 2))
    print(Solution().splitArray([1,2,3,4,5],  2))
    print(Solution().splitArray([1,4,4], 3))