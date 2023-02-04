'''
-Medium-
*GCD*
*Sorting*

ou are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei. A line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:


Return the minimum number of lines needed to represent the line chart.

 

Example 1:


Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
Output: 3
Explanation:
The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
It can be shown that it is not possible to represent the line chart using less than 3 lines.
Example 2:


Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
Output: 1
Explanation:
As shown in the diagram above, the line chart can be represented with a single line.
 

Constraints:

1 <= stockPrices.length <= 105
stockPrices[i].length == 2
1 <= dayi, pricei <= 109
All dayi are distinct.

'''
from typing import List
from numpy import sign

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        P = stockPrices
        P.sort()
        # print(P)
        # print(len(P))
        if len(P) == 1: return 0
        x0, y0 = P[0]
        x1, y1 = P[1]
        
        def gcd(a, b):
            while b != 0:
                r = a % b
                a, b = b, r
            return a  
        x = x1 - x0 
        y = abs(y1 - y0)
        g = gcd(x, y)          
        if g != 0:           
            slope = (x//g, y//g, sign(y1-y0))
        else:
            slope = (x, 0, 0)
        ans = 1
        for i  in range(2, len(P)): 
            x0, y0 = x1, y1
            x1, y1 = P[i]
            x = x1 - x0 
            y = abs(y1 - y0)
            g = gcd(x, y)
            if g != 0:           
                s = (x//g, y//g, sign(y1-y0))
            else:
                s = (x, 0, 0)
            # print(ans, s, slope, x0, y0, x1, y1, g, x, y)
            if s != slope:
                ans += 1
                slope = s
            
        return ans 
    
    def minimumLines2(self, stockPrices: List[List[int]]) -> int:
        P = stockPrices
        P.sort()
        if len(P) == 1: return 0
        x0, y0 = P[0]
        x1, y1 = P[1]       
        ans = 1
        for i  in range(2, len(P)): 
            x2, y2 = P[i]
            if (y2-y1)*(x1-x0) != (y1-y0) * (x2-x1): 
                ans += 1
            x0, y0 = x1, y1
            x1, y1 = x2, y2
        return ans 
            


             

        

if __name__ == "__main__":
    # print(Solution().minimumLines(stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]))
    print(Solution().minimumLines2(stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]))
    # print(Solution().minimumLines(stockPrices = [[3,4],[1,2],[7,8],[2,3]]))
    stockPrices = [[93,6],[87,11],[26,58],[28,1],[69,87],[45,59],[29,3],[5,58],[60,94],[46,54],[38,58],[88,10],[94,7],[72,96],[2,93],[63,54],[74,22],[77,84],[33,64],[13,71],[78,59],[76,93],[3,31],[7,95],[68,32],[27,61],[96,31],[4,67],[75,36],[67,21],[8,66],[83,66],[71,58],[6,36],[34,7],[86,78]]
    print(Solution().minimumLines(stockPrices = stockPrices))
    print(Solution().minimumLines2(stockPrices = stockPrices))