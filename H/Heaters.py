'''
-Medium-

*Binary Search*

Winter is coming! During the contest, your first job is to design a standard heater 
with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius 
range. 

Given the positions of houses and heaters on a horizontal line, return the minimum 
radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will be 
the same.

 

Example 1:

Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the 
radius 1 standard, then all the houses can be warmed.
Example 2:

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use 
radius 1 standard, then all the houses can be warmed.
Example 3:

Input: houses = [1,5], heaters = [2]
Output: 3
 

Constraints:

1 <= houses.length, heaters.length <= 3 * 10^4
1 <= houses[i], heaters[i] <= 10^9
'''

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        res = 0
        for i in houses:
            l, r = 0, len(heaters)
            dist = 0
            while l < r:
                m = l + (r-l) // 2
                if heaters[m] <= i:
                    l = m+1
                else:
                    r = m
            if r == 0:
                dist = heaters[0] - i
            elif r == len(heaters):                
                dist = i - heaters[-1]
            else:     
                dist = min(i-heaters[r-1], heaters[r]-i) 
            res = max(res, dist)     
        return res

if __name__ == "__main__":
    print(Solution().findRadius([1,2,3], [2]))
    print(Solution().findRadius([1,2,3,4], [1,4]))
    print(Solution().findRadius([1,5], [2]))