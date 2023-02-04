'''
-Medium-
*DP*

Given an array of unique integers, arr, where each integer arr[i] is strictly greater 
than 1.

We make a binary tree using these integers, and each number may be used for any 
number of times. Each non-leaf node's value should be equal to the product of the 
values of its children.

Return the number of binary trees we can make. The answer may be too large so return 
the answer modulo 10^9 + 7.

 

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], 
[10, 5, 2].
 

Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 10^9


'''
from collections import defaultdict

class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        dp = defaultdict(int)
        for i in range(len(arr)):
            dp[arr[i]] = 1
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i]//arr[j] in dp:
                    dp[arr[i]] = (dp[arr[i]] + dp[arr[j]] * dp[arr[i]//arr[j]]) \
                                 % (10**9+7)
        res = 0
        for t in dp: res = (res + dp[t]) % (10**9+7)
        return res

if __name__=="__main__":
    print(Solution().numFactoredBinaryTrees([2,4,5,10]))