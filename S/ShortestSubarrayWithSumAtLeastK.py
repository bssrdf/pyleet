'''
-Hard-
*Monotonic Queue*
*Deque*

Return the length of the shortest, non-empty, contiguous subarray of A 
with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9

'''
from collections import deque

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        """
        这里用到了双向队列 deque，这是一种两头都能操作的飞起的数据结构。双向队列不像优先
        队列那样自动排序，这样就节省了排序的时间，我们是按照数组原顺序将数字下标加入双向
        队列的。在建立好累加和数组之和，遍历其每个累加和，然后用一个 while 循环，从
        双向队列的开头开始遍历，假如区间和之差大于等于K，就移除队首元素并更新结果 res。
        之后这个 while 循环非常重要，能有这么高的击败率，全要靠这个循环，这个是从双向
        队列的末尾开始往前遍历，假如当前区间和 sums[i] 小于等于队列末尾的区间和，则
        移除队列末尾元素。这是为啥呢？因为若数组都是正数，那么长度越长，区间和一定越大，
        则 sums[i] 一定大于所有双向队列中的区间和，但由于可能存在负数，从而使得长度变长，
        区间总和反而减少了，之前的区间和之差都没有大于等于K，现在的更不可能大于等于K，
        这个结束位置可以直接淘汰，不用进行计算。循环结束后将当前位置加入双向数组即可
        """
        n = len(A)
        q = deque()
        preSum = [0]*(n+1)
        res = n+1
        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + A[i-1]
        for i in range(n+1):
            while q and preSum[i]-preSum[q[0]] >= K:
                res = min(res, i-q[0])
                q.popleft()
            """
            设下标i和j满足j>i且sum[j]<sum[i]，设下标k满足k>j，若sum[k]-sum[i]>=K，
            则必然有sum[k]-sum[j]>=K，且k > j > i，即之后若存在和i位置相减满足大于
            等于K的位置，其和j位置相减必然满足大于等于K且其与j的距离更近，在这种情况
            下sum[i](i=q[-1])可被丢弃。
            """    
            while q and preSum[i] <= preSum[q[-1]]:                
                q.pop()
            q.append(i)
        return -1 if res == n+1 else res


if __name__ == "__main__":
    print(Solution().shortestSubarray([2,-1,2], 3))