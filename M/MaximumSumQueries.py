'''

-Hard-
*Sorting*
*Binary Search*
*Monotonic Stack*

You are given two 0-indexed integer arrays nums1 and nums2, each of length n, and a 1-indexed 2D array queries where queries[i] = [xi, yi].

For the ith query, find the maximum value of nums1[j] + nums2[j] among all indices j (0 <= j < n), where nums1[j] >= xi and nums2[j] >= yi, or -1 if there is no j satisfying the constraints.

Return an array answer where answer[i] is the answer to the ith query.

 

Example 1:

Input: nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]
Output: [6,10,7]
Explanation: 
For the 1st query xi = 4 and yi = 1, we can select index j = 0 since nums1[j] >= 4 and nums2[j] >= 1. The sum nums1[j] + nums2[j] is 6, and we can show that 6 is the maximum we can obtain.

For the 2nd query xi = 1 and yi = 3, we can select index j = 2 since nums1[j] >= 1 and nums2[j] >= 3. The sum nums1[j] + nums2[j] is 10, and we can show that 10 is the maximum we can obtain. 

For the 3rd query xi = 2 and yi = 5, we can select index j = 3 since nums1[j] >= 2 and nums2[j] >= 5. The sum nums1[j] + nums2[j] is 7, and we can show that 7 is the maximum we can obtain.

Therefore, we return [6,10,7].
Example 2:

Input: nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]
Output: [9,9,9]
Explanation: For this example, we can use index j = 2 for all the queries since it satisfies the constraints for each query.
Example 3:

Input: nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]
Output: [-1]
Explanation: There is one query in this example with xi = 3 and yi = 3. For every index, j, either nums1[j] < xi or nums2[j] < yi. Hence, there is no solution. 
 

Constraints:

nums1.length == nums2.length 
n == nums1.length 
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 109 
1 <= queries.length <= 105
queries[i].length == 2
xi == queries[i][1]
yi == queries[i][2]
1 <= xi, yi <= 109

'''

from typing import List
from collections import defaultdict
from bisect import bisect_left
class Solution:

    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        x = sorted([(a,b) for a,b in zip(nums1,nums2)], reverse=True)
        q = sorted([(a,b,i) for i,(a,b) in enumerate(queries)], reverse=True)
        i, maxy = 0, 0
        res = defaultdict(int)
        stk = []
        for a,b,j in q:
            while i < len(x) and x[i][0] >= a:
                xi, yi = x[i]
                if yi > maxy:
                    maxy = x[i][1]
                    while stk and stk[-1][1] < xi+yi:
                        stk.pop()
                    stk.append((maxy, xi+yi))
                # note: if yi <= maxy, this pair can be ignored for the following reason
                # there already exists in d a pair (xp, yp) where xp + yp > xi + yi      
                # since xp >= xi and yp >= yi 
                i += 1
            print(stk)
            try:
                res[j] = stk[bisect_left(stk, (b, 0))][1]
            except:
                res[j] = -1
        return [res[i] for i in range(len(q))]
    
if __name__ == "__main__":
    # print(Solution().maximumSumQueries(nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]))
    print(Solution().maximumSumQueries(nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5],[1,2]]))