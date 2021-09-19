'''
-Medium-
*Recursion*
*Bit Manipulation*

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every 
subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and 
each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0
Example 2:

Input: n = 2, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01
Example 3:

Input: n = 2, k = 2
Output: 1
Explanation:
row 1: 0
row 2: 01
Example 4:

Input: n = 3, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01
row 3: 0110
 

Constraints:

1 <= n <= 30
1 <= k <= 2^(n - 1)


'''

class Solution(object):
    def kthGrammarTLE(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def helper(i):
            if i == 1: return "0"
            s = helper(i-1)        
            t = ''
            for c in s:
                if c == '0': t +='01'
                else: t += '10'
            print(t)
            return t
        s = helper(n)
        return int(s[k-1])

    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1: return 0
        if n == 2:
            if k == 1: return 0
            if k == 2: return 1     
        d1, d2 = 1 << (n-2), 1 << (n-3)
        if k <= d1:
            return self.kthGrammar(n-1, k)
        elif k <= d1 + d2:
            return self.kthGrammar(n-1, k-d1+d2)     
        else:
            return self.kthGrammar(n-1, k-d1-d2)                    

if __name__ == "__main__":
    print(Solution().kthGrammarTLE(5, 4))
    print(Solution().kthGrammar(5, 4))
    print(Solution().kthGrammar(30, 434991989))