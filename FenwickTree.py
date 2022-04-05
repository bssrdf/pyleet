# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 00:07:56 2017

@author: merli
"""

class FenwickTree(object):
    def __init__(self, n):
        self.sum_array = [0] * (n + 1)
        self.n = n
 
    def lowbit(self, x):
        return x & -x
 
    def add(self, x, val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)
    
    def update(self, x, val):
        self.add(x, val)

    def range_update(self, ui, uj, val):
        self.update(ui, val)
        self.update(uj+1, -val)
 
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res

    def point_query(self, x):
        return self.sum(x)


class FenwickTreeRURQ(object):
    def __init__(self, n):
        self.B1 = [0] * (n + 1)
        self.B2 = [0] * (n + 1)
        self.n = n
 
    def lowbit(self, x):
        return x & -x
 
    def add(self, B, x, val):
        while x <= self.n:
            B[x] += val
            x += self.lowbit(x)
    
    def update(self, B, x, val):
        self.add(B, x, val)

    def range_update(self, ui, uj, val):
        self.update(self.B1, ui, val)
        self.update(self.B1, uj+1, -val)
        self.update(self.B2, ui, val*(ui-1))
        self.update(self.B2, uj+1, -val*uj)
 
    def query(self, B, x):
        res = 0
        while x > 0:
            res += B[x]
            x -= self.lowbit(x)
        return res


    def prefix_sum(self, idx):
        return self.query(self.B1, idx)*idx - self.query(self.B2, idx)

    def range_query(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l-1)


import bisect 

if __name__ == "__main__":
    n = 7
    #print bin(n)
    # print(FenwickTree(10).lowbit(n))
    # # Fenick tree can be used for dynamic query of number of values within a range
    # arr = [8, 1, 0, -1, 2, -2, 5]
    # # query: q[i] is how many numbers <= x to the left of index i
    # x = 6
    # sortA = sorted(arr)
    # bit = FenwickTree(len(arr))
    # q = []
    # for a in arr: 
    #     bit.add(bisect.bisect_left(sortA, a)+1, 1)
    #     q.append(bit.sum(bisect.bisect_right(sortA, x)))
    #     #bit.add(bisect.bisect_left(sortA, a)+1, 1)
    # print(q) 

    rupq = FenwickTree(10)
    rupq.range_update(2,9,1)
    rupq.range_update(6,7,1)
    print(rupq.point_query(6))

    # for i in range(1, 11):        
    #     print(i, rupq.point_query(i))

    rurq = FenwickTreeRURQ(10)
    rurq.range_update(2,9,7)
    rurq.range_update(6,7,3)
    print(rurq.range_query(1,10))
    print(rurq.range_query(6,7))
    













 