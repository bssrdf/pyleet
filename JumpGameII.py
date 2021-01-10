# -*- coding: utf-8 -*-

"""

-Hard-

*Greedy*

Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from 
index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

@author: merli
"""
from collections import deque
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
     
        
        
        
        
if __name__ == "__main__":
    A =[ [2,3,1,1,4] ]
    for a in A:
        #print(Solution().jump(a))
        #print(Solution().jumpAC(a))
        print(Solution().jump1(a))
        print(Solution().jump2(a))
