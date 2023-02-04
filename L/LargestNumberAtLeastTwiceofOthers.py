'''
-Easy-

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
样例
Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
标签


'''

class Solution:
    """
    @param nums: a integer array
    @return: the index of the largest element
    """
    def dominantIndex(self, nums):
        # Write your code here
        m1, m2, idx = -1, -1, -1
        for i,v in enumerate(nums):
            if m1 < v:
                m1, m2, idx = v, m1, i
            elif m2 < i:
                m2 = i
        return idx if m1 >= 2*m2 else -1


if __name__=="__main__":
    print(Solution().dominantIndex(nums = [3, 6, 1, 0]))
    print(Solution().dominantIndex(nums = [1, 2, 3, 4]))