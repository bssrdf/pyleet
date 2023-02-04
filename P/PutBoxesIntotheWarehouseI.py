'''
-Medium-

$$$

*Sorting*
*Greedy*

Given two arrays of positive integers boxes and warehouse representing the heights of some boxes 
of unit width, and the heights of n rooms in a warehouse, respectively. The warehouse's rooms are 
labeled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

Boxes are put into the warehouse by the following rules:

Boxes can't be piled up.
You can rearrange the order of the boxes.
Boxes can only be pushed into the warehouse from left to right only.
If the height of some room in the warehouse is less than the height of a box, then the box will be 
stopped before that room, so are the boxes behind it.
Return the maximum number of boxes you can put into the warehouse.

 

Example 1:



Input: boxes = [4,3,4,1], warehouse = [5,3,3,4,1]
Output: 3
Explanation: 

We can first put the box of height 1 in room 4. Then we can put the box of height 3 in either of the 3 rooms 1, 2, or 3. Lastly, we can put one box of height 4 in room 0.
There is no way we can fit all 4 boxes in the warehouse.
Example 2:



Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
Output: 3
Explanation: 

Notice that it's not possible to put the box of height 4 into the warehouse since it cannot pass the first room of height 3.
Also, for the last two rooms, 2 and 3, only boxes of height 1 can fit.
We can fit 3 boxes maximum as shown above. The yellow box can also be put in room 2 instead.
Swapping the orange and green boxes is also valid, or swapping one of them with the red box.
Example 3:

Input: boxes = [1,2,3], warehouse = [1,2,3,4]
Output: 1
Explanation: Since the first room in the warehouse is of height 1, we can only put boxes of height 1.
Example 4:

Input: boxes = [4,5,6], warehouse = [3,3,3,3,3]
Output: 0
 

Constraints:

n == warehouse.length
1 <= boxes.length, warehouse.length <= 10^5
1 <= boxes[i], warehouse[i] <= 10^9

'''

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        m = len(boxes)
        n = len(warehouse)
        leftMinHeight = [0]*n
        leftMinHeight[0] = warehouse[0]
        for i in range(1, n):
            leftMinHeight[i] = min(leftMinHeight[i-1], warehouse[i])
        boxes.sort()
        j, i = n-1, 0
        ans = 0
        while i < m and j >= 0:
            if boxes[i] <= leftMinHeight[j]:
                ans += 1
                i += 1
            j -= 1
        return ans

    def maxBoxesInWarehouse2(self, boxes, warehouse):
        '''
        这是一道经典题，比较简单的贪心策略是：尽量将最外的仓库（即index较小的位置，它能支持
        最大的高度）留给高的盒子，否则会浪费空间。

        具体的做法是：从左到右遍历cell。对于每个cell，从高到低寻找能fit的盒子，凡是不fit的盒子
        就都舍弃（他们以后肯定放不进任何cell），如果发现某个盒子能fit，就装进去。然后处理
        第二个cell，以此类推。
        '''
        B, W = boxes, warehouse
        B.sort(reverse=True)
        ans, i = 0, 0
        for b in B:            
            if i == len(W):
                break
            if b <= W[i]:
                i += 1
                ans += 1 
        return ans



if __name__ == "__main__":
    print(Solution().maxBoxesInWarehouse(boxes = [4,3,4,1], warehouse = [5,3,3,4,1]))
    print(Solution().maxBoxesInWarehouse(boxes = [1,2,2,3,4], warehouse = [3,4,1,2]))
    print(Solution().maxBoxesInWarehouse2(boxes = [4,3,4,1], warehouse = [5,3,3,4,1]))
    print(Solution().maxBoxesInWarehouse2(boxes = [1,2,2,3,4], warehouse = [3,4,1,2]))
