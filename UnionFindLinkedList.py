
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next 
        self.rep = None

class UnionFindLL(object):    
    def __init__(self, node):
        self.head = node
        self.tail = node
        node.rep = self        
        self.size = 1
        self.pos = None

def makeSet(x):    
    uf = UnionFindLL(x)
    return uf

def findSet(x):
    return x.rep

def union(i, j):
    x, y = findSet(i), findSet(j) 
    if x.size >= y.size:
        x, y = y, x
    y.tail.next = x.head # connect the two list
    y.tail = x.tail
    y.size += x.size  
    cur = x.head
    while cur:
        cur.rep = y
       # print('in union:', cur.val)
        cur = cur.next
    del x 
    return y



class DLLNode(object):
    def __init__(self, Kj = 0, dsetNode=None):
        self.prev = None
        self.next = None
        self.dset = dsetNode
        if dsetNode:
           dsetNode.pos = self
        self.Kj = Kj


if __name__ == "__main__":
    '''
    ufs = [ None ]*9
    items = [Node(i) for i in range(1,10)]    
    for i in range(len(items)):
        ufs[i] = makeSet(items[i])
    print(findSet(items[0]).val)
    union(items[0], items[5])
    
    print(findSet(items[5]).val)
    print(findSet(items[6]).val)
    print(findSet(items[0]).val)
    union(items[0], items[6])
    print('=============================')
    print(findSet(items[5]).val)
    print(findSet(items[6]).val)
    print(findSet(items[0]).val)
    '''


    
    ops = [4, 8, 'E', 3, 'E', 9, 2, 6, 'E', 'E', 'E', 1, 7, 'E', 5]
    n = 9     
    items = [Node(i) for i in range(1,n+1)]    
    dummy = DLLNode()    
    head = dummy
    prev = None
    cnt = 0
    for i in ops:
        if i != 'E':            
            makeSet(items[i-1])
            if prev:
                union(prev, items[i-1])
            #else:
            prev = items[i-1]
        else:
            cnt += 1
            #print(i, cnt)
            if prev:
                node = DLLNode(cnt, findSet(prev))
            else:
                node = DLLNode(cnt, None)
            head.next = node
            node.prev = head
            head = head.next
            prev = None
    extracted = [0]*cnt
    cnt += 1
    if prev:
        print('##',prev.val, cnt)        
        node = DLLNode(cnt, findSet(prev))
    else:
        node = DLLNode(cnt, None)
    head.next = node
    node.prev = head 
    #'''   
    head = dummy.next
    while head:
        if head.dset:
           print('size, Kj =',head.dset.size, head.Kj)
        else:
           print('size, Kj =', 0, head.Kj)    
        head = head.next   
    #'''
    print('===============')
    for item in items:
        t = findSet(item)
        print(item.val, t.pos.Kj)
    print('===============')
    for item in items:
        t = findSet(item)
        #print(item.val, t.pos.Kj)
        if t.pos.next:
            extracted[t.pos.Kj-1] = item.val
            cur = t.pos.next
            #if cur.dset: print('head->',type(cur), type(t.pos), type(cur.dset))
           # while cur and (not cur.dset):
           #     cur = cur.next
            #print(item.val, t.pos.Kj)
            if cur.dset:
                union(cur.dset.head, item)
            else:
                cur.dset = t                     
            t.pos.prev.next = t.pos.next
            t.pos.next.prev = t.pos.prev
            #del t
    print(extracted)
             


       



	

    
        
 



        