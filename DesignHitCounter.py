'''
-Medium-

Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume 
that calls are being made to the system in chronological order (ie, the timestamp is 
monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);

Follow up:
What if the number of hits per second could be very large? Does your design scale?

'''

from collections import deque

class HitCounter(object):
    windowLen = 300

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hitQueue = deque() # each item is a pair [timeStamp,hitCount] where hitCount is the number of hits at timeStamp
        self.hitCountInWindow = 0
    
    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not ( self.hitQueue and self.hitQueue[-1][0]==timestamp ):
            self.hitQueue.append( [timestamp,0] )

        self.hitQueue[-1][1] += 1
        self.hitCountInWindow += 1

    def _removeOldHits(self, timestamp):
        while self.hitQueue and self.hitQueue[0][0] <= timestamp - self.windowLen:
            self.hitCountInWindow -= self.hitQueue.popleft()[1]

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """        
        self._removeOldHits(timestamp)
        return self.hitCountInWindow

class HitCounter2(object):
    # number of hits per second could be very large
    # so queue push is not efficient
    # use a circular buffer
    windowLen = 300

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [0] * self.windowLen 
        self.hits  = [0] * self.windowLen 

    
    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        t = timestamp % self.windowLen
        if self.times[t] != timestamp:
            self.times[t] = timestamp
            self.hits[t] = 1
        else:
            self.hits[t] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        for i in range(self.windowLen):
            if timestamp - self.times[i] < self.windowLen:
                res += self.hits[i]
        return res

    