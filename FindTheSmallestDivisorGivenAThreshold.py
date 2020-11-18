'''
-Medium-
*Binary Search*

Given an array of integers nums and an integer threshold, we will choose a 
positive integer divisor and divide all the array by it and sum the result 
of the division. Find the smallest divisor such that the result mentioned 
above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or 
equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4
 

Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6

'''
import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        mx = 0
        for i in nums:            
            if mx < i: mx = i
        def divsum(denom):
            sm = 0
            for i in nums:
                sm += math.ceil(i/denom)
            return sm
        l, r =  max(1, mx//threshold), mx
        while l <= r:
            m = l + (r-l)//2          
            if divsum(m) <= threshold:
                r = m-1
            else:    
                l = m+1
        return l



            



if __name__ == "__main__":
    #'''
    print(Solution().smallestDivisor([2,3,5,7,11], 11))
    print(Solution().smallestDivisor([1,2,5,9], 6))
    print(Solution().smallestDivisor([9,9,9,9], 6))
    print(Solution().smallestDivisor([19], 5))
    print(Solution().smallestDivisor([1,2,3],1000000))
    #'''
    print(Solution().smallestDivisor([962551,933661,905225,923035,990560], 10))