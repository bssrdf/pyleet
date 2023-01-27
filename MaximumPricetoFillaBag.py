'''
-Medium-
$$$

*Greedy*

You are given a 2D integer array items where items[i] = [pricei, weighti] denotes the price and weight of the ith item, respectively.

You are also given a positive integer capacity.

Each item can be divided into two items with ratios part1 and part2, where part1 + part2 == 1.

The weight of the first item is weighti * part1 and the price of the first item is pricei * part1.
Similarly, the weight of the second item is weighti * part2 and the price of the second item is pricei * part2.
Return the maximum total price to fill a bag of capacity capacity with given items. If it is impossible to fill a bag return -1. Answers within 10-5 of the actual answer will be considered accepted.

 

Example 1:

Input: items = [[50,1],[10,8]], capacity = 5
Output: 55.00000
Explanation: 
We divide the 2nd item into two parts with part1 = 0.5 and part2 = 0.5.
The price and weight of the 1st item are 5, 4. And similarly, the price and the weight of the 2nd item are 5, 4.
The array items after operation becomes [[50,1],[5,4],[5,4]]. 
To fill a bag with capacity 5 we take the 1st element with a price of 50 and the 2nd element with a price of 5.
It can be proved that 55.0 is the maximum total price that we can achieve.
Example 2:

Input: items = [[100,30]], capacity = 50
Output: -1.00000
Explanation: It is impossible to fill a bag with the given item.
 

Constraints:

1 <= items.length <= 105
items[i].length == 2
1 <= pricei, weighti <= 104
1 <= capacity <= 109


'''
from typing import List


class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        ans, puny = 0, 1.e-5
        for p,w in sorted(items, key=lambda x: x[0]/x[1], reverse = True):
            if w <= capacity:
                ans += p
                capacity -= w
            else:
                ans += p * capacity / w 
                capacity = 0
            if capacity < puny:
                break
        return ans if capacity < puny else -1 

    def maxPrice2(self, items: List[List[int]], capacity: int) -> float:
        ans = 0
        for p, w in sorted(items, key=lambda x: x[1] / x[0]):
            v = min(w, capacity)
            ans += v / w * p
            capacity -= v
        return -1 if capacity else ans

from random import randint

if __name__ == '__main__':
    print(Solution().maxPrice(items = [[50,1],[10,8]], capacity = 5))
    print(Solution().maxPrice(items = [[100,30]], capacity = 50))
    N, M, L = 10**5, 10**4, 10**9
    items = [[randint(1,M), randint(1,M)] for _ in range(N)]
    capacity = randint(1, L)
    print(Solution().maxPrice(items = items, capacity = capacity))
    print(Solution().maxPrice2(items = items, capacity = capacity))
    


