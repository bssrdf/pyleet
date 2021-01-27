'''
-Medium-

Given an integer n, return the decimal value of the binary string formed by concatenating 
the binary representations of 1 to n in order, modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
 

Constraints:

1 <= n <= 10^5

'''

class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        One way to solve this problem in competition is just create very long binary string 
        and then find result of division by 10**9 + 7 and it will work fine. However in 
        interview setup it is not the best idea and I prefer more honest way. Let us look 
        at first several n to see how it works:
        1
        110
        11011
        11011100

        Let us try to find answer to n, using information about n-1. 110 = 1 * 100 + 10 
        (all in binary representation), 11011 = 110 * 100 + 11, 11011100 = 11011 * 1000 + 100 
        and so on. We can see that on each step we need to multiply number by lenght of 
        new number and add new number (and use %M) and that is all!

        Complexity: time complexity is O(n), space is O(1).
        """
        ans, M = 0, 10**9 + 7
        for x in range(1,n+1):
            #print(ans, (1 << (len(bin(x)) - 2)), len(bin(x)), x)
            ans = (ans * (1 << (len(bin(x)) - 2)) + x) % M
        return ans        
                  

if __name__ == "__main__":   
    print(Solution().concatenatedBinary(4))