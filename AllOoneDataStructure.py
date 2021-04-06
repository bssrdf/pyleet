'''
-Hard-

Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is 
guaranteed to be a non-empty string.

Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an 
existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed 
to be a non-empty string.

GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return
 an empty string "".

GetMinKey() - Returns one of the keys with minimal value. If no element exists, return 
an empty string "".

Challenge: Perform all these in O(1) time complexity.


'''


from collections import defaultdict

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = defaultdict(set)    
        self.m = {}

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key not in self.m:
            self.buckets[1].add(key)
            self.m[key] = 1                
        else:
            val = self.m[key]
            self.buckets[val].remove(key)
            if not self.buckets[val]: self.buckets.pop(val)                
            self.buckets[val+1].add(key)
            self.m[key] = val+1   
            

        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key in self.m:            
            val = self.m[key]
            self.buckets[val].remove(key)
            if not self.buckets[val]: self.buckets.pop(val)                
            val1 = val - 1
            if val1 != 0:
               self.buckets[val1].add(key)
               self.m[key] = val1
            else: self.m.pop(key)

    def printState(self):
        print(self.buckets)
        print(self.m)
 
          
 

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.buckets:
            mk = max(self.buckets.keys())
            for x in self.buckets[mk]:
                return x 
        return ''
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.buckets:
            mk = min(self.buckets.keys())
            for x in self.buckets[mk]:
                return x 
        return ''

if __name__ == "__main__":
    ao = AllOne()
    '''
    ao.inc('hello')
    ao.printState()
    print("====================")
    ao.inc('hello')
    ao.printState()
    print(ao.getMaxKey())
    print(ao.getMinKey())
    ao.inc('leet')
    ao.printState()
    print(ao.getMaxKey())
    print(ao.getMinKey())
    ao.inc('hello')
    ao.inc('goodbye')
    #ao.printState()
    #print("===================")
    ao.inc('hello')
    #ao.printState()
    
    ao.inc('hello')
    #ao.printState()
    print(ao.getMaxKey())
    ao.inc('leet')
    #ao.printState()
    print("===================")
    ao.inc('code')
    ao.inc('leet')
    #ao.printState()
    #ao.printState()
    ao.dec('hello')
    print(ao.getMaxKey())
    ao.inc('leet')
    ao.inc('code')
    ao.inc('code')
    print(ao.getMaxKey())
    '''

    ao.inc('a')
    ao.inc('b')
    ao.inc('b')
    ao.inc('c')
    ao.inc('c')
    ao.inc('c')
    #ao.printState()
    ao.dec('b')
    
    ao.dec('b')
    ao.printState()
    print(ao.getMinKey())
    ao.dec('a')

    print(ao.getMaxKey())
    print(ao.getMinKey())



