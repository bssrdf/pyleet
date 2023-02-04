'''
-Medium-

Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the 
square of a palindrome.

Given two positive integers left and right represented as strings, return the number of 
super-palindromes integers in the inclusive range [left, right].

 

Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
Example 2:

Input: left = "1", right = "2"
Output: 1
 

Constraints:

1 <= left.length, right.length <= 18
left and right consist of only digits.
left and right cannot have leading zeros.
left and right represent integers in the range [1, 10^18].
left is less than or equal to right.

'''

class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        res = [str(i) for i in range(1,10)]
        for i in range(1,10000):
            s1 = str(i) + str(i)[::-1]
            res.append(s1)
            for j in range(10):
                s2 = str(i)+str(j)+str(i)[::-1]
                res.append(s2)
        res = list(map(int, res))
        res.sort()
        def isValid(s):
            return s == s[::-1]
        ans = 0
        for i in res:
            pal = i*i 
            if isValid(str(pal)) and int(left) <= pal <= int(right) :
                ans += 1
        return ans

        
if __name__ == "__main__":
    print(Solution().superpalindromesInRange(left = "4", right = "1000"))