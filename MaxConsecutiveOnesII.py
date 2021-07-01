'''
-Medium-
Given a binary array, find the maximum number of consecutive 1s in this array if you 
can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, 
you can't store all numbers coming from the stream as it's too large to hold in memory. 
Could you solve it efficiently?

'''
from collections import deque
class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # write your code here
        left, right = 0, 0
        n = len(nums)
        cnt0, cnt1 = 0, 0
        res = 0
        while right < n:
            if nums[right] == 1:
                cnt1 += 1
            else:
                cnt0 += 1
            while left <= right and cnt0 > 1:
                if nums[left] == 1:
                    cnt1 -= 1
                else:
                    cnt0 -= 1
                left += 1
            right += 1
            res = max(res, right-left)
        return res
    
    def findMaxConsecutiveOnesStream(self, nums):
        # Solution to the follow up and also generalizes to the k allowed change 0 to 1
        #Follow up:
        #What if the input numbers come in one by one as an infinite stream? In other words, 
        #you can't store all numbers coming from the stream as it's too large to hold in memory. 
        #Could you solve it efficiently?
        left, right = 0, 0
        n, k = len(nums), 1
        res = 0
        queue = deque()
        while right < n:
            if nums[right] == 0:
                queue.append(right) # We do not have access to previous values in the array.
                                    # use a queue to record the 0's index
            if len(queue) > k:
                left = queue.popleft()+1 # skip the 0 at the very beginning of the queue
            right += 1
            res = max(res, right-left)
        return res

if __name__ == "__main__":
    arr = [1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1,0]
    print(arr[340:360])
    print(Solution().findMaxConsecutiveOnes(arr))
    print(Solution().findMaxConsecutiveOnesStream(arr))
    arr = [1,0,1,1,0]
    print(Solution().findMaxConsecutiveOnes(arr))
    print(Solution().findMaxConsecutiveOnesStream(arr))