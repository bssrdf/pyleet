'''
-Medium-
*Two Pointers*

Given an integer array arr, remove a subarray (can be empty) from arr such that 
the remaining elements in arr are non-decreasing.

A subarray is a contiguous subsequence of the array.

Return the length of the shortest subarray to remove.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The 
remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single 
element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or 
[4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any 
elements.
Example 4:

Input: arr = [1]
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9

'''
import bisect
class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1: return 0
        pre, suf = 0, n-1
        for i in range(1, n):
            if arr[i] >= arr[pre]:
                pre = i
            else: break
        if pre == n-1: return 0    
        for i in range(n-2, -1, -1):
            if arr[i] <= arr[suf]:
                suf = i
            else: break
        ans, i, j = min(n - pre - 1, suf),  0, suf
        while i <= pre and j < n:
            if arr[j] >= arr[i]:
                ans = min(ans, j - i - 1)
                i += 1
            else: j += 1
        return ans
        


if __name__ == "__main__":
    #print(Solution().findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))
    #print(Solution().findLengthOfShortestSubarray([1,2,3]))
    #print(Solution().findLengthOfShortestSubarray([5,4,3,2,1]))
    print(Solution().findLengthOfShortestSubarray([1,2,3,10,0,7,8,9]))