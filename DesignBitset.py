'''

-Medium-



A Bitset is a data structure that compactly stores bits.

Implement the Bitset class:

Bitset(int size) Initializes the Bitset with size bits, all of which are 0.
void fix(int idx) Updates the value of the bit at the index idx to 1. If the value was already 1, no change occurs.
void unfix(int idx) Updates the value of the bit at the index idx to 0. If the value was already 0, no change occurs.
void flip() Flips the values of each bit in the Bitset. In other words, all bits with value 0 will now have value 1 and vice versa.
boolean all() Checks if the value of each bit in the Bitset is 1. Returns true if it satisfies the condition, false otherwise.
boolean one() Checks if there is at least one bit in the Bitset with value 1. Returns true if it satisfies the condition, false otherwise.
int count() Returns the total number of bits in the Bitset which have value 1.
String toString() Returns the current composition of the Bitset. Note that in the resultant string, the character at the ith index should coincide with the value at the ith bit of the Bitset.
 

Example 1:

Input
["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]
Output
[null, null, null, null, false, null, null, true, null, 2, "01010"]

Explanation
Bitset bs = new Bitset(5); // bitset = "00000".
bs.fix(3);     // the value at idx = 3 is updated to 1, so bitset = "00010".
bs.fix(1);     // the value at idx = 1 is updated to 1, so bitset = "01010". 
bs.flip();     // the value of each bit is flipped, so bitset = "10101". 
bs.all();      // return False, as not all values of the bitset are 1.
bs.unfix(0);   // the value at idx = 0 is updated to 0, so bitset = "00101".
bs.flip();     // the value of each bit is flipped, so bitset = "11010". 
bs.one();      // return True, as there is at least 1 index with value 1.
bs.unfix(0);   // the value at idx = 0 is updated to 0, so bitset = "01010".
bs.count();    // return 2, as there are 2 bits with value 1.
bs.toString(); // return "01010", which is the composition of bitset.
 

Constraints:

1 <= size <= 105
0 <= idx <= size - 1
At most 105 calls will be made in total to fix, unfix, flip, all, one, count, and toString.
At least one call will be made to all, one, count, or toString.
At most 5 calls will be made to toString.



'''


class Bitset:

    def __init__(self, size: int):
        self.bit = 0
        self.size = size
        self.bit_count = 0

    def fix(self, idx: int) -> None:
        p = 1 << idx
        if self.bit & p == 0:
            self.bit_count += 1  
        self.bit |= p

    def unfix(self, idx: int) -> None:
        p = 1 << idx
        if self.bit & p > 0:
            self.bit_count -= 1  
        self.bit &= ~p

    def flip(self) -> None:
        self.bit ^= (1<<self.size)-1
        self.bit_count = self.size - self.bit_count  

    def all(self) -> bool:
        # return bin(self.bit).count('1') == self.size 
        return self.bit_count == self.size 

    def one(self) -> bool:
        return self.bit_count > 0 

    def count(self) -> int:
        # return bin(self.bit).count('1')
        return self.bit_count

    def toString(self) -> str:
        e = "{:0"+str(self.size)+ "b}" 
        return e.format(self.bit)[::-1]
    
class Bitset2:
    def __init__(self, size: int):
        self.l = [0] * size
        self.ones = 0
        self.flipp = False
    
    def fix(self, idx: int) -> None:
        if self.flipp:
            if self.l[idx] == 1: self.ones += 1
            self.l[idx] = 0
        else:
            if self.l[idx] == 0: self.ones += 1
            self.l[idx] = 1
    
    def unfix(self, idx: int) -> None:
        if self.flipp:
            if self.l[idx] == 0: self.ones -= 1
            self.l[idx] = 1
        else: 
            if self.l[idx] == 1: self.ones -= 1
            self.l[idx] = 0
    
    def flip(self) -> None:
        self.flipp = not self.flipp
        self.ones = len(self.l) - self.ones
    
    def all(self) -> bool: return self.ones == len(self.l)
    def one(self) -> bool: return self.ones > 0 
    def count(self) -> int: return self.ones
    def toString(self) -> str: 
        return ''.join([str(0 if i else 1) for i in self.l]) if self.flipp else ''.join([str(i) for i in self.l])


if __name__ == "__main__":
    bs = Bitset(5)# // bitset = "00000".
    bs.fix(3)#     // the value at idx = 3 is updated to 1, so bitset = "00010".
    bs.fix(1)#     // the value at idx = 1 is updated to 1, so bitset = "01010". 
    bs.flip()#     // the value of each bit is flipped, so bitset = "10101". 
    print(bs.all())#      // return False, as not all values of the bitset are 1.
    bs.unfix(0)#   // the value at idx = 0 is updated to 0, so bitset = "00101".
    bs.flip()#     // the value of each bit is flipped, so bitset = "11010". 
    print(bs.one())#      // return True, as there is at least 1 index with value 1.
    bs.unfix(0)#   // the value at idx = 0 is updated to 0, so bitset = "01010".
    print(bs.count())#    // return 2, as there are 2 bits with value 1.
    print(bs.toString())# // return "01010", which is the composition of bitset.

    bs = Bitset(2)#
    funs = ["flip","unfix","all","fix","fix","unfix","all","count","toString","toString","toString","unfix","flip","all","unfix","one","one","all","fix","unfix"]
    args = [[],[1],[],[1],[1],[1],[],[],[],[],[],[0],[],[],[0],[],[],[],[0],[0]]
    for f,arg in zip(funs, args):
        # print(arg)
        pars = ''.join([str(i) for i in arg])
        exp = 'bs.'+f+'('+pars+')'
        print(eval(exp))
