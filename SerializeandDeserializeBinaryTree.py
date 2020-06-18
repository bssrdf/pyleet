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