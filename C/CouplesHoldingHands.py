'''
-Hard-

N couples sit in 2N seats arranged in a row and want to hold hands. We want to know 
the minimum number of swaps so that every couple is sitting side by side. A swap 
consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are 
numbered in order, the first couple being (0, 1), the second couple being (2, 3), 
and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is 
initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.

'''

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        """
        see detailed solution
        https://mli9502.github.io/2018/10/24/leetcode-765-Couples-Holding-Hands/

        Assume the size of the input array is N, If all the couples are seat next to 
        each other, we want the graph to have exactly N / 2 connected components as 
        shown in the [0, 0, 2, 2, 4, 4] graph.

        As a result, we can conclude that (the # of components we increased) == 
        (the # of swaps we have to do)

        Our gaol is to increase the total number of components to N / 2. Thus we 
        have (origional # of components) + (# of components we have to increase) == N / 2.
        """
        n = len(row)//2
        self.count = n # starting with n connected components for n groups
        roots = [i for i in range(n)]
        def find(i):
            while roots[i] != i:
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i 
        def union(i, j):
            x, y = find(i), find(j) 
            if x != y:
                roots[x] = y
                self.count -= 1
        # find the (origional # of connected components)
        for i in range(n):
            a = row[2*i]
            b = row[2*i + 1]
            union(a//2, b//2)
        # (# of swaps we have to do) == (# of components we have to increase) 
        # == N / 2 - (origional # of components)
        return n - self.count

if __name__=="__main__":
    print(Solution().minSwapsCouples([0, 2, 1, 3]))
