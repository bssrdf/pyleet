A = [5, 3, 1, 2, 4]
import collections
def increasingQueue(A):
    queue = collections.deque()
    firstSmallerToLeft = [None]*len(A)
    firstSmallerToRight = [None]*len(A)
    firstSmallerIndexToLeft = [-1]*len(A)
    firstSmallerIndexToRight = [len(A)]*len(A)
    for i,v in enumerate(A):
        while queue and A[queue[-1]] >= v: # right is from the popping out
            idx = queue.pop()
            firstSmallerToRight[idx] = v 
            firstSmallerIndexToRight[idx] = i
            
        if queue:  #left is from the pushing in
            firstSmallerToLeft[i] = A[queue[-1]]
            firstSmallerIndexToLeft[i] = queue[-1]
        queue.append(i)
    return firstSmallerToLeft, firstSmallerToRight, \
           firstSmallerIndexToLeft, firstSmallerIndexToRight
    
firstSmallerToLeft, firstSmallerToRight, \
firstSmallerIndexToLeft, firstSmallerIndexToRight = increasingQueue(A)
print(firstSmallerToLeft)
print(firstSmallerToRight)
print(firstSmallerIndexToLeft)
print(firstSmallerIndexToRight)

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
