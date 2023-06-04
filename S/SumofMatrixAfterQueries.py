'''
-Medium-


You are given an integer n and a 0-indexed 2D array queries where queries[i] = [typei, indexi, vali].

Initially, there is a 0-indexed n x n matrix filled with 0's. For each query, you must apply one of the following changes:

if typei == 0, set the values in the row with indexi to vali, overwriting any previous values.
if typei == 1, set the values in the column with indexi to vali, overwriting any previous values.
Return the sum of integers in the matrix after all queries are applied.

 

Example 1:


Input: n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
Output: 23
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 23. 
Example 2:


Input: n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
Output: 17
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 17.
 

Constraints:

1 <= n <= 104
1 <= queries.length <= 5 * 104
queries[i].length == 3
0 <= typei <= 1
0 <= indexi < n
0 <= vali <= 105


'''
from typing import List

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row, col = set(), set() 
        ans = 0
        for t,i,v in queries[::-1]:
            if t == 0:
                if i not in row:
                    ans += (n-len(col))*v
                    row.add(i)
            else:
                if i not in col:
                    ans += (n-len(row))*v 
                    col.add(i)
        return ans   



if __name__ == '__main__':
    print(Solution().matrixSumQueries(n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]))
    print(Solution().matrixSumQueries(n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]))
    n = 8
    queries = [[0,6,30094],[0,7,99382],[1,2,18599],[1,3,49292],[1,0,81549],[1,1,38280],[0,0,19405],[0,4,30065],[1,4,60826],[1,5,9241],[0,5,33729],[0,1,41456],[0,2,62692],[0,3,30807],[1,7,70613],[1,6,9506],[0,5,39344],[1,0,44658],[1,1,56485],[1,2,48112],[0,6,43384]]
    print(Solution().matrixSumQueries(n = n, queries= queries))