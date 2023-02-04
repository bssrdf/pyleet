'''
-Medium-

*Monotonic Stack*

You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

Return the number of steps performed until nums becomes a non-decreasing array.

 

Example 1:

Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.
Example 2:

Input: nums = [4,5,7,7,13]
Output: 0
Explanation: nums is already a non-decreasing array. Therefore, we return 0.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109

'''



from typing import List
import collections
class Solution:
    def totalSteps2(self, nums: List[int]) -> int:
        # wrong answer
        n = len(nums)
        A = nums
        queue = collections.deque()
        firstLargerToRight = [n]*len(A)
        for i,v in enumerate(A):
            while queue and A[queue[-1]] <= v:
                firstLargerToRight[queue.pop()] = i               
            
            queue.append(i)
        
        # print(firstLargerToRight)
        ans = 0
        i = 0
        
        while i < n:
            while i < n and firstLargerToRight[i]-i <= 1:
                i += 1
            if i < n:
                k, j = 0, i+1
                # print(i, j, firstLargerToRight[i])
                while j < min(firstLargerToRight[i], n):
                    while j < min(firstLargerToRight[i],n-1) and A[j] > A[j+1]:
                        j += 1
                    print(k, j, i, A[j])    
                    j += 1
                    
                    k += 1  
                # if j == n and A[j-1] < A[i]:
                #     k += 1  
                ans = max(ans, k)
                i = firstLargerToRight[i]
            # i = j            
        
        return ans

    def totalSteps(self, nums: List[int]) -> int:
        A = nums
        st = [[A[0], 0]]
        ans = 0
        
        for a in A[1:]:
            t = 0
            while st and st[-1][0] <= a:
                t = max(t, st[-1][1])
                # if t == 0: 
                #     t = st[-1][1]
                st.pop()
            if st: 
                t += 1
            else:
                t = 0
            ans = max(ans, t)
            st.append([a, t])
            
        return ans
    
    def totalSteps3(self, nums: List[int]) -> int:
        # wrong answer
        A = nums
        queue = []
        firstLargerToLeft = [-1]*len(A)
        for i,v in enumerate(A):
            while queue and A[queue[-1]] <= v:
                queue.pop()               
            if queue:
                firstLargerToLeft[i] = queue[-1]               
            queue.append(i)
        # print(firstLargerToLeft)
        rounds = [i-j if j != -1 else -1 for i,j in enumerate(firstLargerToLeft) ]        
        # print(rounds)
        return 0
        
        
print(Solution().totalSteps(nums = [5,3,4,4,7,3,6,11,8,5,11]))
print(Solution().totalSteps(nums = [4,5,7,7,13]))
print(Solution().totalSteps(nums = [10,1,2,3,4,5,6,1,2,3]))
print(Solution().totalSteps(nums = [5,11,7,8,11]))
print(Solution().totalSteps(nums = [7,14,4,14,13,2,6,13]))

# print(Solution().totalSteps3(nums = [5,3,4,4,7,3,6,11,8,5,11]))
# print(Solution().totalSteps3(nums = [4,5,7,7,13]))
# print(Solution().totalSteps3(nums = [10,1,2,3,4,5,6,1,2,3]))
# print(Solution().totalSteps3(nums = [5,11,7,8,11]))
# print(Solution().totalSteps3(nums = [7,14,4,14,13,2,6,13]))