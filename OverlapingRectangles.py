'''


'''
import sys


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

    def add(self, i, j):
        if i >= j: return 
        if self.start == i and self.end == j: 
            self.count += 1
        else:
            self.left.add(i, min(self.mid, j))
            self.right.add(max(self.mid, i), j)

    def sub(self, i, j):
        if i >= j: return 
        if self.start == i and self.end == j: 
            self.count -= 1
        else:
            self.left.add(i, min(self.mid, j))
            self.right.add(max(self.mid, i), j)
        

        #return self.total

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


    def overlap(self, rectangles):

        OPEN, CLOSE = 1, -1
        events = []
        global X
        X = set()
        for x1, x2, y1, y2 in rectangles:
            events.append((x1, OPEN, y1, y2))
            events.append((x2, CLOSE, y1, y2))
            X.add(y1)
            X.add(y2)
        events.sort()

        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}

        active = Node(0, len(X) - 1)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for x, typ, y1, y2 in events:
            #ans += cur_x_sum * (y - cur_y)            
            cur_x_sum = active.update(Xi[y1], Xi[y2], typ)
            #print(y, typ, cur_y, ans, cur_x_sum)
            #active.print_count()
            #cur_y = y

        return False

    def overlapN2(self, rectangles):
        """
        """
        n = len(rectangles)
        for i in range(n):
            for j in range(i+1, n):
                r1 = rectangles[i]
                r2 = rectangles[j]
                if r2[0] <= r1[0] and r1[1] <= r2[1] and \
                   r2[2] <= r1[2] and r1[3] <= r2[3]:
                    print(i, j)
                    print(r1, r2)
                    return True
                if r1[0] <= r2[0] and r2[1] <= r1[1] and \
                   r1[2] <= r2[2] and r2[3] <= r1[3]:
                    print(i, j)
                    print(r1, r2)
                    return True
        return False
                

        
from random import randint

if __name__ == "__main__":
    N = 1000
    nums = [_ for _ in range(1,N+1)]
    rects = []
    for i in range(100):
        i1, i2, i3, i4 = randint(0, N-1), randint(0, N-1), randint(0, N-1), randint(0, N-1)  
        if i1 != i2 and i3 != i4:
            rects.append(sorted([nums[i1], nums[i2]])+
                         sorted([nums[i3], nums[i4]]))
    for r in rects:
        print(r) 
    print(Solution().overlapN2(rects))


    





