'''

-Medium-

*Sliding Window*
*Monotonic Queue*

Given an array of integers nums and an integer limit, return the size of the longest 
non-empty subarray such that the absolute difference between any two elements of 
this subarray is less than or equal to limit.


 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
Accepted
66,555
Submissions
146,894


'''

from typing import List
import collections
import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # WRONG!!!
        mx, mi = 0, 10**9+1
        res = 0
        left, right = 0, 0
        minh, maxh = [], []
        while right < len(nums):
            if nums[right] < mi:
                mi = nums[right]
            if nums[right] > mx:
                mx = nums[right]            
            heapq.heappush(minh, nums[right])
            heapq.heappush(maxh, -nums[right])
            right += 1
            while left < right and abs(mx-mi) > limit:
                if nums[left] == mi:
                    heapq.heappop(minh)
                    mi =  minh[0]
                if nums[left] == mx:
                    heapq.heappop(maxh)
                    mx = -maxh[0]
                left += 1
            res = max(res, right-left)           
        return res

    def longestSubarray2(self, nums: List[int], limit: int) -> int:
        A = nums
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(A):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i: heapq.heappop(maxq)
                while minq[0][1] < i: heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res
    
    def longestSubarray3(self, nums: List[int], limit: int) -> int:
        A, res = nums, 0
        # This is a monotonically decreasing double-ended queue. 
        maxd = collections.deque()

        # This is a monotonically increasing double-ended queue.
        mind = collections.deque()

        i = 0
        for j in range(len(A)):
            # At each iteration, we maintain the biggest elements in maxd.
            # Remove any element smaller than A[j]
            while len(maxd) and A[j] > maxd[-1]: maxd.pop()

            # At each iteration, we maintain the smallest elements in mind.
            # Remove any element bigger than A[j]
            while len(mind) and A[j] < mind[-1]: mind.pop()

            # Why do we always add A[j] ?
            # As we will see below, we may have to remove an element(may be A[j-1] if i was j-1) 
            # from the beginning of the maxd/mind.
            # After that, we still need to know the max/min numbers from A[i/i+1]...A[j]
            maxd.append(A[j])
            mind.append(A[j])

            # maxd holds the biggest elements from A[i]...A[j] in decreasing order.
            # So maxd[0] is the biggest element in the window A[i]...A[j]
            # mind holds the smallest elements from A[i]...A[j] in increasing order.
            # So mind[0] is the smallest element in the window A[i]...A[j]
            # maxd[0]-mind[0] is the biggest difference in the window A[i]...A[j]

            # The lazy update using if instead of while is brilliant.
            # Once you reach a new better interval, you just keep the current best 
            # interval between i and j and keep sliding, even when it slides to a 
            # window that failed the limit requirement. Later, when it slides to a 
            # better interval, no pop happens and i won't increase but j will increase 
            # and you get a new better interval. Finally, it slides to the end of the 
            # input vector, and j - i is exactly the answer we need.
            while maxd[0] - mind[0] > limit:
                # The biggest difference is over the limit; so remove A[i] from the window.
                # Why do we check only maxd[0]/mind[0] to remove A[i]?
                # Take maxd as an example. In order for A[i] to be present in maxd, 
                # A[i] >= A[x], where x = i+1...j. In other words, it has to be the biggest element or 
                # it would have already been removed. The biggest element would be in maxd[0]. 
                # Similar explanation applies for mind.
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                # The new window for consideration is A[i+1]...A[j].
                i += 1
            res = max(res, j - i + 1)
        # At every iteration of j, the window size for consideration is from A[i..j]. Its size is j+1-i.
        # At every iteration, an element is added to the window and possibly removed only if the window contains
        # elements with max difference > limit.
        # So the window size only grows monotonically but never shrinks in size. The window grows only if all the elements in
        # the window satisfy the max difference <= limit.
        # Therefore, the last window size in the iteration(when j=len(A)-1) holds the maximum size of the window with max diff <= limit.
        # However, it must be noted that the window in consideration at the last iteration may not really be the window
        # which has the max diff <= limit.
        # This doesn't matter since all we are interested in is the window size and not really the elements in the window.
        return res
        
            

        
if __name__ == "__main__":
    print(Solution().longestSubarray(nums = [8,2,4,7], limit = 4))
    print(Solution().longestSubarray(nums = [10,1,2,4,7,2], limit = 5))
    print(Solution().longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0))
    