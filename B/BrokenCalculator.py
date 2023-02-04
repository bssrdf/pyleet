'''
-Medium-
*Greedy*


On a broken calculator that has a number showing on its display, we can 
perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.

Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.

 

Example 1:

Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
Example 2:

Input: X = 5, Y = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.
Example 3:

Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
Example 4:

Input: X = 1024, Y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.
 

Note:

1 <= X <= 10^9
1 <= Y <= 10^9

'''

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        res = 0        
        while Y != X:
            if X >= Y: return X-Y+res
            if Y % 2 == 1:
               Y += 1
            else:                
               Y //= 2
            res += 1
        return res
            
               



if __name__ == "__main__":
    print(Solution().brokenCalc(1024, 1))
    print(Solution().brokenCalc(2, 3))
    print(Solution().brokenCalc(5, 8))
    print(Solution().brokenCalc(3, 10))
    print(Solution().brokenCalc(4, 10))
    print(Solution().brokenCalc(68, 71))