'''
-Medium-

*Stack*

Design a max stack that supports push, pop, top, peekMax and popMax.

 

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you 
find more than one maximum elements, only remove the top-most one.
 

Example 1:

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
 

Note:

-1e^7 <= x <= 1e^7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.


'''

class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        
    def push(self, x: int) -> None:
        if not self.s2 or x >= self.s2[-1]: self.s2.append(x)
        self.s1.append(x)
        
    def pop(self) -> int:
        if self.s1[-1] == self.s2[-1]: self.s2.pop()
        return self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]
        
    def peekMax(self) -> int:
        return self.s2[-1]

    def popMax(self) -> int:
        mx = self.s2.pop()
        j = len(self.s1)-1
        while self.s1[j] != mx: j -= 1
        self.s1.pop(j) 
        return mx 

import heapq
class MaxStackLogN(object):
    def __init__(self):
        self.soft_deleted = set()
        self.max_heap = []
        self.recency_stack = []
        self.next_id = 0
            
    def push(self, x: int) -> None:
        heapq.heappush(self.max_heap, (-x, self.next_id))
        self.recency_stack.append((x, self.next_id))
        self.next_id -= 1

    def _clean_up(self):
        while self.recency_stack and self.recency_stack[-1][1] in self.soft_deleted:
            self.soft_deleted.remove(self.recency_stack.pop()[1])
        while self.max_heap and self.max_heap[0][1] in self.soft_deleted:
            self.soft_deleted.remove(heapq.heappop(self.max_heap)[1])
    
    def pop(self) -> int:
        entry_to_return = self.recency_stack.pop()
        self.soft_deleted.add(entry_to_return[1])
        self._clean_up()
        return entry_to_return[0]
        
    def top(self) -> int:
        return self.recency_stack[-1][0]
    def peekMax(self) -> int:
        return -self.max_heap[0][0]
        
    def popMax(self) -> int:
        value, time = heapq.heappop(self.max_heap)
        self.soft_deleted.add(time)
        self._clean_up()
        return value * -1

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

if __name__=="__main__":
    stack = MaxStack()
    stack.push(5) 
    stack.push(1)
    stack.push(5)
    print(stack.top())    # -> 5
    print(stack.popMax()) # -> 5
    print(stack.top())    # -> 1
    print(stack.peekMax()) # -> 5
    print(stack.pop()) # -> 1
    print(stack.top()) # -> 5

    stack = MaxStackLogN()
    stack.push(5) 
    stack.push(1)
    stack.push(5)
    print(stack.top())    # -> 5
    print(stack.popMax()) # -> 5
    print(stack.top())    # -> 1
    print(stack.peekMax()) # -> 5
    print(stack.pop()) # -> 1
    print(stack.top()) # -> 5
