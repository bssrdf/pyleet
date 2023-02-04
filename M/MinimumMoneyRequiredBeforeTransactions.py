'''

-Hard-
*Greedy*

You are given a 0-indexed 2D integer array transactions, where transactions[i] = [costi, cashbacki].

The array describes transactions, where each transaction must be completed exactly once in some order. At any given moment, you have a certain amount of money. In order to complete transaction i, money >= costi must hold true. After performing a transaction, money becomes money - costi + cashbacki.

Return the minimum amount of money required before any transaction so that all of the transactions can be completed regardless of the order of the transactions.

 

Example 1:

Input: transactions = [[2,1],[5,0],[4,2]]
Output: 10
Explanation:
Starting with money = 10, the transactions can be performed in any order.
It can be shown that starting with money < 10 will fail to complete all transactions in some order.
Example 2:

Input: transactions = [[3,0],[0,3]]
Output: 3
Explanation:
- If transactions are in the order [[3,0],[0,3]], the minimum money required to complete the transactions is 3.
- If transactions are in the order [[0,3],[3,0]], the minimum money required to complete the transactions is 0.
Thus, starting with money = 3, the transactions can be performed in any order.
 

Constraints:

1 <= transactions.length <= 105
transactions[i].length == 2
0 <= costi, cashbacki <= 109



'''

from typing import List

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # O(NlogN)
        T = transactions
        loss = [t for t in T  if t[1] < t[0]]
        gain = max((t[0] for t in T  if t[1] >= t[0]), default=None)
        loss.sort(key = lambda x: x[1])
        # gain.sort(key = lambda x: -x[0])
        ans, t = 0, 0
        for a,b in loss:
            t += a
            ans = max(ans, t) 
            t -= b
        if gain:            
            t += gain
            ans = max(ans, t)                
        return ans
    

    def minimumMoney2(self, transactions: List[List[int]]) -> int:
        # O(N)
        A = transactions
        res = v = 0
        for i,j in A:
            res += max(0, i - j)
            v = max(v, min(i, j))
        return res + v


if __name__=="__main__":
    print(Solution().minimumMoney(transactions = [[5,3],[10,0],[3,2]]))
    print(Solution().minimumMoney(transactions = [[10,0],[6,3],[5,3]]))
    # print(Solution().minimumMoney(transactions = [[2,1],[5,0],[4,2]]))
    # print(Solution().minimumMoney(transactions = [[3,0],[0,3]]))
    print(Solution().minimumMoney(transactions = [[7,2],[0,10],[5,0],[4,1],[5,8],[5,9]]))