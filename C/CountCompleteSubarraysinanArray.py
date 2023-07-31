'''
-Medium-
*Sliding Window*
You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.

 

Example 1:

Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
Example 2:

Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2000




'''

from typing import List
from collections import Counter
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # O(N^2)
        ndis = len(set(nums))
        n = len(nums)
        ans = 0
        for i in range(n):
            st = set([nums[i]])
            if len(st) == ndis:
                ans += 1
            for j in range(i+1, n): 
                st.add(nums[j])
                if len(st) == ndis:
                    ans += 1
        return ans
    
    def countCompleteSubarrays2(self, nums: List[int]) -> int:
        # O(N)
        ndis = len(set(nums))
        ans = 0
        cnt = Counter()
        j = 0
        proc = False
        for i,a in enumerate(nums):
            cnt[a] += 1
            if len(cnt) == ndis:
                proc = True
            while len(cnt) == ndis:
                cnt[nums[j]] -= 1
                if cnt[nums[j]] == 0:
                    cnt.pop(nums[j])
                j += 1
            if proc:
                ans += j  
        return ans 
if __name__ == "__main__":
    print(Solution().countCompleteSubarrays(nums = [1,3,1,2,2]))
    print(Solution().countCompleteSubarrays2(nums = [1,3,1,2,2]))
    print(Solution().countCompleteSubarrays(nums = [5,5,5,5]))
    print(Solution().countCompleteSubarrays2(nums = [5,5,5,5]))