'''
-Medium-
*DFS*
*DP*

You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.

 

Example 1:


Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
Output: true
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.
Example 2:


Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
Output: false
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.
 

Constraints:

2 <= bottom.length <= 6
0 <= allowed.length <= 216
allowed[i].length == 3
The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
All the values of allowed are unique.


'''
from typing import List
from functools import lru_cache

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed = set(allowed)
        letters = 'ABCDEF'
        n = len(bottom)
        @lru_cache(None)
        def dfs(i, j, currow, lastrow):
            if i == 1:
                for l in letters:
                    if lastrow+l in allowed:
                        return True
                return False
            if j == i:                
                return dfs(i-1, 0, '', currow)
            for l in letters:
                if lastrow[j:j+2]+l in allowed:
                    if dfs(i, j+1, currow+l, lastrow):
                        return True
            return False
        return dfs(n-1, 0, '', bottom)






if __name__ == "__main__":
    print(Solution().pyramidTransition(bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]))
    print(Solution().pyramidTransition(bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]))
    allowed = ["ADA","ADC","ADB","AEA","AEC","AEB","AFA","AFC","AFB","CDA","CDC","CDB","CEA","CEC","CEB","CFA","CFC","CFB","BDA","BDC","BDB","BEA","BEC","BEB","BFA","BFC","BFB","DAA","DAC","DAB","DCA","DCC","DCB","DBA","DBC","DBB","EAA","EAC","EAB","ECA","ECC","ECB","EBA","EBC","EBB","FAA","FAC","FAB","FCA","FCC","FCB","FBA","FBC","FBB","DDA","DDC","DDB","DEA","DEC","DEB","DFA","DFC","DFB","EDA","EDC","EDB","EEA","EEC","EEB","EFA","EFC","EFB","FDA","FDC","FDB","FEA","FEC","FEB","FFA","FFC","FFB","DDD","DDE","DDF","DED","DEE","DEF","DFD","DFE","DFF","EDD","EDE","EDF","EED","EEE","EEF","EFD","EFE","EFF","FDD","FDE","FDF","FED","FEE","FEF","FFD","FFE","FFF"]
    print(Solution().pyramidTransition(bottom = "AFFFFA", allowed = allowed))
        