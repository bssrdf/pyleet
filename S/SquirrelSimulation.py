'''

-Medium-

There's a tree, a squirrel, and several nuts. Positions are represented by the 
cells in a 2D grid. Your goal is to find the minimal distance for the squirrel 
to collect all the nuts and put them under the tree one by one. The squirrel 
can only take at most one nut at one time and can move in four 
directions - up, down, left and right, to the adjacent cell. The 
distance is represented by the number of moves.

All given positions won't overlap.
The squirrel can take at most one nut at one time.
The given positions of nuts have no order.
Height and width are positive integers. 3 <= height * width <= 10,000.
The given positions contain at least one nut, only one tree and one squirrel.
样例
Example 1:

Input: height = 5, width = 7,
  treePosition = [2, 2],
  squirrelPosition = [4, 4],
  nuts = [[3, 0], [2, 5]]
Output: 12


Example 2:

Input: height = 1, width = 3,
  treePosition = [0,1],
  squirrelPosition = [0,0],
  nuts = [[0,2]]
Output: 3

'''

class Solution:
    """
    @param height: the height
    @param width: the width
    @param tree: the position of tree
    @param squirrel: the position of squirrel
    @param nuts: the position of nuts
    @return: the minimal distance 
    """
    def minDistance(self, height, width, tree, squirrel, nuts):
        # Write your code here
        n = len(nuts)
        total = 0
        mi = float('inf')    
        for i in range(n):
            t = abs(tree[0]-nuts[i][0]) + abs(tree[1]-nuts[i][1])  
            total += 2*t
            d = abs(squirrel[0]-nuts[i][0]) + abs(squirrel[1]-nuts[i][1]) - t
            if mi > d: 
                mi = d
        return total + mi
            


        




