'''
-Easy-

This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability 
that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.

'''

import random

class BiasedCoin(object):

    def __init__(self, p):
        self.p = p

    def toss_biased(self):
        toss = random.random()
        if toss < self.p:
            return 1 # head
        else:
            return 0 # tail
    
    def toss_unbiased(self):
        toss1 = self.toss_biased()
        toss2 = self.toss_biased()
        while toss1 == 1 and toss2 == 1 or \
              toss1 == 0 and toss2 == 0:
            toss1 = self.toss_biased()
            toss2 = self.toss_biased()
        if toss1 == 1:
            return 1
        elif toss2 == 1:
            return 0

if __name__ == '__main__':   
    coin = BiasedCoin(0.6)
    N = 10000
    head = 0
    for i in range(N):
        toss = coin.toss_biased()
        if toss == 1:
            head += 1
    print(head)
    head = 0
    for i in range(N):
        toss = coin.toss_unbiased()
        if toss == 1:
            head += 1        
    print(head)


        

