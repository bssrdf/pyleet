'''

-Medium-

Given an array of integers nums and a positive integer k, find whether it is 
possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
 

Constraints:

1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^9
 


'''
from typing import List
from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n, m = len(nums), Counter(nums)
        if n % k != 0: return False
        for a in sorted(m.keys()):
            while a in m:
                for i in range(a, a+k):
                    if i not in m:
                        return False 
                    m[i] -= 1
                    if m[i] == 0:
                        m.pop(i)
        return True

        
if __name__ == "__main__":
    print(Solution().isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4))
    print(Solution().isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))
    print(Solution().isPossibleDivide(nums = [3,3,2,2,1,1], k = 3))
    print(Solution().isPossibleDivide(nums = [1,2,3,4], k = 3))