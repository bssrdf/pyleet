'''
-Medium-



You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.

In one move, you can perform either of the following:

If the pile is not empty, remove the topmost element of the pile.
If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.
You are also given an integer k, which denotes the total number of moves to be made.

Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.

 

Example 1:

Input: nums = [5,2,2,4,0,6], k = 4
Output: 5
Explanation:
One of the ways we can end with 5 at the top of the pile after 4 moves is as follows:
- Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6].
- Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6].
- Step 3: Remove the topmost element = 2. The pile becomes [4,0,6].
- Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6].
Note that this is not the only way to end with 5 at the top of the pile. It can be shown that 5 is the largest answer possible after 4 moves.
Example 2:

Input: nums = [2], k = 1
Output: -1
Explanation: 
In the first move, our only option is to pop the topmost element of the pile.
Since it is not possible to obtain a non-empty pile after one move, we return -1.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i], k <= 109


'''

from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        # We initialize variable (maxi) which keeps track of the maximum topmost element.
        # If k > len(array), then we can traverse the entire array once and find 
        # the maximum element of the array.
        # Example: arr = [5,2,2,4,0,6], k = 40 ==> ans = 6

        # If k == len(array), then we need to traverse upto the k-1th element and 
        # find the maximum element. We use only k-1 steps as the last step 
        # would be required to add the maximum element back at the top.
        # Example: arr = [5,2,2,4,0,6], k = 6 ==> ans = 5

        # If k < len(array), then we can traverse upto the k-1th element of the 
        # array and find the maximum element. In this case there is also a 
        # possibility that the kth element will be greater than the maximum element 
        # that we have found, so we do a check to see which is greater 
        # (We will be removing first k elements from the array if the kth element is greater).
        # Example: arr = [5,2,2,4,0,6], k = 5 ==> ans = 6

        # If the len(array) is 1 and k is odd, then we will not be able to find an answer.
        
        if (len(nums) == 1) and (k & 1): return -1
        
        maxi = -1
        for i in range(min(len(nums), k-1)):
            maxi = max(maxi, nums[i])
        
        if k < len(nums):
            maxi = max(maxi, nums[k])
            
        return maxi
        