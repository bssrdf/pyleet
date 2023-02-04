'''
-Medium-
*Greedy*
*Priority Queue*

In order to decorate your new house, you need to process some sticks with 
positive integer length. You can connect any two sticks of lengths X and Y 
into one stick by paying a cost of X + Y. Due to the construction needs, you must 
connect all the bars into one. Return the minimum cost of connecting all the 
given sticks into one stick in this way. Please note that you can choose any 
order of sticks connection

1 ≤ sticks.length≤10^4 

 
1 <= sticks[i] <= 10^4
 
样例
Example 1:

Input:
[2,4,3]
Output: 
14
Explanation: 
First connect 2 and 3 to 5 and cost 5; then connect 5 and 4 to 9; total cost is 14
Example 2:

Input:
 [1,8,3,5]
Output: 
30

'''
import heapq

class Solution:
    """
    @param sticks: the length of sticks
    @return: Minimum Cost to Connect Sticks
    """
    def MinimumCost(self, sticks):
        # write your code here
        ans = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            cost = s1 + s2
            ans += cost
            heapq.heappush(sticks, cost)
        return ans

        

if __name__ == "__main__":
    print(Solution().MinimumCost([2,4,3]))
    print(Solution().MinimumCost([1,8,3,5]))