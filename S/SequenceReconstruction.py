'''
-Medium-


Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. 
The org sequence is a permutation of the integers from 1 to n, with 1 \leq n \leq 10^41≤n≤10 
4
 . Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., 
 a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether 
 there is only one sequence that can be reconstructed from seqs and it is the org sequence.

样例
Example 1:

Input:org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output:true


'''
from collections import defaultdict, deque

class Solution(object):
    def sequenceReconstruction(self, org, seqs):        
        n = len(org)
        if not org and seqs: return True
        pos, flags = [0]*(n+1), [0]*(n+1)        
        existed = False
        cnt = n-1
        for i in range(n):
            pos[org[i]] = i
        for seq in seqs:
            for i in range(len(seq)):
                existed = True
                if seq[i] < 1 or seq[i] > n: return False
                if i > 0:
                    pre, cur = seq[i-1], seq[i]
                    if pos[pre] >= pos[cur]: return False 
                    if flags[cur] == 0 and pos[pre]+1 == pos[cur]:
                        flags[cur] = 1
                        cnt -= 1
        print(cnt)
        return cnt == 0 and existed
                
         


        


if __name__ == "__main__":
    print(Solution().sequenceReconstruction(org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]))
    print(Solution().sequenceReconstruction(org = [], seqs = [[]]))
    print(Solution().sequenceReconstruction(org = [1,2,3], seqs = [[1,2],[1,3]]))