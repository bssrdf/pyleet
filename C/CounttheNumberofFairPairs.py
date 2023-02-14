'''

-Medium-
*Sorting*
*Fenwick Tree*
*Two Pointers*


Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109


'''

from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        A = sorted(nums)
        ans, n = 0, len(A)
        bits = [0]*(n+1)
        def update(x):
            while x <= n:
                bits[x] += 1
                x += x & (-x)
        def query(x):
            t = 0
            while x > 0:
                t += bits[x]
                x -= x & (-x)
            return t
        for i in nums:
            idx = bisect.bisect_left(A, i)            
            ans += query(bisect.bisect_right(A, upper-i)) - query(bisect.bisect_left(A, lower-i))  
            update(idx+1)  
        return ans
    
    def countFairPairs2(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        Because nums[i] + nums[j] == nums[j] + nums[i] the i < j condition 
        degrades to i != j.
        
        '''
        A = nums
        A.sort()
        def countLess(val):
            res, j = 0, len(A) - 1
            for i in range(len(A)):
                while i < j and A[i] + A[j] > val:
                    j -= 1
                res += max(0, j-i)
            return res
        return countLess(upper) - countLess(lower-1)




        


if __name__ == '__main__':
    print(Solution().countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
    print(Solution().countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11))
    print(Solution().countFairPairs2(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
    print(Solution().countFairPairs2(nums = [1,7,9,2,5], lower = 11, upper = 11))