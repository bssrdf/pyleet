'''

-Medium-
*Greedy*
*Binary Search*
*Sorting*
*Two Pointers*

You are given a 0-indexed integer array nums.

Initially, all of the indices are unmarked. You are allowed to make this operation any number of times:

Pick two different unmarked indices i and j such that 2 * nums[i] <= nums[j], then mark i and j.
Return the maximum possible number of marked indices in nums using the above operation any number of times.

 

Example 1:

Input: nums = [3,5,2,4]
Output: 2
Explanation: In the first operation: pick i = 2 and j = 1, the operation is allowed because 2 * nums[2] <= nums[1]. Then mark index 2 and 1.
It can be shown that there's no other valid operation so the answer is 2.
Example 2:

Input: nums = [9,2,5,4]
Output: 4
Explanation: In the first operation: pick i = 3 and j = 0, the operation is allowed because 2 * nums[3] <= nums[0]. Then mark index 3 and 0.
In the second operation: pick i = 1 and j = 2, the operation is allowed because 2 * nums[1] <= nums[2]. Then mark index 1 and 2.
Since there is no other operation, the answer is 4.
Example 3:

Input: nums = [7,6,8]
Output: 0
Explanation: There is no valid operation to do, so the answer is 0.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109


'''

from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:        
        A = nums
        n = len(A)
        A.sort()
        l, r = 0, len(A)+1
        def possible(m):
            k = m // 2
            j = n - k
            for i in range(k):
                if 2*A[i] > A[j]: return False
                j += 1
            return True 
        while l < r:
            mid = l + (r-l)//2
            if possible(mid):
                # print(mid, 'True')
                l = mid + 1
            else:
                r = mid
        return l-1 if (l-1) % 2 == 0 else l-2
    
    def maxNumOfMarkedIndices2(self, nums: List[int]) -> int:        
        A = nums
        n = len(A)
        A.sort()
        l, r = 0, n // 2        
        ans = 0
        while l < n // 2 and r < n:
            if 2*A[l] <= A[r]:
                l += 1
                r += 1
                ans += 2
            else:
                r += 1
        return ans


if __name__ == '__main__':
    print(Solution().maxNumOfMarkedIndices(nums = [3,5,2,4]))
    print(Solution().maxNumOfMarkedIndices(nums = [9,2,5,4]))
    print(Solution().maxNumOfMarkedIndices(nums = [7,6,8]))

    print(Solution().maxNumOfMarkedIndices2(nums = [3,5,2,4]))
    print(Solution().maxNumOfMarkedIndices2(nums = [9,2,5,4]))
    print(Solution().maxNumOfMarkedIndices2(nums = [7,6,8]))

    nums = [42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]
    print(Solution().maxNumOfMarkedIndices(nums = nums))
    print(Solution().maxNumOfMarkedIndices2(nums = nums))
