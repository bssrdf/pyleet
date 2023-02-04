'''

-Medium-
*Binary Search*
*Sorted List*

Design Memory Allocator

You are given an integer n representing the size of a 0-indexed memory array. All memory units are initially free.

You have a memory allocator with the following functionalities:

Allocate a block of size consecutive free memory units and assign it the id mID.
Free all memory units with the given id mID.
Note that:

Multiple blocks can be allocated to the same mID.
You should free all the memory units with mID, even if they were allocated in different blocks.
Implement the Allocator class:

Allocator(int n) Initializes an Allocator object with a memory array of size n.
int allocate(int size, int mID) Find the leftmost block of size consecutive free memory units and allocate it with the id mID. Return the block's first index. If such a block does not exist, return -1.
int free(int mID) Free all memory units with the id mID. Return the number of memory units you have freed.
 

Example 1:

Input
["Allocator", "allocate", "allocate", "allocate", "free", "allocate", "allocate", "allocate", "free", "allocate", "free"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
Output
[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]

Explanation
Allocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory units are initially free.
loc.allocate(1, 1); // The leftmost block's first index is 0. The memory array becomes [1,_,_,_,_,_,_,_,_,_]. We return 0.
loc.allocate(1, 2); // The leftmost block's first index is 1. The memory array becomes [1,2,_,_,_,_,_,_,_,_]. We return 1.
loc.allocate(1, 3); // The leftmost block's first index is 2. The memory array becomes [1,2,3,_,_,_,_,_,_,_]. We return 2.
loc.free(2); // Free all memory units with mID 2. The memory array becomes [1,_, 3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
loc.allocate(3, 4); // The leftmost block's first index is 3. The memory array becomes [1,_,3,4,4,4,_,_,_,_]. We return 3.
loc.allocate(1, 1); // The leftmost block's first index is 1. The memory array becomes [1,1,3,4,4,4,_,_,_,_]. We return 1.
loc.allocate(1, 1); // The leftmost block's first index is 6. The memory array becomes [1,1,3,4,4,4,1,_,_,_]. We return 6.
loc.free(1); // Free all memory units with mID 1. The memory array becomes [_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
loc.allocate(10, 2); // We can not find any free block with 10 consecutive free memory units, so we return -1.
loc.free(7); // Free all memory units with mID 7. The memory array remains the same since there is no memory unit with mID 7. We return 0.
 

Constraints:

1 <= n, size, mID <= 1000
At most 1000 calls will be made to allocate and free.


'''



import bisect
from collections import defaultdict
class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.blocks = [[0, n]]
        self.ids = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        ret = -1
        for i, b in enumerate(self.blocks):
            if b[1] - b[0] > size:                
                ret = b[0]       
                b[0] = b[0] + size
                self.ids[mID].append((ret, ret+size))                
                return ret
            elif b[1] - b[0] == size:                           
                ret = b[0]       
                self.ids[mID].append((ret, ret+size))                       
                break     
        if ret != -1:
            self.blocks.pop(i)
        return ret
                
        

    def free2(self, mID: int) -> int:
        self.ids[mID].sort()   
        i, j = 0, 0
        newb = []
        ret = 0
        # print(mID, 'len', len(self.ids[mID]))
        while i < len(self.ids[mID]) and j < len(self.blocks):
            a, b = self.ids[mID][i]
            ret += b - a
            c, d = self.blocks[j]
            # print(i, a, b, j, c, d)
            if b < c:
                newb.append([a, b])
                i += 1
            elif a > d:
                newb.append([c, d])
                j += 1
            elif b == c:
                newb.append([a, d])
                i += 1
                j += 1
            elif a == d:
                newb.append([c, b])
                i += 1
                j += 1
            # print(i, a, b, j, c, d)
        while i < len(self.ids[mID]):
            a, b = self.ids[mID][i]
            ret += b - a
            newb.append([a, b])
            i += 1
        while j < len(self.blocks):
            c, d = self.blocks[j]
            newb.append([c, d]) 
            j += 1 
        self.blocks = newb
        return ret
    
    def free(self, mID: int) -> int:
        ret = 0

        for (a,b) in self.ids[mID]:
            ret += b - a 
            if not self.blocks:
                self.blocks.append([a,b])
                continue
            idx = bisect.bisect_left(self.blocks, [a, b])
            if idx == len(self.blocks):
                if self.blocks[-1][1] == a:
                    self.blocks[-1][1] = b
                else:
                    self.blocks.append([a,b])
            elif idx == 0:
                if self.blocks[0][0] == b:
                    self.blocks[0][0] = a
                else:
                    self.blocks.insert(0, [a,b])
            else:
                if self.blocks[idx-1][1] < a and b < self.blocks[idx][0]:
                    self.blocks.insert(idx, [a,b])
                elif self.blocks[idx-1][1] == a and  b == self.blocks[idx][0]:
                    self.blocks[idx-1][1] = self.blocks[idx][1]
                    self.blocks.pop(idx)
                elif self.blocks[idx-1][1] == a:
                    self.blocks[idx-1][1] = b
                elif b == self.blocks[idx][0]:
                    self.blocks[idx][0] = a
        self.ids.pop(mID)
        return ret
    
if __name__ == "__main__":
    loc = Allocator(10) # Initialize a memory array of size 10. All memory units are initially free.
    print(loc.allocate(1, 1))# // The leftmost block's first index is 0. The memory array becomes [1,_,_,_,_,_,_,_,_,_]. We return 0.
    print(loc.allocate(1, 2))# // The leftmost block's first index is 1. The memory array becomes [1,2,_,_,_,_,_,_,_,_]. We return 1.
    print(loc.allocate(1, 3))# // The leftmost block's first index is 2. The memory array becomes [1,2,3,_,_,_,_,_,_,_]. We return 2.
    print(loc.free(2))# // Free all memory units with mID 2. The memory array becomes [1,_, 3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
    print(loc.allocate(3, 4))# // The leftmost block's first index is 3. The memory array becomes [1,_,3,4,4,4,_,_,_,_]. We return 3.
    print(loc.allocate(1, 1))# // The leftmost block's first index is 1. The memory array becomes [1,1,3,4,4,4,_,_,_,_]. We return 1.
    print(loc.allocate(1, 1))# // The leftmost block's first index is 6. The memory array becomes [1,1,3,4,4,4,1,_,_,_]. We return 6.
    print(loc.free(1))# // Free all memory units with mID 1. The memory array becomes [_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
    print(loc.allocate(10, 2))# // We can not find any free block with 10 consecutive free memory units, so we return -1.
    print(loc.free(7))# // Free all memory units with mID 7. The memory array remains the same since there is no memory unit with mID 7. We return 0.


    ins = ["allocate","allocate","allocate","allocate","free","free","free","allocate","allocate","allocate","allocate","free","free","free","free","free","free","free","allocate","free","free","allocate","free","allocate","allocate","free","free","free","allocate","allocate","allocate","allocate","free","allocate","free","free","allocate","allocate","allocate","allocate","allocate","allocate","allocate","free","free","free","free"]
    para = [[12,6],[28,16],[17,23],[50,23],[6],[10],[10],[16,8],[17,41],[44,27],[12,45],[33],[8],[16],[23],[23],[23],[29],[38,32],[29],[6],[40,11],[16],[22,33],[27,5],[3],[10],[29],[16,14],[46,47],[48,9],[36,17],[33],[14,24],[16],[8],[2,50],[31,36],[17,45],[46,31],[2,6],[16,2],[39,30],[33],[45],[30],[27]]    
    loc = Allocator(50)
    ans = []
    for i, p in zip(ins, para):
        if i == 'allocate':
            ret = loc.allocate(*p)
        else:        
            ret = loc.free(p[0])
        ans.append(ret)
    sol = [0,12,-1,-1,12,0,0,-1,-1,-1,0,0,0,28,0,0,0,0,12,0,0,-1,0,-1,-1,0,0,0,-1,-1,-1,-1,0,-1,0,0,-1,-1,-1,-1,-1,-1,-1,0,12,0,0]
    for a,s,i,p in zip(ans, sol, ins, para):
        if a != s:
            print(a, s, i, p)







