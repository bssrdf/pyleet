'''
-Medium-

There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers 
enter the store. You are given an integer array customers of length n where customers[i] is the number 
of the customer that enters the store at the start of the ith minute and all those customers leave 
after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] 
is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, 
they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive 
minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
 

Constraints:

n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 10^4
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.

'''

from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        C, G, M = customers, grumpy, minutes
        n = len(C)
        preSum = [0]*(n+1)
        for i in range(1,n+1):
            preSum[i] = preSum[i-1] + (C[i-1] if G[i-1] == 0 else 0)
        total = 0
        for i in range(M):
           total += C[i]
        #res = total + preSum[n] - preSum[M]   
        res = total - preSum[M]   
        for i in range(M, n):
            total +=  C[i] - C[i-M]
            #res = max(res, total + preSum[n] - preSum[i+1] + preSum[i-M+1])   
            res = max(res, total - preSum[i+1] + preSum[i-M+1])   
        return res + preSum[n]

    def maxSatisfied2(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        C, G, M = customers, grumpy, minutes
        n = len(C)
        preSumi, preSumim = 0, 0
        #for i in range(1,n+1):
        #    preSum[i] = preSum[i-1] + (C[i-1] if G[i-1] == 0 else 0)
        total = 0
        for i in range(M):
           preSumi += C[i] if G[i] == 0 else 0
           total += C[i]
        res = total - preSumi   
        for i in range(M, n):
            total +=  C[i] - C[i-M]
            preSumi += C[i] if G[i] == 0 else 0
            preSumim += C[i-M] if G[i-M] == 0 else 0
            res = max(res, total - preSumi + preSumim)  
        #print(preSumi) 
        return res + preSumi
        
        
if __name__ == '__main__':
    customers = [1,0,1,2,1,1,7,5]; grumpy = [0,1,0,1,0,1,0,1]; minutes = 3
    print(Solution().maxSatisfied(customers, grumpy, minutes))
    print(Solution().maxSatisfied2(customers, grumpy, minutes))
    customers = [1]; grumpy = [0]; minutes = 1
    print(Solution().maxSatisfied(customers, grumpy, minutes))
    print(Solution().maxSatisfied2(customers, grumpy, minutes))
