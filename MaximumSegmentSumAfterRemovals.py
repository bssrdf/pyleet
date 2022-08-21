'''
-Hard-

You are given two 0-indexed integer arrays nums and removeQueries, both of length n. For the ith query, the element in nums at the index removeQueries[i] is removed, splitting nums into different segments.

A segment is a contiguous sequence of positive integers in nums. A segment sum is the sum of every element in a segment.

Return an integer array answer, of length n, where answer[i] is the maximum segment sum after applying the ith removal.

Note: The same index will not be removed more than once.

 

Example 1:

Input: nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
Output: [14,7,2,2,0]
Explanation: Using 0 to indicate a removed element, the answer is as follows:
Query 1: Remove the 0th element, nums becomes [0,2,5,6,1] and the maximum segment sum is 14 for segment [2,5,6,1].
Query 2: Remove the 3rd element, nums becomes [0,2,5,0,1] and the maximum segment sum is 7 for segment [2,5].
Query 3: Remove the 2nd element, nums becomes [0,2,0,0,1] and the maximum segment sum is 2 for segment [2]. 
Query 4: Remove the 4th element, nums becomes [0,2,0,0,0] and the maximum segment sum is 2 for segment [2]. 
Query 5: Remove the 1st element, nums becomes [0,0,0,0,0] and the maximum segment sum is 0, since there are no segments.
Finally, we return [14,7,2,2,0].
Example 2:

Input: nums = [3,2,11,1], removeQueries = [3,2,1,0]
Output: [16,5,3,0]
Explanation: Using 0 to indicate a removed element, the answer is as follows:
Query 1: Remove the 3rd element, nums becomes [3,2,11,0] and the maximum segment sum is 16 for segment [3,2,11].
Query 2: Remove the 2nd element, nums becomes [3,2,0,0] and the maximum segment sum is 5 for segment [3,2].
Query 3: Remove the 1st element, nums becomes [3,0,0,0] and the maximum segment sum is 3 for segment [3].
Query 4: Remove the 0th element, nums becomes [0,0,0,0] and the maximum segment sum is 0, since there are no segments.
Finally, we return [16,5,3,0].
 

Constraints:

n == nums.length == removeQueries.length
1 <= n <= 105
1 <= nums[i] <= 109
0 <= removeQueries[i] < n
All the values of removeQueries are unique.


'''

from typing import List

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.maxSum = 0
        self.total = 0
        self.left = None
        self.right = None
        

class SegTree(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        #helper function to create the tree from input array
        def createTree(nums, l, r):
            
            #base case
            if l > r:
                return None
                
            #leaf node
            if l == r:
                n = Node(l, r)
                n.maxSum = nums[l]
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            
            root = Node(l, r)
            
            #recursively build the Segment tree
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            
            #Total stores the sum of all leaves under root
            #i.e. those elements lying between (start, end)
            root.total = root.left.total + root.right.total
            root.maxSum = max(root.left.total, root.right.total)
                
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)
            
    def update(self, i):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        #Helper function to update a value
        def updateVal(root, i):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is then propogated upwards
            if root.start == root.end:
                root.total = 0
                root.maxSum = 0
                return
        
            mid = (root.start + root.end) // 2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
               updateVal(root.left, i)
                
            #Otherwise, the right subtree
            else:
                updateVal(root.right, i)
            
            #Propogate the changes after recursive call returns
            root.total = root.left.total + root.right.total
            root.maxSum = max(root.left.total, root.right.total)
            if root.start == 0 and root.end == 2:
                print(root.total, root.maxSum )
        
        updateVal(self.root, i)

    def query(self):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        return self.root.maxSum 

class Item(object):
    def __init__(self, sm):
        # self.start = s
        # self.end = t
        self.total = sm
        self.valid = True 

    def __lt__(self, other):
        return self.total > other.total

import heapq
from sortedcontainers import SortedList
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        preSum = [0]*(n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
        m = {}
        # m[(0, n-1)] = Item(0, n-1, preSum[-1])    
        m[(0, n-1)] = Item(preSum[-1])    
        pq = [m[(0,n-1)]]
        sl = SortedList([(0, n-1)])
        ans = [0]*n
        for i in range(n):
            idx = removeQueries[i]
            j = max(0, sl.bisect_right((idx, n)) - 1)             

            print('a', j, idx, sl)
            # if j < len(sl):
            m[sl[j]].valid = False
            s, t = sl[j]
            sl.pop(j)
            if idx-1 >= s:
                m[(s, idx-1)] = Item(preSum[idx]-preSum[s])
                heapq.heappush(pq, m[(s, idx-1)]) 
                sl.add((s, idx-1))
            if idx+1 <= t:
                m[(idx+1,t)] = Item(preSum[t+1]-preSum[idx+1])
                heapq.heappush(pq, m[(idx+1, t)])                             
                sl.add((idx+1, t))
                
            print('b', j, idx, sl)
            while pq and not pq[0].valid:
                heapq.heappop(pq)
            if pq:    
               ans[i] = pq[0].total 
        return ans



if __name__ == "__main__":
    # print(Solution().maximumSegmentSum(nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]))
    # print(Solution().maximumSegmentSum(nums = [3,2,11,1], removeQueries = [3,2,1,0]))
    nums = [244,19,445,671,801,103,291,335,781,33,51,789,746,510,38,7,529,905]
    removeQueries = [4,8,11,12,1,5,0,9,6,17,3,15,14,7,2,13,16,10]
    print(Solution().maximumSegmentSum(nums = nums, removeQueries = removeQueries))
