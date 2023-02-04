'''
-Medium-

Your task is to calculate ab mod 1337 where a is a positive integer and b 
is an extremely large positive integer given in the form of an array.

 

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
Example 3:

Input: a = 1, b = [4,3,3,8,5,2]
Output: 1
Example 4:

Input: a = 2147483647, b = [2,0,0]
Output: 1198
 

Constraints:

1 <= a <= 2^31 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b doesn't contain leading zeros.


'''

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def pow(x, n):
            if n == 0: return 1
            if n == 1: return x % 1337
            return pow(x % 1337, n // 2) * pow(x % 1337, n - n // 2) % 1337
        res = 1
        for i in b:
            res = pow(res, 10) * pow(a, i) % 1337
        return res


if __name__ == '__main__':
    print(Solution().superPow(a = 2, b = [1,0]))

