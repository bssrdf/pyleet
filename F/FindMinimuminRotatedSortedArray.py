'''
-Medium-

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of 
this array.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] < nums[r]: return nums[l]
            m = l+(r-l)//2
            if nums[m] < nums[r]:
                # we know that nums[mid] <= nums[right].
                # therefore, we know it is possible for the mid index to store a smaller
                # value than at least one other index in the list (at right), so we do
                # not discard it by doing right = mid - 1. it still might have the minimum value.
                r = m
            else:
                # we know that the number at mid is greater than at least
                # one number to the right, so we can use mid + 1 and
                # never consider mid again; we know there is at least
                # one value smaller than it on the right
                l = m+1       
        return min(nums[l], nums[r])

if __name__ == "__main__":
    print(Solution().findMin([4,5,6,7,0,1,2]))

