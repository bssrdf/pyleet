
#Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.val = 0        
        self.lazy = 0
        self.left = None
        self.right = None

    def __repr__(self):
        return " {0} : {1} : ({2},{3})".format(self.val, self.lazy, self.start, self.end)

        

class SegmentTree(object):
    
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        self.vals = nums[:]
        self.root = self.createTree(nums, 0, len(nums)-1)
        

    def createTree(self, nums, l, r):
            
        #base case
        if l > r:
            return None
            
        #leaf node
        if l == r:
            n = Node(l, r)
            n.val = nums[l]
            return n
        
        mid = (l + r) // 2
        
        root = Node(l, r)
        
        #recursively build the Segment tree
        root.left = self.createTree(nums, l, mid)
        root.right = self.createTree(nums, mid+1, r)
        
        #Total stores the sum of all leaves under root
        #i.e. those elements lying between (start, end)
        root.val = root.left.val + root.right.val
            
        return root

    def updateLazy(self, i, j, delta):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        #Helper function to update a value
        def updateValLazy(root, i, j, delta):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is then propogated upwards
            #if not root: return 0

            if root.lazy != 0:
                root.val += root.lazy 
                if root.start != root.end:
                    root.left.lazy += root.lazy 
                    root.right.lazy += root.lazy 
                root.lazy = 0    

            if root.start == root.end:
                if root.start <= j and root.start >= i:
                   root.val += delta
                #return root.val
                return
        
            if i <= root.start and j >= root.end:
                root.val += (root.end-root.start+1)*delta
                if root.start != root.end:
                    root.left.lazy += delta
                    root.right.lazy += delta                
                #return root.val
                return

            #mid = (root.start + root.end) // 2
            
            if root.left: 
                updateValLazy(root.left, i, j, delta)
            if root.right:
                updateValLazy(root.right, i, j, delta)
            
            #Propogate the changes after recursive call returns
            root.val = root.left.val + root.right.val
            
            #return root.val
        
        #return updateValLazy(self.root, i, j, delta)    
        updateValLazy(self.root, i, j, delta)    
        
            
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
                root.val = val
                return val
        
            mid = (root.start + root.end) // 2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)
                
            #Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)
            
            #Propogate the changes after recursive call returns
            root.val = root.left.val + root.right.val
            
            return root.val
        
        return updateVal(self.root, i, val)

    def query(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def _query(root, i, j):
            
            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.val
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return _query(root.left, i, j)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return _query(root.right, i, j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return _query(root.left, i, mid) + _query(root.right, mid+1, j)
        
        return _query(self.root, i, j)

    def queryLazy(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def _query(root, i, j):            

            if root.lazy != 0:
                root.val += root.lazy 
                if root.start != root.end:
                    root.left.lazy += root.lazy 
                    root.right.lazy += root.lazy 
                root.lazy = 0    

            #If the range exactly matches the root, we already have the sum
            if i <= root.start and j >= root.end:
               return root.val
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return _query(root.left, i, j)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return _query(root.right, i, j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return _query(root.left, i, mid) + _query(root.right, mid+1, j)
        
        return _query(self.root, i, j)

    def print(self):
        def _print(root, lvl):
            if root:
                print("\t"*lvl, end='->')
                print(root)
                _print(root.left, lvl+1)
                _print(root.right, lvl+1)
        _print(self.root, 0)



        
if __name__ == '__main__':   
    sg = SegmentTree([2,3,1,4])
    sg.print()
    print(sg.query(1,3))
    sg.update(1, 2)
    sg.print()
    print(sg.query(1,3))
    sg.updateLazy(1, 2, 1)
    sg.print()
    print(sg.queryLazy(1,3))
    sg.print()
    print('***********************')
    sg.updateLazy(0, 2, 5)
    sg.print()
    print(sg.queryLazy(1,3))
    sg.print()
    print(sg.queryLazy(0,3))
    sg.print()

