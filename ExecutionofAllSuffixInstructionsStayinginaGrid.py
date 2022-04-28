'''
-Medium-
*Simulation*

There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell 
at (n - 1, n - 1). You are given the integer n and an integer array startPos where 
startPos = [startrow, startcol] indicates that a robot is initially at 
cell (startrow, startcol).

You are also given a 0-indexed string s of length m where s[i] is the ith 
instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), 
and 'D' (move down).

The robot can begin executing from any ith instruction in s. It executes the 
instructions one by one towards the end of s but it stops if either of these 
conditions is met:

The next instruction will move the robot off the grid.
There are no more instructions left to execute.
Return an array answer of length m where answer[i] is the number of instructions 
the robot can execute if the robot begins executing from the ith instruction in s.

 

Example 1:


Input: n = 3, startPos = [0,1], s = "RRDDLU"
Output: [1,5,4,3,1,0]
Explanation: Starting from startPos and beginning execution from the ith instruction:
- 0th: "RRDDLU". Only one instruction "R" can be executed before it moves off the grid.
- 1st:  "RDDLU". All five instructions can be executed while it stays in the grid and ends at (1, 1).
- 2nd:   "DDLU". All four instructions can be executed while it stays in the grid and ends at (1, 0).
- 3rd:    "DLU". All three instructions can be executed while it stays in the grid and ends at (0, 0).
- 4th:     "LU". Only one instruction "L" can be executed before it moves off the grid.
- 5th:      "U". If moving up, it would move off the grid.
Example 2:


Input: n = 2, startPos = [1,1], s = "LURD"
Output: [4,1,0,0]
Explanation:
- 0th: "LURD".
- 1st:  "URD".
- 2nd:   "RD".
- 3rd:    "D".
Example 3:


Input: n = 1, startPos = [0,0], s = "LRUD"
Output: [0,0,0,0]
Explanation: No matter which instruction the robot begins execution from, it would move off the grid.
 

Constraints:

m == s.length
1 <= n, m <= 500
startPos.length == 2
0 <= startrow, startcol < n
s consists of 'L', 'R', 'U', and 'D'.


'''

from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        # DP overkills
        m = len(s)
        xs,ys = startPos
        dp = [[[0]*(m+1) for _ in range(n)] for _ in range(n)]        
        for k in range(m-1, -1, -1):
            for i in range(n):
                for j in range(n):
                    if s[k] == 'L':                    
                       ans = 1+dp[i][j-1][k+1] if j > 0 else 0
                    if s[k] == 'R':                    
                       ans = 1+dp[i][j+1][k+1] if j < n-1 else 0
                    if s[k] == 'U':                    
                       ans = 1+dp[i-1][j][k+1] if i > 0 else 0
                    if s[k] == 'D':                    
                       ans = 1+dp[i+1][j][k+1] if i < n-1 else 0
                    dp[i][j][k] = ans
        return [dp[xs][ys][i] for i in range(m)]
    
    def executeInstructions2(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        x, y = startPos
        ans = [0]*m
        for l in range(m):          
            x, y = startPos
            k = l
            while k < m:            
                if s[k] == 'L':                    
                    y -= 1 
                if s[k] == 'R':                    
                    y += 1
                if s[k] == 'U': 
                    x -= 1                   
                if s[k] == 'D':                                        
                    x += 1
                if x < 0 or x >= n or y < 0 or y >= n:
                    break
                k += 1                
            ans[l] = k-l

        return ans


if __name__ == "__main__":
    print(Solution().executeInstructions(n = 3, startPos = [0,1], s = "RRDDLU"))
    print(Solution().executeInstructions2(n = 3, startPos = [0,1], s = "RRDDLU"))
    s = "LULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDLLULLDLUDRDUDLRRDDDUURLLDL"
    print(Solution().executeInstructions2(n = 145, startPos = [139,133], s = s))
