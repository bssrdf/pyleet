'''
-Medium-

Given an array nums of distinct positive integers, return the number of tuples 
(a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, 
and a != b != c != d.

 

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valids tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
Example 3:

Input: nums = [2,3,4,6,8,12]
Output: 40
Example 4:

Input: nums = [2,3,5,7]
Output: 0
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 10^4
All elements in nums are distinct.

'''

from collections import defaultdict
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = defaultdict(int)
        n = len(nums)
        def factorial(k):
            ans = 1
            for i in range(1,k+1):
                ans *= i
            return ans
        for i in range(n):
            for j in range(i+1, n):
                cnt[nums[i]*nums[j]] += 1
        res = 0
        for k,v in cnt.items():
            if v > 1:                
                res += 4 * (factorial(v)//factorial(v-2))
        return res  

        

if __name__ == "__main__":
    print(Solution().tupleSameProduct([2,3,4,6]))
    print(Solution().tupleSameProduct([2,3,4,6,8,12]))