'''
-Medium-

In this challenge, you will be given an array of integers, each unique within the array, and an 
integer representing a target difference. Determine the number of pairs of elements in the array 
that have a difference equal to the target difference.
For example, consider the array [1, 3, 5] and a target difference 2. There are two pairs:[1, 3] 
and [3, 5],that have the target difference.you must return an integer count of the number of 
pairs within a having a difference of k.

2 <= array length <= 10^5.
Each element of nums,nums[i] <= 2 * 10^9.
Each nums[i] is unique within nums.
1 <= target <= 10^9.
样例
Example 1:

Input: nums = [1, 3, 5, 7], target = 2
Output: 3
Explanation:
3 - 1 = 2
5 - 3 = 2
7 - 5 = 2
Example 2:

Input: nums = [7, 2, 6], target = 2 
Output: 0
Explanation:
no pair have a difference of k 

'''

class Solution:
    """
    @param nums: a integer array
    @param target: 
    @return: return a integer
    """
    def KDifference(self, nums, target):
        # write your code here
        s = set()
        nums.sort()
        res = 0
        for i in nums:
            if i-target in s: res += 1
            s.add(i)
        return res