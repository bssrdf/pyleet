'''
Given a list of non negative integers, arrange them such that they form the 
largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of 
an integer.

'''
import functools

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def sorted_by(a,b):
            x, y = a+b, b+a
            if x == y:
                return 0
            elif x > y:
                return -1
            else:
                return 1 
        s = [str(i) for i in nums]                   
        s.sort(key=functools.cmp_to_key(sorted_by))                
        res = ''.join(s)
        return res.lstrip('0') or '0'
        


if __name__ == "__main__":
    print(Solution().largestNumber([34,3,30,5,9]))
    print(Solution().largestNumber([0,0]))