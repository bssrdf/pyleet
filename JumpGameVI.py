'''
-Medium-
*Monotonic Queue"

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps 
forward without going outside the boundaries of the array. That is, you can jump 
from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the 
sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

 

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
 

Constraints:

 1 <= nums.length, k <= 10^5
-10^4 <= nums[i] <= 10^4
   
'''

'''
Let dp[i] be "the maximum score to reach the end starting at index i". The answer 
for dp[i] is nums[i] + min{dp[i+j]} for 1 <= j <= k. That gives an O(n*k) solution.

Instead of checking every j for every i, keep track of the smallest dp[i] values 
in a heap and calculate dp[i] from right to left. When the smallest value in the 
heap is out of bounds of the current index, remove it and keep checking.


'''
import heapq
from collections import deque

class Solution(object):
    def maxResultTLE(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # run time is O(n*k)
        n = len(nums)
        dp = [0] * n
        dp[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            mn = -float('inf')
            for j in range(1, min(k+1, n-i)):
                #print(i, j, nums[i], dp[j+i])
                mn = max(mn, dp[j+i])
            dp[i] = nums[i] + mn
           # print(dp)
        return dp[0]

    def maxResultNLogk(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # run time is O(n*log(k))
        n = len(nums)
        ans = nums[n-1]
        pq = [(-nums[n-1], n-1)]
        for i in range(n-2, -1, -1):
            while pq and pq[0][1]-i > k:
                heapq.heappop(pq) 
            ans = nums[i] - pq[0][0]
            heapq.heappush(pq,(-ans,i))
        return ans

    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # run time is O(n)
        # Monotonic Queue
        n = len(nums)
        score = nums[n-1]
        q = deque([(score,n-1)]) 
        for i in range(n-2, -1, -1):
            while q and q[0][1]-i > k:
                q.popleft()
            score = nums[i] + q[0][0] if q else 0
            while q and q[-1][0] < score:
                q.pop()
            q.append((score,i))
        return score 


if __name__ == "__main__":
    print(Solution().maxResult(nums = [1,-1,-2,4,-7,3], k = 2))     
    print(Solution().maxResult(nums = [10,-5,-2,4,0,3], k = 3))  