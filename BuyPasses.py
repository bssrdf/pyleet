'''
-Medium-

Alex plans on visiting the museum and is at the counter to purchase passes for the same. 
The administrators have decided not to sell group passes, and are providing only one pass 
at a time. If a visitor needs more than one pass, he/she has to pass through the queue again 
to reach the counter and buy the next pass, Alex wants to buy many passe.Considering that 
the visitors and number of passes each visitor needs is known, how much time does Alex 
require to buy all passes?Alex's place in the queue to the counter will be given, and each 
transaction takes 1 unit of time. The time needed to go to the back of the line each time can be ignored.

|arr|<=100000
arr[i]<=10000

样例
Example 1:

Input:
arr=[1,2,5],k=1
Output:
4
Explanation:
There is three persons.0,1,2.Alex is 1.
at 1 time,0(1)<-1(2)<-2(5).people 0 gets one pass.
at 2 time,1(2)<-2(5) Alex gets one pass,and he goes to the back of the line.
at 3 time,2(5)<-1(1),people 2 gets one pass,and he goes to the back of the line.
at 4 time,1(1)<-2(4),Alex gets one pass. Alex  buys all passes.
Example 2:

Input:
arr=[3,2,1], k = 0,
Output:
6

'''

from collections import deque

class Solution:
    """
    @param arr: the line 
    @param k: Alex place
    @return: the time when Alex requires to buy all passes
    """
    def buyPassesTLE(self, arr, k):
        # Write your code here.
        # 
        q = deque([(arr[i], i) for i in range(len(arr))])
        t = 0
        while True:
            t += 1
            ps, idx = q.popleft()
            ps -= 1
            if idx == k and ps == 0:
                return t            
            if ps > 0:
                q.append((ps, idx))
        return -1  

    def buyPasses(self, arr, k):
        # Write your code here.
        # 
        res, n = 0, len(arr)
        for i in range(n):
            if i < k:
                res += arr[i] if arr[i] < arr[k] else arr[k]
            elif i == k:
                res += arr[k]
            else:
                res += arr[i] if arr[i] <= arr[k]-1 else arr[k]-1
        return res


        


if __name__ == "__main__":
    print(Solution().buyPasses(arr=[1,2,5],k=1))
    print(Solution().buyPasses(arr=[3,2,1],k=0))