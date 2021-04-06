'''
-Easy-

Given a stream of integers and a window size, calculate the moving average of all 
integers in the sliding window.

样例
Example 1:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000

'''

from collections import deque

class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.q = deque()   
        self.size = size
        self.sm = 0.0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if len(self.q) == self.size:
            self.sm -= self.q.popleft()            
        self.q.append(val)
        self.sm += val
        return self.sm/len(self.q)
