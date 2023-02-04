'''
-Hard-
*DP*
*Greedy*

There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at 
the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means 
the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden 
cannot be watered return -1.

 

Example 1:


Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
Example 3:

Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
Output: 3
Example 4:

Input: n = 8, ranges = [4,0,0,0,0,0,0,0,4]
Output: 2
Example 5:

Input: n = 8, ranges = [4,0,0,0,4,0,0,0,4]
Output: 1
 

Constraints:

1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100

'''

class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        # 所有喷头覆盖的区间
        maxRanges = [0]*(n+1)
        # 循环每一个喷头
        for i in range(len(ranges)):
            # 喷头覆盖区间的左下标
            left = i-ranges[i]
            # 左下标小于0时，设为0
            if left < 0: left = 0
            # 喷头覆盖区间的右下标
            right = i+ranges[i]
            # 右下标大于n时，设为n
            if right > n: right = n
            # 将区间存入maxRanges
            # maxRanges[left]代表左下标为left的区间最远可以到达的坐标
            maxRanges[left] = max(maxRanges[left], right)
        # 找出能够覆盖整个区间的最少区间个数
        # 第一个区间从0开始，maxRanges[0]结束
        #print(maxRanges)
        l, r = 0, maxRanges[0]
        res = 1 # 返回结果
        # 当右区间小于n时循环
        while r < n:
            # 找到下一个区间，下一个区间的left在当前区间内
            # 并且下一个区间的right大于当前区间right
            # 找到符合上述要求的一个right最大区间
            maxLeft, maxRight = l, r
            for i in range(l, r+1):
                if maxRanges[i] > maxRight:
                    maxRight = maxRanges[i]
                    maxLeft = i
            # 如果最大right不能大于当前right，返回-1
            if maxRight == r: return -1
            # 更新下一个区间的left和right
            l, r = maxLeft+1, maxRight
            res += 1
        return res
        
if __name__ == "__main__":
    print(Solution().minTaps(n = 5, ranges = [3,4,1,1,0,0]))