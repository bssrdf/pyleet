'''
-Medium-

*Monotonic Queue*

Given an integer array, you need to find one continuous subarray that if you only 
sort this subarray in ascending order, then the whole array will be sorted in 
ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole 
array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.


'''


class Solution(object):

    def findUnsortedSubarrayFast(self, nums):
        n = len(nums)
        beg, end, mi, mx = -1, -2, nums[n-1], nums[0]
        for i in range(1, n):
            mx = max(mx, nums[i])
            mi = min(mi, nums[n-1-i])
            if nums[i] < mx: end = i
            if nums[n-1-i] > mi: beg = n-1-i
        return end - beg + 1

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        if not nums: 
           return  0
         #find the left bound which is 6, and the right bound is 10, 
         # these two violates the mono increasking/decreasing stack
        leftbound = len(nums)-1
        rightbound = 0
        q = collections.deque()
        for i in range(len(nums)):
            while q and nums[i] < nums[q[-1]] :
                leftbound = min(leftbound, q.pop()) 
            q.append(i)

        q = collections.deque()
        for i in range(len(nums)-1, -1, -1):
            while q and nums[i] > nums[q[-1]] :
                rightbound = max(rightbound, q.pop()) 
            q.append(i)
        return rightbound-leftbound+1 if rightbound > leftbound else 0

if __name__ == "__main__":
    print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

        
    


