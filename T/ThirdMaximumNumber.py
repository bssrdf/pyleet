'''
-Easy-

Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

'''

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        m1, m2, m3 = sorted(nums[:3], reverse=True)
        for i in range(3, len(nums)):
            if nums[i] > m1:
                m3, m2, m1 = m2, m1, nums[i]
            elif nums[i] > m2:
                m3, m2 = m2, nums[i]
            elif nums[i] > m3:
                m3 = nums[i]
        return m3





if __name__ == "__main__":
    print(Solution().thirdMax([3, 2, 1]))
    print(Solution().thirdMax([2, 3, 2, 1]))