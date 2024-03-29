"""
-Medium-
$$$

*Iterators*


Premium Question.

Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
 

By calling next repeatedly until hasNext returns false, the order of 
elements returned by next should be: [1,2,3,4,5,6].

Hint:

How many variables do you need to keep track?
Two variables is all you need. Try with x and y.
Beware of empty rows. It could be the first few rows.
To write correct code, think about the invariant to maintain. What is it?
The invariant is x and y must always point to a valid point in the 2d vector.
Should you maintain your invariant ahead of time or right when you need it?
Not sure? Think about how you would implement hasNext(). Which is more complex?
Common logic in two different places should be refactored into a common method.
Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""
__author__ = 'Daniel'


class Vector2D:
    def __init__(self, vec2d):
        """
        :type vec2d: list[list[int]]
        :type: None
        """
        
        self.main_iter = None
        self.main_next = None
        self.sub_iter = None
        self.sub_next = None

        if not vec2d:
            return

        self.main_iter = iter(vec2d)
        self.main_next = next(self.main_iter, None)
        #print('inital array length: {} with type {}'.format(len(self.main_next), type(self.main_next))) 
        self.next_sub()
        if self.sub_iter:
            self.sub_next = next(self.sub_iter, None)

    def next_sub(self):
        while self.main_next is not None:
            if len(self.main_next) > 0:
                self.sub_iter = iter(self.main_next)
                break
            self.main_next = next(self.main_iter, None)
        self.main_next = next(self.main_iter, None)


    def next(self):
        """
        :rtype: int
        """
        val = self.sub_next

        self.sub_next = next(self.sub_iter, None)
        if self.sub_next is None:
            self.next_sub()
            self.sub_next = next(self.sub_iter, None)

        return val
       

    def hasNext(self):
        """
        This function structures the two pointers.
        :rtype: bool
        """
        # update
        return self.sub_next is not None

if __name__ == "__main__":
    v2d = [
  [1,2],
  [3],
  [4,5,6]
]
    vec2d, v = Vector2D(v2d), []
    while vec2d.hasNext(): 
        v.append(vec2d.next())
    print(v)
