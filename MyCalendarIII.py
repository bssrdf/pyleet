'''
-Hard-
*Segment Tree*
*Lazy Propagation*

A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.
 

Example 1:

Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3
 

Constraints:

0 <= start < end <= 10^9
At most 400 calls will be made to book.


'''

class SegmentTree:
    class SegmentTreeNode:
        def __init__(self, l, r, val=0):
            self.l = l
            self.r = r
            self.left = self.right = None
            self.lazy = 0
            self.val = val

    def __init__(self, l, r):
        self.root = self.SegmentTreeNode(l, r, 0)

    def normalize(self, node):

        if node.l < node.r:
            if not node.left or not node.right:
                mid = (node.l + node.r) // 2
                node.left = self.SegmentTreeNode(node.l, mid, node.val)
                node.right = self.SegmentTreeNode(mid+1, node.r, node.val)
            elif node.lazy > 0:
                node.left.val += node.lazy
                node.right.val += node.lazy
                node.left.lazy += node.lazy
                node.right.lazy += node.lazy

        node.lazy = 0
    
    def query(self, start, end):
        return self._query(start, end, self.root)

    def _query(self, start, end, node):        

        if start > end or not node or node.l > end or node.r < start:
            return 0

        if start <= node.l and node.r <= end:
            return node.val
        
        self.normalize(node)

        return max(self._query(start, end, node.left), self._query(start, end, node.right))


    def update(self, start, end):
        return self._update(start, end, self.root, 1)

    def _update(self, start, end, node, val):
        
        if start > end or not node or node.l > end or node.r < start:
            return

        if start <= node.l and node.r <= end:
            node.val += val
            node.lazy += val
            return

        self.normalize(node)
        
        self._update(start, end, node.left, val)
        self._update(start, end, node.right, val)

        node.val = max(node.left.val, node.right.val)

class MyCalendarThree(object):

    def __init__(self):
        self.sTree = SegmentTree(0, 10**9+1)
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """        
        self.sTree.update(start, end-1)
        return self.sTree.root.val

import collections

class MyCalendarThreeSegmenTreeFast(object):

    def __init__(self):
        
        self.seg = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """       
        def update(s, e, l = 0, r = 10**9, ID = 1):
            if r <= s or e <= l: return 
            if s <= l < r <= e:
                self.seg[ID] += 1
                self.lazy[ID] += 1
            else:
                m = (l + r) // 2
                update(s, e, l, m, 2 * ID)
                update(s, e, m, r, 2*ID+1)
                self.seg[ID] = self.lazy[ID] + max(self.seg[2*ID], self.seg[2*ID+1])
        update(start, end)
        return self.seg[1]


class TreeNode:
    def __init__(self,start,end,count):
        self.start = start
        self.end = end
        self.count = count
        self.right,self.left = None, None
   

class MyCalendarThreeBST(object):

    def __init__(self):        
        self.root = None
        self.res = 0
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """   
        self.root = self.build(start, end, self.root, 1)
        return self.res
        
    def build(self, start, end, root, count):
        if not root:
			# Base condition to add node in BST
            root = TreeNode(start, end, count)
            self.res = max(self.res, root.count)
        elif start >= root.end: 
			# No overlap, add  node in right subtree
            root.right = self.build(start, end, root.right, count)
        elif end <= root.start: 
			# No overlap, add node in left subtree
            root.left = self.build(start, end, root.left, count)
        else: 
			# Overlap, break nodes into multiple nodes (1/2/3 nodes)
            startMin = min(start, root.start)
            startMax = max(start, root.start)
            endMin = min(end, root.end)
            endMax = max(end, root.end)
            if startMin < startMax:
				# No need to add new node if both are equal, instead update the count of current node.
                root.left = self.build(startMin, startMax, root.left,  
                            count if start < root.start else root.count)

            if endMin < endMax: 
				# No need to add new node if both are equal, instead update the count of current node.
                root.right = self.build(endMin, endMax, root.right, 
                                  count if end > root.end else root.count)

            root.start = startMax
            root.end = endMin
            root.count += count
            self.res = max(self.res, root.count)
        return root



if __name__ == "__main__":
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
    myCalendar = MyCalendarThreeBST()
    print(myCalendar.book(10, 20)) # returns 1
    print(myCalendar.book(50, 60)) # returns 1
    print(myCalendar.book(10, 40)) # returns 2
    print(myCalendar.book(5,  15)) # returns 3
    print(myCalendar.book(5,  10)) # returns 3
    print(myCalendar.book(25, 55)) # returns 3