'''
-Medium-

You are given an integer array nums. In one move, you can choose one element of 
nums and change it by any value.

Return the minimum difference between the largest and smallest value of nums 
after performing at most three moves.

 

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

'''

from typing import List

import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # We have 4 plans:

        # kill 3 biggest elements
        # kill 2 biggest elements + 1 smallest elements
        # kill 1 biggest elements + 2 smallest elements
        # kill 3 smallest elements

        # Example from @himanshusingh11:

        # A = [1,5,6,13,14,15,16,17]
        # n = 8

        # Case 1: kill 3 biggest elements

        # All three biggest elements can be replaced with 14
        # [1,5,6,13,14,15,16,17] -> [1,5,6,13,14,14,14,14] == can be written as A[n-4] - A[0] == (14-1 = 13)

        # Case 2: kill 2 biggest elements + 1 smallest elements

        # [1,5,6,13,14,15,16,17] -> [5,5,6,13,14,15,15,15] == can be written as A[n-3] - A[1] == (15-5 = 10)

        # Case 3: kill 1 biggest elements + 2 smallest elements

        # [1,5,6,13,14,15,16,17] -> [6,6,6,13,14,15,16,16] == can be written as A[n-2] - A[2] == (16-6 = 10)

        # Case 4: kill 3 smallest elements

        # [1,5,6,13,14,15,16,17] -> [13,13,13,13,14,15,16,17] == can be written as A[n-1] - A[3] == (17-13 = 4)

        # Answer is minimum of all these cases!
        A = nums
        A.sort()
        return min(b - a for a, b in zip(A[:4], A[-4:]))
    
    def minDifference2(self, nums: List[int]) -> int:
        A = nums
        return min(a - b for a,b in zip(heapq.nlargest(4, A), heapq.nsmallest(4, A)[::-1]))

if __name__ == "__main__":
    print(Solution().minDifference([1,5,0,10,14]))
        