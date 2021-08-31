'''
-Hard-
*Backtracking*

You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. 
The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. 
Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.

 

Example 1:

Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.
Example 2:

Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.
 

Constraints:

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 10^7


'''
import sys

class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        workers = [0]*k
        
        self.res = sys.maxsize
        # jobs.sort(reverse = True)
        def dfs(curr):
            if curr == len(jobs):
                self.res = min(self.res, max(workers))
                return
            
            seen = set() # record searched workload of workers
            for i in range(k):
                if workers[i] in seen: continue # if we have searched the workload of 5, skip it.
                if workers[i] + jobs[curr] >= self.res: continue # another branch cutting
                seen.add(workers[i])
                workers[i] += jobs[curr]
                dfs(curr+1)
                workers[i] -= jobs[curr]
        
        dfs(0)
        return self.res
    def minimumTimeRequiredLee(self, jobs, k):
        A = jobs
        n = len(A)
        #A.sort(reverse=True) # opt 1, not sorting is faster
        self.res = sum(A)
        count = [0] * k

        def dfs(i):
            if i == n:
                self.res = min(self.res, max(count))
                return
            for j in range(k):
                if count[j] + A[i] < self.res: # opt 3
                    count[j] += A[i]
                    dfs(i + 1)
                    count[j] -= A[i]
                if count[j] == 0: break # opt 2
            return False
        dfs(0)
        return self.res
        
        
if __name__ == "__main__":
    print(Solution().minimumTimeRequired([1,2,4,7,8], 2))