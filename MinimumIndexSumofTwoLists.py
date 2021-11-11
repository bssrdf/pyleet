'''


'''
from typing import List

from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m = defaultdict(int)
        for i in range(len(list1)):
            m[list1[i]] += i
        res = []
        isum = 10**9
        for i in range(len(list2)):
            if list2[i] in m:
                print(i, list2[i])
                if i+m[list2[i]] < isum:
                    res = [list2[i]]
                    isum = i+m[list2[i]]
                elif i+m[list2[i]] == isum:
                    res.append(list2[i])
        return res  

if __name__ == "__main__":
    print(Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
        
