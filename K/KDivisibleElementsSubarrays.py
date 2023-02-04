'''
-Medium-

Given an integer array nums and two integers k and p, return the number of distinct subarrays which have at most k elements divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:

They are of different lengths, or
There exists at least one index i where nums1[i] != nums2[i].
A subarray is defined as a non-empty contiguous sequence of elements in an array.

 

Example 1:

Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 11
Explanation:
The elements at indices 0, 3, and 4 are divisible by p = 2.
The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are:
[2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2].
Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once.
The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.
Example 2:

Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10
Explanation:
All element of nums are divisible by p = 1.
Also, every subarray of nums will have at most 4 elements that are divisible by 1.
Since all subarrays are distinct, the total number of subarrays satisfying all the constraints is 10.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i], p <= 200
1 <= k <= nums.length



'''

from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n, st, mod = len(nums), set(), 10**9+7
        
        for i in range(n):
            hash = 0
            cnt = 0
            for j in range(i,n):
                if nums[j] % p == 0: cnt += 1
                if cnt > k: break      
                hash = (hash*200 + nums[j]) % mod
                st.add(hash)
        return len(st)
    
    def countDistinct2(self, nums: List[int], k: int, p: int) -> int:
        n, st, mod = len(nums), set(), 10**9+7
        
        for i in range(n):
            cnt = 0
            for j in range(i,n):
                if nums[j] % p == 0: cnt += 1
                if cnt > k: break     
                
                st.add(tuple(nums[i:j+1]))
        return len(st)


if __name__ == "__main__":
    nums = [77,37,81,38,90,60,182,100,12,116,7,10,165,1,81,48,56,134,129,62,16,100,47,138,164,114,34,126,57,97,146,174,163,61,68,32,178,171,200,90,122,141,78,183,9,2,113,75]
    print(Solution().countDistinct(nums,14,114))
    print(Solution().countDistinct2(nums,14,114))

                
        