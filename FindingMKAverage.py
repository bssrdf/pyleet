

'''
-Hard-
*Priority Queue*


You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream.

The MKAverage can be calculated using these steps:

If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. Otherwise, copy the last m elements of the stream to a separate container.
Remove the smallest k elements and the largest k elements from the container.
Calculate the average value for the rest of the elements rounded down to the nearest integer.
Implement the MKAverage class:

MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
void addElement(int num) Inserts a new element num into the stream.
int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.
 

Example 1:

Input
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
Output
[null, null, null, -1, null, 3, null, null, null, 5]

Explanation
MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3);        // current elements are [3]
obj.addElement(1);        // current elements are [3,1]
obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
obj.addElement(10);       // current elements are [3,1,10]
obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
                          // After removing smallest and largest 1 element the container will be [3].
                          // The average of [3] equals 3/1 = 3, return 3
obj.addElement(5);        // current elements are [3,1,10,5]
obj.addElement(5);        // current elements are [3,1,10,5,5]
obj.addElement(5);        // current elements are [3,1,10,5,5,5]
obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
                          // After removing smallest and largest 1 element the container will be [5].
                          // The average of [5] equals 5/1 = 5, return 5
 

Constraints:

3 <= m <= 105
1 <= k*2 < m
1 <= num <= 105
At most 105 calls will be made to addElement and calculateMKAverage.



'''

import heapq
from heapq import heappop, heappush
import math

from sortedcontainers import SortedList
import collections


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.minh = []
        self.maxh = []
        self.minhd = []
        self.maxhd = []
        self.nums = []
        self.cnt = 0
        self.t = m - 2*k
        self.sums = 0
        self.sminh = 0 
        self.smaxh = 0 
        

    def addElement(self, num: int) -> None:
        # print('xxx', num, self.sums, self.sminh, self.smaxh)
        self.sums += num
        self.nums.append(num) 
        i = -1
        if self.cnt >= self.m:      
            i = self.cnt - self.m
            while self.minhd and self.minhd[0][1] < i:
                heapq.heappop(self.minhd)
            while self.minhd and self.maxhd[0][1] < i:
                heapq.heappop(self.maxhd)
            mark = 0
            if self.nums[i] > self.minhd[0][0]: 
                self.sminh -= self.nums[i] 
                self.sums -= self.nums[i] 
                mark = 1
            elif self.nums[i] < -self.maxh[0][0]:
                self.smaxh -= self.nums[i]
                self.sums -= self.nums[i] 
                mark = -1
            else:
                self.sums -= self.nums[i] 
            if mark > 0:
                val, pos = heapq.heappop(self.maxhd)
                heapq.heappush(self.minh, (-val, pos))
            elif mark < 0:
                val, pos = heapq.heappop(self.minhd)
                heapq.heappush(self.maxh, (-val, pos))
            
        # while self.minh and self.minh[0][1] <= i:
        #     heapq.heappop(self.minh)
        # while self.maxh and self.maxh[0][1] <= i:
        #     heapq.heappop(self.maxh)
        # print('before add', num, self.sums, self.sminh, self.smaxh, self.minh, self.maxh)
        
        # if not self.minhd:
        #     heapq.heappush(self.minhd, (num, self.cnt))        

        # if not self.maxhd:
        #     heapq.heappush(self.maxhd, (-num, self.cnt))
        

        self.sminh += num
        if len(self.minh) > self.k:
            while self.minh and self.minh[0][1] < i:
                heapq.heappop(self.minh)
            val, pos = heapq.heappop(self.minh)
            # heapq.heappush(self.minhd, (val, pos))
            heapq.heappush(self.maxhd, (-val, pos))
            self.sminh -= val 
        self.smaxh += num
        heapq.heappush(self.maxh, (-num, self.cnt))
        if len(self.maxh) > self.k:
            while self.maxh and self.maxh[0][1] < i:
                heapq.heappop(self.maxh)
            val, pos = heapq.heappop(self.maxh)
            heapq.heappush(self.minhd, (-val, pos))
            # heapq.heappush(self.maxhd, (val, pos))
            self.smaxh -= -val 
        self.cnt += 1
        print('afetr add', num, self.sums, self.sminh, self.smaxh, self.minh, self.maxh, self.minhd, self.maxhd)
        

    def calculateMKAverage(self) -> int:
        if self.cnt < self.m: return -1
        # print(self.minh, self.maxh)
        # print(self.sums,  self.sminh,  self.smaxh, self.t)
        return math.floor((self.sums - self.sminh - self.smaxh) / self.t)

class MKAverage2:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.deque = collections.deque()
        self.sl = SortedList()
        self.total = self.first_k = self.last_k = 0

    def addElement(self, num: int) -> None:
        self.total += num
        self.deque.append(num)
        index = self.sl.bisect_left(num)
        if index < self.k:
            self.first_k += num
            if len(self.sl) >= self.k:
                self.first_k -= self.sl[self.k - 1]
        if index >= len(self.sl) + 1 - self.k:
            self.last_k += num
            if len(self.sl) >= self.k:
                self.last_k -= self.sl[-self.k]
        self.sl.add(num)
        if len(self.deque) > self.m:
            num = self.deque.popleft()
            self.total -= num
            index = self.sl.index(num)
            if index < self.k:
                self.first_k -= num
                self.first_k += self.sl[self.k]
            elif index >= len(self.sl) - self.k:
                self.last_k -= num
                self.last_k += self.sl[-self.k - 1]
            self.sl.remove(num)

    def calculateMKAverage(self) -> int:
        if len(self.sl) < self.m:
            return -1
        return (self.total - self.first_k - self.last_k) // (self.m - 2 * self.k)    

class MKAverage3:
    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.arr = [0]*m
        self.lh1, self.rh1 = self.heap_init(m, k)
        self.lh2, self.rh2 = self.heap_init(m, m - k)
        self.score = 0
        
    def heap_init(self, p1, p2):
        h1 = [(0, i) for i in range(p1-p2, p1)]
        h2 = [(0, i) for i in range(p1-p2)]
        heapq.heapify(h1)
        heapq.heapify(h2)
        return (h1, h2)
        
    def update(self, lh, rh, m, k, num):
        score, T = 0, len(self.arr)
        if num > rh[0][0]:
            heappush(rh, (num, T))        
            if self.arr[T - m] <= rh[0][0]:
                if rh[0][1] >= T - m: score += rh[0][0]
                score -= self.arr[T - m]
                heappush(lh, (-rh[0][0], rh[0][1]))
                heappop(rh)
        else:
            heappush(lh, (-num, T))       
            score += num
            if self.arr[T - m] >= rh[0][0]: 
                heappush(rh, (-lh[0][0], lh[0][1]))
                q = heappop(lh)
                score += q[0]
            else:
                score -= self.arr[T - m]

        while lh and lh[0][1] <= T - m: heappop(lh)  # lazy-deletion
        while rh and rh[0][1] <= T - m: heappop(rh)  # lazy-deletion
        return score
        
    def addElement(self, num):
        t1 = self.update(self.lh1, self.rh1, self.m, self.k, num)
        t2 = self.update(self.lh2, self.rh2, self.m, self.m - self.k, num)
        self.arr.append(num)
        self.score += (t2 - t1)
    
    def calculateMKAverage(self):
        if len(self.arr) < 2*self.m: return -1
        return self.score//(self.m - 2*self.k)



def negateX(z):
    return ( -z[0],-z[1] )

class MKAverage4:

    def __init__(self, m: int, k: int):
        # use 4 heaps (2 min, 2 max)
        # lowQ and lowA consist of a pair, complementing each other
        # together they hold all the numbers in the window
        # the key step is to maintain lowQ having k smallest numbers
        # if not, exchange lowQ[0] with lowA[0] until satisfied 
        # similarly for highA and highQ

        self.lowQ = []  # max-heap, smallest k numbers in the window
        self.highQ = [] # min-heap, largest k numbers in the window
        self.lowA = []  # min-heap, largest m-k numbers in the window
        self.highA = [] # max-heap, smallest m-k numbers in the window
        self.total = 0
        self.counter = 0
        self.m = m
        self.k = k
        self.divisor = m - k - k
        self.allNums = []

        
    def addElement(self, num: int) -> None:
        # print("addElement",num)
        self.total += num
        heappush(self.lowA, (num,self.counter) )
        heappush(self.highA, (-num,-self.counter) )

        if self.counter < self.m:
            if self.counter == self.m-1:
                # print(self.lowA)
                # print(self.highA)
                for _ in range(self.k):
                    heappush(self.lowQ, negateX(heappop(self.lowA)))
                    heappush(self.highQ, negateX(heappop(self.highA)))
                self.total -= -sum( n for n,_ in self.lowQ )
                self.total -= sum( n for n,_ in self.highQ )
        else:
            removedIndex = self.counter-self.m
            removed = (self.allNums[self.counter-self.m], removedIndex)
            # print("removedNum",removed)
            if removed <= negateX(self.lowQ[0]):
                # print("removedNum from lowQ")
                low = heappop(self.lowA)
                self.total -= low[0]
                heappush(self.lowQ, negateX(low))
            elif removed >= self.highQ[0]:
                # print("removedNum from highQ")
                high = heappop(self.highA)
                self.total -= -high[0]
                heappush(self.highQ, negateX(high))
            else:
                self.total -= removed[0]
            
            while -self.lowQ[0][1] <= removedIndex:
                heappop(self.lowQ)
            while self.lowA[0][1] <= removedIndex:
                heappop(self.lowA)
            while self.highQ[0][1] <= removedIndex:
                heappop(self.highQ)
            while -self.highA[0][1] <= removedIndex:
                heappop(self.highA)
            
            while self.highA[0] < negateX(self.highQ[0]):
                a,q = heappop(self.highA),heappop(self.highQ)
                self.total += a[0]
                self.total += q[0]
                heappush(self.highA, negateX(q))
                heappush(self.highQ, negateX(a))
                # print("swizzle high")
            while self.lowA[0] < negateX(self.lowQ[0]):
                a,q = heappop(self.lowA),heappop(self.lowQ)
                self.total -= a[0]
                self.total -= q[0]
                heappush(self.lowA, negateX(q))
                heappush(self.lowQ, negateX(a))
                # print("swizzle low")


        self.allNums.append(num)
        self.counter += 1
        # print(self.total, self.allNums, "|||", self.lowQ, self.highQ, "|||", self.lowA, self.highA)

    def calculateMKAverage(self) -> int:
        if self.counter < self.m:
            return -1
        return self.total // self.divisor

if __name__ == "__main__":
    # obj = MKAverage(3, 1) 
    # obj.addElement(3)#        // current elements are [3]
    # obj.addElement(1)#        // current elements are [3,1]
    # print(obj.calculateMKAverage())# // return -1, because m = 3 and only 2 elements exist.
    # obj.addElement(10)#       // current elements are [3,1,10]
    # print(obj.calculateMKAverage())# // The last 3 elements are [3,1,10].
    #                         # // After removing smallest and largest 1 element the container will be [3].
    #                         # // The average of [3] equals 3/1 = 3, return 3
    # obj.addElement(5)#        // current elements are [3,1,10,5]
    # obj.addElement(5)#        // current elements are [3,1,10,5,5]
    # obj.addElement(5)#        // current elements are [3,1,10,5,5,5]
    # print(obj.calculateMKAverage())# // The last 3 elements are [5,5,5].
    #                         # // After removing smallest and largest 1 element the container will be [5].
    #                         # // The average of [5] equals 5/1 = 5, return 5
    
    # obj = MKAverage(6, 1) 
    # obj.addElement(3)#        // current elements are [3]
    # obj.addElement(1)#        // current elements are [3,1]
    
    # obj.addElement(12)#       // current elements are [3,1,10]
    
    # obj.addElement(5)#        // current elements are [3,1,10,5]
    # obj.addElement(3)#        // current elements are [3,1,10,5,5]
    # obj.addElement(4)#        // current elements are [3,1,10,5,5,5]
    # print(obj.calculateMKAverage())# // The last 3 elements are [5,5,5].
    #                         # // After removing smallest and largest 1 element the container will be [5].
    #                         # // The average of [5] equals 5/1 = 5, return 5

    obj = MKAverage(3, 1) 
    obj.addElement(17612)#        // current elements are [3]
    obj.addElement(74607)#        // current elements are [3,1]
    print(obj.calculateMKAverage())# // return -1, because m = 3 and only 2 elements exist.
    obj.addElement(8272)#       // current elements are [3,1,10]
    
    obj.addElement(33433)#        // current elements are [3,1,10,5]
    print(obj.calculateMKAverage())# // return -1, because m = 3 and only 2 elements exist.
    obj.addElement(15456)#        // current elements are [3,1,10,5,5]
    obj.addElement(64938)#        // current elements are [3,1,10,5,5,5]
    print(obj.calculateMKAverage())# // The last 3 elements are [5,5,5].
                            # // After removing smallest and largest 1 element the container will be [5].
                            # // The average of [5] equals 5/1 = 5, return 5
    obj.addElement(99741)#        // current elements are [3,1,10,5,5,5]
 
