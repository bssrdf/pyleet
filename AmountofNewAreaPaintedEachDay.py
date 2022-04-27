'''
-Hard-


There is a long and thin painting that can be represented by a number line. 
You are given a 0-indexed 2D integer array paint of length n, where 
paint[i] = [starti, endi]. This means that on the ith day you need to paint 
the area between starti and endi.

Painting the same area multiple times will create an uneven painting so you 
only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount 
of new area that you painted on the ith day.

 

Example 1:



Input: paint = [[1,4],[4,7],[5,8]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1. 
Example 2:



Input: paint = [[1,4],[5,8],[4,7]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 5 and 8.
The amount of new area painted on day 1 is 8 - 5 = 3.
On day 2, paint everything between 4 and 5.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 5 - 4 = 1. 
Example 3:



Input: paint = [[1,5],[2,4]]
Output: [4,0]
Explanation:
On day 0, paint everything between 1 and 5.
The amount of new area painted on day 0 is 5 - 1 = 4.
On day 1, paint nothing because everything between 2 and 4 was already painted on day 0.
The amount of new area painted on day 1 is 0.
 

Constraints:

1 <= paint.length <= 105
paint[i].length == 2
0 <= starti < endi <= 5 * 104


'''

from typing import List
import collections
import heapq

from sortedcontainers import SortedList

class Node:
    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.v = 0
        self.add = 0

class SegmentTree2:
    # bottom-up segment tree
    def __init__(self, N, query_fn, update_fn):
        self.base = N
        self.query_fn = query_fn
        self.update_fn = update_fn
        self.tree = [0]*(2*N)
        self.lazy = [0]*(2*N)
        self.count = [1]*(2*N)
        H = 1
        while 1 << H < N:
            H += 1
        self.H = H
        for i in range(N-1, 0, -1):
            self.count[i] = self.count[i<<1] + self.count[(i<<1)+1]
    def update(self, L, R, val):
        L += self.base
        R += self.base
        self.push(L)#  // key point
        self.push(R)#  // key point
        L0, R0 = L, R
        while L <= R:
            if (L & 1) == 1:
                self.apply(L, val)
                L += 1
            if (R & 1) == 0: 
                self.apply(R, val)
                R -= 1
            L >>= 1
            R >>= 1
        self.pull(L0)
        self.pull(R0)

    def query(self, L, R):
        result = 0
        if L > R:
            return result        
        L += self.base
        R += self.base
        self.push(L)
        self.push(R)
        while L <= R:
            if (L & 1) == 1:
                result = self.query_fn(result, self.tree[L])
                L += 1
            if (R & 1) == 0:
                result = self.query_fn(result, self.tree[R])
                R -= 1
            L >>= 1; R >>= 1
        return result
    
    def apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val * self.count[x])
        if x < self.base:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def pull(self, x):
        while x > 1:
            x >>= 1
            # print(x << 1, x<<1+1)
            self.tree[x] = self.query_fn(self.tree[x<<1], self.tree[(x<<1) + 1])
            if self.lazy[x]:
                self.tree[x] = self.update_fn(self.tree[x], self.lazy[x] * self.count[x])
    def push(self, x):
        for h in range(self.H, 0, -1):
           y = x >> h
           if self.lazy[y]:
                self.apply(y << 1,     self.lazy[y])
                self.apply((y << 1) + 1, self.lazy[y])
                self.lazy[y] = 0
        

class SegmentTree:
    def __init__(self):
        self.root = Node(1, 10**5 + 10)

    def modify(self, l, r, v, node=None):
        if l > r:
            return
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            node.v = node.r - node.l + 1
            node.add = v
            return
        self.pushdown(node)
        if l <= node.mid:
            self.modify(l, r, v, node.left)
        if r > node.mid:
            self.modify(l, r, v, node.right)
        self.pushup(node)

    def query(self, l, r, node=None):
        if l > r:
            return 0
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            return node.v
        self.pushdown(node)
        v = 0
        if l <= node.mid:
            v += self.query(l, r, node.left)
        if r > node.mid:
            v += self.query(l, r, node.right)
        return v

    def pushup(self, node):
        node.v = node.left.v + node.right.v

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.r)
        if node.add:
            left, right = node.left, node.right
            left.v = left.r - left.l + 1
            right.v = right.r - right.l + 1
            left.add = node.add
            right.add = node.add
            node.add = 0



class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # Wrong 
        m = len(paint)
        n = 5*10**4+1
        n = 23
        B1 = [0]*n
        B2 = [0]*n
        def query(BIT, x):
            sums = 0
            while x > 0:
                sums += BIT[x]
                x -= x & (-x)
            return sums 
        def update(BIT, x, i):
            while x < n:                
                BIT[x] += i
                x += x & (-x)
            
        def range_update(l, r, x):
            update(B1, l, x)
            update(B1, r+1, -x)
            update(B2, l, x*(l-1))
            update(B2, r+1, -x*r)

            

        def prefix_sum(idx):
            return query(B1, idx)*idx - query(B2, idx)

        def range_query(l, r):
            return prefix_sum(r-1) - prefix_sum(l-1)

        ans = [0]*m
        for i,(s,e) in enumerate(paint):  
            a = range_query(s,e)          
            ans[i] = (e-s) - range_query(s, e)
            range_update(s,e-1,1)
            # print(s, e, a, B1, B2)
        return ans    
    
    def amountPainted2(self, paint: List[List[int]]) -> List[int]:
        tree = SegmentTree()
        ans = []
        for i, (start, end) in enumerate(paint):
            l, r = start + 1, end
            v = tree.query(l, r)
            ans.append(r - l + 1 - v)
            tree.modify(l, r, 1)
        return ans

    def amountPainted3(self, paint):
        """
        :type paint: List[List[int]]
        :rtype: List[int]
        """
        points = collections.defaultdict(list)
        for i, (s, e) in enumerate(paint):
            points[s].append((True, i))
            points[e].append((False, i))
        min_heap = []
        lookup = [False]*len(paint)
        result = [0]*len(paint)
        prev = -1
        for pos in sorted(points.keys()):
            while min_heap and lookup[min_heap[0]]:
                heapq.heappop(min_heap)
            if min_heap:
                result[min_heap[0]] += pos-prev
            prev = pos
            for t, i in points[pos]:
                if t:
                    heapq.heappush(min_heap, i)
                else:
                    lookup[i] = True
        return result
    
    def amountPainted4(self, paint: List[List[int]]) -> List[int]:
        minDay = min(s for s, e in paint)
        maxDay = max(e for s, e in paint)
        ans = [0] * len(paint)
        # store indices of paint that are available now
        runningIndices = SortedList()
        events = []  # (day, index, type)

        for i, (start, end) in enumerate(paint):
            events.append((start, i, 1))  # 1 := entering
            events.append((end, i, -1))  # -1 := leaving

        events.sort()

        i = 0  # events' index
        for day in range(minDay, maxDay):
            while i < len(events) and events[i][0] == day:
                day, index, type = events[i]
                if type == 1:
                    runningIndices.add(index)
                else:
                    runningIndices.remove(index)
                i += 1
            if runningIndices:
                ans[runningIndices[0]] += 1
        return ans
    
    def amountPainted5(self, paint: List[List[int]]) -> List[int]:        
        maxDay = max(e for s, e in paint)
        query  = lambda x,y: x+y
        update = lambda x,y: y
        st = SegmentTree2(maxDay, query_fn=query, update_fn=update)
        res = []
        for x,y in paint:
            cnt = st.query(x, y-1)
            st.update(x, y-1, 1)
            res.append(st.query(x, y-1)-cnt)
        return res

import random
if __name__ == "__main__":
    # paint = [[1,4],[4,7],[5,8]]
    paint = [[14,18],[12,16],[4,7],[3,22]]
    print(Solution().amountPainted(paint))
    print(Solution().amountPainted2(paint))
    print(Solution().amountPainted3(paint))
    print(Solution().amountPainted4(paint))
    print(Solution().amountPainted5(paint))
    paint = [[1,4],[5,8],[4,7]]
    print(Solution().amountPainted(paint))
    print(Solution().amountPainted2(paint))
    print(Solution().amountPainted5(paint))
    paint = [[1,5],[2,4]]
    print(Solution().amountPainted(paint))
    print(Solution().amountPainted2(paint))
    print(Solution().amountPainted5(paint))


    # paint = [[1,10],[20,34], [8, 12], [16,19]]
    # print(Solution().amountPainted(paint))
    # print(Solution().amountPainted2(paint))
    # N, segs = 1000, set()
    # while len(segs) < N:
    #     i, j = random.randint(1,1000), random.randint(1,1000)
    #     if i < j:
    #         segs.add((i,j))
    # paint = list(segs)
    # print(paint)
    # paint = [(73, 493), (454, 900), (204, 270), (54, 941)]
    # print(Solution().amountPainted(paint))
    # print(Solution().amountPainted2(paint))

    





