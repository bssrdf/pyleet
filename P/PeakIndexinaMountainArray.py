'''
-Easy-

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such 
that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
Example 4:

Input: arr = [3,4,5,1]
Output: 2
Example 5:

Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2
 

Constraints:

3 <= arr.length <= 10^4
0 <= arr[i] <= 10^6
arr is guaranteed to be a mountain array.

Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?


'''

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i
        return -1

    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 1, n-1
        while l < r:            
            mid = l + (r-l)//2
    #        print(l, r, mid)
            if arr[mid] > arr[r]:
                if arr[mid] < arr[mid+1]:
                    l = mid + 1
                else:
                    r = mid
            else:
                l = mid + 1
        return r
        

if __name__ == "__main__":
    print(Solution().peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))
    print(Solution().peakIndexInMountainArray([3,4,5,1]))
    print(Solution().peakIndexInMountainArray([0,10,5,2]))
    print(Solution().peakIndexInMountainArray([0,2,1,0]))
    print(Solution().peakIndexInMountainArray([18,29,38,59,98,100,99,98,90]))
    print(Solution().peakIndexInMountainArray2([24,69,100,99,79,78,67,36,26,19]))
    print(Solution().peakIndexInMountainArray2([3,4,5,1]))
    print(Solution().peakIndexInMountainArray2([0,10,5,2]))
    print(Solution().peakIndexInMountainArray2([0,2,1,0]))
    print(Solution().peakIndexInMountainArray2([18,29,38,59,98,100,99,98,90]))
