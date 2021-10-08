'''

-Medium-

You are given an integer array nums and two integers limit and goal. The array nums has an 
interesting property that abs(nums[i]) <= limit.

Return the minimum number of elements you need to add to make the sum of the array equal to 
goal. The array must maintain its property that abs(nums[i]) <= limit.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: nums = [1,-1,1], limit = 3, goal = -4
Output: 2
Explanation: You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.
Example 2:

Input: nums = [1,-10,9,1], limit = 100, goal = 0
Output: 1
 

Constraints:

1 <= nums.length <= 10^5
1 <= limit <= 10^6
-limit <= nums[i] <= limit
-10^9 <= goal <= 10^9

'''

from typing import List

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = goal - sum(nums) 
        #if diff == 0: return 0
        #elif diff > 0: return diff // limit + (1 if diff % limit != 0 else 0)
        #else:  return (-diff) // limit + (1 if (-diff) % limit != 0 else 0)
        return (abs(diff)+limit-1) // limit
            
        
if __name__ == "__main__":
    print(Solution().minElements([1,-1,1], 3, -4))
    print(Solution().minElements([1,-10,9,1], 100, 0))