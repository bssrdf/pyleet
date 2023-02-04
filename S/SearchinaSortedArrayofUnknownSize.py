'''
-Medium-


Given an integer array sorted in ascending order, write a function to search target in nums.  
If target exists, then return its index, otherwise return -1. However, the array size is 
unknown to you. You may only access the array using an ArrayReader interface, where 
ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array 
out of bounds, ArrayReader.get will return 2147483647.

 

Example 1:

Input: 
array = [-1,0,3,5,9,12], 
target = 9
Output: 4
Explanation: 9 exists in 
nums
 and its index is 4
Example 2:

Input: 
array
 = [-1,0,3,5,9,12], 
target
 = 2
Output: -1
Explanation: 2 does not exist in 
nums
 so return -1
 

Constraints:

You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].
The length of the array will be in the range [1, 10^4].


'''

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader(object):
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        """
        :type index: int
        :rtype int
        """
        if index >= len(self.arr): return 2147483647
  
        return self.arr[index]

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 10**4
        while left < right:
            mid = left + (right - left) // 2
            val = reader.get(mid)
            if  val == target:
                return mid
            elif val > 10000 or val > target:
                right = mid
            else:
                left = mid+1
        return -1

    def searchAC(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        k = 0
        if reader.get(k)==target:
            return k
        
        l,r = 0,1
        while reader.get(r)<target:
            l = r
            r = r<<1
        
        while l<=r:
            mid = l + (r-l)//2
            if reader.get(mid)==target:
                return mid
            elif reader.get(mid)>target:
                r = mid-1
            else:
                l = mid+1
        return -1



if __name__ == "__main__":    
    ar = ArrayReader([-1,0,3,5,9,12])
    print(Solution().search(ar, 9))
    print(Solution().search(ar, 4))