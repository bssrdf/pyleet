'''
-Easy-
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 10^6

'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        check = [True]*(n)
        ans = 0
        for i in range(2,n):
            if check[i]:
                ans += 1
                j = 2*i
                while j < n:
                    if check[j]: check[j] = False
                    j += i
            
        #ans = 0
        #for i in check[2:]:
        #    ans += 1 if i else 0
        #print(check)
        return ans   





if __name__ == "__main__":
    print(Solution().countPrimes(10))