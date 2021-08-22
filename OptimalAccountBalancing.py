'''
-Hard-
*BFS*
*DFS*

题目大意：

有一群朋友去度假，度假期间，他们会相互借钱，比如 Alice 帮助Bill支付了他的午饭费用10美金，
之后 Chris 帮助 Alice 支付了5美金的打车费。我们将每笔借款使用（x,y,z）来表示，即x借了
z美金给y假设Alice, Bill和Chris 的编号分别是0，1，2。那么上述所有的借款可以表示为 
[[0, 1, 10], [2, 0, 5]]。

题目会给出一群人的所有借款情况，求将所有欠款还清最少需要多少次。

注意：

每笔借款使用 (x, y, z) 的形式表示，其中x!=y, z>0。
每个人的id不一定是连续的，他们的id可能是0，1，2。也可能是0，2，6。
示例1：

输入:
[[0,1,10], [2,0,5]]

输出:
2

解释:
Person #0 借给 person #1 10美金.
Person #2  借给 person #0 5美金.

我们需要2笔还款. 一种方式是 person #1 分别还给 person #0 和 #2 各5美金.
示例2：

输入:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

输出:
1

解释:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.

Given a directed graph where each edge is represented by a tuple, such as [u, v, w] 
represents an edge with a weight w from u to v.
You need to calculate at least the need to add the number of edges to ensure that each 
point of the weight are balancing. That is, the sum of weight of the edge pointing to 
this point is equal to the sum of weight of the edge of the point that points to the 
other point.

1.Note that u ≠ v and w > 0.
2.index may not be linear, e.g. we could have the points 0, 1, 2 or we could also 
have the points 0, 2, 6.

样例
Example 1

Input: [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Two edges are need to added. There are [1,0,5] and [1,2,5]
Example 2

Input: [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Only one edge need to added. There is [1,0,4]


'''

from collections import defaultdict
from collections import deque

class Solution:
    """
    @param edges: a directed graph where each edge is represented by a tuple
    @return: the number of edges
    """
    def balanceGraph(self, edges):
        # Write your code here
        m = defaultdict(int)
        for u,v,w in edges:
            m[u] -= w
            m[v] += w
        res, s = 0, []   
        #print(m)
        for i in m.values():
            if i == 0: continue
            if -i in s:
                s.remove(-i)
                res += 1 
                continue
            s.append(i)            
        balance = list(s)
        print(balance)
        ans = [float('inf')]        
        def helper(accnt, start, cnt): 
            n = len(accnt)
            while start < n and accnt[start] == 0: start +=1
            if start == n:
                ans[0] = min(ans[0], cnt)
                return
            for i in range(start + 1, n):
                if accnt[i] * accnt[start] < 0:
                    accnt[i] += accnt[start]
                    helper(accnt, start + 1, cnt + 1)
                    accnt[i] -= accnt[start]
        def dfs(arr, idx):
            if idx == len(arr): return 0
            cur = arr[idx]
            if cur == 0: return dfs(arr, idx+1)
            ans = float('inf')
            for i in range(idx+1, len(arr)):
                nxt = arr[i]
                if cur*nxt < 0:
                    diff = cur + nxt
                    arr[i] = diff
                    ans = min(ans, dfs(arr, idx+1)+1)
                    arr[i] = nxt
            if ans == float('inf'): ans = 0
            return ans
        helper(balance, 0, 0)
        return res + ans[0]     
        #return res + dfs(balance, 0)
    def balanceGraphBFS(self, edges):
        # Write your code here

        def bfs(non_zero):
            q = deque()
            q.append(([0], non_zero[0][1]))
            min_set = None
            n = len(non_zero)
            while q:
                cur_set, balance_sum = q.popleft()
                if balance_sum == 0:
                    min_set = cur_set # all nodes in cur_set sums to 0 
                    break
                for i in range(cur_set[-1] + 1, n):
                    q.append((cur_set + [i], balance_sum + non_zero[i][1]))
                    
            min_set = set(min_set) 
            return [non_zero[i] for i in range(n) if i not in min_set]
        
        account = defaultdict(int)
        
        for i, j, c in edges:
            account[i] -= c
            account[j] += c
        
        non_zero = [(people, balance) for people, balance in account.items() if balance != 0]
        
        non_zero = sorted(non_zero, key = lambda a : a[1])
        print(non_zero)
        res = len(non_zero)
        
        while len(non_zero) > 0:
            non_zero = bfs(non_zero)
            print(non_zero)
            res -= 1
        return res


if __name__ == "__main__":
    print(Solution().balanceGraph([[0,1,10],[2,0,5]]))
    print(Solution().balanceGraphBFS([[0,1,10],[2,0,5]]))
    #edges = [[11,16,1],[12,15,59],[9,5,46],[7,6,92],[7,6,92],[2,3,93],[6,8,96],[15,11,39],[2,4,36],[3,1,23],[3,4,42],[8,7,45],[7,9,24],[4,3,17],[10,11,89],[5,7,65],[6,5,91],[0,1,2],[3,4,24],[4,1,41]]
    #print(Solution().balanceGraph(edges)) #TLE
    #print(Solution().balanceGraphBFS(edges))