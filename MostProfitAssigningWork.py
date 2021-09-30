'''
-Medium-

You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with 
difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. 
If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

 

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0
 

Constraints:

n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 10^4
1 <= difficulty[i], profit[i], worker[i] <= 10^5


'''
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        df = list(zip(difficulty, profit))
        worker.sort()
        df.sort()
        pmax = [0]*len(df)
        mx = 0
        for i in range(len(df)):
            if mx < df[i][1]:
                mx = df[i][1]
            pmax[i] = mx
        i = j = 0 
        res = 0
        while i < len(df) and j < len(worker):
            if df[i][0] <= worker[j]:
                i += 1
            else:
                if i > 0:
                    res += pmax[i-1] 
                j += 1
        if i == len(df):
           while j < len(worker): 
               res += pmax[i-1] 
               j += 1
        return res



        




if __name__ == "__main__":
    print(Solution().maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], 
    worker = [4,5,6,7]))    
    print(Solution().maxProfitAssignment(difficulty = [85,47,57], profit = [24,66,99], 
    worker = [40,25,25]))
    print(Solution().maxProfitAssignment([13,37,58], [4,90,96],[34,73,45]))
    print(Solution().maxProfitAssignment([2,4,6,8,10],[10,20,30,40,50],[4,5,6,7]))
    print(Solution().maxProfitAssignment([7,20,68], [26,28,57], [71,20,71]))
    print(Solution().maxProfitAssignment([68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82]))