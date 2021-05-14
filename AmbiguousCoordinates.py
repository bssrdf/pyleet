'''
-Medium-

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, 
decimal points, and spaces, and ended up with the string s.  Return a list of strings representing 
all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", 
"0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  
Also, a decimal point within a number never occurs without at least one digit occuring before it, 
so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final 
answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: s = "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
Example 2:
Input: s = "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation: 
0.0, 00, 0001 or 00.01 are not allowed.
Example 3:
Input: s = "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
Example 4:
Input: s = "(100)"
Output: [(10, 0)]
Explanation: 
1.0 is not allowed.
 

Note:

4 <= s.length <= 12.
s[0] = "(", s[s.length - 1] = ")", and the other elements in s are digits.


'''


class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def findAll(S):
            n = len(S)
            if n == 0 or (n > 1 and S[0] == '0' and S[n - 1] == '0'): return []
            if n > 1 and S[0] == '0': return ["0." + S[1:]]
            if S[n - 1] == '0': return [S]
            res = [S]
            for i in range(1, n):
                res.append(S[:i] + "." + S[i:])
            return res
        res = []
        n = len(s)
        for i in range(1, n - 2):
            print(s[1:i+1], s[i+1:n-1])
            A = findAll(s[1:i+1])
            B = findAll(s[i+1:n-1])
            res += ["(" + a + ", " + b + ")" for a in A for b in B]
        return res     

if __name__ == "__main__":
    #print(Solution().ambiguousCoordinates(s = "(123)"))
    print(Solution().ambiguousCoordinates(s = "(00011)"))