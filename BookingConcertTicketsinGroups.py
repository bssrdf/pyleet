'''

-Hard-
A concert hall has n rows numbered from 0 to n - 1, each with m seats, numbered from 0 to m - 1. You need to design a ticketing system that can allocate seats in the following cases:

If a group of k spectators can sit together in a row.
If every member of a group of k spectators can get a seat. They may or may not sit together.
Note that the spectators are very picky. Hence:

They will book seats only if each member of their group can get a seat with row number less than or equal to maxRow. maxRow can vary from group to group.
In case there are multiple rows to choose from, the row with the smallest number is chosen. If there are multiple seats to choose in the same row, the seat with the smallest number is chosen.
Implement the BookMyShow class:

BookMyShow(int n, int m) Initializes the object with n as number of rows and m as number of seats per row.
int[] gather(int k, int maxRow) Returns an array of length 2 denoting the row and seat number (respectively) of the first seat being allocated to the k members of the group, who must sit together. In other words, it returns the smallest possible r and c such that all [c, c + k - 1] seats are valid and empty in row r, and r <= maxRow. Returns [] in case it is not possible to allocate seats to the group.
boolean scatter(int k, int maxRow) Returns true if all k members of the group can be allocated seats in rows 0 to maxRow, who may or may not sit together. If the seats can be allocated, it allocates k seats to the group with the smallest row numbers, and the smallest possible seat numbers in each row. Otherwise, returns false.
 

Example 1:

Input
["BookMyShow", "gather", "gather", "scatter", "scatter"]
[[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
Output
[null, [0, 0], [], true, false]

Explanation
BookMyShow bms = new BookMyShow(2, 5); // There are 2 rows with 5 seats each 
bms.gather(4, 0); // return [0, 0]
                  // The group books seats [0, 3] of row 0. 
bms.gather(2, 0); // return []
                  // There is only 1 seat left in row 0,
                  // so it is not possible to book 2 consecutive seats. 
bms.scatter(5, 1); // return True
                   // The group books seat 4 of row 0 and seats [0, 3] of row 1. 
bms.scatter(5, 1); // return False
                   // There are only 2 seats left in the hall.
 

Constraints:

1 <= n <= 5 * 104
1 <= m, k <= 109
0 <= maxRow <= n - 1
At most 5 * 104 calls in total will be made to gather and scatter.

'''

from typing import List


class SegmentTree():
    def __init__(self, l, r):
        self.val = 0
        self.mid = (l + r) // 2
        self.l = l
        self.r = r
        self.left, self.right = None, None
        self.max = 0
        self.sums = 0
        if l != r:
            self.left = SegmentTree(l, self.mid)
            self.right = SegmentTree(self.mid + 1, r)

    def update(self, l, r, val=1):
        if self.l >= l and self.r <= r:
            self.val += val
            self.max += val
            self.sums += val*(r-l+1)
            return
        if self.l > r or self.r < l:
            return

        self.left.update(l, r, val)
        self.right.update(l, r, val)
        self.max = self.val + max(self.left.max, self.right.max)
        self.sums = self.val*(self.r-self.l+1)+self.left.sums+self.right.sums

    def query(self, i):
        if self.l == self.r and self.l == i:
            return self.val
        if i < self.l or i > self.r:
            return 0
        if i <= self.mid:
            return self.val + self.left.query(i)
        return self.val + self.right.query(i)
    
    def querySum(self,l,r):
        #return sum value in range [l,r]
        if self.l >= l and self.r <= r:
            return self.sums
        if self.l > r or self.r < l:
            return 0
        return self.val*(min(r,self.r)-max(l,self.l)+1)+self.left.querySum(l,r)+self.right.querySum(l,r)

    def queryLowestGreater(self,v):
        #return the smallest row that remain seats greater than v
        if self.max<v:
            return -1
        if self.l == self.r:
            return -1 if self.max<v else self.l
        if self.left.max >= v-self.val:
            return self.left.queryLowestGreater(v-self.val)
        return self.right.queryLowestGreater(v-self.val)



class BookMyShow:

    def __init__(self, n: int, m: int):
        self.st = SegmentTree(0,n-1)
        self.st.update(0,n-1,m)
        self.m = m
        self.k = 0
        self.n = n
        

    def gather(self, k: int, maxRow: int) -> List[int]:
        i = self.st.queryLowestGreater(k)
        if i<0 or i>maxRow:
            return []
        v = self.st.query(i)
        self.st.update(i,i,-k)
        return [i,self.m-v]
        

    def scatter(self, k: int, maxRow: int) -> bool:
         # if sum 0_maxRow greater than k,it's possible to book
        if self.st.querySum(0,maxRow)>=k:
            #book seats from lowest row
            while self.k<self.n and k>0:
                v = self.st.query(self.k)
                self.st.update(self.k,self.k,-min(v,k))
                if v>k:
                    break
                else:
                    k -= v
                    self.k += 1
            return True
        return False

class BookMyShow2:

    def __init__(self, n: int, m: int):        
        self.m = m        
        self.n = n
        sz = 1 
        while sz < 2*n:
            sz <<= 1
        self.stree = [[0,0] for _ in range(sz)]
        self.build(0, 0, n-1)

    def build(self, i, p, q):
        # print(i, p, q)
        if p == q :
            self.stree[i] = [self.m, self.m]
            return
        m = (p + q) // 2
        self.stree[i] = [self.m, (q-p+1)*self.m]
        self.build(2*i+1, p, m)
        self.build(2*i+2, m+1, q)

    def query_max(self, i, p, q, k, maxRow):
        if p > maxRow: return []
        if self.stree[i][0] < k:  return []
        if p == q:
            return [p, (self.m - self.stree[i][0])]
        m = (p + q) // 2
        ret = self.query_max(2*i+1, p, m, k, maxRow)
        if ret: return ret
        return self.query_max(2*i+2, m+1, q, k, maxRow)

    def update_max(self, i, p, q, row, k):
        if p > row or q < row: return
        if p == q:
            self.stree[i][0] -= k
            self.stree[i][1] -= k
            # // cout << p << " " << stree[i][0] << endl;
            return
        m = (p + q) // 2
        self.stree[i][1] -= k
        self.update_max(2*i+1, p, m, row, k)
        self.update_max(2*i+2, m+1, q, row, k)
        self.stree[i][0] = max(self.stree[2*i+1][0], self.stree[2*i+2][0])
    
    def query_sum(self, i, p,  q, maxRow):
        if p > maxRow:  return 0
        if q <= maxRow:  return self.stree[i][1]
        m = (p + q) // 2
        return self.query_sum(2*i+1, p, m, maxRow) + self.query_sum(2*i+2, m+1, q, maxRow)
    
    def update_sum(self, i, p, q, k, maxRow): 
        if p > maxRow:  return
        if p == q:
            self.stree[i][0] -= k
            self.stree[i][1] -= k
            # // cout << p << " " << stree[i][0] << endl;
            return
        m = (p + q) // 2
        self.stree[i][1] -= k
        if m+1 > maxRow or self.stree[2*i+1][1] >= k:
            self.update_sum(2*i+1, p, m, k, maxRow)
        else:
            k -= self.stree[2*i+1][1]
            self.update_sum(2*i+1, p, m, self.stree[2*i+1][1], maxRow)
            # Be aware: stree[2*i+1][1] updates while updating the left tree
            self.update_sum(2*i+2, m+1, q, k, maxRow)
        self.stree[i][0] = max(self.stree[2*i+1][0], self.stree[2*i+2][0])

    def gather(self, k: int, maxRow: int) -> List[int]:
        ret = self.query_max(0, 0, self.n-1, k, maxRow)
        if ret:
            self.update_max(0, 0, self.n-1, ret[0], k)
        return ret
    
    def scatter(self, k: int, maxRow: int) -> bool:
        cnt = self.query_sum(0, 0, self.n-1, maxRow)
        # print('cnt = ', cnt)
        ret = cnt >= k
        if ret:
            self.update_sum(0, 0, self.n-1, k, maxRow)
        return ret
         


if __name__ == "__main__":
    bms = BookMyShow2(2, 5) # There are 2 rows with 5 seats each 
    # print(bms.stree)
    print(bms.gather(4, 0))# return [0, 0]
                    # // The group books seats [0, 3] of row 0. 
    print(bms.gather(2, 0)) # return []
                    # // There is only 1 seat left in row 0,
                    # // so it is not possible to book 2 consecutive seats. 
    # print(bms.stree)
    print(bms.scatter(5, 1)) # return True
                    # // The group books seat 4 of row 0 and seats [0, 3] of row 1. 
    print(bms.scatter(5, 1)) # return False
                    # // There are only 2 seats left in the hall.
