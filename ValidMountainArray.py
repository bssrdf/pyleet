'''
-Easy-

Given an array of integers arr, return true if and only if it is a valid 
mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^4

'''

class Solution(object):

    def validMountainArrayFast(self, A):
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: i += 1        
        while j > 0 and A[j - 1] > A[j]: j -= 1        
        return 0 < i == j < n - 1

    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3: return False 
        mx = -1
        mxi = -1
        for i,v in enumerate(arr):
            if mx < v: 
                mx = v
                mxi = i 
        asc = False
        for i in range(1, mxi+1):
            if arr[i] <= arr[i-1]:
                return False
            else:
                asc = True
        des = False        
        for i in range(mxi+1, n):
            if arr[i] >= arr[i-1]:
                return False
            else:
                des = True
        return asc and des







if __name__ == "__main__":
    print(Solution().validMountainArray([0,3,2,1]))
    print(Solution().validMountainArray([3,5,5]))
    print(Solution().validMountainArray([0,1,2,3,4,5,6,7,8,9]))
    print(Solution().validMountainArrayFast([0,1,3,5,6,7,8,9,8,7,6]))