"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
"""
import heapq


__author__ = 'Daniel'



class Solution(object):
    def nthUglyNumber(self, n):
        """
        Prime factor: 2, 3, 5
        Heap
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        t2,t3,t5=0,0,0
        k=[0]*n
        k[0] = 1
        for i in range(1, n):
            k[i] = min(k[t2]*2, k[t3]*3, k[t5]*5)
            print(i, k[i], t2, t3, t5, k[t2], k[t3], k[t5])
            if k[i] == k[t2]*2:
                t2 += 1
            if k[i] == k[t3]*3:
                t3 += 1
            if k[i] == k[t5]*5:
                t5 += 1
            print(i, k[i], t2, t3, t5)
        return k[n-1]

if __name__ == "__main__":
    print(Solution().nthUglyNumber(17))
