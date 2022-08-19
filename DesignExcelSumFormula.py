'''
-Hard-
$$$


*BFS*



Design the basic function of Excel and implement the function of the sum formula.

Implement the Excel class:

Excel(int height, char width) Initializes the object with the height and the width of the sheet. The sheet is an integer matrix mat of size height x width with the row index in the range [1, height] and the column index in the range ['A', width]. All the values should be zero initially.
void set(int row, char column, int val) Changes the value at mat[row][column] to be val.
int get(int row, char column) Returns the value at mat[row][column].
int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by numbers and returns the value at mat[row][column]. This sum formula should exist until this cell is overlapped by another value or another sum formula. numbers[i] could be on the format:
"ColRow" that represents a single cell.
For example, "F7" represents the cell mat[7]['F'].
"ColRow1:ColRow2" that represents a range of cells. The range will always be a rectangle where "ColRow1" represent the position of the top-left cell, and "ColRow2" represents the position of the bottom-right cell.
For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.
Note: You could assume that there will not be any circular sum reference.

For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").
 

Example 1:

Input
["Excel", "set", "sum", "set", "get"]
[[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
Output
[null, null, 4, null, 6]


Explanation
Excel excel = new Excel(3, "C");
 // construct a 3*3 2D array with all zero.
 //   A B C
 // 1 0 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.set(1, "A", 2);
 // set mat[1]["A"] to be 2.
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.sum(3, "C", ["A1", "A1:B2"]); // return 4
 // set mat[3]["C"] to be the sum of value at mat[1]["A"] and the values sum of the rectangle range whose top-left cell is mat[1]["A"] and bottom-right cell is mat[2]["B"].
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 4
excel.set(2, "B", 2);
 // set mat[2]["B"] to be 2. Note mat[3]["C"] should also be changed.
 //   A B C
 // 1 2 0 0
 // 2 0 2 0
 // 3 0 0 6
excel.get(3, "C"); // return 6
 

Constraints:

1 <= height <= 26
'A' <= width <= 'Z'
1 <= row <= height
'A' <= column <= width
-100 <= val <= 100
1 <= numbers.length <= 5
numbers[i] has the format "ColRow" or "ColRow1:ColRow2".
At most 100 calls will be made to set, get, and sum.



'''

import collections

class Excel(object):
    # 解题思路：
    # 观察者模式（Observer Pattern）

    # 为单元格cell注册观察者列表target（关心cell变化的单元格），
    # 被观察者列表source（变化会影响到cell的单元格）

    # 利用字典values存储每个单元格的值

    # 单元格之间的观察者关系为图结构，当某一单元格发生变化时，其所有观察者节点均会依次发生变化

    # 对于某单元格触发的观察者单元格更新操作，可以利用BFS实现

    # 当执行set操作时，清除单元格的被观察者列表，然后更新其观察者列表的值

    # 当执行sum操作时，清除单元格的被观察者列表，然后重新注册其被观察者，并更新其被观察者的观察关系，
    # 最后更新其观察者列表的值

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.col = lambda c: ord(c) - ord('A')
        self.H, self.W = H, self.col(W) + 1
        self.values = collections.defaultdict(int)
        self.target = collections.defaultdict(lambda : collections.defaultdict(int))
        self.source = collections.defaultdict(lambda : collections.defaultdict(int))
        self.getIdx = lambda r, c: (r - 1) * self.W + self.col(c)

    def updateTgt(self, idx, delta):
        queue = [idx]
        while queue:
            first = queue.pop(0)
            for tgt in self.target[first]:
                self.values[tgt] += self.target[first][tgt] * delta
                queue.append(tgt)

    def removeSrc(self, idx):
        for src in self.source[idx]:
            del self.target[src][idx]
        del self.source[idx]

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        idx = self.getIdx(r, c)
        delta = v - self.values[idx]
        self.values[idx] = v
        self.removeSrc(idx)
        self.updateTgt(idx, delta)

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        return self.values[self.getIdx(r, c)]

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        idx = self.getIdx(r, c)
        self.removeSrc(idx)
        cval = self.values[idx]
        self.values[idx] = 0
        for src in strs:
            if ':' not in src:
                sc, sr = src[0], int(src[1:])
                sidx = self.getIdx(sr, sc)
                self.target[sidx][idx] += 1
                self.source[idx][sidx] += 1
                self.values[idx] += self.values[sidx]
            else:
                st, ed = src.split(':')
                for r in range(int(st[1:]), int(ed[1:]) + 1):
                    for c in range(self.col(st[0]), self.col(ed[0]) + 1):
                        sidx = (r - 1) * self.W + c
                        self.target[sidx][idx] += 1
                        self.source[idx][sidx] += 1
                        self.values[idx] += self.values[sidx]
        self.updateTgt(idx, self.values[idx] - cval)
        return self.values[idx]

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs) 