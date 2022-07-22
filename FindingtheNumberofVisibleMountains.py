'''
-Medium-

You are given a 0-indexed 2D integer array peaks where peaks[i] = [xi, yi] states that mountain i has a peak at coordinates (xi, yi). A mountain can be described as a right-angled isosceles triangle, with its base along the x-axis and a right angle at its peak. More formally, the gradients of ascending and descending the mountain are 1 and -1 respectively.

A mountain is considered visible if its peak does not lie within another mountain (including the border of other mountains).

Return the number of visible mountains.

 

Example 1:



Input: peaks = [[2,2],[6,3],[5,4]]
Output: 2
Explanation: The diagram above shows the mountains.
- Mountain 0 is visible since its peak does not lie within another mountain or its sides.
- Mountain 1 is not visible since its peak lies within the side of mountain 2.
- Mountain 2 is visible since its peak does not lie within another mountain or its sides.
There are 2 mountains that are visible.
Example 2:



Input: peaks = [[1,3],[1,3]]
Output: 0
Explanation: The diagram above shows the mountains (they completely overlap).
Both mountains are not visible since their peaks lie within each other.
 

Constraints:

1 <= peaks.length <= 105
peaks[i].length == 2
1 <= xi, yi <= 105


'''

from typing import List
from collections import defaultdict
class Solution:
    def numberOfMountains(self, peaks: List[int]) -> int:
        m = defaultdict(int)
        for p in peaks:
            m[tuple(p)] += 1
        invs = [[min(x+y, x-y), max(x+y, x-y)] for x,y in m if m[(x,y)] == 1] 
        invs.sort()
        # print(invs)
        i, ans = 0, 0
        while i < len(invs):
            ans += 1
            j = i+1
            while j < len(invs) and invs[j][1] <= invs[i][1]:
                j += 1
            i = j                 
        return ans

if __name__ == "__main__":
    print(Solution().numberOfMountains(peaks = [[2,2],[6,3],[5,4]]))
    print(Solution().numberOfMountains(peaks = [[2,2],[6,3],[4,6]]))
    print(Solution().numberOfMountains(peaks = [[1,3],[1,3]]))
    print(Solution().numberOfMountains(peaks = [[2,2],[6,3],[9,2],[10,3]]))
    print(Solution().numberOfMountains(peaks = [[2,2],[6,3],[1,3],[1,3],[9,2],[10,3]]))


