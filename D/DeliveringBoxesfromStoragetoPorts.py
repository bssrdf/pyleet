'''
-Hard-

*Sliding Window*
*Monotonic Queue*
*DP*

You have the task of delivering some boxes from storage to their ports using only one ship. 
However, this ship has a limit on the number of boxes and the total weight that it can carry.

You are given an array boxes, where boxes[i] = [ports​​i​, weighti], and three integers portsCount, 
maxBoxes, and maxWeight.

ports​​i is the port where you need to deliver the ith box and weightsi is the weight of the ith box.
portsCount is the number of ports.
maxBoxes and maxWeight are the respective box and weight limits of the ship.
The boxes need to be delivered in the order they are given. The ship will follow these steps:

The ship will take some number of boxes from the boxes queue, not violating the maxBoxes and 
maxWeight constraints.
For each loaded box in order, the ship will make a trip to the port the box needs to be delivered 
to and deliver it. If the ship is already at the correct port, no trip is needed, and the box can 
immediately be delivered.
The ship then makes a return trip to storage to take more boxes from the queue.
The ship must end at storage after all the boxes have been delivered.

Return the minimum number of trips the ship needs to make to deliver all boxes to their respective ports.

 

Example 1:

Input: boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
Output: 4
Explanation: The optimal strategy is as follows: 
- The ship takes all the boxes in the queue, goes to port 1, then port 2, then port 1 again, then returns to storage. 4 trips.
So the total number of trips is 4.
Note that the first and third boxes cannot be delivered together because the boxes need to be delivered in order (i.e. the second box needs to be delivered at port 2 before the third box).
Example 2:

Input: boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6
Output: 6
Explanation: The optimal strategy is as follows: 
- The ship takes the first box, goes to port 1, then returns to storage. 2 trips.
- The ship takes the second, third and fourth boxes, goes to port 3, then returns to storage. 2 trips.
- The ship takes the fifth box, goes to port 3, then returns to storage. 2 trips.
So the total number of trips is 2 + 2 + 2 = 6.
Example 3:

Input: boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7
Output: 6
Explanation: The optimal strategy is as follows:
- The ship takes the first and second boxes, goes to port 1, then returns to storage. 2 trips.
- The ship takes the third and fourth boxes, goes to port 2, then returns to storage. 2 trips.
- The ship takes the fifth and sixth boxes, goes to port 3, then returns to storage. 2 trips.
So the total number of trips is 2 + 2 + 2 = 6.
Example 4:

Input: boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]], portsCount = 5, maxBoxes = 5, maxWeight = 7
Output: 14
Explanation: The optimal strategy is as follows:
- The ship takes the first box, goes to port 2, then storage. 2 trips.
- The ship takes the second box, goes to port 2, then storage. 2 trips.
- The ship takes the third and fourth boxes, goes to port 3, then storage. 2 trips.
- The ship takes the fifth box, goes to port 3, then storage. 2 trips.
- The ship takes the sixth and seventh boxes, goes to port 3, then port 4, then storage. 3 trips. 
- The ship takes the eighth and ninth boxes, goes to port 1, then port 5, then storage. 3 trips.
So the total number of trips is 2 + 2 + 2 + 2 + 3 + 3 = 14.
 

Constraints:

1 <= boxes.length <= 105
1 <= portsCount, maxBoxes, maxWeight <= 105
1 <= ports​​i <= portsCount
1 <= weightsi <= maxWeight 

'''
import collections
class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
        # details see
        # https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/discuss/969560/Python-O(n).-DP-%2B-Monotonic-Queue-(Sliding-Window)-with-Full-Explanation
        n = len(boxes)
        que = collections.deque([(-1,0)])  # monotonic queue. item: (division_position, trip_cost)
        pre = -1  # latest end of previous trip
        ws = 0  # maximal weights of current trip
        for i, (p, w) in enumerate(boxes):  # p: port; w: weight
            # update the earliest possible start of current trip:
            ws += w
            while i - pre > maxBoxes or ws > maxWeight: # shrink sliding window, 
                pre += 1                                # if number of boxes exceeds maxBoxes  
                ws -= boxes[pre][1]                     # if totalweight excessds maxWeight 
            while que[0][0] < pre: que.popleft()  ## pop out the boxes out of range of current trip
            
            # min cost of current trip. front of monotonic queue is always the minimal cost that meets the limitation
            mn = (2 if i+1<n and p==boxes[i+1][0] else 1) + que[0][1]
            while que[-1][1] >= mn: que.pop()  # maintain the queue monotonic
            que.append((i, mn))
            print(i, (p,w), mn, que)

        base_trip = 1  # calc base trip cost
        for i in range(n-1):
            if boxes[i][0] != boxes[i+1][0]: base_trip += 1

        return base_trip + que[-1][1]
    
    def boxDelivering2(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
        def takeOffStartBox(sum_, start, diff):
            sum_ -= boxes[start][1]
            if C[start]: diff -= 1
            start += 1
            return sum_, start, diff
        
        n = len(boxes)
        
        C = []
        for i in range(n-1):
            C.append(boxes[i][0]!=boxes[i+1][0])
        
        dp = [0 for el in range(n+1)]
        sum_, start, diff = 0, 0, 0
        for i in range(n):
            if (i-start) == maxBoxes: # drop 1 box because of # of boxes constraint
                sum_, start, diff = takeOffStartBox(sum_, start, diff)
            
            # Add box i, update cur weight, diff
            sum_ += boxes[i][1]
            if i > 0 and C[i-1]: diff += 1
                
            while sum_ > maxWeight:
                sum_, start, diff = takeOffStartBox(sum_, start, diff)
            
            while start < i and dp[start] == dp[start+1]:
                sum_, start, diff = takeOffStartBox(sum_, start, diff)
            
            dp[i+1] = diff+2 + dp[start]
        
        return dp[n]
    
    def boxDelivering3(self, boxes, portsCount, maxBoxes, maxWeight):
        # DP + sliding window
        A, B, W = boxes, maxBoxes, maxWeight
        n = len(A)
        C = [False]*n # consecutive ports are different or not
        for i in range(n-1):
            if A[i][0] != A[i+1][0]: C[i] = True
        dp = [0]*(n+1) # dp[i+1] be the minimum cost (# of trips) to process 
                       # all boxes from 0 to i and return to the storage.
                       # the answer is dp[n]
        sums = 0  # total current weight on the ship
        start = 0 # load all boxes from start to i in one voyage
        diff = 0  # number of different consecutive ports between start and i
        for i in range(n):
            if i-start == B: # drop 1 box because of # boxes constraint
                sums -= A[start][1]
                if C[start]: diff -= 1
                start += 1
            sums += A[i][1]
            if i > 0 and C[i-1]: diff += 1
            while sums > W: # drop more boxex because of weight constraint
                sums -= A[start][1]
                if C[start]: diff -= 1
                start += 1
            while start < i and dp[start] == dp[start+1]:
                # drop more boxes if there is no point to carry them
                sums -= A[start][1]
                if C[start]: diff -= 1
                start += 1
            dp[i+1] = diff + 2 + dp[start] # we can load all boxes from start to i and deliver 
                                           # them in one voyage with the cost = diff + 2
        return dp[n]
            



        
if __name__ == '__main__':   
    boxes = [[1,1],[2,1],[1,1]]
    print(Solution().boxDelivering(boxes, 2, 3, 3))
    boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]]
    print(Solution().boxDelivering(boxes, 3, 3, 6))
