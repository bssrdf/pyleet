# -*- coding: utf-8 -*-
"""
-Medium-

*Greedy*

Created on Sat Aug 12 21:32:36 2017

Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

@author: merli
"""

class Solution(object):
    def canJump(self, nums):
        #return self.canJumpBacktracking(0, nums)
        return self.canJumpDPTopdown(0, nums, {})
        
    def canJumpBacktracking(self, position, nums):
        if position == len(nums)-1:
            return True
        furthestPos = min(position + nums[position], len(nums)-1)
        for i in range(position+1, furthestPos+1):
            if self.canJumpBacktracking(i, nums):
                return True
        return False
        
    def canJumpDPTopdown(self, position, nums, dp):
        if position == len(nums)-1:
            return True
        if position in dp:
            return dp[position]
        furthestPos = min(position + nums[position], len(nums)-1)
        for i in range(position+1, furthestPos+1):
            if self.canJumpDPTopdown(i, nums, dp):
                dp[i] = True
                return True    
        dp[position] = False       
        return False        
        
    
    def canJumpGreedyDP(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        维护一个一维数组 dp，其中 dp[i] 表示达到i位置时剩余的跳力，若到达某个位置时
        跳力为负了，说明无法到达该位置。接下来难点就是推导状态转移方程啦，想想啊，到
        达当前位置的剩余跳力跟什么有关呢，其实是跟上一个位置的剩余跳力（dp 值）和上
        一个位置新的跳力（nums 数组中的值）有关，这里新的跳力就是原数组中每个位置的
        数字，因为其代表了以当前位置为起点能到达的最远位置。所以当前位置的剩余跳力
        （dp 值）和当前位置新的跳力中的较大那个数决定了当前能到的最远距离，而下一
        个位置的剩余跳力（dp 值）就等于当前的这个较大值减去1，因为需要花一个跳力到达
        下一个位置，所以就有状态转移方程了：
        dp[i] = max(dp[i - 1], nums[i - 1]) - 1，
        如果当某一个时刻 dp 数组的值为负了，说明无法抵达当前位置，则直接返回 false，
        最后循环结束后直接返回 true  即可，
        """
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(dp[i-1], nums[i-1])-1
            if dp[i] < 0: return False
        return True

    def canJumpGreedy(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPos = 0
        for i in range(len(nums)):
            if i > lastPos: # we can never reach i
                print(i, nums[i], lastPos)
                break
            lastPos = max(lastPos, i+nums[i]) # greedily jump to the furthest
        return lastPos >= len(nums)-1
        
        
        
if __name__ == "__main__":
    A=[ [2,3,1,1,4],
     [3,2,1,0,4],
     [2,0],
    [0,2]
    ]
    for a in A:
        print(Solution().canJump(a))
        print(Solution().canJumpGreedy(a))
    a = [3,2,1,0,4]
    print(Solution().canJumpGreedy(a))