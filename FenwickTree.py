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
 
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res
    

import bisect 

if __name__ == "__main__":
    n = 7
    #print bin(n)
    print(FenwickTree(10).lowbit(n))
    # Fenick tree can be used for dynamic query of number of values within a range
    arr = [8, 1, 0, -1, 2, -2, 5]
    # query: q[i] is how many numbers <= x to the left of index i
    x = 6
    sortA = sorted(arr)
    bit = FenwickTree(len(arr))
    q = []
    for a in arr: 
        bit.add(bisect.bisect_left(sortA, a)+1, 1)
        q.append(bit.sum(bisect.bisect_right(sortA, x)))
        #bit.add(bisect.bisect_left(sortA, a)+1, 1)
    print(q) 





 