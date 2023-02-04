'''


-Medium-
$$$

*Sorting*
*Greedy*

You are given two arrays of positive integers, boxes and warehouse, representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. The warehouse's rooms are labeled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

Boxes are put into the warehouse by the following rules:

Boxes cannot be stacked.
You can rearrange the insertion order of the boxes.
Boxes can be pushed into the warehouse from either side (left or right)
If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.
Return the maximum number of boxes you can put into the warehouse.

 

Example 1:



Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
Output: 4
Explanation:

We can store the boxes in the following order:
1- Put the yellow box in room 2 from either the left or right side.
2- Put the orange box in room 3 from the right side.
3- Put the green box in room 1 from the left side.
4- Put the red box in room 0 from the left side.
Notice that there are other valid ways to put 4 boxes such as swapping the red and green boxes or the red and orange boxes.
Example 2:



Input: boxes = [3,5,5,2], warehouse = [2,1,3,4,5]
Output: 3
Explanation:

It is not possible to put the two boxes of height 5 in the warehouse since there's only 1 room of height >= 5.
Other valid solutions are to put the green box in room 2 or to put the orange box first in room 2 before putting the green and red boxes.
 

Example 3:

Input: boxes = [1,2,3], warehouse = [1,2,3,4]

Output: 3

Example 4:

Input: boxes = [4,5,6], warehouse = [3,3,3,3,3]

Output: 0

Constraints:

n == warehouse.length
1 <= boxes.length, warehouse.length <= 105
1 <= boxes[i], warehouse[i] <= 109



'''

import heapq

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        B, W = boxes, warehouse
        m = len(boxes)
        n = len(warehouse) 
        leftMinHeight = [0]*n
        leftMinHeight[0] = warehouse[0]
        for i in range(1, n):
            leftMinHeight[i] = min(leftMinHeight[i-1], warehouse[i])
        right = W[-1]
        for i in range(n-2, -1, -1):
            right = min(right, W[i])
            W[i] = max(leftMinHeight[i], right)
        B.sort()
        W.sort() 
        j, i = 0, 0
        ans = 0
        while i < m and j < n:
            while j < n and boxes[i] > W[j]:
                j += 1
            if j < n and B[i] <= W[j]:   
               ans += 1
               j += 1
            i += 1
        return ans

    def maxBoxesInWarehouse2(self, boxes, warehouse):
        '''
        此题的本质是贪心法。我们首先需要有这样一个概念，在最终的排列中，高的箱子会摆放在靠
        两边的位置。越高的箱子会摆得越靠边。

        于是我们从高到低遍历每一个箱子，查看是否能fit仓库的第一个或者最后一个。如果两个都fit，那
        我们挑一个较矮的仓库。于是我们就把这个箱子安置好了。于是我们将指向仓库两头的指针做
        必要的移动，将其中一个挪开已经放置箱子的位置朝中间进发。

        然后我们考察下一个箱子。因为这个箱子比刚才的矮，所以必然可以穿越之前那个箱子所在的仓库，等价
        于忽略掉warehouse的一个边缘元素。于是我们又面对一样的问题，此时的箱子能否fit仓库的第一个
        或者最后一个？如果两个都fit，那么我们再挑一个较矮的仓库。于是双指针中的一个又可以往中间移动。
        每移动一次就代表安置了一个箱子。

        当箱子都遍历结束，或者双指针i>j的时候，就完成了探索。
        '''
        B, W = boxes, warehouse
        B.sort(reverse=True)
        ans, left, right = 0, 0, len(W)-1
        for b in B:
            if left > right:
                break 
            if b > max(W[left], W[right]): continue
            if W[right] < b or W[left] >= b and W[left] < W[right]:
                left += 1
            else:
                right -= 1
            ans += 1 
        return ans

        


if __name__ == "__main__":
    print(Solution().maxBoxesInWarehouse(boxes = [1,2,2,3,4], warehouse = [3,4,1,2]))
    print(Solution().maxBoxesInWarehouse(boxes = [3,5,5,2], warehouse = [2,1,3,4,5]))
    print(Solution().maxBoxesInWarehouse(boxes = [1,2,3], warehouse = [1,2,3,4]))
    print(Solution().maxBoxesInWarehouse2(boxes = [1,2,2,3,4], warehouse = [3,4,1,2]))
    print(Solution().maxBoxesInWarehouse2(boxes = [3,5,5,2], warehouse = [2,1,3,4,5]))
    print(Solution().maxBoxesInWarehouse2(boxes = [1,2,3], warehouse = [1,2,3,4]))




