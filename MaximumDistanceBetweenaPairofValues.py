'''

-Medium-


You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is 
valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.

 

Example 1:

Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).
Example 2:

Input: nums1 = [2,2,2], nums2 = [10,10,1]
Output: 1
Explanation: The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).
Example 3:

Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
Output: 2
Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).
Example 4:

Input: nums1 = [5,4], nums2 = [3,2]
Output: 0
Explanation: There are no valid pairs, so return 0.
 

Constraints:

1 <= nums1.length <= 10^5
1 <= nums2.length <= 10^5
1 <= nums1[i], nums2[j] <= 10^5
Both nums1 and nums2 are non-increasing.


'''
from typing import List
import bisect

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = nums1, nums2
        res = i = j = 0
        while i < len(nums1) and j < len(nums2):
            if A[i] <= B[j]: 
                res = max(res, j-i)
                j += 1
            else:
                i += 1
                #j = i
        return res

    def maxDistance2(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = nums1, nums2
        res = 0
        def bs2(a, x, start):
            l, r = start, len(a)
            while l < r:
                mid = l + (r-l)//2
                if a[mid] < x:
                    r = mid
                else:
                    l = mid+1
            return l 
        for i in range(len(A)):            
            j = bs2(B, A[i], 0)
            if j == len(B) or A[i] != B[j]:
               j -= 1  
            if i <= j:
                res = max(res, j-i)    

        return res

   
            



        

if __name__ == "__main__":
    print(Solution().maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))
    print(Solution().maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]))
    print(Solution().maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]))
    print(Solution().maxDistance(nums1 = [5,4], nums2 = [3,2]))
    print(Solution().maxDistance2(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))
    print(Solution().maxDistance2(nums1 = [2,2,2], nums2 = [10,10,1]))
    print(Solution().maxDistance2(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]))
    print(Solution().maxDistance2(nums1 = [5,4], nums2 = [3,2]))
    