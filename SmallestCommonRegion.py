'''

-Medium-


You are given some lists of regions where the first region of each list includes all other regions 
in that list.
Naturally, if a region X contains another region Y then X is bigger than Y. Also by definition a 
region X contains itself.
Given two regions region1, region2, find out the smallest region that contains both of them.
If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 
such that r2 includes r3.

It's guaranteed the smallest region exists.

Example 1:
Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"

Constraints:
2 <= regions.length <= 10^4
region1 != region2
All strings consist of English letters and spaces with at most 20 letters.

'''
class Solution(object):

    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        dic = {}
        for region in regions:
            parent = region[0]
            for i in range(1,len(region)):
                dic[region[i]] = parent

        dic_region1 = {}
        while region1 in dic:
            dic_region1[region1] = 1
            region1 = dic[region1]

        while region2 in dic:
            if region2 in dic_region1:
                return region2
            region2 = dic[region2]
        return regions[0][0]

if __name__ == "__main__":
    regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]]
    region1 = "Quebec"
    region2 = "New York"
    print(Solution().findSmallestRegion(regions, region1, region2))