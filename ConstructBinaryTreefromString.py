'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or 
two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis 

contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".

'''
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def str2tree(self, s):
        if not s:
            return None
        #print(s)
        found = s.find('(')
        if found == -1:
            return TreeNode(int(s))
        root = TreeNode(int(s[:found])) 
        start, cnt = found, 0
        for i in range(start, len(s)):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
            if cnt == 0 and start == found:               
                root.left = self.str2tree(s[start+1:i])
                start = i+1
            elif cnt == 0:                
                root.right = self.str2tree(s[start+1:i])            
        return root

    def str2treeWithStack(self, s):
        if not s:
            return None
        st = []
        for i in range(len(s)):
            j = i
            if s[i] == ')':
                st.pop()
            if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9') or ord(s[i]) == ord('-'):
                while ord(s[i+1]) >= ord('0') and ord(s[i+1]) <= ord('9'):
                    i += 1
                #print(j, i, s[j:i])
                cur = TreeNode(int(s[j:i+1]))
                if st:
                    t = st[-1]
                    if not t.left:
                        t.left = cur
                    else:
                        t.right = cur
                st.append(cur)
        return st[-1]



#node = Solution().str2tree("4(2(3)(1))(6(5))")
node = Solution().str2treeWithStack("4(2(3)(1))(6(5))")
print(node.val)





