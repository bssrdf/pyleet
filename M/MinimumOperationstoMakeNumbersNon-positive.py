'''

-Hard-
$$$

*Binary Search*

You are given a 0-indexed integer array nums and two integers x and y. In one operation, you must choose an index i such that 0 <= i < nums.length and perform the following:

Decrement nums[i] by x.
Decrement values by y at all indices except the ith one.
Return the minimum number of operations to make all the integers in nums less than or equal to zero.

 

Example 1:

Input: nums = [3,4,1,7,6], x = 4, y = 2
Output: 3
Explanation: You will need three operations. One of the optimal sequence of operations is:
Operation 1: Choose i = 3. Then, nums = [1,2,-1,3,4]. 
Operation 2: Choose i = 3. Then, nums = [-1,0,-3,-1,2].
Operation 3: Choose i = 4. Then, nums = [-3,-2,-5,-3,-2].
Now, all the numbers in nums are non-positive. Therefore, we return 3.
Example 2:

Input: nums = [1,2,1], x = 2, y = 1
Output: 1
Explanation: We can perform the operation once on i = 1. Then, nums becomes [0,0,0]. All the positive numbers are removed, and therefore, we return 1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= y < x <= 109


'''
from typing import List
import math
import bisect
class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        def isPossible(m):
        # Returns True if it's possible to make all nums <= 0 using m operations.

        # If we want m operations, first decrease all the numbers by y * m. Then
        # we have m operations to select indices to decrease them by x - y.
            return sum(max(0, math.ceil((num - y * m) / (x - y)))
                        for num in nums) <= m

        return bisect.bisect_left(range(max(nums)), True,
                                key=isPossible)
    
    def minOperations2(self, nums: List[int], x: int, y: int) -> int:
        def isPossible(m):
        # Returns True if it's possible to make all nums <= 0 using m operations.

        # If we want m operations, first decrease all the numbers by y * m. Then
        # we have m operations to select indices to decrease them by x - y.
            return sum(max(0, math.ceil((num - y * m) / (x - y)))
                        for num in nums) <= m
        left, right = 0, max(nums)
        while left < right:
            mid = left + (right-left)//2 
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
    
if __name__ == "__main__":
    print(Solution().minOperations2(nums = [3,4,1,7,6], x = 4, y = 2))
    print(Solution().minOperations2(nums = [1,2,1], x = 2, y = 1))