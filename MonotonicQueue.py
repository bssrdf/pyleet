A = [5, 3, 1, 2, 4]
import collections
import bisect
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

def leftFurthestGreaterOrEqual(nums):
    n = len(nums)
    indx = [-1]*n 
    stack = []
    s1 = []
    for i in range(n-1, -1, -1):
        while stack and nums[stack[-1]] > nums[i]:
            stack.pop() 
            s1.pop()
        if stack:
            indx[stack[-1]] = i
        #else:
        #    indx[i] = 0    
        stack.append(i) 
        s1.append(nums[i])
    print(s1)
    return indx

def rightFurthestGreaterOrEqual(nums):
    A, n = nums, len(nums)    
    indx = [-1]*n 
    stack, stackv = [], []
    for i in range(n-1, -1, -1):
        if not stack or nums[stack[-1]] < nums[i]:
            stack.append(i) 
            stackv.append(nums[i])
        else:
            idx = bisect.bisect_left(stackv, nums[i])
            indx[i] = stack[idx]
    return indx

B = [2,3,3,1,2]
leftGreat = leftFurthestGreaterOrEqual(B)
print(leftGreat)
rightGreat = rightFurthestGreaterOrEqual(B)
print(rightGreat)
B = [9,8,1,0,1,9,4,0,4,1]
rightGreat = rightFurthestGreaterOrEqual(B)
print(B)
print(rightGreat)

