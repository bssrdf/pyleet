'''
-Hard-
*DP*

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove 
to make nums​​​ a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any 
elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making 
the array nums = [1,5,6,3,1].
Example 3:

Input: nums = [4,3,2,1,1,2,3,1]
Output: 4
Example 4:

Input: nums = [1,2,3,4,4,3,2,1]
Output: 1
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 10^9
It is guaranteed that you can make a mountain array out of nums.


'''

class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)        
        F1 = [1]*n
        F2 = [1]*n        
        def LIS(lis):
            F = [1]*n        
            maxa = 1
            for i in range(1, n):            
                # starting from index i, traverse back until index 0,
                # if A[i] > any given number A[j], we have a potential 
                # new LIS with length F[j]+1, update F[i] and the result
                for j in range(i):
                    if nums[i] > nums[j] and F[i] < 1+F[j]:
                        F[i] = 1+F[j]
                maxa = max(maxa, F[i])
                lis[i] = maxa
        LIS(F1)
        nums = nums[::-1]
        LIS(F2)
        res = n        
        for i in range(1, n-1):            
            #  only when lis length >= 2 (i.e, forming uphill in both directions), 
            #  update res           
            if F1[i] > 1 and F2[n-i-1] > 1:
                res = min(res, n-F1[i]-F2[n-i-1]+1)
        return res
            

if __name__ == "__main__":
    print(Solution().minimumMountainRemovals([2,1,1,5,6,2,3,1]))
    print(Solution().minimumMountainRemovals([4,3,2,1,1,2,3,1]))
    print(Solution().minimumMountainRemovals([1,2,3,4,4,3,2,1]))
    print(Solution().minimumMountainRemovals([100,92,89,77,74,66,64,66,64]))