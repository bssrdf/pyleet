# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 00:10:01 2017

@author: merli
"""

"""
    The idea here is to build a segment tree. Each node stores the left and right
    endpoint of an interval and the sum of that interval. All of the leaves will store
    elements of the array and each internal node will store sum of leaves under it.
    Creating the tree takes O(n) time. Query and updates are both O(log n).
"""

#Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        

class NumArray(object):
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
                
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)
            
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        #Helper function to update a value
        def updateVal(root, i, val):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is then propogated upwards
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)
                
            #Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)
            
            #Propogate the changes after recursive call returns
            root.total = root.left.total + root.right.total
            
            return root.total
        
        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def rangeSum(root, i, j):
            
            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        
        return rangeSum(self.root, i, j)


# implementation using Fenwick tree
class NumArrayBIT(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.BIT = [0]*(len(nums)+1)
        self.size = len(nums)
        self.nums = nums
        for i,n in enumerate(nums):
            self.add(i, n)

    def update(self, i, val):
        self.add(i, val-self.nums[i])
        self.nums[i] = val

    def add(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        j = i + 1                
        while j <= self.size:
            self.BIT[j] += val
            j += j & (-j)

    def query(self, n):
        sum = 0
        while n > 0:
            sum += self.BIT[n]
            n -= n & (-n)
        return sum
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        #print(self.query(j+1))
        #print(self.query(i))
        return self.query(j+1) - self.query(i)   

                
if __name__ == "__main__":
  numA = NumArray([3, 1, 7, 8, 5, 10, 2])
  print(numA.sumRange(2,5))
  numC = NumArrayBIT([3, 1, 7, 8, 5, 10, 2])
  print(numC.sumRange(2,5))

  numB = NumArrayBIT([1, 3, 5])
  print(numB.sumRange(0,2))
  numB.update(1,2)
  print(numB.sumRange(0,2))
  


  