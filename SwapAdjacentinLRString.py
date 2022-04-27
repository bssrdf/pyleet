'''
-Medium-


In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", 
a move consists of either replacing one occurrence of "XL" with "LX", or 
replacing one occurrence of "RX" with "XR". Given the starting string start 
and the ending string end, return True if and only if there exists a 
sequence of moves to transform one string to the other.

 

Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false
 

Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.

'''

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # Wrong solution
        S, E, n = start, end, len(start)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            if i > 1:
                if S[i-2:i] == 'XL' and E[i-2:i] == 'LX':
                    if dp[i-2]: dp[i] = True
                if S[i-2:i] == 'RX' and E[i-2:i] == 'XR':
                    if dp[i-2]: dp[i] = True
            if S[i-1] == E[i-1]: 
                if dp[i-1]: dp[i] = True
        # print(dp)
        return dp[n]        

    def canTransform2(self, start: str, end: str) -> bool:
        if len(start) != len(end): return False
        
        # check L R orders are the same
        if start.replace('X','') != end.replace('X', ''): return False
        
        n = len(start)
        Lstart = [i for i in range(n) if start[i] == 'L']
        Lend = [i for i in range(n) if end[i] == 'L']
        
        Rstart = [i for i in range(n) if start[i] == 'R']
        Rend = [i for i in range(n) if end[i] == 'R']
		# check L positions are correct
        for i, j in zip(Lstart, Lend):
            if i < j:
                return False
            
        # check R positions are correct
        for i, j in zip(Rstart, Rend):
            if i > j:
                return False
            
        return True
                



if __name__ == "__main__":
    print(Solution().canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))
    print(Solution().canTransform(start = "X", end = "L"))
    print(Solution().canTransform(start ="XXXLXXXXXX", end= "XXXLXXXXXX"))
    print(Solution().canTransform(start ="XXXXXLXXXX", end= "LXXXXXXXXX"))
        