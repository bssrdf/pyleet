''''

-Medium-

Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
 

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
 

Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Deque library.

'''

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.capacity = k
        self.size = 0
        self.tail = 0
        self.head = k-1
        self.data = [0] * k
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return False
        self.data[self.head] = value
        self.head = (self.head-1) % self.capacity     
        self.size += 1
        #print('enq: tail-> ', self.tail)
        #print('enq: data-> ', self.data)
        return True
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return False
        self.data[self.tail] = value
        self.tail = (self.tail+1) % self.capacity     
        self.size += 1
        #print('enq: tail-> ', self.tail)
        #print('enq: data-> ', self.data)
        return True
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return False
        self.head = (self.head+1) % self.capacity
        self.size -= 1
        return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return False
        self.tail = (self.tail-1) % self.capacity
        self.size -= 1
        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.data[(self.head+1)%self.capacity]
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.data[(self.tail-1)%self.capacity]

        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == self.capacity
        

if __name__=="__main__":
    circularDeque = MyCircularDeque(3) # set the size to be 3
    print(circularDeque.insertLast(1))			# return true
    print(circularDeque.insertLast(2))			# return true
    print(circularDeque.insertFront(3))			# return true
    print(circularDeque.insertFront(4))			# return false, the queue is full
    print(circularDeque.getRear())  			# return 2
    print(circularDeque.isFull())				# return true
    print(circularDeque.deleteLast())			# return true
    print(circularDeque.insertFront(4))			# return true
    print(circularDeque.getFront())			# return 4
 
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()