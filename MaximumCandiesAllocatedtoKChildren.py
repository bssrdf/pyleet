'''

-Medium-
*Binary Search*


You are given a 0-indexed integer array candies. Each element in the array denotes 
a pile of candies of size candies[i]. You can divide each pile into any number 
of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children 
such that each child gets the same number of candies. Each child can take at most 
one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.

 

Example 1:

Input: candies = [5,8,6], k = 3
Output: 5
Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.
Example 2:

Input: candies = [2,5], k = 11
Output: 0
Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.
 

Constraints:

1 <= candies.length <= 105
1 <= candies[i] <= 107
1 <= k <= 1012



'''
from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        A = candies
        n = len(candies)        
        if sum(A) < k: return 0
        l, r = 1, max(A)+1
        def canAllocate(m):
            sums = 0
            for i in A:
                sums += i // m
            return sums >= k
        while l < r:
            mid = l + (r-l)//2
            if canAllocate(mid):
                l = mid + 1 
            else:
                r = mid
            # print(l,r,mid)
        return l-1




if __name__ == "__main__":
    print(Solution().maximumCandies(candies = [5,8,6], k = 3))
    print(Solution().maximumCandies(candies = [5,8,6], k = 4))
    print(Solution().maximumCandies(candies = [5,8,6], k = 5))
    print(Solution().maximumCandies(candies = [1,2,3,4,10], k = 5))
    print(Solution().maximumCandies([9,10,1,2,10,9,9,10,2,2],3))