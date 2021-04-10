'''
-Medium-

You are playing the following Flip Game with your friend: Given a string that contains only 
these two characters: + and -, you and your friend take turns to flip two consecutive "++" 
into "--". The game ends when a person can no longer make a move and therefore the other 
person will be the winner.

Write a function to determine if the starting player can guarantee a win.

样例
Example1

Input:  s = "++++"
Output: true
Explanation:
The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Example2

Input: s = "+++++"
Output: false 
Explanation:
The starting player can not win 
"+++--" --> "+----"
"++--+" --> "----+"
挑战
Derive your algorithm's runtime complexity.

'''

class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    def canWin(self, s):
        # write your code here
        def dfs(s, player):
            if player == 0:
                for i in range(len(s)-1):
                    if s[i] == '+' and s[i+1] == '+':
                        t = s[:i]+'--'+s[i+2:]
                        if dfs(t, abs(player-1)):
                            return True
                return False
            else:
                for i in range(len(s)-1):
                    if s[i] == '+' and s[i+1] == '+':
                        t = s[:i]+'--'+s[i+2:]
                        if not dfs(t, abs(player-1)):
                            return False
                return True
        return dfs(s, 0)



if __name__ == "__main__":
    print(Solution().canWin("++++"))
    print(Solution().canWin("+++++"))