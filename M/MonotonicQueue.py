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
    n = len(A)
    # queue = collections.deque()
    queue = []
    firstLargerToLeft = [-1]*len(A)
    firstLargerToRight = [-1]*len(A)
    firstLargerIndexToLeft = [0]*len(A)
    firstLargerIndexToRight = [n]*len(A)
    for i,v in enumerate(A):
        while queue and A[queue[-1]] < v:
            k = queue.pop()
            firstLargerToRight[k] = v
            firstLargerIndexToRight[k] = i
            
        if queue:
            firstLargerToLeft[i] = A[queue[-1]]
            firstLargerIndexToLeft[i] = queue[-1]
        queue.append(i)
    # print(queue)
    return firstLargerToLeft, firstLargerToRight, firstLargerIndexToLeft, firstLargerIndexToRight
    
firstLargerToLeft, firstLargerToRight, _, _ = decreasingQueue(A)
print(firstLargerToLeft)
print(firstLargerToRight)

# A = [3,1,3,5]
# A = [4,1,3,6]
# A = [2,1,3,6]
A = [4,1,3,3,6]
_, _, _,  firstLargerIndexToRight = decreasingQueue(A)
print('larger to the right', firstLargerIndexToRight)
mark = [0]*(len(A)+1)
for i in range(len(A)):
    mark[firstLargerIndexToRight[i]] -= 1
    mark[i+1] += 1
print('mark', mark)
res = [0]*len(A)
res[0] = mark[0]   
for i in range(1, len(A)):
    res[i] = res[i-1] + mark[i]
print(res)






def leftFurthestGreaterOrEqual(nums):
    n = len(nums)    
    indx = [-1]*n 
    stack, stackv = [], []
    for i in range(n):
        if not stack or nums[stack[-1]] < nums[i]:
            stack.append(i) 
            stackv.append(nums[i])
        else:
            idx = bisect.bisect_left(stackv, nums[i])
            indx[i] = stack[idx]
    return indx

def rightFurthestGreaterOrEqual(nums):
    n = len(nums)    
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
print(rightGreat)

