'''
-Hard-
*Greedy*
*Prefix Sum*
There is a garden of n flowers, and each flower has an integer beauty value. The flowers 
are arranged in a line. You are given an integer array flowers of size n and each 
flowers[i] represents the beauty of the ith flower.

A garden is valid if it meets these conditions:

The garden has at least two flowers.
The first and the last flower of the garden have the same beauty value.
As the appointed gardener, you have the ability to remove any (possibly none) flowers 
from the garden. You want to remove flowers in a way that makes the remaining garden valid. 
The beauty of the garden is the sum of the beauty of all the remaining flowers.

Return the maximum possible beauty of some valid garden after you have removed any 
(possibly none) flowers.

 

Example 1:

Input: flowers = [1,2,3,1,2]
Output: 8
Explanation: You can produce the valid garden [2,3,1,2] to have a total beauty of 2 + 3 + 1 + 2 = 8.
Example 2:

Input: flowers = [100,1,1,-3,1]
Output: 3
Explanation: You can produce the valid garden [1,1,1] to have a total beauty of 1 + 1 + 1 = 3.
Example 3:

Input: flowers = [-1,-2,0,-1]
Output: -2
Explanation: You can produce the valid garden [-1,-1] to have a total beauty of -1 + -1 = -2.
 

Constraints:

2 <= flowers.length <= 10^5
-10^4 <= flowers[i] <= 10^4
It is possible to create a valid garden by removing some (possibly none) flowers.

'''

class Solution(object):
    def maximumBeauty(self, flowers) :
        n = len(flowers)
        preSum = [0]*(n+1)
        for i in range(1,n+1):
            preSum[i] = preSum[i-1] + max(0,flowers[i-1]) #计算前缀和，把负数都去掉
        m = {}
        res = -float('inf')
        for i in range(n):
            if flowers[i] in m: # 此时遍历到的元素在前面出现过，可以组成有效花园，计算这个花园的值
                sm = preSum[i+1] - preSum[m[flowers[i]]]
                if flowers[i] < 0:
                    sm += 2*flowers[i] #由于负数在之前前缀和的计算中没有算过，这里要加上
                res = max(res, sm) 
            else:
                m[flowers[i]] = i
        return res



if __name__ == "__main__":
    print(Solution().maximumBeauty([1,2,3,1,2]))
    print(Solution().maximumBeauty([-1,-2,0,-1]))
    print(Solution().maximumBeauty([100,1,1,-3,1]))