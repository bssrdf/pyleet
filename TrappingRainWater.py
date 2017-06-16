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


if __name__ == "__main__":
    print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) #== 6
