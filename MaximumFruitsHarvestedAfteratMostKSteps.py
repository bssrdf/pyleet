'''
-Hard-

Fruits are available at some positions on an infinite x-axis. You are given 
a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts 
amounti fruits at the position positioni. fruits is already sorted by 
positioni in ascending order, and each positioni is unique.

You are also given an integer startPos and an integer k. Initially, you are 
at the position startPos. From any position, you can either walk to the left 
or right. It takes one step to move one unit on the x-axis, and you can 
walk at most k steps in total. For every position you reach, you harvest 
all the fruits at that position, and the fruits will disappear from that position.

Return the maximum total number of fruits you can harvest.

 

Example 1:


Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
Output: 9
Explanation: 
The optimal way is to:
- Move right to position 6 and harvest 3 fruits
- Move right to position 8 and harvest 6 fruits
You moved 3 steps and harvested 3 + 6 = 9 fruits in total.
Example 2:


Input: fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
Output: 14
Explanation: 
You can move at most k = 4 steps, so you cannot reach position 0 nor 10.
The optimal way is to:
- Harvest the 7 fruits at the starting position 5
- Move left to position 4 and harvest 1 fruit
- Move right to position 6 and harvest 2 fruits
- Move right to position 7 and harvest 4 fruits
You moved 1 + 3 = 4 steps and harvested 7 + 1 + 2 + 4 = 14 fruits in total.
Example 3:


Input: fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
Output: 0
Explanation:
You can move at most k = 2 steps and cannot reach any position with fruits.
 

Constraints:

1 <= fruits.length <= 105
fruits[i].length == 2
0 <= startPos, positioni <= 2 * 105
positioni-1 < positioni for any i > 0 (0-indexed)
1 <= amounti <= 104
0 <= k <= 2 * 105


'''

from typing import List
import bisect

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # 
        fpos = {}
        for p, a in fruits:
            fpos[p] = a
        dp = [[0]*(k+1) for _ in range(2)]
        pos = [startPos, startPos]
        if startPos in fpos:
           dp[0][0] = fpos[startPos]
        ans = 0
        for i in range(1, k+1):
            pos[0] -= 1
            pos[1] += 1          
            dp[0][i] = (dp[0][i-1] + fpos[pos[0]]) if pos[0] in fpos else dp[0][i-1] 
            dp[1][i] = (dp[1][i-1] + fpos[pos[1]]) if pos[1] in fpos else dp[1][i-1]
        # print(dp[0])
        # print(dp[1])
        for i in range(k+1):
            j = k - 2 * i
            ans = max(ans, dp[0][i] + dp[1][j] if j >= 0 else 0)
            ans = max(ans, dp[1][i] + dp[0][j] if j >= 0 else 0)
            # print(i, k-2*i, dp[0][i], dp[1][k-2*i], dp[1][i], dp[0][k-2*i])
        return ans 
    
    def maxTotalFruits2(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        preSum = [0]
        pos = []
        ans = 0
        for p, a in fruits:
            pos.append(p)
            preSum.append(preSum[-1]+a)        
        idx2 = bisect.bisect_right(pos, startPos)
        # print('idx2:', idx2)
        for i in range(k+1):
            newp = startPos - i
            idx1 = bisect.bisect_left(pos, newp) 
            # print('l', idx1, idx2, newp)           
            left = preSum[idx2] - preSum[idx1] 
            right = 0
            if k-2*i >= 0:
                newp = startPos + (k-2*i)
                idx1 = bisect.bisect_right(pos, newp)            
                # print(idx1, idx2, k, i, newp) 
                right = preSum[idx1] - preSum[idx2] 
            
            ans = max(ans, left + right)
            # print('l,r', i, left, right, ans)
        for i in range(k+1):
            newp = startPos + i
            idx1 = bisect.bisect_right(pos, newp) 
            right = preSum[idx1] - preSum[idx2] 
            left = 0
            if k-2*i >= 0:
                newp = startPos - (k-2*i)
                idx1 = bisect.bisect_left(pos, newp)            
                left = preSum[idx2] - preSum[idx1] 
            ans = max(ans, left + right)
        return ans 
    
    def maxTotalFruits3(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        preSum = [0]
        pos = []
        ans = 0
        for p, a in fruits:
            pos.append(p)
            preSum.append(preSum[-1]+a)        
        idx2 = bisect.bisect_right(pos, startPos)
        for i in range(idx2-1, -1, -1):
            newp = pos[i]
            d = startPos - newp
            if d <= k:
                idx1 = bisect.bisect_left(pos, newp) 
                left = preSum[idx2] - preSum[idx1] 
                right = 0
                if k - 2*d >= 0:
                    newp = startPos + (k-2*d)
                    idx1 = bisect.bisect_right(pos, newp)            
                    right = preSum[idx1] - preSum[idx2] 
                ans = max(ans, left + right)
        for i in range(idx2, len(pos)):
            newp = pos[i]
            d = pos[i] - startPos
            if d <= k:
                idx1 = bisect.bisect_right(pos, newp) 
                right = preSum[idx1] - preSum[idx2] 
                left = 0
                if k-2*d >= 0:
                    newp = startPos - (k-2*d)
                    idx1 = bisect.bisect_left(pos, newp)            
                    left = preSum[idx2] - preSum[idx1] 
                ans = max(ans, left + right)
        return ans 
        

    
    def maxTotalFruits4(self, A: List[List[int]], pos: int, k: int) -> int:
        amt = {}
        for a, b in A:
            amt[a] = b
            
        # Every position with fruit except the start position.
        position = [a for a, b in A if a != pos]
        lft, rgt, n = [], [], len(position)
      
        idx = bisect.bisect_right(position, pos)
        
        # Right pre-sum
        cur_f = 0
        for i in range(idx, n):
            cur_pos = position[i]
            cur_f += amt[cur_pos]
            rgt.append([cur_pos - pos, cur_f])
        
        # Left pre-sum
        cur_f = 0
        for i in range(idx - 1, -1, -1):
            cur_pos = position[i]
            cur_f += amt[cur_pos]
            lft.append([pos - cur_pos, cur_f])
        
        # Go right then turn left
        ans = 0
        for r_dist, r_f in rgt:
            if r_dist <= k:
                cur_f = r_f
                l_dist = k - 2 * r_dist
                if l_dist > 0:             # Check fruit collected from the left side.
                    idx = bisect.bisect_right(lft, [l_dist, float('inf')])
                    if idx > 0:
                        cur_f += lft[idx - 1][1]
                ans = max(ans, cur_f)
        
        # Go left then turn right
        for l_dist, l_f in lft:
            if l_dist <= k:
                cur_f = l_f
                r_dist = k - 2 * l_dist
                if r_dist > 0:             # Check fruit collected from the right side.
                    idx = bisect.bisect_right(rgt, [r_dist, float('inf')])
                    if idx > 0:
                        cur_f += rgt[idx - 1][1]
                ans = max(ans, cur_f)

        return ans + amt.get(pos, 0)       # Add fruit collected at the start position.


        
if __name__ == "__main__":
    # print(Solution().maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4))
    # print(Solution().maxTotalFruits(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4))
    # print(Solution().maxTotalFruits(fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2))
    # print(Solution().maxTotalFruits(fruits = [[200000,10000]], startPos = 200000, k=0))

    # print(Solution().maxTotalFruits([[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]],
    #     21,30))

    print(Solution().maxTotalFruits3(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4))
    print(Solution().maxTotalFruits3(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4))
    print(Solution().maxTotalFruits3(fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2))
    print(Solution().maxTotalFruits3(fruits = [[200000,10000]], startPos = 200000, k=0))

    print(Solution().maxTotalFruits3([[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]],
        21,30))


    # print(Solution().maxTotalFruits2(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4))
    # print(Solution().maxTotalFruits2(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4))
    # print(Solution().maxTotalFruits2(fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2))
    # print(Solution().maxTotalFruits2(fruits = [[200000,10000]], startPos = 200000, k=0))

    # print(Solution().maxTotalFruits2([[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]],
    #     21,30))