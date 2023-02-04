'''
-Hard-
*Sliding Window*

You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously 
changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in 
the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
 

Constraints:

1 <= nums.length <= 105
1 <= k <= nums.length


'''



from typing import List
from collections import deque


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        A, K = nums, k
        cur = res = 0
        for i in range(len(A)):
            if i >= K and A[i - K] == 2:
                cur -= 1
            if (cur % 2) == A[i]:
                if i + K > len(A):
                    return -1
                A[i] = 2
                cur, res = cur + 1, res + 1
        return res




    def minKBitFlips2(self, nums: List[int], k: int) -> int:
        flips = deque()
        res = 0
        for i in range(len(nums)):
            # The size of the queue will indicate number of flips
            if nums[i] != (0 if len(flips)%2 else 1):
                res += 1
                flips.append(i+k-1)
            if flips and flips[0] <= i:
                flips.popleft()
        return res if not flips else -1



        
if __name__ == "__main__":
    print(Solution().minKBitFlips(nums = [0,1,0], k = 1))
    print(Solution().minKBitFlips(nums = [0,0,0,1,0,1,1,0], k = 3))