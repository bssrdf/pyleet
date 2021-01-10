'''

-Medium-

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also 
be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].



'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from collections import deque

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = deque()
        def make_queue(nlist):
            for a in nlist:
                if a.isInteger():
                    self.queue.append(a.getInteger())
                else:
                    make_queue(a.getList())
        make_queue(nestedList) 
            
    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0
        

if __name__ == "__main__":
    # Your NestedIterator object will be instantiated and called as such:
    i, v = NestedIterator([[1,1],2,[1,1]]), []
    while i.hasNext(): 
        v.append(i.next())
    print(v)