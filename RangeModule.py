'''
A Range Module is a module that tracks ranges of numbers. Your task is to 
design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), 
tracking every real number in that interval. Adding an interval that 
partially overlaps with currently tracked numbers should add any numbers in 
the interval [left, right) that are not already tracked.

queryRange(int left, int right) Returns true if and only if every real 
number in the interval [left, right) is currently being tracked.

removeRange(int left, int right) Stops tracking every real number currently 
being tracked in the interval [left, right).

Example 1:
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are 
not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, 
despite the remove operation)

Note:

A half open interval [left, right) denotes all real numbers left <= x < right.
0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
The total number of calls to addRange in a single test case is at most 1000.
The total number of calls to queryRange in a single test case is at most 5000.
The total number of calls to removeRange in a single test case is at most 1000.


'''

import bisect

class RangeModule:

    '''
    We make use of the python bisect_left and bisect_right functions. 
    bisect_left returns an insertion index in a sorted array to the left of 
    the search value. bisect_right returns an insertion index in a sorted 
    array to the right of the search value. See the python documentation. 
    To keep track of the start and end values of the ranges being tracked, 
    we use a tracking array of integers. This array consists of a number 
    of sorted pairs of start and end values. So, it always has an even 
    number of elements.

    '''

    def __init__(self):
        self.track = []

    def __str__(self):
        return str(self.track)

    def addRange(self, left, right):
        '''
        addRange first gets the leftmost insertion index of the left value and 
        the rightmost insertion index of the right value. Then, we check if 
        either of these indexes are even. If the index is even, it means that 
        it is currently outside the range of start and end indexes being tracked. 
        In this case, we include this index to be updated in the tracking array. 
        We then use python array slicing to overwrite the tracking array with the 
        left and right values placed in the correct index. Complexity is O(n).
        '''
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)

        print(start, end)	
        self.track[start:end] = subtrack

    def removeRange(self, left, right):
        '''
        removeRange first gets the leftmost insertion index of the left value and 
        the rightmost insertion index of the right value. Then, we check if 
        either of these indexes are odd. If the index is odd, it means that it is 
        currently inside the range of start and end indexes being tracked. In 
        this case, we include this index to be updated in the tracking array. We 
        then use python array slicing to overwrite the tracking array with the 
        left and right values placed in the correct index. Complexity is O(n).

        '''
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
			
        self.track[start:end] = subtrack
		
    def queryRange(self, left, right):
        '''
        queryRange gets the rightmost insertion index of the left value and the 
        leftmost insertion index of the right value. If both these indexes are 
        equal and these indexes are odd, it means the range queried is inside 
        the range of values being tracked. In this case, we return True. Else, 
        we return False. Complexity is O(log n).
        '''
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)
		
        return start == end and start % 2 == 1


if __name__ == "__main__":
    rn = RangeModule()
    rn.addRange(10, 20)
    rn.addRange(24, 30)
    print(rn)
    rn.addRange(14, 27)
    #rn.removeRange(14, 16)
    print(rn)
