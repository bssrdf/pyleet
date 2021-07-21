'''
-Medium-

You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those 
indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, 
then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions, the final 
array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). 
Return the minimum possible value of answer.length.

 

Example 1:

Input: strs = ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, strs = ["a", "b", "c"].
Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.
Example 2:

Input: strs = ["xc","yb","za"]
Output: 0
Explanation: 
strs is already in lexicographic order, so we do not need to delete anything.
Note that the rows of strs are not necessarily in lexicographic order:
i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)
Example 3:

Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: We have to delete every column.
 

Constraints:

n == strs.length
1 <= n <= 100
1 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


'''

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        A = strs
        res, n, m = 0, len(A), len(A[0])
        is_sorted = [0] * (n - 1)
        for j in range(m):
            is_sorted2 = is_sorted[:]
            for i in range(n - 1):
                if A[i][j] > A[i + 1][j] and is_sorted[i] == 0:
                    res += 1
                    break
                is_sorted2[i] |= A[i][j] < A[i + 1][j]
            else:
                is_sorted = is_sorted2
        return res

    def minDeletionSizeSet(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        A = strs
        res, n, m = 0, len(A), len(A[0])
        unsorted = set(range(n - 1))
        for j in range(m):
            if any(A[i][j] > A[i + 1][j] for i in unsorted):
                res += 1
            else:
                unsorted -= {i for i in unsorted if A[i][j] < A[i + 1][j]}
            print(unsorted)
        return res

if __name__ == "__main__": 
    print(Solution().minDeletionSizeSet(["ca","bb","ac"]))

    print(Solution().minDeletionSizeSet(["zyx","wvu","tsr"]))
    print(Solution().minDeletionSizeSet(["xc","yb","za"]))
    print(Solution().minDeletionSizeSet(["wyx","wvu","xsr"]))
