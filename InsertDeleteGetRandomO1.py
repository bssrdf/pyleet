'''
-Medium-
*Hash Table*

Implement the RandomizedSet class:

bool insert(int val) Inserts an item val into the set if not present. Returns 
true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns 
true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

Follow up: Could you implement the functions of the class with each function 
works in average O(1) time?

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", 
"getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-2^31 <= val <= 2^31 - 1
At most 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

'''
import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m1 = {}
        self.m2 = {}
        self.nextid = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.m1:
            self.m1[val] = self.nextid
            self.m2[self.nextid] = val
            self.nextid += 1
            return True
        return False
        
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.m1:
            nid = self.m1.pop(val)
            self.m2.pop(nid)            
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, self.nextid-1)
        while idx not in self.m2:
            idx = random.randint(0, self.nextid-1)
        return self.m2[idx]

class RandomizedSetAC(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}
        self.arr = []
        
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.m:
            self.m[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False
        
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.m:
            nid = self.m[val]
            if nid < len(self.arr)-1:
                self.m[self.arr[-1]] = nid 
                self.arr[nid], self.arr[-1] = self.arr[-1], self.arr[nid]
            self.m.pop(val)   
            self.arr.pop()
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, len(self.arr)-1)        
        return self.arr[idx]

if __name__=="__main__":
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(1)) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    print(randomizedSet.remove(2)) # Returns false as 2 does not exist in the set.
    print(randomizedSet.insert(2)) # Inserts 2 to the set, returns true. Set now contains [1,2].
    print(randomizedSet.getRandom()) # getRandom() should return either 1 or 2 randomly.
    print(randomizedSet.remove(1))  # Removes 1 from the set, returns true. Set now contains [2].
    print(randomizedSet.insert(2))  # 2 was already in the set, so return false.
    print(randomizedSet.getRandom()) # Since 2 is the only number in the set, getRandom() will always return 2.
    
    randomizedSet = RandomizedSetAC()
    print(randomizedSet.insert(1)) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    print(randomizedSet.remove(2)) # Returns false as 2 does not exist in the set.
    print(randomizedSet.insert(2)) # Inserts 2 to the set, returns true. Set now contains [1,2].
    print(randomizedSet.getRandom()) # getRandom() should return either 1 or 2 randomly.
    print(randomizedSet.remove(1))  # Removes 1 from the set, returns true. Set now contains [2].
    print(randomizedSet.insert(2))  # 2 was already in the set, so return false.
    print(randomizedSet.getRandom()) # Since 2 is the only number in the set, getRandom() will always return 2.
 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()