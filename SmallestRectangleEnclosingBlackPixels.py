'''
-Hard-

*Binary Search*

An image is represented by a binary matrix with 0 as a white pixel and 1 as a 
black pixel. The black pixels are connected, i.e., there is only one black 
region. Pixels are connected horizontally and vertically. Given the location 
(x, y) of one of the black pixels, return the area of the smallest (axis-aligned) 
rectangle that encloses all black pixels.

Example:

Input:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2

Output: 6

'''

class Solution(object):
    def minArea(self, image, x, y):
        """        
        :type intervals: List[str]
        :type x: int
        :type y: int
        :rtype: int
        """
        """
        use (x,y) as a center, search boundaries in all 4 directions
        binary search can be used to speed up 
        """
        m = len(image)
        n = len(image[0])
        def searchBnd(i,j,direction,bnd):
            while i < j:                
                mid = i + (j-i)//2
                found = False
                for k in range(n if direction == 0 else m):
                    h = image[mid][k] if direction == 0 else image[k][mid]
                    if h == '1':
                        found = True
                        break                
                if found: 
                    # if a black pixel is encountered
                      
                    # when searching for upper and left boundary
                    # move j to mid so to make sure the final index is 
                    # for a row or col which has a black pixel                                         
                    if bnd == 0: j = mid
                    # when searching for lower and right boundary
                    # move i to mid+1 so to make sure the final index is 
                    # for a row or col which has no black pixels                     
                    else: i = mid+1                            
                else:
                    # if no black pixels are encountered

                    # when searching for upper and left boundary
                    # move i to mid+1 so to make sure the final index is 
                    # for a row or col which has a black pixel                                         
                    if bnd == 0: i = mid+1
                    # when searching for lower and right boundary
                    # move j to mid so to make sure the final index is 
                    # for a row or col which has no black pixels                     
                    else: j = mid                            
            return i
        up    = searchBnd(0, x, 0, 0)
        down  = searchBnd(x+1, m, 0, 1) # this side is always 1-row below 
        left  = searchBnd(0, y, 1, 0)
        right = searchBnd(y+1, n, 1, 1) # this side is always 1-column right
        #print(up, down, left, right)
        return (down-up)*(right-left)

if __name__ == "__main__":
    A = [
  "0010",
  "0110",
  "0100"
    ]
    #print(Solution().minArea(A, 0, 2))
    A = [
        "0000000",
        "0110100",
        "0110000",
        "0111000",
        "0111110",
        "0000000",
        "0000000"
    ]
    print(Solution().minArea(A, 1, 2))

 
                        



        
