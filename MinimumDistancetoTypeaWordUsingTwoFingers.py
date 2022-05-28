'''

-Hard-
*DP*

You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
Given the string word, return the minimum total distance to type such string using only two fingers.

The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

 

Example 1:

Input: word = "CAKE"
Output: 3
Explanation: Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3
Example 2:

Input: word = "HAPPY"
Output: 6
Explanation: Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -> cost = 0
Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -> cost = 0
Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6
 

Constraints:

2 <= word.length <= 300
word consists of uppercase English letters.

'''

class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(s, t):
            if s == 26: return 0
            y = s // 6
            x = s % 6
            y2 = t // 6
            x2 = t % 6
            return abs(y2-y) + abs(x2-x)
        n = len(word)
        dp = [[[0]*27 for _ in range(27)] for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(27):
                for k in range(27):
                    d1 = dist(j, ord(word[i])-ord('A'))
                    d2 = dist(k, ord(word[i])-ord('A'))
                    dp[i][j][k] = min(dp[i+1][ord(word[i])-ord('A')][k]+d1,
                                      dp[i+1][j][ord(word[i])-ord('A')]+d2)
        return dp[0][26][26]
    
    def minimumDistance2(self, word: str) -> int:
        def dist(s, t):
            if s == 26: return 0
            y = s // 6
            x = s % 6
            y2 = t // 6
            x2 = t % 6
            return abs(y2-y) + abs(x2-x)
        n = len(word)
        dp = [[[0]*27 for _ in range(27)] for _ in range(2)]
        for i in range(n-1, -1, -1):
            l = ord(word[i])-ord('A')
            for j in range(27):
                for k in range(27):
                    d1 = dist(j, l)
                    d2 = dist(k, l)
                    dp[i%2][j][k] = min(dp[(i+1)%2][l][k]+d1,
                                        dp[(i+1)%2][j][l]+d2)
        return dp[0][26][26]

    def minimumDistance2(self, word: str) -> int:
        def dist(s, t):
            if s == 26: return 0
            y, x = divmod(s, 6)
            y2, x2 = divmod(t, 6)
            return abs(y2-y) + abs(x2-x)
        n = len(word)
        dis = [[0]*27 for _ in range(27)]
        for j in range(27):
            for k in range(27):
                dis[j][k] = dist(j, k)                    

        dp = [[[0]*27 for _ in range(27)] for _ in range(2)]
        for i in range(n-1, -1, -1):
            l = ord(word[i])-ord('A')
            for j in range(27):
                for k in range(27):
                    d1 = dis[j][l]
                    d2 = dis[k][l]
                    dp[i%2][j][k] = min(dp[(i+1)%2][l][k]+d1,
                                        dp[(i+1)%2][j][l]+d2)
        return dp[0][26][26]


        