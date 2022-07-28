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
from collections import defaultdict, Counter
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

    def numberOfMountains2(self, peaks: List[int]) -> int:
        m = defaultdict(int)
        for x,y in peaks:
            tup = (x-y, x+y)
            m[tup] += 1
        invs = [item for item in m if m[item] == 1] 
        invs.sort(key=lambda x: (x[0], -x[1]))
        # print(invs)
        stack = []
        for iv in invs:
            if not stack or iv[1] > stack[-1][-1]:
                stack.append(iv)                 
        return len(stack)

    def numberOfMountains3(self, peaks: List[int]) -> int:
        aux = defaultdict(int)
        for x,y in peaks:
            tup = (x-y, x+y)
            aux[tup] += 1
        aux = {item for item in aux if aux[item] == 1}
        invs = sorted(aux, key=lambda x: [x[0], -x[1]])
        # print(invs)
        stack = []
        for a,b in invs:
            if not stack or b> stack[-1][-1]:
                stack.append((a,b))                 
        return len(stack)

    def numberOfMountains4(self, peaks: List[int]) -> int:
        # correct solution
        invs = [(x-y, x+y) for x,y in peaks]
        invs.sort()
        s,e = -float('inf'), -float('inf')
        cnt = 0
        for a, b in invs:
            if a == s:
                if b > e:
                    s, e = a, b
                    cnt += 1
                if b == e:
                    cnt -= 1
                    cnt = max(cnt, 0)
            else:
                if b > e:
                    cnt += 1
                    s, e = a, b
        return cnt

    def numberOfMountains5(self, peaks: List[int]) -> int:
        count = Counter((x, y) for x, y in peaks)
        peaks = sorted([k for k, v in count.items() if v == 1])
        stack = []

        # returns True if `peak1` is hidden by `peak2`
        def isHidden(peak1: List[int], peak2: List[int]) -> bool:
            x1, y1 = peak1
            x2, y2 = peak2
            return x1 - y1 >= x2 - y2 and x1 + y1 <= x2 + y2

        for i, peak in enumerate(peaks):
            while stack and isHidden(peaks[stack[-1]], peak):
                stack.pop()
            if stack and isHidden(peak, peaks[stack[-1]]):
                continue
            stack.append(i)

        return len(stack)




if __name__ == "__main__":
    # print(Solution().numberOfMountains(peaks = [[2,2],[6,3],[5,4]]))
    # print(Solution().numberOfMountains(peaks = [[2,2],[6,3],[4,6]]))
    # print(Solution().numberOfMountains(peaks = [[1,3],[1,3]]))
    # print(Solution().numberOfMountains(peaks = [[1,3],[1,3], [1,2]]))
    # print(Solution().numberOfMountains(peaks = [[2,2],[6,3],[9,2],[10,3]]))
    # print(Solution().numberOfMountains(peaks = [[2,2],[6,3],[1,3],[1,3],[9,2],[10,3]]))

    # print(Solution().numberOfMountains2(peaks = [[2,2],[6,3],[5,4]]))
    # print(Solution().numberOfMountains2(peaks = [[2,2],[6,3],[4,6]]))
    # print(Solution().numberOfMountains2(peaks = [[1,3],[1,3]]))
    # print(Solution().numberOfMountains2(peaks = [[1,3],[1,3], [1,2]]))
    # print(Solution().numberOfMountains2(peaks = [[2,2],[6,3],[9,2],[10,3]]))
    # print(Solution().numberOfMountains2(peaks = [[2,2],[6,3],[1,3],[1,3],[9,2],[10,3]]))

    # print(Solution().numberOfMountains3(peaks = [[1,3],[1,3], [1,2]]))
    # print(Solution().numberOfMountains4(peaks = [[1,3],[1,3], [1,2]]))

    print(Solution().numberOfMountains3(peaks = [[2,2],[6,3],[5,4]]))
    print(Solution().numberOfMountains3(peaks = [[2,2],[6,3],[4,6]]))
    print(Solution().numberOfMountains3(peaks = [[1,3],[1,3]]))
    print(Solution().numberOfMountains3(peaks = [[1,3],[1,3], [1,2]]))
    print(Solution().numberOfMountains3(peaks = [[2,2],[6,3],[9,2],[10,3]]))
    print(Solution().numberOfMountains3(peaks = [[2,2],[6,3],[1,3],[1,3],[9,2],[10,3]]))
    print("*************************************")
    print(Solution().numberOfMountains4(peaks = [[2,2],[6,3],[5,4]]))
    print(Solution().numberOfMountains4(peaks = [[2,2],[6,3],[4,6]]))
    print(Solution().numberOfMountains4(peaks = [[1,3],[1,3]]))
    print(Solution().numberOfMountains4(peaks = [[1,3],[1,3], [1,2]]))
    print(Solution().numberOfMountains4(peaks = [[2,2],[6,3],[9,2],[10,3]]))
    print(Solution().numberOfMountains4(peaks = [[2,2],[6,3],[1,3],[1,3],[9,2],[10,3]]))
    print("*************************************")
    print(Solution().numberOfMountains5(peaks = [[2,2],[6,3],[5,4]]))
    print(Solution().numberOfMountains5(peaks = [[2,2],[6,3],[4,6]]))
    print(Solution().numberOfMountains5(peaks = [[1,3],[1,3]]))
    print(Solution().numberOfMountains5(peaks = [[1,3],[1,3], [1,2]]))
    print(Solution().numberOfMountains5(peaks = [[2,2],[6,3],[9,2],[10,3]]))
    print(Solution().numberOfMountains5(peaks = [[2,2],[6,3],[1,3],[1,3],[9,2],[10,3]]))


