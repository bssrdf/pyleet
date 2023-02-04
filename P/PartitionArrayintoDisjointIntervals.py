'''
-Medium-

Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a 
partitioning exists.

 

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
 

Note:

2 <= nums.length <= 30000
0 <= nums[i] <= 10^6
It is guaranteed there is at least one way to partition nums as described.

'''

class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        INT_MAX = 10**6+1
        leftMax = [-1]*(n)
        leftMax[0] = nums[0]
        rightMin = [INT_MAX]*n
        rightMin[-1] = nums[-1]
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1], nums[i])
        for i in range(n-2, -1, -1):
            rightMin[i] = min(rightMin[i+1], nums[i])
       # print(leftMax)    
       # print(rightMin)
        for i in range(n-1):
            if leftMax[i] <= rightMin[i+1]:
                return i+1
        return 0

    def partitionDisjointFast(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        INT_MAX = 10**6+1
        leftMax = -1
        rightMin = [INT_MAX]*n
        rightMin[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            rightMin[i] = min(rightMin[i+1], nums[i])
        for i in range(n-1):
            leftMax = max(leftMax, nums[i])
            if leftMax <= rightMin[i+1]:
                return i+1
        return 0



if __name__ == "__main__": 
    print(Solution().partitionDisjoint([5,0,3,8,6]))
    print(Solution().partitionDisjoint([1,1,1,0,6,12]))
    print(Solution().partitionDisjoint([1,1]))
    print(Solution().partitionDisjointFast([5,0,3,8,6]))
    print(Solution().partitionDisjointFast([1,1,1,0,6,12]))
    print(Solution().partitionDisjointFast([1,1]))