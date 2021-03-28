'''
-Easy-

Given an integer columnNumber, return its corresponding column title as 
it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
Example 4:

Input: columnNumber = 2147483647
Output: "FXSHRXW"
 

Constraints:

1 <= columnNumber <= 2^31 - 1



'''
import string

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        n = columnNumber
        m = {x:y for x,y in zip(range(1,27), string.ascii_uppercase)}
        res = ''
        while n != 0:
            rem = n % 26 
            res += m[rem] if rem != 0 else 'Z'
            n = (n-1) // 26   
        return res[::-1]



if __name__ == "__main__":
    print(Solution().convertToTitle(701))
    print(Solution().convertToTitle(2147483647))