'''
-Hard-
*Monotonic Queue*

Given an array nums, there is a sliding window of size k which is moving from 
the very left of the array to the very right. You can only see the k numbers 
in the window. Each time the sliding window moves right by one position. Return 
the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

Can be solved using a general data structure: monotonic queue
more information:
https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6


Solution Using Dequeue: O(N)

Very similar code structure to heap solution
http://yuanhsh.iteye.com/blog/2190852
https://docs.python.org/2/library/collections.html#collections.deque
Add to dequeue at tail using the rule where you pop all numbers from tail which are less than 
equal to the number. Think why? 300->50->27 and say 100 comes. 50 and/or 27 can never be the 
maximum in any range.
When you do the above, the largest number is at head. But you still need to test if front is 
within the range or not.
Pop or push each element at-max once. O(N)
*So, to maintain the queue in order,

When moves to a new number, iterate through back of the queue, removes all numbers that are 
not greater than the new one, and then insert the new one to the back.
findMax only need to take the first one of the queue.
To remove a number outside the window, only compare whether the current index is greater 
than the front of queue. If so, remove it.*

'''
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if k == 0:
            return nums
# Defining Deque and result list
        dq = deque()
        result = []
        
# First traversing through K in the nums and only adding maximum value's index to the deque.
# Note: We are olny storing the index and not the value.
# Now, Comparing the new value in the nums with the last index value from deque,
# and if new valus is less, we don't need it

        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()            
            dq.append(i)
            
        #print(deq)
            
# Here we will have deque with index of maximum element for the first subsequence of length k.
	
# Now we will traverse from k to the end of array and do 4 things
# 1. Appending left most indexed value to the result
# 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
# 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
# 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)
 
        for i in range(k, len(nums)):
            result.append(nums[dq[0]])
            if dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()            
            dq.append(i)
            
        
#Adding the maximum for last subsequence
        result.append(nums[dq[0]])
        
        return result


print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
