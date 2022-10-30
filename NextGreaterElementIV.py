'''

-Hard-

You are given a 0-indexed array of non-negative integers nums. For each integer in nums, you must find its respective second greater integer.

The second greater integer of nums[i] is nums[j] such that:

j > i
nums[j] > nums[i]
There exists exactly one index k such that nums[k] > nums[i] and i < k < j.
If there is no such nums[j], the second greater integer is considered to be -1.

For example, in the array [1, 2, 4, 3], the second greater integer of 1 is 4, 2 is 3, and that of 3 and 4 is -1.
Return an integer array answer, where answer[i] is the second greater integer of nums[i].

 

Example 1:

Input: nums = [2,4,0,9,6]
Output: [9,6,6,-1,-1]
Explanation:
0th index: 4 is the first integer greater than 2, and 9 is the second integer greater than 2, to the right of 2.
1st index: 9 is the first, and 6 is the second integer greater than 4, to the right of 4.
2nd index: 9 is the first, and 6 is the second integer greater than 0, to the right of 0.
3rd index: There is no integer greater than 9 to its right, so the second greater integer is considered to be -1.
4th index: There is no integer greater than 6 to its right, so the second greater integer is considered to be -1.
Thus, we return [9,6,6,-1,-1].
Example 2:

Input: nums = [3,3]
Output: [-1,-1]
Explanation:
We return [-1,-1] since neither integer has any integer greater than it.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109


'''

from typing import DefaultDict, List
from collections import defaultdict
import bisect



class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        stack = []
        A = nums 
        n = len(A)
        nextG = [-1]*n
        pos = [-1]*n
        for i,a in enumerate(A):
            while stack and A[stack[-1]] < a:
                nextG[stack[-1]] = a
                pos[stack[-1]] = i
                stack.pop()
            stack.append(i)
        # print(nextG)
        # print(pos)
        ans = []
        def find(num, idx):
            j = idx + 1
            while j < n:
                if A[j] > num:
                    return A[j]
                j += 1
            return -1 
        for i in range(n):
            if pos[i] == -1 or pos[i] == n-1:
                ans.append(-1)
            else:
                ans.append(find(A[i], pos[i]))
        return ans
    
    def secondGreaterElement2(self, nums: List[int]) -> List[int]:
        stack = []
        A = nums 
        n = len(A)
        pos = [-1]*n
        for i,a in enumerate(A):
            while stack and A[stack[-1]] < a:
                pos[stack[-1]] = i
                stack.pop()
            stack.append(i)
        ans = [-1]*n
        pos2i = defaultdict(list)
        for i,p in enumerate(pos):
            if p != -1:
                pos2i[p+1].append(i)
        stack = []
        def binarysearch(arr, x):
            l, r = 0, len(arr)
            while l < r:
                mid = l + (r-l)//2
                if arr[mid] > x:
                    l = mid + 1
                else:
                    r = mid
            return l-1
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= A[i]:
                stack.pop()
            stack.append(A[i])     
            if i in pos2i:
                for j in pos2i[i]:                    
                    idx = binarysearch(stack, A[j])
                    if idx >= 0:
                        ans[j] = stack[idx]
                    elif stack[idx+1] > A[j]:
                        ans[j] = stack[idx+1]
        return ans





if __name__ == "__main__":   
    # print(Solution().secondGreaterElement(nums = [2,4,0,9,6]))
    # print(Solution().secondGreaterElement2(nums = [2,4,0,9,6]))
    # print(Solution().secondGreaterElement(nums = [2,4,0,6,9]))
    # print(Solution().secondGreaterElement2(nums = [2,4,0,6,9]))
    # print(Solution().secondGreaterElement(nums = [3,3]))
    # print(Solution().secondGreaterElement2(nums = [3,3]))
    # nums= [8]*(10**5)
    # nums[10**5//2] = 9
    # Solution().secondGreaterElement(nums = nums)
    # Solution().secondGreaterElement2(nums = nums)


    nums = [272,238,996,406,763,164,102,948,217,760,609,700,848,637,748,718,469,449,502,703,292,86,91,551,699,293,244,406,22,968,434,805,910,927,623,79,108,541,411]
    print(Solution().secondGreaterElement2(nums = nums))


    
        