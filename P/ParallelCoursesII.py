'''
-Hard-

*BFS*

*Bit Mask*


Given the integer n representing the number of courses at some university labeled from 1 to n, 
and the array dependencies where dependencies[i] = [xi, yi] represents a prerequisite 
relationship, that is, the course xi must be taken before the course yi. Also, you are 
given the integer k.

In one semester you can take at most k courses as long as you have taken all the prerequisites 
for the courses you are taking.

Return the minimum number of semesters to take all courses. It is guaranteed that you can take 
all courses in some way.

 

Example 1:



Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
Output: 3 
Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.
Example 2:



Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4 
Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.
Example 3:

Input: n = 11, dependencies = [], k = 2
Output: 6
 

Constraints:

1 <= n <= 15
1 <= k <= n
0 <= dependencies.length <= n * (n-1) / 2
dependencies[i].length == 2
1 <= xi, yi <= n
xi != yi
All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
The given graph is a directed acyclic graph.

'''
from itertools import permutations
from collections import deque
from itertools import combinations

class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        def bitsoncount(x):
            return bin(x).count('1')
        def numberOfSetBits(i):
            i = i - ((i >> 1) & 0x55555555)
            i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
            return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24
        pre = [0]*n # pre[i]: the bit representation of all dependencies of course i
        for e in dependencies:
            e[0] -= 1
            e[1] -= 1
            pre[e[1]] |= 1 << e[0]

        # i is the bit representation of a combination of courses. 
        # dp[i] is the minimum days to complete all the courses
        dp = [n] * (1 << n)
        # no need time to finish 0 courses
        dp[0] = 0
        for i in range(1 << n):
            ex = 0
            # find  out ex, the bit representation of the all courses that we can study now.
            # since we have i and pre[j], we know course j can be studied if i contains all it's prerequisites ((i & pre[j]) == pre[j])
            for j in range(n): 
                if (i & pre[j]) == pre[j]: ex |= 1 << j
            # we don't want to study anything from what we have already studied (i represents set of courses that we have studied)
            ex &= ~i
            # enumerate all the bit 1 combinations of ex
            # this is a typical method to enumerate all subsets of a bit representation:
            # for (int i = s; i; i = (i - 1) &ｓ)
            #  __builtin_popcount counts bits == 1 
            #for(int s = ex; s; s = (s - 1) & ex) if(__builtin_popcount(s) <= k)
            s = ex
            while s: 
                # any combination of courses (if less or equal than k) could be studied at 
                # this step
                # i | s means what we combine already studied courses before with courses 
                #  we can study at the current step
                #print(i, s)
                #if bitsoncount(s) <= k:
                if numberOfSetBits(s) <= k:
                    dp[i | s] = min(dp[i | s], dp[i] + 1)
                s = (s - 1) & ex
        # dp.back is the state when we studied all the courses. e.g. 11111...
        return dp[-1] 
    
    def minNumberOfSemestersAC(self, n, dependencies, k):
        dp = [[(100, 0, 0)] * n for _ in range(1<<n)]
        
        bm_dep = [0]*(n)
        for i,j in dependencies:
            bm_dep[j-1]^=(1<<(i-1))

        for i in range(n):
            if bm_dep[i] == 0: dp[1<<i][i] = (1, 1, 1<<i)
        
        for i in range(1<<n):
            n_z_bits = [len(bin(i))-p-1 for p,c in enumerate(bin(i)) if c=="1"]
                    
            for t, j in permutations(n_z_bits, 2):
                if bm_dep[j] & i == bm_dep[j]:
                    cand, bits, mask = dp[i^(1<<j)][t]
                    if bm_dep[j] & mask == 0 and bits < k:
                        dp[i][j] = min(dp[i][j], (cand, bits + 1, mask + (1<<j)))
                    else:
                        dp[i][j] = min(dp[i][j], (cand+1, 1, 1<<j))
                                          
        return min([i for i, j, k in dp[-1]])    

    def minNumberOfSemestersBFS(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        pre = [0]*n
        occupy = [20]*(1<<(n))
        for dep in dependencies:
            pre[dep[1]-1] += 1<<(dep[0]-1)
        queue = deque([[0,0]])
        while queue:
            [num,step] = queue.popleft()
            nextlist = []
            for i in range(n):
                if pre[i]&num != pre[i]: continue # prerequisite not taken yet
                if (1<<i)&num: continue # course i already taken
                nextlist.append(i) # we can take course i in this semester    
            if len(nextlist)<=k:
                for ele in nextlist: num += 1<<ele
                if num+1==1<<n: return step+1 # we have taken all n courses 
                if occupy[num]>step+1: 
                    queue.append([num,step+1])
                    occupy[num] = step+1
            else:
                thelist = combinations(nextlist,k)
                for seq in thelist:
                    temp = num
                    for ele in list(seq): temp += 1<<ele
                    if occupy[temp]>step+1:
                        queue.append([temp,step+1])
                        occupy[temp] = step + 1

if __name__ == "__main__":
    print(Solution().minNumberOfSemesters(5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2))
    print(Solution().minNumberOfSemesters(15, dependencies = [[2,1]], k = 4))