'''
-Medium-

Given a binary tree where every node has a unique value, and a target key k, find the value 
of the nearest leaf node to target k in the tree.

Here,  nearest  to a leaf means the least number of edges travelled on the binary tree to 
reach any leaf of the tree. Also, a node is called a  leaf  if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The 
actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
 

Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
 

Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest 
to the node with value 2.
 

Note:

root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.


'''

from BinaryTree import (null, TreeNode, constructBinaryTree)
from collections import deque
class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """
    def findClosestLeaf(self, root, k):
        # Write your code here
        back = {}
        def find(node):
            if node.val == k: return node
            if node.left:
                back[node.left] = node
                left = find(node.left)
                if left: return left
            if node.right:
                back[node.right] = node
                right = find(node.right)
                if right: return right
            return None
        kNode = find(root)
        q = deque([kNode])
        visited = {kNode}
        while q:
            t = q.popleft()
            if not t.left and not t.right: return t.val
            if t.left and t.left not in visited:
                visited.add(t.left)
                q.append(t.left)
            if t.right and t.right not in visited:
                visited.add(t.right)
                q.append(t.right)
            if  t in back and back[t] not in visited:
                visited.add(back[t])
                q.append(back[t])
        return -1
            
if __name__ == "__main__":
    root = constructBinaryTree([1,2,3,4,null,null,null,5,null,null,null,null,null,null,null,6])
    root.prettyPrint()
    print(Solution().findClosestLeaf(root, 2))
