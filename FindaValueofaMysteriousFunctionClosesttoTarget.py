'''
-Hard-
*Segment Tree*
*Set*

Winston was given the above mysterious function func. He has an integer array arr and an integer target and he wants to find the values l and r that make the value |func(arr, l, r) - target| minimum possible.

Return the minimum possible value of |func(arr, l, r) - target|.

Notice that func should be called with the values l and r where 0 <= l, r < arr.length.

 

Example 1:

Input: arr = [9,12,3,7,15], target = 5
Output: 2
Explanation: Calling func with all the pairs of [l,r] = [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]], Winston got the following results [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0]. The value closest to 5 is 7 and 3, thus the minimum difference is 2.
Example 2:

Input: arr = [1000000,1000000,1000000], target = 1
Output: 999999
Explanation: Winston called the func with all possible values of [l,r] and he always got 1000000, thus the min difference is 999999.
Example 3:

Input: arr = [1,2,4,8,16], target = 0
Output: 0
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 106
0 <= target <= 107

'''


from typing import List

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.val = 0
        self.left = None
        self.right = None

class SegmentTree(object):
    
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        self.ans = float('inf')
        self.root = self.createTree(nums, 0, len(nums)-1)


    def createTree(self, nums, l, r):
            
        #base case
        if l > r:
            return None

        root = Node(l, r)    
        #leaf node
        if l == r:            
            root.val = nums[l]
            return root
        
        mid = (l + r) // 2        
        
        #recursively build the Segment tree
        root.left = self.createTree(nums, l, mid)
        root.right = self.createTree(nums, mid+1, r)
        
        #Total stores the sum of all leaves under root
        #i.e. those elements lying between (start, end)

        root.val = root.left.val & root.right.val 
        # print(l, r, root.val, root.left.val, root.right.val, abs(root.val-t))
        return root
    
    def query(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def _query(root, i, j):
            
            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.val
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return _query(root.left, i, j)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return _query(root.right, i, j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return _query(root.left, i, mid) & _query(root.right, mid+1, j)
        
        return _query(self.root, i, j)
    
    

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        st = SegmentTree(arr)
        ans = float('inf')        
        l, r = 0, 0                     
        while r < len(arr):
            v = st.query(l, r)
            ans = min(ans, abs(v-target))
            if v >= target:
                r += 1
            else:
                if l < r:
                    l += 1
                else:
                    l += 1
                    r += 1
        return ans
    
    def closestToTarget2(self, arr: List[int], target: int) -> int:
        st, n = {arr[-1]}, len(arr)
        ans = float('inf')
        for i in range(n-2, -1, -1):
            setnew = {arr[i]}
            for j in st:
                setnew.add(arr[i] & j)
            for j in setnew:
                ans = min(ans, abs(j-target))    
            st = setnew
        return ans




if __name__ == "__main__":   
    print(Solution().closestToTarget(arr = [9,12,3,7,15], target = 5))
    print(Solution().closestToTarget(arr = [1000000,1000000,1000000], target = 1))
    print(Solution().closestToTarget(arr = [1,2,4,8,16], target = 0))
    print(Solution().closestToTarget([70,15,21,96],4))

    print(Solution().closestToTarget2(arr = [9,12,3,7,15], target = 5))
    print(Solution().closestToTarget2(arr = [1000000,1000000,1000000], target = 1))
    print(Solution().closestToTarget2(arr = [1,2,4,8,16], target = 0))
    print(Solution().closestToTarget2([70,15,21,96],4))