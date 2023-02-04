'''

-Medium-

*Two Pointers*

You are given an m x n matrix of characters box representing a side-view of a box. 
Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to 
fall due to gravity. Each stone falls down until it lands on an obstacle, 
another stone, or the bottom of the box. Gravity does not affect the 
obstacles' positions, and the inertia from the box's rotation does 
not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, 
or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 

Example 1:



Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:



Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:



Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 

Constraints:

m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.


'''

from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        res = [['']*m for _ in range(n)]
        for i in range(m):
            j, e, o = n-1, n-1, n-1
            while j >= 0:
                while o >= 0 and box[i][o] != '*':                    
                    o -= 1
                while j >= o and e >= o:
                    while e > o and box[i][e] != '.':
                        e -= 1
                    while j > o and box[i][j] != '#':                    
                        j -= 1
                    if j == o:
                        break
                    elif j < e:
                        box[i][e], box[i][j] = '#', '.'
                        j -= 1
                        e -= 1                   
                    else:
                        j = e-1      
                o  -= 1        
                j, e = o, o 

        for i in range(m):
            for j in range(n):
               res[j][m-i-1] = box[i][j]
        return res 

                


if __name__ == "__main__":
    box = [["#","#","*",".","*","."],
           ["#","#","#","*",".","."],
           ["#","#","#",".","#","."]]
    box = Solution().rotateTheBox(box)
    for row in box:
        print(row)
    box = [["#",".","#"]]
    box = Solution().rotateTheBox(box)
    for row in box:
        print(row)
    box = [["#",".","*","."],
           ["#","#","*","."]]
    box = Solution().rotateTheBox(box)
    for row in box:
        print(row)
