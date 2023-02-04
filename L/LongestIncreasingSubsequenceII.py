'''
-Hard-

*Segment Tree*
*DP*

You are given an integer array nums and an integer k.

Find the longest subsequence of nums that meets the following requirements:

The subsequence is strictly increasing and
The difference between adjacent elements in the subsequence is at most k.
Return the length of the longest subsequence that meets the requirements.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,2,1,4,3,4,5,8,15], k = 3
Output: 5
Explanation:
The longest subsequence that meets the requirements is [1,3,4,5,8].
The subsequence has a length of 5, so we return 5.
Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 15 - 8 = 7 is larger than 3.
Example 2:

Input: nums = [7,4,5,1,8,12,4,7], k = 5
Output: 4
Explanation:
The longest subsequence that meets the requirements is [4,5,8,12].
The subsequence has a length of 4, so we return 4.
Example 3:

Input: nums = [1,5], k = 1
Output: 1
Explanation:
The longest subsequence that meets the requirements is [1].
The subsequence has a length of 1, so we return 1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 105



'''

from typing import List


class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n
       
    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1: # same as l % 2, aka l is odd
                ans = max(ans, self.tree[l])
                l += 1 # l is even now
            if r & 1: # same as r % 2, aka r is odd
                r -= 1 # r is even now
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        A = nums
        def bisect_diy(l, r, a):    
            while l<r:
                m = l+(r-l)//2
                if A[bis[m]] >= a:
                    r = m
                else:
                    l = m+1
            return r  
        # bis[k] : the index the best increasing sequence of length k ends at            
        # k = 0, ll-1
        bis=[0]*len(A)        
        ll = 1 # length of LIS, which is 1 initially for len(A)=1
        for i in range(1, len(A)):       
            if A[i] < A[bis[0]]:
                bis[0] = i # new smallest value
            elif A[i] > A[bis[ll-1]]:
                if A[i] - A[bis[ll-1]] <= k : # A[i] can extend the LIS found so far
                    bis[ll] = i # after the extension the longest IS ends at i  
                    ll +=1 # after the extension the longest length is ll  
                else:
                    bis[ll-1] = i
            else:                                
                j = bisect_diy(0, ll, A[i]) # find a location j in [0, ll)  
                bis[j] = i  # replace bis[j] with i, indicating we have found a
                            # better bis[j] ending with A[i]                           
        return ll
    
    def lengthOfLIS2(self, nums: List[int], k: int) -> int:
        A = nums
        F=[1]*len(A)        
        maxa = 1
        for i in range(1, len(A)):
            # starting from index i, traverse back until index 0,
            # if A[i] > any given number A[j], we have a potential 
            # new LIS with length F[j]+1, update F[i] and the result
            for j in range(i):
                if A[i] > A[j] and A[i]- A[j] <= k and F[i] < 1+F[j]:
                    F[i] = 1+F[j]
            maxa = max(maxa, F[i])
        return maxa     
    
    def lengthOfLIS3(self, nums: List[int], k: int) -> int:
        A = nums
        n, ans = max(A)+1, 1
        seg = SEG(n)
        for a in A:
            # a -= 1
            premax = seg.query(max(0, a - k), a)
            ans = max(ans, premax + 1)
            seg.update(a, premax + 1)
        return ans
    


if __name__ == "__main__":
    # print(Solution().lengthOfLIS(nums = [4,2,1,4,3,4,5,8,15], k = 3))
        
    # print(Solution().lengthOfLIS(nums = [7,4,5,1,8,12,4,7], k = 5))
    # print(Solution().lengthOfLIS(nums = [1,5], k = 1))
    # print(Solution().lengthOfLIS(nums = [1,3,3,4], k=1))
    # print(Solution().lengthOfLIS(nums = [1,4,7,15,5], k=1))
    # print(Solution().lengthOfLIS2(nums = [1,4,7,15,5], k=1))
    print(Solution().lengthOfLIS3(nums = [1,4,7,15,5], k=1))
    print(Solution().lengthOfLIS4(nums = [1,4,7,15,5], k=1))
    # print(Solution().lengthOfLIS2(nums = [1,3,3,4], k=1))
    print(Solution().lengthOfLIS3(nums = [1,3,3,4], k=1))
    print(Solution().lengthOfLIS4(nums = [1,3,3,4], k=1))