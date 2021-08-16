
'''
-Hard-


Given an integer d between 0 and 9, and two positive integers low and high as lower and 
upper bounds, respectively. Return the number of times that d occurs as a digit in all 
integers between low and high, including the bounds low and high.
 

Example 1:

Input: d = 1, low = 1, high = 13
Output: 6
Explanation: 
The digit 
d=1
 occurs 
6
 times in 
1,10,11,12,13
. Note that the digit 
d=1
 occurs twice in the number 
11
.
Example 2:

Input: d = 3, low = 100, high = 250
Output: 35
Explanation: 
The digit 
d=3
 occurs 
35
 times in 
103,113,123,130,131,...,238,239,243
.
 

Note:

0 <= d <= 9
1 <= low <= high <= 2×10^8
Hints
Define a function f(x) to get the requested sum from 1 to x. So the answer will be f(hi) - f(lo - 1)
In order to solve f(x) we need to do a DP over digits approach.

'''

class Solution(object):
       
    def countDigits(self, d, number):
        count = 0
        multiplier = 1
        n = 0
        
        while number > 0:
            # for each loop count all digits for the rightmost digit
            right_digit = number % 10
            number = number // 10

            # Add all extra for leftmost digit
            if (right_digit > d):
                count += (1+number - (d==0))*multiplier
            elif right_digit == d:
                count += (number - (d==0))*multiplier+n+1
            else:
                count += (number - (d==0))*multiplier
            n += right_digit * multiplier
            multiplier = multiplier * 10
            
        return count
        
    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        return self.countDigits(d, high) - self.countDigits(d, low-1)

if __name__ == "__main__":
    print(Solution().digitsCount(d = 3, low = 100, high = 250))