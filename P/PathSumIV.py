'''
-Medium-

If the depth of a tree is smaller than 5, then this tree can be represented by a 
list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 
1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary tree with 
the depth smaller than 5, you need to return the sum of all paths from the root 
towards the leaves.

It's guaranteed that the given list represents a valid connected binary tree.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
 

Example 2:

Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.

'''

from collections import deque
class Solution(object):
    def pathSum(self, nums):
        """
        :type digits: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums.sort()
        res = 0
        m = {}
        q = deque([nums[0] // 10])
        for num in nums:
            m[num // 10] = num % 10
        while q:
            t = q.popleft()
            level = t // 10
            pos = t % 10
            left = (level + 1) * 10 + 2 * pos - 1
            right = left + 1            
            if left not in m and right not in m:
                res += m[t] # a leaf node, add path sum to total
            if left in m:
                m[left] += m[t] # add val to its left child
                q.append(left)
            if right in m:
                m[right] += m[t] # add val to its right child
                q.append(right)
        return res

if __name__ == "__main__":
    print(Solution().pathSum([113, 215, 221]))
    print(Solution().pathSum([456,331,320,229,215,113,468,342,431]))