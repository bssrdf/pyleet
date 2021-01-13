'''
-Easy-

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 
as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n 
respectively. You may assume that nums1 has enough space (size that 
is equal to m + n) to hold additional elements from nums2.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
 

Constraints:

0 <= n, m <= 200
1 <= n + m <= 200
nums1.length == m + n
nums2.length == n
-10^9 <= nums1[i], nums2[i] <= 10^9

'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
        


if __name__ == "__main__":
    nums1 = [7,8,9,0,0,0,0]
    m = 3 
    nums2 = [2,5,6,7]    
    n = 4
    Solution().merge(nums1, m, nums2, n)
    print(nums1)