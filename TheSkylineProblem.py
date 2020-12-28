# -*- coding: utf-8 -*-
"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a
distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo
(Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

 Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the
x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that
0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on
an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10],
[19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that
uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point,
where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height.
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:
[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24,0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5],
[7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output
as such: [...[2 3], [4 5], [12 7], ...]
"""
__author__ = 'Daniel'
from collections import defaultdict, namedtuple
import heapq

from functools import total_ordering

@total_ordering
class Building(object):
    def __init__(self, h):
        self.h = h
        self.deleted = False  # lazy deletion
    def __str__(self):
        return str(self.h)
    def __cmp__(self, other):
        # Reverse order by height to get max-heap
        assert isinstance(other, Building)
        return other.h - self.h
    def __eq__(self, other):
        return self.h == other.h
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):        
        assert isinstance(other, Building)
        # Reverse order by height to get max-heap
        return self.h > other.h
    def __repr__(self):
        return "%s" % (self.h)

# An event represents the buildings that start and end at a particular
# x-coordinate.
Event = namedtuple('Event', 'starts ends')


class Solution:
    
    def recurSkyline(self, buildings, l, r):
        assert l <= r
        if l == r:
            return [[buildings[l][0],buildings[l][2]], [buildings[l][1],0]]
        else:
            mid = l + (r-l)//2
            
            return self.merge(self.recurSkyline(buildings, l, mid), 
                              self.recurSkyline(buildings, mid+1, r))
            
    def merge(self, lsky, rsky):
        res = []
        l, r = 0, 0  
        curh = 0
        curl,curr = 0,0
        while l < len(lsky) and r < len(rsky):          
          
            if lsky[l][0] < rsky[r][0]:
                curl = lsky[l][1]
                maxh = max(curl, curr)
                if maxh != curh:                    
                    curh = maxh
                    res.append([lsky[l][0], curh])                                
                l += 1
            elif lsky[l][0] > rsky[r][0]:
                curr = rsky[r][1]
                maxh = max(curl, curr)
                if maxh != curh:               
                    curh = maxh
                    res.append([rsky[r][0], curh])                
                r += 1       
            else:
                curl = lsky[l][1]
                curr = rsky[r][1]
                maxh = max(curl, curr)
                if maxh != curh:               
                    curh = maxh
                    res.append([rsky[r][0], curh])                
                l += 1
                r += 1
                
        if l == len(lsky):
            while r < len(rsky):
                res.append([rsky[r][0], rsky[r][1]])  
                r += 1
        if r == len(rsky):
            while l < len(lsky):
                res.append([lsky[l][0], lsky[l][1]])          
                l += 1
        #print res
        return res
        
    def getSkylineDC(self, buildings):    
        if not buildings:
            return []
        return self.recurSkyline(buildings, 0, len(buildings)-1)
        
    
    def getSkyline(self, buildings):
        """
        Sweep line
        The change of skyline only happens at start and end of buildings.

        Treat a building as entering line and leaving line
        :type buildings: list[list[int]]
        :rtype: list[list[int]]
        """
        # Map from x-coordinate to event.
        events = defaultdict(lambda: Event(starts=[], ends=[]))
        for left, right, height in buildings:
            building = Building(height)
            events[left].starts.append(building)  # possible multiple building at the same x-coordinate.
            events[right].ends.append(building)

        heap_h = []  # Heap of buildings currently standing.
        cur_h = 0  # current max height of standing buildings. the current skyline
        ret = []
        # Process events in order by x-coordinate.
        for x, event in sorted(events.items(), key=lambda x: x[0]):  # sort the dictionary by key
            #print('key = ', x)
            for building in event.starts:
               # print 'starts ', x, building
                heapq.heappush(heap_h, building)
            for building in event.ends:
               # print 'ends ',  x, building
               # mark the building to be deleted
                building.deleted = True

            # Pop any finished buildings from the top of the heap.
            # if a building ends at this location, its height cannot 
            # be part of the skyline any more
            # To avoid using multiset - lazy deletion.
            while heap_h and heap_h[0].deleted:
                heapq.heappop(heap_h)

            # Top of heap (if any) is the highest standing building, so
            # its height is the current height of the skyline.
            new_h = heap_h[0].h if heap_h else 0
            #print(x, new_h, cur_h) 
            #print(heap_h)

            if new_h != cur_h:
                cur_h = new_h
                ret.append([x, cur_h])

        return ret


if __name__ == "__main__":
    #assert Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]) == \
     #      [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    assert Solution().getSkylineDC([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]) == \
          [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    print(Solution().getSkylineDC([[1,2,1],[1,2,2],[1,2,3]]))
    print(Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], 
                                  [15, 20, 10], [19, 24, 8]]))
           