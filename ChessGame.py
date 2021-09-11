'''
-Easy-
*Hash Table*
*Diagonal*

In a game of chess, you are given two binary arrays:
a binary array queen with size N, which represents the coordinates of N queens;
a binary array knight with size M, which represents the coordinates of M knights.
A queen can attack any knight chess in the same row, column and diagonal.
You are asked to return an answer array with size M, the ith element of which 
shows whether the ith knight can be attacked.

1 \leq N,M \leq 10^51≤N,M≤10 
5
 
The range of chess coordinates is a positive integer from 11 to 10^910 
9
 

样例
Example:
Input: [[1,1],[2,2]]
[[3,3],[1,3],[4,5]]
Output: [true,true,false]
Explanation: The first knight can be attacked by queen 1 and 2.
The second knight can be attacked by queen 1 and 2.
The last knight can not be attacked.


'''


class Solution:
    """
    @param queen: queen‘coordinate
    @param knight: knight‘coordinate
    @return: if knight is attacked please return true，else return false
    """
    def isAttacked(self, queen, knight):
        # write your code here
        # write your code here
        n = len(queen)
        m = len(knight)
        Row = set()
        Column = set()
        Diagonal = set()
        Diagonal2 = set()

        for i in range(n):
            Row.add(queen[i][0])
            Column.add(queen[i][1])
            Diagonal.add(queen[i][1] - queen[i][0])
            Diagonal2.add(queen[i][1] + queen[i][0])

        ans = [False] * m

        for i in range(m):
            if knight[i][0] in Row or knight[i][1] in Column or  \
               (knight[i][1] - knight[i][0]) in Diagonal  or  \
               (knight[i][1] + knight[i][0]) in Diagonal2:
                   ans[i] = True

        return ans

