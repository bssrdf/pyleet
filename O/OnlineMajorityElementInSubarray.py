'''
-Hard-
*Fenwick Tree*

Design a data structure that efficiently finds the majority element of a given subarray.

The majority element of a subarray is an element that occurs threshold times or more in the subarray.

Implementing the MajorityChecker class:

MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] that occurs at least threshold times, or -1 if no such element exists.
 

Example 1:

Input
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
Output
[null, 1, -1, 2]

Explanation
MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2
 

Constraints:

1 <= arr.length <= 2 * 10^4
1 <= arr[i] <= 2 * 10^4
0 <= left <= right < arr.length
threshold <= right - left + 1
2 * threshold > right - left + 1
At most 10^4 calls will be made to query.


'''
from collections import defaultdict

class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.size = len(arr)
        self.BIT = [defaultdict(int) for _ in range(self.size+1)]
        for i, a in enumerate(arr):
            self.update(i+1, a)
        print(self.BIT)

    def update(self, index, val):
        while index < len(self.BIT):
            self.BIT[index][val] += 1 
            index += index & (-index)   

    def getSet(self, index):
        s = defaultdict(int)
        while index > 0:
            for key in self.BIT[index]:
                if key in s:
                    s[key] += self.BIT[index][key]
                else:
                    s[key] = self.BIT[index][key]                    
            index -= index & (-index)   
        return s


    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        lset = self.getSet(left)
        rset = self.getSet(right+1)
        for i in lset:
            if i in rset:
                rset[i] -= lset[i]
        for i in rset:
            if rset[i] >= threshold:
                return i 
        return -1
        

if __name__ == "__main__":
# Your MajorityChecker object will be instantiated and called as such:
#  obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
    majorityChecker = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(majorityChecker.query(0, 5, 4)) # return 1
    print(majorityChecker.query(0, 3, 3)) # return -1
    print(majorityChecker.query(2, 3, 2)) # return 2
