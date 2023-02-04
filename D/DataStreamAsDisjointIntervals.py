'''
-Hard-

Given a data stream input of non-negative integers a1, a2, ..., an, ..., 
summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., 
then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
 

Follow up:

What if there are lots of merges and the number of disjoint intervals are 
small compared to the data stream's size?


'''


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.intervals:
            self.intervals.append([val, val])
        else:            
            n = len(self.intervals)
            l = 0
            r = n
            while l < r:
                m = l+(r-l)//2
                if self.intervals[m][1] < val:
                    l = m+1
                else:
                    r = m
            r -= 1            
            if r < 0:
                if  val >= self.intervals[0][0] and \
                    val <= self.intervals[0][1]:
                    return
                elif self.intervals[0][0]-val == 1:
                    self.intervals[0] = [val, self.intervals[0][1]]
                else:
                    self.intervals[0:0] = [[val, val]]
            elif r == n-1: 
                if val-self.intervals[-1][1] == 1:
                    self.intervals[-1] = [self.intervals[-1][0], val]
                else:
                    self.intervals[n:n] = [[val, val]]
            else:
                if val >= self.intervals[r+1][0] and \
                   val <= self.intervals[r+1][1]:
                    return
                elif val-self.intervals[r][1] == 1 and self.intervals[r+1][0]-val == 1:   
                    self.intervals[r:r+2] = [[self.intervals[r][0], 
                                             self.intervals[r+1][1]]]
                elif val-self.intervals[r][1] == 1: 
                    self.intervals[r] = [self.intervals[r][0], val]
                elif self.intervals[r+1][0]-val == 1: 
                    self.intervals[r+1] = [val, self.intervals[r+1][1]]
                else:
                    self.intervals[r+1:r+1] = [[val, val]]    
                                              


    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.intervals
        

if __name__ == "__main__":
# Your SummaryRanges object will be instantiated and called as such:
    '''
    obj = SummaryRanges()
    obj.addNum(1)
    print(obj.getIntervals())
    obj.addNum(3)
    print(obj.getIntervals())
    obj.addNum(7)
    print(obj.getIntervals())
    obj.addNum(2)
    print(obj.getIntervals())
    obj.addNum(6)
    print(obj.getIntervals())
    '''
    obj = SummaryRanges()
    obj.addNum(6)
    print(obj.getIntervals())
    obj.addNum(6)
    print(obj.getIntervals())
    obj.addNum(0)
    print(obj.getIntervals())
    obj.addNum(4)
    print(obj.getIntervals())
    obj.addNum(8)
    print(obj.getIntervals())
    obj.addNum(7)
    print(obj.getIntervals())
    obj.addNum(6)
    print(obj.getIntervals())
    obj.addNum(4)
    print(obj.getIntervals())
    obj.addNum(7)
    print(obj.getIntervals())
    obj.addNum(5)
    print(obj.getIntervals())