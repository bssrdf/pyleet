'''
-Hard-
You are given an array of integers distance.

You start at point (0,0) on an X-Y plane and you move distance[0] meters to the north, then distance[1] meters to the west, distance[2] meters to the south, distance[3] meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

Return true if your path crosses itself, and false if it does not.

 

Example 1:


Input: distance = [2,1,1,2]
Output: true
Example 2:


Input: distance = [1,2,3,4]
Output: false
Example 3:


Input: distance = [1,1,1,1]
Output: true
 

Constraints:

1 <= distance.length <= 10^5
1 <= distance[i] <= 10^5


'''

class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        x = distance
        for i in range(3,  len(x)):
            # 第一类是第四条边和第一条边相交的情况，需要满足的条件是第一条边大于等于第三条边，第四条边大于等于第二条边。
            # 同样适用于第五条边和第二条边相交，第六条边和第三条边相交等等，依次向后类推的情况...
            if x[i] >= x[i - 2] and x[i - 3] >= x[i - 1]:
                return True
            # 第二类是第五条边和第一条边重合相交的情况，需要满足的条件是第二条边和第四条边相等，第五条边大于等于第三条边
            # 和第一条边的差值，同样适用于第六条边和第二条边重合相交的情况等等依次向后类推...    
            if i >= 4  and x[i-1] == x[i-3] and x[i] >= x[i-2] - x[i-4]:
                return True
            # 第三类是第六条边和第一条边相交的情况，需要满足的条件是第四条边大于等于第二条边，第三条边大于等于第五条边，
            # 第五条边大于等于第三条边和第一条边的差值，第六条边大于等于第四条边和第二条边的差值，同样适用于第七条边和
            # 第二条边相交的情况等等依次向后类推...    
            if i >= 5 and x[i-2] >= x[i-4] and x[i-3] >= x[i-1] and x[i-1] >= x[i-3] - x[i-5] and x[i] >= x[i-2] - x[i-4]:
                return True
        return False