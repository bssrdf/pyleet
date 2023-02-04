'''
-Medium-
*Greedy*
*Priority Queue*

You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where 
tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process 
at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.

If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. 
If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.

Once a task is started, the CPU will process the entire task without stopping.

The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.

 

Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
Example 2:

Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.
 

Constraints:

tasks.length == n
1 <= n <= 10^5
1 <= enqueueTimei, processingTimei <= 10^9


'''
from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        newtasks = [(c, d, i) for i,(c,d) in enumerate(tasks)]
        n = len(newtasks)
        newtasks.sort()
        pq = [(newtasks[0][1], newtasks[0][2], newtasks[0][0])]
        res, j = [], 1
        curTime = newtasks[0][0]
        while pq:
            d, i, c = heapq.heappop(pq)
            curTime += d
            res.append(i)
            while j < n and newtasks[j][0] <= curTime:
                heapq.heappush(pq, (newtasks[j][1], newtasks[j][2], newtasks[j][0])) 
                j += 1
            if not pq and j < n:
                heapq.heappush(pq, (newtasks[j][1], newtasks[j][2], newtasks[j][0])) 
                curTime = newtasks[j][0]
                j += 1        
        return res
            




        

if __name__ == "__main__":
    #print(Solution().getOrder(tasks = [[1,2],[2,4],[3,2],[4,1]]))
    #print(Solution().getOrder(tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]))
    tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],
            [33,6],[45,4],[18,18],[46,39],[12,24]]
    #for i,v in enumerate(tasks):
    #    print(i,v)
    #print(Solution().getOrder(tasks))
    tasks = [[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]]
    #print(Solution().getOrder(tasks))
    tasks =[[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]
    print(Solution().getOrder(tasks))