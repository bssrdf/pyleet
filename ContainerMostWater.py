
'''

Given n non-negative integers a1, a2, ..., an , where each represents a 
point at coordinate (i, ai). n vertical lines are drawn such that the two 
endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together 
with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        Start by evaluating the widest container, using the first and the last 
        line. All other possible containers are less wide, so to hold more 
        water, they need to be higher. Thus, after evaluating that widest 
        container, skip lines at both ends that don't support a higher height. 
        Then evaluate that new container we arrived at. Repeat until there are 
        no more possible containers left.
        """
        n = len(height)
        l, r = 0, n-1
        res = 0
        while l < r:
            h = min(height[l],height[r])
            res = max(res, h*(r-l))
            while height[l] <= h and l < r:
               l += 1
            while height[r] <= h and l < r:
                r -= 1
        return res


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))