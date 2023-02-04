'''
-Medium-
*Sliding Window*

You are given a 0-indexed integer array candies, where candies[i] represents 
the flavor of the ith candy. Your mom wants you to share these candies with 
your little sister by giving her k consecutive candies, but you want to keep 
as many flavors of candies as possible.

Return the maximum number of unique flavors of candy you can keep after 
sharing with your sister.

 

Example 1:

Input: candies = [1,2,2,3,4,3], k = 3
Output: 3
Explanation: 
Give the candies in the range [1, 3] (inclusive) with flavors [2,2,3].
You can eat candies with flavors [1,4,3].
There are 3 unique flavors, so return 3.
Example 2:

Input: candies = [2,2,2,2,3,3], k = 2
Output: 2
Explanation: 
Give the candies in the range [3, 4] (inclusive) with flavors [2,3].
You can eat candies with flavors [2,2,2,3].
There are 2 unique flavors, so return 2.
Note that you can also share the candies with flavors [2,2] and eat the candies with flavors [2,2,3,3].
Example 3:

Input: candies = [2,4,5], k = 0
Output: 3
Explanation: 
You do not have to give any candies.
You can eat the candies with flavors [2,4,5].
There are 3 unique flavors, so return 3.
 

Constraints:

1 <= candies.length <= 105
1 <= candies[i] <= 105
0 <= k <= candies.length

'''

from typing import List
from collections import Counter, defaultdict


class Solution:

    def maxUniqueCandies(self, candies: List[int], k: int) -> int:
        count = Counter(candies)
        ans = 0      
        for i,c in enumerate(candies): # Give out candies in window `[i-k+1, i]`
            count[c] -= 1 # Give out `A[i]`
            if i-k >= 0 :
                count[candies[i-k]] += 1 # Reclaim `A[i-k]`
            if count[c] == 0:
                count.pop(c)
            if i >= k-1: ans = max(ans, len(count)) # Take the maximum possible unique flavors left after giving out.
        return ans

    def maxUniqueCandies1(self, candies: List[int], k: int) -> int:
        # wrong answer
        count = Counter(candies)
        n = len(count)
        if k == 0: return n
        mi, mig, given = n, None, defaultdict(int)
        for i,c in enumerate(candies):
            given[c] += 1
            if i+1 > k:
                given[candies[i-k]] -= 1
                if given[candies[i-k]] == 0:
                    given.pop(candies[i-k])
            if mi > len(given):
                mi = len(given)
                mig = dict(given)
        ans = n
        for c in mig:
            if mig[c] == count[c]:
                ans -= 1
        return ans


if __name__ == "__main__":
    print(Solution().maxUniqueCandies(candies = [1,2,2,3,4,3], k = 3))
    print(Solution().maxUniqueCandies(candies = [2,2,2,2,3,3], k = 2))
    print(Solution().maxUniqueCandies(candies = [2,4,5], k = 0))