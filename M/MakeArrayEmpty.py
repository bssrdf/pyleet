'''
-Hard-

*Sorting*
*Binary Search*

You are given an integer array nums containing distinct numbers, and you can perform the following operations until the array is empty:

If the first element has the smallest value, remove it
Otherwise, put the first element at the end of the array.
Return an integer denoting the number of operations it takes to make nums empty.

 

Example 1:

Input: nums = [3,4,-1]
Output: 5
Operation	Array
1	[4, -1, 3]
2	[-1, 3, 4]
3	[3, 4]
4	[4]
5	[]
Example 2:

Input: nums = [1,2,4,3]
Output: 5
Operation	Array
1	[2, 4, 3]
2	[4, 3]
3	[3, 4]
4	[4]
5	[]
Example 3:

Input: nums = [1,2,3]
Output: 3
Operation	Array
1	[2, 3]
2	[3]
3	[]
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
All values in nums are distinct.


'''
from typing import List
from math import inf
from sortedcontainers import SortedList
import bisect
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [(c,i) for i,c in enumerate(nums)]
        sl = SortedList()
        b0 = [0]*n # b0[i]: # of elements > nums[i] in nums[0:i-1]
        s0 = [0]*n # s0[i]: # of elements < nums[i] in nums[0:i-1]
        sl.add(nums[0])
        for i in range(1, n):
            s0[i] = sl.bisect_left(nums[i])
            b0[i] = len(sl) - s0[i]
            sl.add(nums[i])
        b1 = [0]*n # b1[i]: # of elements > nums[i] in nums[i+1:]
        sl = SortedList()
        sl.add(nums[-1])
        for i in range(n-2, -1, -1):
            b1[i] = len(sl) - sl.bisect_left(nums[i])
            sl.add(nums[i])
        arr.append((-inf, -1))
        arr.sort()
        ans = 0
        for i in range(1, n+1):
            _, cur = arr[i]            
            last = arr[i-1][1]
            if cur > last:
                if arr[i-1][1] == -1: # this is for the min of nums
                    ans += cur - last # the # of ops is just moves to the left end plus 1 (remove op)
                else: # for all others if the last pos is to the left, find the # of elements < nums[idx] 
                      # b.w. the last pos and idx (= s0[cur]-s0[last]-1); this is the # of elemnts 
                      # already removed, so not counting any more  
                      # the # of ops is just moves to the left end (cur-last-1) minus
                      # the # of elements already removed (from above) plus 1 (remove op)
                    ans += (cur-last-1) - (s0[cur]-s0[last]-1) + 1
            else:# if the last pos is on the right, we need to find the # of elements > nums[idx]
                 # who are to the left of cur and to the right of the last pos  
                 # the # of ops in this case is just moves to pass all those bigger elements 
                 # plus 1 (remove op)
                ans += b0[cur] + b1[last] + 1
        return ans
    
    def countOperationsToEmptyArray2(self, nums: List[int]) -> int:
        A = nums
        pos = {a: i for i, a in enumerate(A)}
        res = n = len(A)
        A.sort()
        for i in range(1, n):
            if pos[A[i]] < pos[A[i - 1]]:
                res += n - i
        return res


    





if __name__ == '__main__':
    print(Solution().countOperationsToEmptyArray(nums = [3,4,-1]))
    print(Solution().countOperationsToEmptyArray(nums = [1,2,4,3]))
    print(Solution().countOperationsToEmptyArray(nums = [1,2,3]))
    print(Solution().countOperationsToEmptyArray(nums = [1,2,3,4,5]))
    print(Solution().countOperationsToEmptyArray(nums = [2,-15,17,15]))
        