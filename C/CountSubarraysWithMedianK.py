'''
-Hard-
*Hash Table*

You are given an array nums of size n consisting of distinct integers from 1 to n and a positive integer k.

Return the number of non-empty subarrays in nums that have a median equal to k.

Note:

The median of an array is the middle element after sorting the array in ascending order. If the array is of even length, the median is the left middle element.
For example, the median of [2,3,1,4] is 2, and the median of [8,4,3,5,1] is 4.
A subarray is a contiguous part of an array.
 

Example 1:

Input: nums = [3,2,1,4,5], k = 4
Output: 3
Explanation: The subarrays that have a median equal to 4 are: [4], [4,5] and [1,4,5].
Example 2:

Input: nums = [2,3,1], k = 3
Output: 1
Explanation: [3] is the only subarray that has a median equal to 3.
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i], k <= n
The integers in nums are distinct.



'''

from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # wrong
        A = nums
        n = len(nums)
        idx = -1
        for i,v in enumerate(A):
            if v == k:
                idx = i
                break
        ans = 1
        i, l = idx, 1
        small, large = 0, 0
        while i-l >= 0 and i+l < n:
            small += 1 if A[i-l] < k else 0
            small += 1 if A[i+l] < k else 0
            large += 1 if A[i-l] > k else 0
            large += 1 if A[i+l] > k else 0
            if small == large:
                ans += 1
            l += 1

        i, j = idx, idx+1        
        if j < n:
            small = 1 if A[j] < k else 0 
            large = 1 if A[j] > k else 0 
            ans += 1 if small == large-1 else 0        
            i -= 1
            j += 1
            while i >= 0 and j < n:
                small += 1 if A[i] < k else 0
                small += 1 if A[j] < k else 0
                large += 1 if A[i] > k else 0
                large += 1 if A[j] > k else 0
                if small == large-1: 
                    ans += 1
                i -= 1
                j += 1

        i, j = idx, idx-1        
        if j >= 0:
            small = 1 if A[j] < k else 0 
            large = 1 if A[j] > k else 0 
            ans += 1 if small == large-1 else 0        
            i += 1
            j -= 1
            while i < n and j >= 0:
                small += 1 if A[i] < k else 0
                small += 1 if A[j] < k else 0
                large += 1 if A[i] > k else 0
                large += 1 if A[j] > k else 0
                if small == large-1: 
                    ans += 1
                i += 1
                j -= 1
        return ans     

    def countSubarrays2(self, nums: List[int], k: int) -> int:
        '''
        We can check the elements before k and after k, and count the number of 
        elements larger/smaller than k.

        let's use l1 and s1 denoting the number of elements larger and smaller than k, Before k.
        and l2, s2 denoting the number of elements larger and smaller than k, After k.
        => The above equation becomes:
        l1 + l2 == s1 + s2 => l1 - s1 == s2 - l2
        l1 + l2 + 1 == s1 + s2 => l1 - s1 == s2 - l2 + 1
        Now we can use a hash map to count the frequency of l1 - s1 for the subarray 
        before k (and contains k).
        Then, check if s2 - l2 and s2 - l2 + 1 in the hash map for the subarray 
        after k (and contains k) to compute the result.
        
        '''
        A = nums
        n = len(nums)
        idx = A.index(k)
        # l (larger) is count of element>k
        # s (smaller) is count of element<k
        res = l1 = s1 = 0
        before = defaultdict(int)
        for i in range(idx-1, -1, -1):
            if A[i] > k: l1 += 1
            else: s1 += 1
            before[(l1-s1)] += 1
             # If the number of larger element and smaller element are the same,
            # we find a valid subarray which is nums[i:index+1], so increase res.
            if l1-s1==1 or l1-s1==0: res += 1
        
        l2 = s2 = 0
        for i in range(idx+1, n):
            if A[i] > k: l2 += 1
            else: s2 += 1
            # we need the number of larger elements and smaller elements to be the same in a subarray,
            #    l1 + l2 == s1 + s2 or l1 + l2 + 1 == s1 + s2
            # => l1 - s1 == s2 - l2 or l1 - s1 == s2 - l2 + 1
            # so we need to check if s2-l2 or s2-l2+1 exist in before
            res += before[s2-l2] + before[s2-l2+1]
            
            if l2-s2==1 or l2-s2==0: res += 1
        return res + 1 # [k] is also valid subarray
    

    def countSubarrays3(self, nums: List[int], k: int) -> int:
        '''
        We can check the elements before k and after k, and count the number of 
        elements larger/smaller than k.

        let's use l1 and s1 denoting the number of elements larger and smaller than k, Before k.
        and l2, s2 denoting the number of elements larger and smaller than k, After k.
        => The above equation becomes:
        l1 + l2 == s1 + s2 => l1 - s1 == s2 - l2
        l1 + l2 + 1 == s1 + s2 => l1 - s1 == s2 - l2 + 1
        Now we can use a hash map to count the frequency of l1 - s1 for the subarray 
        before k (and contains k).
        Then, check if s2 - l2 and s2 - l2 + 1 in the hash map for the subarray 
        after k (and contains k) to compute the result.
        
        '''
        A = nums
        n = len(nums)
        idx = A.index(k)
        # l (larger) is count of element>k
        # s (smaller) is count of element<k
        res = sm = 0 
        before = defaultdict(int)
        for i in range(idx-1, -1, -1):
            if A[i] > k: sm += 1
            else: sm -= 1
            before[sm] += 1
             # If the number of larger element and smaller element are the same,
            # we find a valid subarray which is nums[i:index+1], so increase res.
            if sm == 1 or sm == 0: res += 1
        
        sm = 0
        for i in range(idx+1, n):
            if A[i] > k: sm += 1
            else: sm -= 1
            # we need the number of larger elements and smaller elements to be the same in a subarray,
            #    l1 + l2 == s1 + s2 or l1 + l2 + 1 == s1 + s2
            # => l1 - s1 == s2 - l2 or l1 - s1 == s2 - l2 + 1
            # so we need to check if s2-l2 or s2-l2+1 exist in before
            res += before[-sm] + before[-sm+1]
            
            if sm==1 or sm==0: res += 1
        return res + 1 # [k] is also valid subarray
        


if __name__=="__main__":
    # print(Solution().countSubarrays(nums = [3,2,1,4,5], k = 4))
    # print(Solution().countSubarrays(nums = [2,3,1], k = 3))
    # print(Solution().countSubarrays(nums = [2,5,1,4,3,6], k = 1))
    # print(Solution().countSubarrays(nums = [1], k = 1))
    print(Solution().countSubarrays2(nums = [5,19,11,15,13,16,4,6,2,7,10,8,18,20,1,3,17,9,12,14], k=6))
    print(Solution().countSubarrays3(nums = [5,19,11,15,13,16,4,6,2,7,10,8,18,20,1,3,17,9,12,14], k=6))
        