'''
$$$
-Easy-

Design and implement a TwoSum class. It should support the following 
operations: add and find.
  
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal 
to the value.

Example 1:

add(1); add(3); add(5);                                                                                                                    
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false

'''

class TwoSum(object):

    def __init__(self):
        """

        """
        self.m = {}

    def add(self, x):
        """

        """
        if x in self.m:
            self.m[x] += 1
        else:
            self.m[x] = 1


    def find(self, x):
        for y in self.m:
            z = x - y            
            if z in self.m:
                if z == y and self.m[z] > 1:
                    return True
                if z != y:
                    return True
        return False




if __name__ == "__main__":
    tw = TwoSum()
    tw.add(1) 
    tw.add(3) 
    tw.add(5)
    print(tw.find(4))
    print(tw.find(7))

    tw = TwoSum()
    tw.add(2)     
    tw.add(5)
    print(tw.find(4))
    print(tw.find(7))
