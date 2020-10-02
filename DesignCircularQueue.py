'''
Design your implementation of the circular queue. The circular queue is a linear 
data structure in which the operations are performed based on FIFO (First In 
First Out) principle and the last position is connected back to the first 
position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces 
in front of the queue. In a normal queue, once the queue becomes full, we cannot 
insert the next element even if there is a space in front of the queue. But using 
the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the 
operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the 
operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
 

Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4

'''

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.capacity = k
        self.size = 0
        self.tail = 0
        self.head = k-1
        self.data = [0] * k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
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
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return False
        self.head = (self.head+1) % self.capacity
        self.size -= 1
        #print('deq: head-> ', self.head)
        #print('deq: data-> ', self.data)
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.data[(self.head+1)%self.capacity]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """        
        return -1 if self.isEmpty() else self.data[(self.tail-1)%self.capacity]


        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.capacity


if __name__=="__main__":

    circularQueue = MyCircularQueue(5)
    print(circularQueue.enQueue(1))   # return true
    print(circularQueue.enQueue(2))   # return true
    print(circularQueue.enQueue(3))   # return true
    #print(circularQueue.enQueue(4))   # return false, the queue is full
    #print(circularQueue.enQueue(5))   # return false, the queue is full
    print(circularQueue.Rear())  # return 3
    print(circularQueue.isFull())  # return true
    print(circularQueue.deQueue())  # return true
    print(circularQueue.Front())  # return true
    print(circularQueue.enQueue(4))  # return true
    print(circularQueue.Rear())  # return 4
