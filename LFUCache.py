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


# Your LFUCache object will be instantiated and called as such:
cache = LFUCache(2)
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