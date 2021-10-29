'''

-Medium-
*Hash Table*
*Binary Search*


Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  
Initially, each element equals 0.

void set(index, val) sets the element at the given index to be equal to val.

int snap() takes a snapshot of the array and returns the snap_id: the total number of 
times we called snap() minus 1.

int get(index, snap_id) returns the value at the given index, at the time we took the 
snapshot with the given snap_id
 

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9


'''

from collections import defaultdict
import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.n = length
        self.m = defaultdict(list)
        self.snapid = 0
        

    def set(self, index: int, val: int) -> None:
        if index not in self.m:       
            self.m[index].append((0,0))     
        self.m[index].append((self.snapid, val))        

    def snap(self) -> int:
        res = self.snapid
        self.snapid += 1
        return res 
        

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.m: return 0
        idx = bisect.bisect_right(self.m[index], (snap_id, 10**9+1))
        return self.m[index][idx-1][1]
        

        
if __name__ == "__main__":
    snapshotArr = SnapshotArray(3) # // set the length to be 3
    snapshotArr.set(0,5)#  // Set array[0] = 5
    print(snapshotArr.snap())#  // Take a snapshot, return snap_id = 0
    snapshotArr.set(0,6) #
    print(snapshotArr.get(0,0)) #  // Get the value of array[0] with snap_id = 0, return 5
    print(snapshotArr.snap())#  // Take a snapshot, return snap_id = 0
    print(snapshotArr.get(0,1)) #  // Get the value of array[0] with snap_id = 0, return 6