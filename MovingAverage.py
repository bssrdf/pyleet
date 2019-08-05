from collections import deque


class MovingAverage(object):

    def __init__(self, N):
        self.window_size = N
        self.window = deque()
        self.sum = 0.0

    def next(self, num):
        if(len(self.window) == self.window_size):
            self.sum -= self.window.popleft()

        self.window.append(num)
        self.sum += num
        
        return self.sum / len(self.window)
        

ma = MovingAverage(3)
print(ma.next(1))
print(ma.next(10))
print(ma.next(3))
print(ma.next(5))



