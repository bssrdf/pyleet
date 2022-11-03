'''
-Hard-

$$$

You are given an integer array nums of size n containing each element from 0 to n - 1 (inclusive). Each of the elements from 1 to n - 1 represents an item, and the element 0 represents an empty space.

In one operation, you can move any item to the empty space. nums is considered to be sorted if the numbers of all the items are in ascending order and the empty space is either at the beginning or at the end of the array.

For example, if n = 4, nums is sorted if:

nums = [0,1,2,3] or
nums = [1,2,3,0]
...and considered to be unsorted otherwise.

Return the minimum number of operations needed to sort nums.

 

Example 1:

Input: nums = [4,2,0,3,1]
Output: 3
Explanation:
- Move item 2 to the empty space. Now, nums = [4,0,2,3,1].
- Move item 1 to the empty space. Now, nums = [4,1,2,3,0].
- Move item 4 to the empty space. Now, nums = [0,1,2,3,4].
It can be proven that 3 is the minimum number of operations needed.
Example 2:

Input: nums = [1,2,3,4,0]
Output: 0
Explanation: nums is already sorted so return 0.
Example 3:

Input: nums = [1,0,2,4,3]
Output: 2
Explanation:
- Move item 2 to the empty space. Now, nums = [1,2,0,4,3].
- Move item 3 to the empty space. Now, nums = [1,2,3,4,0].
It can be proven that 2 is the minimum number of operations needed.
 

Constraints:

n == nums.length
2 <= n <= 105
0 <= nums[i] < n
All the values of nums are unique.



'''

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> int:
        #wrong
        n = len(nums)
        zero, k1, k2 = -1, 0, 0        
        for i,v in enumerate(nums):
            if v > 0: 
                if v == i+1:
                    k1 += 1
                if v == i:
                    k2 += 1 
            else:
                zero = i 
        # print(k1, k2, zero)
        if zero == 0:
            return n - 1 - k2
        elif zero == n-1:
            return n - 1 - k1 
        else:
            return n - 1 - max(k1, k2)

    def sortArray2(self, nums: List[int]) -> int:
        def f(nums, k):
            vis = [False] * n
            cnt = 0
            for i, v in enumerate(nums):
                if i == v or vis[i]:
                    continue
                cnt += 1
                j = i
                while not vis[j]:
                    vis[j] = True
                    cnt += 1
                    j = nums[j]
            return cnt - 2 * (nums[k] != k)

        n = len(nums)
        a = f(nums, 0)
        b = f([(v - 1 + n) % n for v in nums], n - 1)
        return min(a, b)




if __name__ == "__main__":   
    print(Solution().sortArray(nums = [4,2,0,3,1]))
    print(Solution().sortArray(nums = [4,2,3,1,0]))
    print(Solution().sortArray(nums = [1,2,3,4,0]))
    print(Solution().sortArray(nums = [1,0,2,4,3]))