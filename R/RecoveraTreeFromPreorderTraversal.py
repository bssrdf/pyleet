'''
-Hard-

We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109



'''
import re
from typing import Optional
from BinaryTree import (TreeNode, null)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def search(s, n):
            idx = -1
            # target = '-'*n
            i = 0
            while i < len(s):                
                while i < len(s) and s[i] != '-':
                    i += 1
                k, j = 0, i
                while i < len(s) and k < n and s[i] == '-':
                    k += 1
                    i += 1
                print('a', n, s, i, j, k)
                if j > 0 and s[j-1] != '-' and s[i+1] != '-':
                    idx = -1
                    break
                # print(s, i, j, k)
                # i = k                 

            return idx   
              
        def helper(s, d):
            if not s: return None
            # s1 = s.split('-'*d) 
            i = 0
            while i < len(s) and s[i].isdigit():
                i += 1
            # print(s, s[:i])
            root = TreeNode(int(s[:i]))
            if i == len(s): return root
            # j = i 
            while i < len(s) and s[i] == '-':
                i += 1
            idx = search(s[i:], d)
            print(d, i, '#'+s[i:]+'#', idx)
            if idx != -1:
                root.left = helper(s[i:i+idx], d+1)
                root.right = helper(s[i+idx+d:], d+1)
            else:
                root.left = helper(s[i:], d+1)
            return root
        return helper(traversal, 1)
    
    def recoverFromPreorder2(self, traversal: str) -> Optional[TreeNode]:
        S = traversal
        vals = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", S)][::-1]
        print(vals)
        def fn(level):
            if not vals or level != vals[-1][0]: return None
            node = TreeNode(vals.pop()[1])
            node.left = fn(level+1)
            node.right = fn(level+1)
            return node
        return fn(0)

    def recoverFromPreorder3(self, traversal: str) -> Optional[TreeNode]:
        nodes = []
        S = traversal
        i = 0
        # print(nodes) 
        def dfs(s, depth, i):
            nDashes = 0
            while i + nDashes < len(s) and s[i + nDashes] == '-':
                nDashes += 1
            if nDashes != depth:
                return None

            i += depth
            start = i
            while i < len(s) and s[i].isdigit():
               i += 1

            val = int(s[start:i])
            root = TreeNode(val)

            root.left = dfs(s, depth + 1, i)
            root.right = dfs(s, depth + 1, i)

            return root
        return dfs(S, 0, i)

    def recoverFromPreorder4(self, traversal: str) -> Optional[TreeNode]:
        # global index to keep track of current position inside all recursive calls
        index = 0
        S = traversal
        def recurse(depth):
            nonlocal index
            
            # count the number of dashes starting from index position
            dash_count = 0
            while index + dash_count < len(S) and S[index + dash_count] == '-':
                dash_count += 1
            
            # number of dashes should be same as the depth value
            if dash_count != depth:
                return None
        
            # find the position+1 where the integer value ends
            int_end = index + dash_count
            while int_end < len(S) and S[int_end] != '-':
                int_end += 1
            
            # convert integer value from string to int type
            int_value = int(S[index+dash_count:int_end])
            
            # move index forward to the values read so far
            index = int_end
            
            # create a new node with this integer value
            root = TreeNode(int_value)
            # make recursive calls for left and right child (index is being tracked in global variable)
            root.left = recurse(depth+1)
            root.right = recurse(depth+1)
            
            return root
            
        
        return recurse(0)
            
            

        




if __name__ == "__main__":
    root = Solution().recoverFromPreorder4(traversal = "1-2--3--4-5--6--7")
    root.prettyPrint()