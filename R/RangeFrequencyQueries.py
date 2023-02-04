'''
-Medium-

Design a data structure to find the frequency of a given value in a given subarray.

The frequency of a value in a subarray is the number of occurrences of that value 
in the subarray.

Implement the RangeFreqQuery class:

RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed 
integer array arr.

int query(int left, int right, int value) Returns the frequency of value in the 
subarray arr[left...right].

A subarray is a contiguous sequence of elements within an array. arr[left...right] 
denotes the subarray that contains the elements of nums between indices left and 
right (inclusive).

 

Example 1:

Input
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
Output
[null, 1, 2]

Explanation
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i], value <= 104
0 <= left <= right < arr.length
At most 105 calls will be made to query


'''

from typing import List
from collections import defaultdict

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.vals = defaultdict(int)        
        self.left = None
        self.right = None

class SegmentTree(object):
    
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        # self.vals = nums[:]
        self.root = self.createTree(nums, 0, len(nums)-1)

    def createTree(self, nums, l, r):
            
        #base case
        if l > r:
            return None
            
        #leaf node
        if l == r:
            n = Node(l, r)
            n.vals[nums[l]] = 1
            return n
        
        mid = (l + r) // 2
        
        root = Node(l, r)
        
        #recursively build the Segment tree
        root.left = self.createTree(nums, l, mid)
        root.right = self.createTree(nums, mid+1, r)
        
        #Total stores the sum of all leaves under root
        #i.e. those elements lying between (start, end)

        for i in root.left.vals: 
            root.vals[i] = root.left.vals[i]
        for i in root.right.vals: 
            root.vals[i] += root.right.vals[i]     
            
        return root
    
    def query(self, i, j, val):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def _query(root, i, j, val):
            
            if val not in root.vals: return 0
            
            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.vals[val]
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return _query(root.left, i, j, val)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return _query(root.right, i, j, val)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return _query(root.left, i, mid, val) + _query(root.right, mid+1, j, val)
        
        return _query(self.root, i, j, val)


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.segtr = SegmentTree(arr)
        

    def query(self, left: int, right: int, value: int) -> int:
        return self.segtr.query(left, right, value)



if __name__ == "__main__":   
    rangeFreqQuery = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])

    print(rangeFreqQuery.query(1, 2, 4))   #  return 1. The value 4 occurs 1 time in the subarray [33, 4]
    print(rangeFreqQuery.query(0, 11, 33)) # return 2. The value 33 occurs 2 times in the whole array.
