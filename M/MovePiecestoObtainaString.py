'''
-Medium-

You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

 

Example 1:

Input: start = "_L__R__R_", target = "L______RR"
Output: true
Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.
Example 2:

Input: start = "R_L_", target = "__LR"
Output: false
Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
Example 3:

Input: start = "_R", target = "R_"
Output: false
Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.
 

Constraints:

n == start.length == target.length
1 <= n <= 105
start and target consist of the characters 'L', 'R', and '_'.


'''


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        S, T = start, target
        i = j = 0
        while i < len(S) and j < len(T):
            while i < len(S) and S[i] == '_':
                i += 1
            while j < len(T) and T[j] == '_':
                j += 1
            if S[i] != T[j]:
                return False
            i += 1
            j += 1
        return True    
    
    def canChange2(self, start: str, target: str) -> bool:
        S, T = start, target
        i = j = 0
        while i < len(S) or j < len(T):
            while i < len(S) and S[i] == '_':
                i += 1
            while j < len(T) and T[j] == '_':
                j += 1
            if i == len(S) or j == len(T):
                return i == len(S) and j == len(T)
            if S[i] != T[j]:
                return False
            if T[j] == 'L':
                if i < j: return False 
            else:
                if i > j: return False
            i += 1
            j += 1
        return True    
            

        
    
if __name__ == "__main__":
    print(Solution().canChange(start = "_L__R__R_", target = "L______RR"))