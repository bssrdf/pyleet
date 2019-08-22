# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:38:48 2017

@author: merli
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:32:36 2017

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
        res, n,  cur, i = 0, len(nums), 0, 0
        while cur < n - 1:
            res += 1
            pre = cur
            while i <= pre:         
                cur = max(cur, i + nums[i])
                i += 1
            if pre == cur:
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
    A=[ [2,3,1,1,4]
      ]
    for a in A:
        #print(Solution().jump(a))
        #print(Solution().jumpAC(a))
        print(Solution().jump1(a))
        print(Solution().jump2(a))