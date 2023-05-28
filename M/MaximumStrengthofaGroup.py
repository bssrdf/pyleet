'''

-Medium-
*Recursion*
*Enumeration*



You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].

Return the maximum strength of a group the teacher can create.

 

Example 1:

Input: nums = [3,-1,-5,2,5,-9]
Output: 1350
Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
Example 2:

Input: nums = [-4,-5,-4]
Output: 20
Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.
 

Constraints:

1 <= nums.length <= 13
-9 <= nums[i] <= 9


'''

from typing import List
from math import inf
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        def dfs(i, pro):
            if i == n:
                return pro 
            ret = dfs(i+1, pro)    
            if pro == -inf:
                pro = 1
            ret = max(ret, dfs(i+1, pro*nums[i]))                
            return ret
        return dfs(0, -inf)
     


if __name__ == "__main__":
    print(Solution().maxStrength(nums = [3,-1,-5,2,5,-9]))
    print(Solution().maxStrength(nums = [-4,-5,-4]))
    print(Solution().maxStrength(nums = [0, -1]))