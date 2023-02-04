'''
-Hard-


Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key 
exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reaches its capacity, it should invalidate the least 
frequently used item before inserting a new item. For the purpose of this
problem, when there is a tie (i.e., two or more keys that have the same 
frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to 
the get and put functions for that item since it was inserted. This 
number is set to zero when the item is removed.

'''

from collections import deque
from collections import defaultdict

class KeyNode(object):
        def __init__(self, key, next=None):
            self.key = key
            self.next = next

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.kv = {}
        self.kf = {}
        self.fk = defaultdict(deque)
        self.size = capacity
        self.minFreq = 0

    def increaseMinFreqKey(self, key):
        freq = self.kf[key] 
        self.kf[key] += 1      
        self.fk[freq].remove(key)
        self.fk[freq+1].append(key)
        if len(self.fk[freq]) == 0:
            self.fk.pop(freq)
            if freq == self.minFreq:
                self.minFreq += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.kv:           
            self.increaseMinFreqKey(key)
            return self.kv[key]
        else:
            return -1
        
    def removeMinFreqKey(self):
        kl = self.fk[self.minFreq]
        k = kl.popleft()
        if len(kl) == 0:
            self.fk.pop(self.minFreq)
        self.kv.pop(k)
        self.kf.pop(k)
    

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.kv:
            self.kv[key] = value            
            self.increaseMinFreqKey(key)
        else:
            if len(self.kv) >= self.size:
                self.removeMinFreqKey()  
            self.kv[key] = value
            self.kf[key] = 1 
            self.fk[1].append(key)
            self.minFreq = 1

import collections

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    """ An implementation of doubly linked list.
	
	Two APIs provided:
    
    append(node): append the node to the head of the linked list.
    pop(node=None): remove the referenced node. 
                    If None is given, remove the one from tail, which is the least recently used.
                    
    Both operation, apparently, are in O(1) complexity.
    """
    def __init__(self):
        self._sentinel = Node(None, None) # dummy node
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1
    
    def pop(self, node=None):
        if self._size == 0:
            return
        
        if not node:
            node = self._sentinel.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        
        return node
        
class LFUCacheDLL:
    def __init__(self, capacity):
        """
        :type capacity: int
        
        Three things to maintain:
        
        1. a dict, named as `self._node`, for the reference of all nodes given key.
           That is, O(1) time to retrieve node given a key.
           
        2. Each frequency has a doubly linked list, store in `self._freq`, where key
           is the frequency, and value is an object of `DLinkedList`
        
        3. The min frequency through all nodes. We can maintain this in O(1) time, taking
           advantage of the fact that the frequency can only increment by 1. Use the following
		   two rules:
           
           Rule 1: Whenever we see the size of the DLinkedList of current min frequency is 0,
                   the min frequency must increment by 1.
           
           Rule 2: Whenever put in a new (key, value), the min frequency must 1 (the new node)
           
        """
        self._size = 0
        self._capacity = capacity
        
        self._node = dict() # key: Node
        self._freq = collections.defaultdict(DLinkedList)
        self._minfreq = 0
        
        
    def _update(self, node):
        """ 
        This is a helper function that used in the following two cases:
        
            1. when `get(key)` is called; and
            2. when `put(key, value)` is called and the key exists.
         
        The common point of these two cases is that:
        
            1. no new node comes in, and
            2. the node is visited one more times -> node.freq changed -> 
               thus the place of this node will change
        
        The logic of this function is:
        
            1. pop the node from the old DLinkedList (with freq `f`)
            2. append the node to new DLinkedList (with freq `f+1`)
            3. if old DlinkedList has size 0 and self._minfreq is `f`,
               update self._minfreq to `f+1`
        
        All of the above opeartions took O(1) time.
        """
        freq = node.freq
        
        self._freq[freq].pop(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)
    
    def get(self, key):
        """
        Through checking self._node[key], we can get the node in O(1) time.
        Just performs self._update, then we can return the value of node.
        
        :type key: int
        :rtype: int
        """
        if key not in self._node:
            return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        """
        If `key` already exists in self._node, we do the same operations as `get`, except
        updating the node.val to new value.
        
        Otherwise, the following logic will be performed
        
        1. if the cache reaches its capacity, pop the least frequently used item. (*)
        2. add new node to self._node
        3. add new node to the DLinkedList with frequency 1
        4. reset self._minfreq to 1
        
        (*) How to pop the least frequently used item? Two facts:
        
        1. we maintain the self._minfreq, the minimum possible frequency in cache.
        2. All cache with the same frequency are stored as a DLinkedList, with
           recently used order (Always append at head)
          
        Consequence? ==> The tail of the DLinkedList with self._minfreq is the least
                         recently used one, pop it...
        
        :type key: int
        :type value: int
        :rtype: void
        """
        if self._capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
                
            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1




# Your LFUCache object will be instantiated and called as such:
'''
cache = LFUCache(2)
#cache = LFUCacheDLL(2)
# param_1 = obj.get(key)
# obj.put(key,value)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)  
print(cache.get(2))
print(cache.get(3))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
'''


#cache = LFUCache(3)
cache = LFUCacheDLL(3)
# param_1 = obj.get(key)
# obj.put(key,value)
cache.put(2, 2)
cache.put(1, 1)
print(cache.get(2))
print(cache.get(1))
print(cache.get(2))
cache.put(3, 3)
cache.put(4, 4)
print(cache.get(3))
print(cache.get(2))
print(cache.get(1))
print(cache.get(4))