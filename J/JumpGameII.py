# -*- coding: utf-8 -*-

"""

-Medium-

*Greedy*
*BFS (implicit)*


You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].


"""

from typing import List

from collections import deque
from sortedcontainers import SortedList

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q = deque()
        lev = 0
        q.append((0,lev))
        visited = [False]*len(nums)
        visited[0] = True
        while q:
            pos,lev = q.popleft()
            if pos == len(nums)-1:
                return lev
            for i in range(1, nums[pos]+1):
                nextPos = min(pos+i, len(nums)-1)
                if nextPos == len(nums)-1:
                    return lev+1
                if not visited[nextPos]:
                    visited[nextPos] = True
                    q.append((nextPos,lev+1))
        return lev
        
    def jumpAC(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step    
    
    def jump3(self, nums):        
        n = len(nums)
        if n == 1: return 0
        # 从0开始，看其最远覆盖范围是多少。
        currendEnd = nums[0]
        # 返回结果，将0计入次数中，所以初始值为1
        res = 1
        # 因为0已经预先定义好，所以从1开始循环
        i = 1
        # 当currendEnd 大于等于目标值T时，结束循环
        while currendEnd < n-1:
            # 定义下一个最远覆盖范围
            nextMaxEnd = 0
            # 从当前位置到currendEnd范围内的所有数为起点，找其能覆盖的最远距离
            for j in range(i, currendEnd+1):
                nextMaxEnd = max(nextMaxEnd, j+nums[j])
            # 如果找到的最远距离无法超越currendEnd，说明后续片段无法连接
            #print(nextMaxEnd, currendEnd)
            if nextMaxEnd <= currendEnd:
                return -1
            # 将i至于currendEnd之后
            i = currendEnd + 1
            # 当前能覆盖的最远距离更新为nextMaxEnd
            currendEnd = nextMaxEnd
            # 次数加一
            res += 1
        return res
     
    def jump1(self, nums):
        '''
        此题的核心方法是利用贪婪算法 Greedy 的思想来解，想想为什么呢？ 为了较快的
        跳到末尾，想知道每一步能跳的范围，这里贪婪并不是要在能跳的范围中选跳力最远
        的那个位置，因为这样选下来不一定是最优解，这么一说感觉又有点不像贪婪算法了。
        其实这里贪的是一个能到达的最远范围，遍历当前跳跃能到的所有位置，然后根据该
        位置上的跳力来预测下一步能跳到的最远距离，贪出一个最远的范围，一旦当这个范
        围到达末尾时，当前所用的步数一定是最小步数
        '''
        res, n,  cur, i = 0, len(nums), 0, 0
        while cur < n - 1:
            res += 1
            pre = cur
            while i <= pre:   
                # greedily expand the jump range      
                cur = max(cur, i + nums[i])
                i += 1
            # cur is the furthest pos we can jump to from last range (.. pre]
            if pre == cur: # we can not jump further
                return -1
        return res

    def jump2(self, nums):
        res, n,  cur, last = 0, len(nums), 0, 0
        for i in range(n-1):
            cur = max(cur, i + nums[i])
            if i == last:
                last = cur
                res += 1
                if cur >= n-1:
                   break
        return res
    
    def jump5(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList(range(n))
        que = deque([(0, 0)])
        while que:
            pos, d = que.popleft()
            if pos == n-1:
                return d
            for k in list(sl.irange(pos, min(pos+nums[pos], n))):
                que.append((k, d+1))
                sl.remove(k)     
        return -1
    
    def jump6(self, nums: List[int]) -> int:
        # implicit BFS
        jumps, curEnd, curFarthest = 0, 0, 0
        # going through each pos level by level
        for i in range(len(nums)-1):
            # get the fathest point the positions in 
            # current level can reach 
            # initially (the 0-th level), curEnd = 0 and the fathest point is 0+nums[0]
            curFarthest = max(curFarthest, i+nums[i]) 
            if i == curEnd: # finish at the end of current level
                jumps += 1  # make one jump
                curEnd = curFarthest # go to next level
        return jumps

    

     
        
        
        
        
if __name__ == "__main__":
    A =[[2,3,1,1,4], [1,2,1,1,1]]
    for a in A:
        #print(Solution().jump(a))
        #print(Solution().jumpAC(a))
        #print(Solution().jump1(a))
        #print(Solution().jump2(a))
        print(Solution().jump3(a))
