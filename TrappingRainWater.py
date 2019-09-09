'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        lh = []
        rh = []
        lmax = 0
        for h in height:
            if h>=lmax:
                lmax=h
            lh.append(lmax)
        lmax = 0
        for h in reversed(height):
            if h>=lmax:
                lmax=h
            rh.append(lmax)
        rh.reverse()        
        water = 0
        for h, l, r in zip(height, lh, rh):
            water = water + min(l, r)-h          
        return water
        
    def trap_o1space(self, height):
        if not height:
            return 0
        leftMax = rightMax = 0
        left = 0
        right = len(height)-1
        water = 0        
        while left < right:
            if leftMax < height[left]:
                leftMax = height[left]
            if rightMax < height[right]:
                rightMax = height[right]
            if leftMax < rightMax:
                water = water + leftMax-height[left]
                left = left + 1
            else:
                water = water + rightMax-height[right]
                right = right - 1
            print(left, right, leftMax, rightMax, water)
        return water

    def trap_stack(self, height):
             st = []
             res = 0
             i = 0
             while i < len(height):
                if not st or height[i] <= height[st[-1]]:
                   st.append(i)
                   i += 1
                else:
                   t = st.pop()
                   if not st:
                      continue
                   res += (min(height[i], height[st[-1]])-height[t])*(i-st[-1]-1)
<<<<<<< HEAD
                print st, res
=======
                print(st, res)
>>>>>>> 116cc6699e6d001cb6a62f0e62a7074353734518
             return res
        

if __name__ == "__main__":
#    print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) #== 6
    #print Solution().trap_o1space([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) #== 6
    #print Solution().trap([0, 3, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) #== 6
   # print(Solution().trap_o1space([0, 3, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) #== 6
<<<<<<< HEAD
    print Solution().trap_stack([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) #== 6
=======
    #print(Solution().trap_stack([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) #== 6

    print(Solution().trap_stack([0, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5, 6])) #== 6
>>>>>>> 116cc6699e6d001cb6a62f0e62a7074353734518
