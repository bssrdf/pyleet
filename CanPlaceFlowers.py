'''
-Easy-

You have a long flowerbed in which some of the plots are planted, and 
some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means 
empty and 1 means not empty, and an integer n, return if n new flowers 
can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1: 
            if flowerbed[0] == 1:
                 return True if n==0 else False
            else:
                 return True if n<2 else False
        for i in range(len(flowerbed)):
            if i==0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1 
                n -= 1                
            elif i == len(flowerbed)-1 and flowerbed[i] ==0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1 
                n -= 1          
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and \
                 flowerbed[i+1] == 0:
                flowerbed[i] = 1 
                n -= 1
        return True if n <= 0 else False
        
    def canPlaceFlowersCleanCode(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n ==0: return True
        flowerbed = [0] + flowerbed + [0]
        size = len(flowerbed)
        for i in range(1, size-1):
           if flowerbed[i]:
              continue
           elif flowerbed[i - 1] == flowerbed[i + 1] == 0:
              n-=1
              flowerbed[i] = 1
              if n == 0:return True
        return False
       

if __name__ == "__main__":
    #print(Solution().canPlaceFlowers([1,0,0,0,1],  1))
    #print(Solution().canPlaceFlowers([1,0,0,0,1],  2))
    #print(Solution().canPlaceFlowers([1,0,0,0,1,0,0], 2))
    print(Solution().canPlaceFlowers([0,0,1,0,0],1))