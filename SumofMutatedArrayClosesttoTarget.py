'''
-Medium-
*Binary Search*
*Prefix Sum*
Given an integer array arr and a target value target, return the integer value such that 
when we change all the integers larger than value in the given array to be equal to value, 
the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

 

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5


'''

import bisect

class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        n = len(arr)
        preSum = [0]*(n+1)
        for i in range(1,n+1):
            preSum[i] = preSum[i-1] + arr[i-1]
        l, r = 0, arr[-1]+1
        def mySum(num):
            i = bisect.bisect_right(arr, num)
            return preSum[i]+(n-i)*num
        while l < r:
            mid = l + (r-l)//2
            sm = mySum(mid)
            if sm == target:
                return mid
            elif sm > target:
                r = mid
            else:
                l = mid+1
            print(l, r, mid, sm)            
        if abs(mySum(r-1)-target) <= abs(mySum(r)-target):
            return r-1
        return r

        
        
if __name__ == "__main__":
    print(Solution().findBestValue(arr = [4,9,3], target = 10))
    #print(Solution().findBestValue(arr = [2,3,5], target = 10))
    #print(Solution().findBestValue(arr = [60864,25176,27249,21296,20204], target = 56803))