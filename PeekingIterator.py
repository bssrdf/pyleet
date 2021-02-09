'''
-Medium-

Given an Iterator class interface with methods: next() and hasNext(), design and implement a 
PeekingIterator that support the peek() operation -- it essentially peek() at the element that 
will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?

'''

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.itor = iterator
        self._value = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self._value:
            self._value = self.itor.next()
        return self._value

    def next(self):
        """
        :rtype: int
        """
        if not self._value: 
            return self.itor.next()
        return self._value
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._value is not None or self.itor.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].