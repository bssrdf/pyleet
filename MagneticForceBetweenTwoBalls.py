'''
-Medium-
*Binary Search*
*Sorting*

In the universe Earth C-137, Rick discovered a special form of magnetic 
force between two balls if they are put in his new invented basket. 
Rick has n empty baskets, the ith basket is at position[i], Morty 
has m balls and needs to distribute the balls into the baskets such 
that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at 
positions x and y is |x - y|.

Given the integer array position and the integer m. Return the 
required force.

 

Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 105
1 <= position[i] <= 109
All integers in position are distinct.
2 <= m <= position.length


'''

from typing import List
import bisect

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        P = position
        def canDistribute(d):
            i, pos = m-1, P[0]
            while i > 0:
                pos += d
                idx = bisect.bisect_left(P, pos)
                # print(i, pos, idx, P)
                if idx < len(P):
                    i -= 1
                    pos = P[idx]
                else:
                    return False
            return True
        l, r = 1, P[-1]-P[0]+1
        # print(l, r)
        while l < r:
            mid = l + (r-l)//2
            # print('A', l, r, mid)
            if canDistribute(mid):
                l = mid + 1
            else:
                r = mid
            # print('B',l, r, mid)
        return l-1


if __name__ == "__main__":
    print(Solution().maxDistance(position = [1,2,3,4,7], m = 3))
    print(Solution().maxDistance(position = [5,4,3,2,1,1000000000], m = 2))

    print(Solution().maxDistance(position = [79,74,57,22], m = 4))