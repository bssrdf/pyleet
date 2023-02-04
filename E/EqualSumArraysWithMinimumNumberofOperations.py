'''

-Medium-

*Greedy*

You are given two arrays of integers nums1 and nums2, possibly of different 
lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays 
to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values 
in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not 
possible to make the sum of the two arrays equal.

 

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6


'''

from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)        
        if n1 > 6*n2 or 6*n1 < n2:
            return -1
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        sum1, sum2 = sum(nums1), sum(nums2)
        def getOps(small, large, diff):
            diffs = Counter()
            for i in range(1, 6):
                diffs[6-i] += small[i]
            for j in range(6, 1, -1):
                diffs[j-1] += large[j]
            ops = 0
            i = 5
            while i > 0 and diff > 0:
                cnt = diffs[i]
                maxReduce = i*cnt
                if maxReduce < diff:
                    diff -= maxReduce
                    ops += cnt
                else:
                    cur = diff // i
                    if diff % i:
                        cur += 1
                    ops += cur
                    diff = 0
                i -= 1
            return ops    
        if sum1 == sum2: return 0
        elif sum1 < sum2: return getOps(cnt1, cnt2, sum2-sum1)
        else: return getOps(cnt2, cnt1, sum1-sum2)



        

if __name__ == "__main__":
    print(Solution().minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]))