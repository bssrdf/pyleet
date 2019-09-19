A = [5, 3, 1, 2, 4]
import collections
def increasingQueue(A):
    queue = collections.deque()
    firstSmallerToLeft = [-1]*len(A)
    firstSmallerToRight = [-1]*len(A)
    for i,v in enumerate(A):
        while queue and A[queue[-1]] >= v: # right is from the popping out
            firstSmallerToRight[queue.pop()] = v 
            
        if queue:  #left is from the pushing in
            firstSmallerToLeft[i] = A[queue[-1]]
        queue.append(i)
    print(queue)
    return firstSmallerToLeft, firstSmallerToRight
    
firstSmallerToLeft, firstSmallerToRight = increasingQueue(A)
print(firstSmallerToLeft)
print(firstSmallerToRight)

def decreasingQueue(A):
    queue = collections.deque()
    firstLargerToLeft = [-1]*len(A)
    firstLargerToRight = [-1]*len(A)
    for i,v in enumerate(A):
        while queue and A[queue[-1]] <= v:
            firstLargerToRight[queue.pop()] = v
            
        if queue:
            firstLargerToLeft[i] = A[queue[-1]]
        queue.append(i)
    print(queue)
    return firstLargerToLeft, firstLargerToRight
    
firstLargerToLeft, firstLargerToRight = decreasingQueue(A)
print(firstLargerToLeft)
print(firstLargerToRight)