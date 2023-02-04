'''
-Medium-

*Sort*
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
        """
        这道题的关键是排序，排序方法既不是按照数字大小，也不是字典顺序。比如，数字21和2，
        不论是数值大小还是字典顺序，21都应该大于2，但结果却不是212，而应该是221。因此我们
        需要自己写一个排序方法，排序时，为了方便，先将所有数字转化为字符串，对于任意两个
        字符串s1和s2，比较s1+s2与s2+s1，如果前者字典顺序大，我们就将s1放在s2前面，
        反之s2在s1前面。
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