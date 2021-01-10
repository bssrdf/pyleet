'''
-Easy-

Given an array arr of positive integers sorted in a strictly increasing 
order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd 
missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length

'''

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        
        """        
        n = len(arr)
        init, missing = 0, 0
        for i in range(1, n+1):
            if arr[i-1]-i > 0:
                missing = arr[i-1]-i
            if missing >= k:                  
                return arr[i-2]+k-init if i >= 2 else k-init
            init = missing           
        return arr[-1]+k-missing

    def findKthPositiveLogN(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            # search the last appreance of 'i' 
            # such that a[i]-i <= k
            if arr[mid] - mid > k:
                r = mid
            else:
                l = mid + 1
        print(arr[mid], mid, r, k)
        return r + k       


if __name__ == "__main__":
    print(Solution().findKthPositive([2,3,4,7,11], 5))
    print(Solution().findKthPositive([1,2,3,4], 2))
    print(Solution().findKthPositive([1,13,18],17))
    print(Solution().findKthPositiveLogN([2,3,4,7,11], 5))
    print(Solution().findKthPositiveLogN([1,2,3,4], 2))
    print(Solution().findKthPositiveLogN([1,13,18],17))