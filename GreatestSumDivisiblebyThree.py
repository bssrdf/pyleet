'''
Given an array nums of integers, we need to find the maximum possible sum of 
elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4


'''
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        state = [0, float('-inf'), float('-inf')]

        for num in nums:
            if num % 3 == 0:
                state = [state[0] + num, state[1] + num, state[2] + num]
            if num % 3 == 1:
                a = max(state[2] + num, state[0])
                b = max(state[0] + num, state[1])
                c = max(state[1] + num, state[2])
                state = [a, b, c]
            if num % 3 == 2:
                a = max(state[1] + num, state[0])
                b = max(state[2] + num, state[1])
                c = max(state[0] + num, state[2])
                state = [a, b, c]
        return state[0]
        