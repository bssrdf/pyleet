'''

-Hard-
*BFS*


Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

'''

from BinaryTree import (TreeNode, constructBinaryTree, null)
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()
        L = []
        if root:
            q.append(root)
        else:
            return ''
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            L.append(str(node.val) if node else '#')         
              
        return ','.join(L)



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1
        
            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root
        
        
if __name__ == "__main__":
# Your Codec object will be instantiated and called as such:
   codec = Codec()
   root = constructBinaryTree([1,2,3,null,null,4,5])
   #root = constructBinaryTree([5,2,3,null,null,2,4,3,1])
   print(codec.serialize(root))
   print(codec.deserialize(codec.serialize(root)))