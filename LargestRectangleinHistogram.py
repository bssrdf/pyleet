'''
-Hard-

*Stack*

*Monotonic Queue*

Given n non-negative integers representing the histogram's bar height where 
the width of each bar is 1, find the area of largest rectangle in the 
histogram.

Example:

Input: [2,1,5,6,2,3]
Output: 10

'''


class Solution(object):
    def largestRectangleArea(self, heights):
        '''
        For any bar i the maximum rectangle is of width r - l - 1 where r - is 
        the last coordinate of the bar to the right with height h[r] >= h[i] 
        and l - is the last coordinate of the bar to the left which height 
        h[l] >= h[i]

        So if for any i coordinate we know his utmost higher (or of the same 
        height) neighbors to the right and to the left, we can easily find the 
        largest rectangle:

        '''

        if not heights: 
          return 0
        n = len(heights)
        lessFromLeft = [0] * n
        lessFromRight = [0] * n
        lessFromLeft[0] = -1
        lessFromRight[n-1] = n
        for i in range(1, n):
            p = i-1
            '''
            for example in order to left[i]; if height[i - 1] < height[i] then 
            left[i] = i - 1; other wise we do not need to start scan from i - 1; 
            we can start the scan from left[i - 1], because since left[i - 1] is 
            the first position to the left of i - 1 that have height less than 
            height[i - 1], and we know height[i - 1] >= height[i]; so left[i] must 
            be at the left or at left[i - 1]; similar for the right array;
            Since we do not need to scan from scratch for each i, the time 
            complexity can be simplified to O(n);
            '''
            while p >= 0 and heights[p] >= heights[i]:
                p = lessFromLeft[p]
            lessFromLeft[i] = p
        for i in range(n-2, -1, -1):
            p = i+1
            while p < n and heights[p] >= heights[i]:
                p = lessFromRight[p]
            lessFromRight[i] = p
        print(lessFromLeft)
        print(lessFromRight)
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, heights[i]*(lessFromRight[i]-lessFromLeft[i]-1))
        return maxArea
  
    def largestRectangleAreaMonoQueue(self, heights):
        '''
        For any bar i the maximum rectangle is of width r - l - 1 where 
        r - is the first coordinate of the bar to the right with 
             height h[r] < h[i]; if no such exists, set to len(heights)
        l - is the first coordinate of the bar to the left with height 
             h[l] < h[i]; if no such exists, set to -1

        So for any i coordinate we can easily find the rectangle formed
        using the ith bar as 
           h[i]*width = h[i]*(r-l-1)        
        '''

        if not heights: 
          return 0
        n = len(heights)
        # rationale for setting -1 and n:
        # consider a bar with minimum height hmin
        # the rectangle it can form has height hmin 
        # lessFromLeft will be -1 and 
        # lessFromRight will be n for this bard
        # hence the width = (n - (-1)) - 1 = n, i.e., 
        # the width of the whole histogram
        lessFromLeft = [-1] * n
        lessFromRight = [n] * n        
        stack = []    
        for i,v in enumerate(heights):
            while stack and heights[stack[-1]] >= v: # right is from the popping out
                lessFromRight[stack.pop()] = i
            if stack:  #left is from the pushing in
                # after popping above, what is left at the stack top is the
                # first smaller h than heights[i]
                lessFromLeft[i] = stack[-1]
            stack.append(i)  
        
        print(lessFromLeft)
        print(lessFromRight)
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, heights[i]*(lessFromRight[i]-lessFromLeft[i]-1))
            print(i, maxArea)
        return maxArea

    def largestRectangleAreaStack(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        maxArea = 0
        s = []
        i = 0
        
        while i < n:
            if (not s) or heights[i] >= heights[s[-1]]:
                s.append(i)
                i += 1
            else:
                tp = s.pop()
                width = i if not s else i-1-s[-1]
                maxArea = max(maxArea, heights[tp]*width)   
        while s:
            tp = s.pop()
            width = i if not s else i-1-s[-1]
            maxArea = max(maxArea, heights[tp]*width)

        return maxArea


print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleAreaMonoQueue([2,1,5,6,2,3]))
print(Solution().largestRectangleAreaMonoQueue([2,2,5,6,2,3]))
print(Solution().largestRectangleAreaStack([2,1,5,6,2,3]))
#print(Solution().largestRectangleArea([6, 2, 5, 4, 5, 1, 6]))