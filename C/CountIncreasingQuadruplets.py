'''

-Hard-

Given a 0-indexed integer array nums of size n containing all numbers from 1 to n, return the number of increasing quadruplets.

A quadruplet (i, j, k, l) is increasing if:

0 <= i < j < k < l < n, and
nums[i] < nums[k] < nums[j] < nums[l].
 

Example 1:

Input: nums = [1,3,2,4,5]
Output: 2
Explanation: 
- When i = 0, j = 1, k = 2, and l = 3, nums[i] < nums[k] < nums[j] < nums[l].
- When i = 0, j = 1, k = 2, and l = 4, nums[i] < nums[k] < nums[j] < nums[l]. 
There are no other quadruplets, so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Explanation: There exists only one quadruplet with i = 0, j = 1, k = 2, l = 3, but since nums[j] < nums[k], we return 0.
 

Constraints:

4 <= nums.length <= 4000
1 <= nums[i] <= nums.length
All the integers of nums are unique. nums is a permutation.



'''

from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        #TLE
        A, n = nums, len(nums)
        bits = [0]*(n+1)
        def query(x):
            t = 0
            while x > 0:
                t += bits[x]
                x -= x & (-x)
            return t 
        def update(x):
            while x <= n:
                bits[x] += 1
                x += x & (-x)                 

        prefix = [[0]*n for _ in range(n)]
        suffix = [[0]*n for _ in range(n)] 
        ans = 0
        for k in range(n-2, 1, -1):
            bits = [0]*(n+1)
            for j in range(k):  
                if A[j] > A[k]:              
                    prefix[j][k] = query(A[k])
                update(A[j])
        for j in range(n-3, 0, -1):
            bits = [0]*(n+1)
            for k in range(n-1, j, -1):      
                if A[j] > A[k]:                        
                    suffix[k][j] = query(n) - query(A[j])
                update(A[k])

        for j in range(1, n-2):
            for k in range(j+1, n-1):                
                ans += prefix[j][k] * suffix[k][j] 
                # print(j, k, prefix[j][k], suffix[k][j], ans)
        return ans

    
    def countQuadruplets2(self, nums: List[int]) -> int:
        A, n = nums, len(nums)
        prefix = [[0]*n for _ in range(n)]
        suffix = [[0]*n for _ in range(n)] 
        ans = 0
        # prefix[j][k] is the number of i's where i < j and A[i] < A[k] < A[j]
        for k in range(n-2, 1, -1):
            cnt = 0
            for j in range(k):  
                prefix[j][k] = cnt
                cnt += A[j] < A[k] 
        # suffix[k][j] is the number of l's where k < l and A[k] < A[j] < A[l]
        for j in range(n-3, 0, -1):
            cnt = 0
            for k in range(n-1, j, -1):      
                suffix[k][j] = cnt
                cnt += A[k] > A[j] 

        for j in range(1, n-2):
            for k in range(j+1, n-1):
                if A[j] > A[k]:                      
                    ans += prefix[j][k] * suffix[k][j] 
        return ans
    
    def countQuadruplets3(self, nums: List[int]) -> int:
        A, n = nums, len(nums)
        prefix = [[0]*n for _ in range(n)]
        suffix = [[0]*n for _ in range(n)] 
        ans = 0
        # prefix[j][k] is the number of i's where i < j and A[i] < A[k] < A[j]
        for k in range(n-2, 1, -1):
            cnt = 0
            for j in range(k):  
                if A[j] > A[k]:              
                    prefix[k][j] = cnt
                cnt += A[j] < A[k] 
        # suffix[k][j] is the number of l's where k < l and A[k] < A[j] < A[l]
        for j in range(n-3, 0, -1):
            cnt = 0
            for k in range(n-1, j, -1):      
                if A[j] > A[k]:                        
                    suffix[j][k] = cnt
                cnt += A[k] > A[j] 

        for j in range(1, n-2):
            for k in range(j+1, n-1):                
                ans += prefix[k][j] * suffix[j][k] 
        return ans


if __name__ == '__main__':
    print(Solution().countQuadruplets(nums = [1,3,2,4,5]))
    print(Solution().countQuadruplets(nums = [2,5,3,1,4]))
    print(Solution().countQuadruplets2(nums = [1,3,2,4,5]))
    print(Solution().countQuadruplets2(nums = [2,5,3,1,4]))
