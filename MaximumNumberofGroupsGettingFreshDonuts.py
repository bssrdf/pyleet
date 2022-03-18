'''

-Hard-
*DP*
*Bitmask*
*Greedy*


There is a donuts shop that bakes donuts in batches of batchSize. They have a rule 
where they must serve all of the donuts of a batch before serving any donuts of 
the next batch. You are given an integer batchSize and an integer array groups, 
where groups[i] denotes that there is a group of groups[i] customers that will 
visit the shop. Each customer will get exactly one donut.

When a group visits the shop, all customers of the group must be served before 
serving any of the following groups. A group will be happy if they all get fresh 
donuts. That is, the first customer of the group does not receive a donut that was 
left over from the previous group.

You can freely rearrange the ordering of the groups. Return the maximum possible 
number of happy groups after rearranging the groups.

 

Example 1:

Input: batchSize = 3, groups = [1,2,3,4,5,6]
Output: 4
Explanation: You can arrange the groups as [6,2,4,5,1,3]. Then the 1st, 2nd, 4th, and 6th groups will be happy.
Example 2:

Input: batchSize = 4, groups = [1,3,2,5,2,2,1,6]
Output: 4
 

Constraints:

1 <= batchSize <= 9
1 <= groups.length <= 30
1 <= groups[i] <= 10^9


'''

from typing import List
from functools import lru_cache
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        B = batchSize
        ans = sum(g%B == 0 for g in groups)
        groups = [g for g in groups if g%B != 0]

        pos = [0]*B
        for g in groups: pos[g%B] += 1

        for i in range(1, B):
            t = min(pos[i], pos[B-i]) if 2*i != B else pos[i]//2
            ans += t
            pos[i] -= t
            pos[B-i] -= t
            
        if sum(pos) == 0: return ans

        @lru_cache(None)
        def dfs(position, last):
            if sum(position) == 0: return 0

            ans = float("-inf")
            for i in range(B):
                if position[i] > 0:
                    t = list(position)
                    t[i] -= 1
                    U = (last - i) % B
                    ans = max(ans, dfs(tuple(t), U) + (U == 0))
                      
            return ans

        return max(dfs(tuple(pos), i) for i in range(1, B)) + ans
        

    def maxHappyGroups2(self, batchSize: int, groups: List[int]) -> int:
        n = len(groups)
        allmask = 1 << n
        ans = [0]
        @lru_cache(None)
        def dp(idx, mask, happy, rem):
            #if idx == n:
            #if len(grp) == 6:
            #    print(bin(mask), grp, happy)
            #if mask == allmask:
            ans[0] = max(ans[0], happy)
                #return
            for i in range(idx, n):
                if mask & (1 << i) > 0: continue
                #if mask == int('1011',base=2):
                #    print('X', happy, rem, bin(mask), grp)
                newmask = mask | (1 << i)
                if rem == 0:
                    newrem = groups[i] % batchSize if groups[i] > batchSize else (batchSize - groups[i])                        
                   # if mask == int('1011',base=2):
                   #     print('A', happy, rem, bin(newmask), grp)
                    dp(i+1, newmask, happy+1, newrem)
                else:
                    num = groups[i] - rem
                    if num > 0 :
                        newrem = num % batchSize if num > batchSize else (batchSize - num)                        
                    else:
                        newrem = rem - groups[i]    
                    #if mask == int('1011',base=2):
                    #    print('B', happy, rem, bin(newmask), grp)
                    dp(i+1, newmask, happy, newrem)
                #grp.pop()
        for i in range(n):
           dp(i, 0, 0, 0)
        return ans[0]
        

    

if __name__ == "__main__":
    print(Solution().maxHappyGroups(batchSize = 3, groups = [1,2,3,4,5,6]))
    print(Solution().maxHappyGroups2(batchSize = 3, groups = [1,2,3,4,5,6]))
    print(Solution().maxHappyGroups(batchSize = 4, groups = [1,3,2,5,2,2,1,6]))
    print(Solution().maxHappyGroups2(batchSize = 4, groups = [1,3,2,5,2,2,1,6]))

    print(Solution().maxHappyGroups(1, [909925048,861425549,820096754,67760437,
    273878288,126614243,531969375,817077202,482637353,507069465,699642631,407608742,
    846885254,225437260,100780964,523832097,30437867,959191866,897395949]))
    print(Solution().maxHappyGroups2(1, [909925048,861425549,820096754,67760437,
    273878288,126614243,531969375,817077202,482637353,507069465,699642631,407608742,
    846885254,225437260,100780964,523832097,30437867,959191866,897395949]))
