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
        """
        It is easy to get TLE, so how should we cut some branches and speed up the searching process?
        We use an array of length n to record the workload assigned to each worker.

        The core idea is that assume at certain point of dfs searching,
        we have the following workload for 10 workers,
        workers = [10, 5, 5, 5, 5, 5, 5, 5, 5, 5]

        if we want to assign the current task jobs[curr] to someone,
        it makes no difference if we assign it to any worker whose current workload is 5.
        Therefore we can use a set named seen to store searched workload such that we only search 5 once.

        There is also another branch cutting step, if the total workload is already larger than self.res,
        we can exit the dfs search, too.
        """
        workers = [0]*k
        
        self.res = sys.maxsize
        # jobs.sort(reverse = True)
        def dfs(curr):
            if curr == len(jobs):
                self.res = min(self.res, max(workers))
                return
            # because k is small (k<=12), using either a list of set
            # works the same 
            # seen = set() # record searched workload of workers
            seen = [] # record searched workload of workers
            for i in range(k):
                if workers[i] in seen: continue # if we have searched the workload of 5, skip it.
                if workers[i] + jobs[curr] >= self.res: continue # another branch cutting
                #seen.add(workers[i])
                seen.append(workers[i])
                workers[i] += jobs[curr]
                dfs(curr+1)
                workers[i] -= jobs[curr]
        
        dfs(0)
        return self.res

    def minimumTimeRequiredMoreTricks(self, jobs, k):
        '''
        If we just reverse sort the job, it makes it much slower. This is because all the long jobs will bias toward 
        earlier buckets.

        Another trick is to change the for loop. Instead of always looping from 0 through k - 1, change it such that 
        the first time iterates through (0, k), the second time iterates (1, k + 1), etc. So the first branch of 
        the dfs will even out the job assignment instead of frontloading all into the first bucket. This speeds up 
        runtime from ~480ms to ~80ms.
        '''
        workers = [0]*k
        jobs.sort(reverse=True)
        self.res = sys.maxsize
        self.start = 0
        
        def dfs(curr):
            self.start += 1
            if curr == len(jobs):
                self.res = min(self.res, max(workers))
                return
            
            seen = set() # record searched workload of workers
            for i in range(self.start, self.start + k):
                idx = i % k
                if workers[idx] in seen: continue # if we have searched the workload of 5, skip it.
                if workers[idx] + jobs[curr] >= self.res: continue # another branch cutting
                seen.add(workers[idx])
                workers[idx] += jobs[curr]
                dfs(curr+1)
                workers[idx] -= jobs[curr]
        
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
            return #False
        dfs(0)
        return self.res

    def minimumTimeRequiredBinarySearch(self, A, k):
        n = len(A)
        A.sort(reverse=True) # opt 1

        def dfs(i):
            if i == n: return True # opt 3
            for j in range(k):
                if cap[j] >= A[i]:
                    cap[j] -= A[i]
                    if dfs(i + 1): return True
                    cap[j] += A[i]
                if cap[j] == x: break # opt 2
            return False

        # binary search
        left, right = max(A), sum(A)
        while left < right:
            x = (left + right) / 2
            cap = [x] * k
            if dfs(0):
                right = x
            else:
                left = x + 1
        return left
        
        
if __name__ == "__main__":
    print(Solution().minimumTimeRequired([1,2,4,7,8], 2))
    print(Solution().minimumTimeRequired([9899456,8291115,9477657,9288480,5146275,7697968,8573153,3582365,3758448,9881935,2420271,4542202],9))
    print(Solution().minimumTimeRequiredLee([9899456,8291115,9477657,9288480,5146275,7697968,8573153,3582365,3758448,9881935,2420271,4542202],9))
    print(Solution().minimumTimeRequiredBinarySearch([9899456,8291115,9477657,9288480,5146275,7697968,8573153,3582365,3758448,9881935,2420271,4542202],9))