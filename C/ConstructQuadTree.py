'''

-Medium-

Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are 
accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, 
each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to 
the value of the grid and set the four children to Null and stop.

If the current grid has different values, set isLeaf to False and set val to any value and divide 
the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null 
signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node 
is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the 
value of isLeaf or val is False we represent it as 0.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:



Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

Example 3:

Input: grid = [[1,1],[1,1]]
Output: [[1,1]]
Example 4:

Input: grid = [[0]]
Output: [[1,0]]
Example 5:

Input: grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
Output: [[0,1],[1,1],[1,0],[1,0],[1,1]]
 

Constraints:

n == grid.length == grid[i].length
n == 2^x where 0 <= x <= 6


'''

#"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
#"""
from typing import List

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        sums = [[0]*(n+1) for _ in range(n+1)]
        def build(l, r, t, b):
            if l == r:
                val = True if grid[t][l] == 1 else False
                node = Node(val, True, None, None, None, None)
                return node
            k = sums[b+1][r+1]-sums[b+1][l]-sums[t][r+1]+sums[t][l] 
            if k == (r-l+1)**2 or k == 0:
                val = False if k == 0 else True
                node = Node(val, True, None, None, None, None)
                return node
            node = Node(False, False, None, None, None, None)
            node.topLeft      = build(l, l + (r-l)//2, t, t+(b-t)//2)
            node.topRight     = build(l + (r-l)//2+1, r, t, t+(b-t)//2)
            node.bottomLeft   = build(l, l + (r-l)//2, t+(b-t)//2+1, b)
            node.bottomRight  = build(l + (r-l)//2+1, r, t+(b-t)//2+1, b)
            return node
        for i in range(1, n+1):
            for j in range(1, n+1):
                sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + grid[i-1][j-1]

        return build(0, n-1, 0, n-1)

if __name__ == '__main__':
    grid = [[1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0]]
    #root = Solution().construct(grid)
    #print(root.topLeft.val)
    #print(root.topRight.val)
    #print(root.bottomLeft.val)
    #print(root.bottomRight.val)
    grid = [[1,1,0,0],
            [0,0,1,1],
            [1,1,0,0],
            [0,0,1,1]]
    
    root = Solution().construct(grid)

