'''
-Hard-
*Hash Table*

Design a data structure that supports all following operations in average 
O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. 
The probability of each element being returned is linearly related to the 
number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();


'''

import random
from collections import defaultdict

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m1 = defaultdict(list)
        self.m2 = {}
        self.nextid = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        present = val in self.m1
        self.m1[val].append(self.nextid)            
        self.m2[self.nextid] = val
        self.nextid += 1
        return not present
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.m1:
            nid = self.m1[val].pop()
            if len(self.m1[val]) == 0:
                self.m1.pop(val)
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

if __name__=="__main__":
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(1)) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    print(randomizedSet.insert(1)) # Returns false as 2 does not exist in the set.
    print(randomizedSet.insert(2)) # Inserts 2 to the set, returns true. Set now contains [1,2].
    print(randomizedSet.getRandom()) # getRandom() should return either 1 or 2 randomly.
    print(randomizedSet.remove(1))  # Removes 1 from the set, returns true. Set now contains [2].
    print(randomizedSet.getRandom()) # Since 2 is the only number in the set, getRandom() will always return 2.