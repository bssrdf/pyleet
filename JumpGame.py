# -*- coding: utf-8 -*-
"""
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
        
    
    def canJumpGreedy(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPos = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= lastPos:
                lastPos = i
        return lastPos==0
        
        
        
if __name__ == "__main__":
    A=[ [2,3,1,1,4],
     [3,2,1,0,4],
     [2,0],
    [0,2]
    ]
    for a in A:
        print Solution().canJump(a)