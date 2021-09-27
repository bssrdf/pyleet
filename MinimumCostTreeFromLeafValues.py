'''
-Medium-
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;

The values of arr correspond to the values of each leaf in an in-order 
traversal of the tree;

The value of each non-leaf node is equal to the product of the largest leaf 
value in its left and right subtree, respectively.

Among all possible binary trees considered, return the smallest possible 
sum of the values of each non-leaf node. It is guaranteed this sum fits 
into a 32-bit integer.

A node is a leaf if and only if it has zero children.

 

Example 1:


Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.
Example 2:


Input: arr = [4,11]
Output: 44
 

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 231).

'''

class Solution(object):
    def mctFromLeafValuesGreedy(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        while len(arr) > 1:
            index = arr.index(min(arr))
            if 0 < index < len(arr) - 1:
                res += arr[index] * min(arr[index - 1], arr[index + 1])
            else:
                res += arr[index] * (arr[index + 1] if index == 0 else arr[index - 1])
            arr.pop(index)
        return res
    
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        for i,v in enumerate(arr):
            while stack and arr[stack[-1]] < v:
                idx = stack.pop() 
                if stack:
                    res += arr[idx]*min(v,arr[stack[-1]]) 
                else:
                    res += arr[idx]*v
            stack.append(i)
        while len(stack) > 1:   
            i = stack.pop()    
            res += arr[i]*arr[stack[-1]]
        return res

if __name__ == "__main__":
    print(Solution().mctFromLeafValuesGreedy([6,2,4]))
    print(Solution().mctFromLeafValuesGreedy([4,11]))
    print(Solution().mctFromLeafValuesGreedy([6,2,4,3]))
    print(Solution().mctFromLeafValuesGreedy([15,13,5,3,15]))
    print(Solution().mctFromLeafValuesGreedy([6,9,6,15,15]))

    print(Solution().mctFromLeafValues([6,2,4]))
    print(Solution().mctFromLeafValues([4,11]))
    print(Solution().mctFromLeafValues([6,2,4,3]))
    print(Solution().mctFromLeafValues([15,13,5,3,15]))
    print(Solution().mctFromLeafValues([6,9,6,15,15]))
