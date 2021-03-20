'''

-Hard-
*Binary Search*



Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
the median of the two sorted arrays.

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
 

Follow up: The overall run time complexity should be O(log (m+n)).

'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
        """
        m, n = len(nums1),  len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        # make sure n >= m
        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin <= imax:
            # A -> nums1, B-> nums2
            # if i and j are chosen as below, there are always equal number
            # of elements on the left and right as shown below
            #       left        |     right
            #  ...    A[i-1]    |    A[i] ...
            #  ...    B[j-1]    |    B[j] ...
            i = imin + (imax-imin)//2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]: # i < m ==> j > 0
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]: # i > 0 ==> j < n
                imax = i - 1
            else: # now both B[j-1] <= A[i] and A[i-1] <= B[j] are satisfied
                  # we can compute the median 
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])
                if (m+n) % 2 == 1: return max_left
                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])
                return (min_right+max_left)/2.0
        return 0



if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,2], [3,4]))