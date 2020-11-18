'''
-Medium-

*DFS*
*Symmetric*

Given an Android 3x3 key lock screen and two integers m and n, where 
1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the 
Android lock screen, which consist of minimum of m keys and 
maximum n keys.

 

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes 
through any other keys, the other keys must have previously selected 
in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
 


 

Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been 
selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been 
selected in the pattern.

 

Example:

Input: m = 1, n = 1
Output: 9

'''

class Solution(object):
    def numPatterns(self, m, n):        
        """
        :type m: int
        :type n: int
        :rtype: int

        """        
        visited = [False] * 10
        paths = {(1,3):2, (3,1):2, (1,7):4, (7,1):4,
                 (7,9):8, (9,7):8, (3,9):6, (9,3):6,
                 (1,9):5, (9,1):5, (3,7):5, (7,3):5}
        def dfs(visited, pre, remain):
            if remain < 0: return 0            
            if remain == 0: return 1            
            visited[pre] = True            
            cnt = 0
            for k in range(1,10):
                if visited[k]: continue
                if (pre, k) in paths and not visited[paths[(pre, k)]]:
                    continue                
                cnt += dfs(visited, k, remain-1)                
            visited[pre] = False            
            return cnt
        res = 0
        for i in range(m, n+1):    
            res += dfs(visited, 1, i-1) * 4 # 1,3,7,9 are symmetric
            res += dfs(visited, 2, i-1) * 4 # 2,4,6,8 are symmetric
            res += dfs(visited, 5, i-1) 
        return res



            

if __name__ == "__main__":
    print(Solution().numPatterns(4, 4))