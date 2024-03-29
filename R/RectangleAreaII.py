'''
https://leetcode.com/problems/rectangle-area-ii/

We are given a list of (axis-aligned) rectangles.  Each rectangle[i] =
[x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left 
 corner, and (x2, y2) are the coordinates of the top-right corner of the 
 ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer 
may be too large, return it modulo 10^9 + 7.

Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus 
will fit in a 64-bit signed integer.

'''

import heapq

class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end)
        return self._right

    def print_count(self):
        print('start, end, count, total : ',
             self.start, self.end, self.count, self.total)
        if self._left:
            self._left.print_count()
        if self._right:
            self._right.print_count()    

    '''   

    The data array for segmentation tree is made up of all the x-coordinates 
    encountered in sweep line algorithm.

    The segmentation tree leaves in this problem take the form of [i, i+1] 
    rather than [i, i].

    ST leave of range [i, i+1] contains value of X[i+1] - X[i], if the count 
    of this range is larger than 0.
    
    Adding and removing edges is done by updating ranges, specifically the 
    count attributes. Note that count field is updated only for leave nodes. 
    For nonleave nodes, we only update total field.

    '''
    def update(self, i, j, val):
        if i >= j: return 0
        if self.start == i and self.end == j: 
            self.count += val
        else:
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)

        if self.count > 0: 
            self.total = X[self.end] - X[self.start]
        else:          
            self.total = self.left.total + self.right.total

        return self.total

class Solution(object):
    def rectangleAreaSegTree(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        OPEN, CLOSE = 1, -1
        events = []
        global X
        X = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            X.add(x1)
            X.add(x2)
        events.sort()

        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}

        active = Node(0, len(X) - 1)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)            
            cur_x_sum = active.update(Xi[x1], Xi[x2], typ)
            print(y, typ, cur_y, ans, cur_x_sum)
            active.print_count()
            cur_y = y

        return ans % (10**9 + 7)

    def rectangleAreaDivideandConquer(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        def getSum(batch):
            batch.sort(key=lambda x: x[1])
            temp = []            
            temp.append(batch[0])
            i = 1
            while i < len(batch):
                cur = batch[i]
                end = temp[-1]
                if cur[1] <= end[3]:
                    end[3] = max(end[3], cur[3])
                else:
                    temp.append(cur)
                i += 1
            sm = 0
            for t in temp:
                sm += t[3] - t[1]
            return sm
    
        def verticalCut(batch, queue):
            mi = batch[0][2] if not queue else queue[0][0]

            for rec in batch:
                mi = min(mi, rec[2])
            
            for rec in batch:
                if rec[2] > mi:
                    right = [mi, rec[1], rec[2], rec[3]]
                    rec[2] = mi
                    heapq.heappush(queue, right)

        queue = rectangles
        heapq.heapify(queue)
        
        total = 0
        while queue:
            batch = [] 
            cur = heapq.heappop(queue)
            batch.append(cur)
            while queue and queue[0][0] == cur[0]:
                batch.append(heapq.heappop(queue))
            
            verticalCut(batch, queue)
            total += getSum(batch) * (batch[0][2] - batch[0][0])
        
        return total % (1000000000 + 7)

    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """   
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        x_i = {v: i for i, v in enumerate(xs)}
        count = [0] * len(x_i)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        return area % (10 ** 9 + 7)

if __name__ == "__main__":    
    print(Solution().rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))
    print(Solution().rectangleAreaSegTree([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))
    print(Solution().rectangleAreaDivideandConquer([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))