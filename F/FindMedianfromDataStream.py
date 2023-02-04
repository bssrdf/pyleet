'''

-Hard-
*Heap*
*Priority Queue*

Median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

'''

from heapq import (heappush, heappushpop)

class MedianFinder(object):
    """
    The invariant of the algorithm is two heaps, small and large, each represent half of 
    the current list. The length of smaller half is kept to be n / 2 at all time and the 
    length of the larger half is either n / 2 or n / 2 + 1 depend on n's parity.

    This way we only need to peek the two heaps' top number to calculate median.

    Any time before we add a new number, there are two scenarios, (total n numbers, k = n / 2):

    (1) length of (small, large) == (k, k)
    (2) length of (small, large) == (k, k + 1)
    After adding the number, total (n + 1) numbers, they will become:

    (1) length of (small, large) == (k, k + 1)
    (2) length of (small, large) == (k + 1, k + 1)
    Here we take the first scenario for example, we know the large will gain one more 
    item and small will remain the same size, but we cannot just push the item into large. 
    What we should do is we push the new number into small and pop the maximum item from 
    small then push it into large (all the pop and push here are heappop and heappush). By 
    doing this kind of operations for the two scenarios we can keep our invariant.

    Therefore to add a number, we have 3 O(log n) heap operations. Luckily the heapq provided 
    us a function "heappushpop" which saves some time by combine two into one. The document 
    says:

    Push item on the heap, then pop and return the smallest item from the heap. The combined 
    action runs more efficiently than heappush() followed by a separate call to heappop().
    Alltogether, the add operation is O(logn), The findMedian operation is O(1).
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        print('small: ', self.small)
        print('large: ', self.large)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])       

        

if __name__ == "__main__":
# Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()
    obj.addNum(-1)
    print(obj.findMedian())
    obj.addNum(-2)
    print(obj.findMedian())
    obj.addNum(-3)
    print(obj.findMedian())
    obj.addNum(-4)
    print(obj.findMedian())
    obj.addNum(-5)
    print(obj.findMedian())
    
