
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


class SegmentTree2:
    # bottom-up segment tree
    def __init__(self, N, query_fn, update_fn):
        self.base = N
        self.query_fn = query_fn
        self.update_fn = update_fn
        self.tree = [0]*(2*N)
        self.lazy = [0]*(2*N)
        self.count = [1]*(2*N)
        H = 1
        while 1 << H < N:
            H += 1
        self.H = H
        for i in range(N-1, 0, -1):
            self.count[i] = self.count[i<<1] + self.count[(i<<1)+1]
    def update(self, L, R, val):
        L += self.base
        R += self.base
        self.push(L)#  // key point
        self.push(R)#  // key point
        L0, R0 = L, R
        while L <= R:
            if (L & 1) == 1:
                self.apply(L, val)
                L += 1
            if (R & 1) == 0: 
                self.apply(R, val)
                R -= 1
            L >>= 1
            R >>= 1
        self.pull(L0)
        self.pull(R0)

    def query(self, L, R):
        result = 0
        if L > R:
            return result        
        L += self.base
        R += self.base
        self.push(L)
        self.push(R)
        while L <= R:
            if (L & 1) == 1:
                result = self.query_fn(result, self.tree[L])
                L += 1
            if (R & 1) == 0:
                result = self.query_fn(result, self.tree[R])
                R -= 1
            L >>= 1; R >>= 1
        return result
    
    def apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val * self.count[x])
        if x < self.base:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def pull(self, x):
        while x > 1:
            x >>= 1
            # print(x << 1, x<<1+1)
            self.tree[x] = self.query_fn(self.tree[x<<1], self.tree[(x<<1) + 1])
            if self.lazy[x]:
                self.tree[x] = self.update_fn(self.tree[x], self.lazy[x] * self.count[x])
    def push(self, x):
        for h in range(self.H, 0, -1):
           y = x >> h
           if self.lazy[y]:
                self.apply(y << 1,     self.lazy[y])
                self.apply((y << 1) + 1, self.lazy[y])
                self.lazy[y] = 0


from math import ceil, log2

class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:x+y, basef=lambda x:x, basev = 0):
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = len(array)
        self.array = array
        self.tree = [0] * ( 2**ceil(log2(len(array))+1) - 1 )
        self.build(array)
    
    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if(l==r):
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l+r)//2
        self.tree[i] = self.merge(self._build_util(l,mid, 2*i+1, a), self._build_util(mid+1, r, 2*i+2, a))
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a)-1, 0, a)

    def _query_util(self, i, ln, rn, l, r):
        if ln>=l and rn<=r:
            return self.tree[i]
        if ln>r or rn<l:
            return self.basev
        return self.merge( self._query_util( 2*i+1, ln, (ln+rn)//2, l, r ), self._query_util( 2*i+2, (ln+rn)//2+1, rn, l, r ) )

    def query(self, l, r):
        return self._query_util( 0, 0, self.n-1, l, r )

    def _update_util(self, i, ln, rn, x, v):
        if x>=ln and x<=rn:
            if ln != rn:
                self._update_util( 2*i+1, ln, (ln+rn)//2, x, v )
                self._update_util( 2*i+2, (ln+rn)//2 + 1, rn, x, v )
                self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
            else:
                self.tree[i] = self.basef(v)

    def update(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] = v 


class SEG:
    # a basic segment tree template
    # it is capable of:
    # 1. modify one element in the array;
    # 2. find the max of elements on some segment or min or sum
    
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n
       
    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0 # for max range query if minimum is > 0 or
                # for sum range query 
        # ans = -inf # for max range query if minimum is allowed to be < 0
        # ans = inf # for min range query 
        while l < r:
            if l & 1: # same as l % 2, aka l is odd
                ans = max(ans, self.tree[l])   # for max range query
                #ans = min(ans, self.tree[l])  # for min range query
                #ans += self.tree[l]           # for sum range query
                l += 1 # l is even now
            if r & 1: # same as r % 2, aka r is odd
                r -= 1 # r is even now
                ans = max(ans, self.tree[r])   # for max range query
                #ans = min(ans, self.tree[r])  # for min range query
                #ans += self.tree[r]           # for sum range query
            l >>= 1
            r >>= 1
        return ans
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1]) # for max range query
            #self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1]) # for min range query
            #self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1] # for sum range query


        
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

