'''

-Hard-
*Combinatorics"
*DP*
*Divide and Conquer*

Given an array nums that represents a permutation of integers from 1 to n. We are 
going to construct a binary search tree (BST) by inserting the elements of nums 
in order into an initially empty BST. Find the number of different ways to reorder 
nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, 
and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields 
a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to 
the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:


Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
Example 2:


Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
Example 3:


Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.

Hints:

If the subtree doesn't contain 1, then the missing value will always be 1.

What data structure allows us to dynamically update the values that are currently not present?

'''
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        table = [[] for _  in range(n+1)]
        for i in range(n+1):
            table[i] = [1]*(i+1)
            for j in range(1, i):
                table[i][j] = (table[i-1][j-1] + table[i-1][j]) % MOD 
        def dfs(arr):
            m = len(arr)
            if m <= 2: return 1
            left, right = [], []
            for i in range(1, m):
                if arr[i] < arr[0]:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
            l = dfs(left)
            r = dfs(right)
            # note the use m-1 intead of m below 
            # the reason is arr[0] is the root of the subtree
            # what we need is C(len(left)+len(right), len(left))
            # and len(left)+len(right) = m-1
            return (((table[m-1][len(left)]*l)%MOD)*r)%MOD
        return dfs(nums)%MOD - 1 # - 1 is to account for the original permutation            
        # for t in table:
        #     print(t)

if __name__ == "__main__":
    print(Solution().numOfWays([3,4,5,1,2]))
        