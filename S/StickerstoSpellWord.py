'''
-Hard-

*DP*

We are given n different types of stickers. Each sticker has a lowercase 
English word on it.

You would like to spell out the given string target by cutting individual 
letters from your collection of stickers and rearranging them. You can use 
each sticker more than once if you want, and you have infinite quantities 
of each sticker.

Return the minimum number of stickers that you need to spell out target. 
If the task is impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most 
common US English words, and target was chosen as a concatenation of two 
random words.

 

Example 1:

Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.
 

Constraints:

n == stickers.length
1 <= n <= 50
1 <= stickers[i].length <= 10
1 <= target <= 15
stickers[i] and target consist of lowercase English letters.

'''

from typing import List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers.sort(key = lambda x:len(x),reverse = True)
        targetLength = len(target)
        dp = [-1]*(1 << targetLength)
        dp[0] = 0
        for sticker in stickers:
            for state in range(1 << targetLength):
                if dp[state] >= 0:
                    curState = state
                    for i in range(len(sticker)):
                        for j in range(targetLength):
                            if sticker[i] == target[j] and curState & (1 << j) == 0:
                                curState |= 1 << j
                                break
                    if dp[curState] == -1:
                        dp[curState] = dp[state] + 1
                    else:
                        dp[curState] = min(dp[curState], dp[state] + 1)
        return dp[(1 << targetLength) - 1]
    

    def minStickers2(self, stickers: List[str], target: str) -> int:
        m = len(stickers)
        mp = [[0]*26 for y in range(m)] 
        for i in range(m):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1    
        dp = {}
        dp[""] = 0
        
        def helper(dp, mp, target):
            if target in dp:
                return dp[target]
            tar = [0]*26
            for c in target:
                tar[ord(c)-ord('a')] += 1   
            ans = float('inf')
            for i in range(m):
                if mp[i][ord(target[0])-ord('a')] == 0:
                    continue
                s = ''
                for j in range(26):
                    if tar[j] > mp[i][j]:
                        s += chr(ord('a')+j)*(tar[j] - mp[i][j]) 
                tmp = helper(dp, mp, s)
                if tmp != -1: 
                    ans = min(ans, 1+tmp)    
            dp[target] = -1 if ans == float('inf') else ans
            return dp[target]
                
        return helper(dp, mp, target)
    
        

if __name__ == '__main__':
    print(Solution().minStickers(stickers = ["with","example","science"], target = "thehat"))
    print(Solution().minStickers2(stickers = ["with","example","science"], target = "thehat"))