'''
-Medium-

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
Example 2:

Input: arr = [4,8,12,16]
Output: 2
Example 3:

Input: arr = [100]
Output: 1
 

Constraints:

1 <= arr.length <= 4 * 10^4
0 <= arr[i] <= 10^9


'''

class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [0]*n
        dp[0] = 1
        res = 1
        for i in range(1, n):
            if dp[i-1] == 1:
                if arr[i] != arr[i-1]: 
                    dp[i] = dp[i-1]+1
                else:
                    dp[i] = 1
            elif arr[i-1] > arr[i] and arr[i-2] < arr[i-1] or \
                arr[i-1] < arr[i] and arr[i-2] > arr[i-1]:
                dp[i] = dp[i-1]+1
            elif arr[i-1] != arr[i]:
                dp[i] = 2
            else:
                dp[i] = 1
            res = max(res, dp[i])
           # print(i, arr[i], res, dp)
        return res

    def maxTurbulenceSizeO1Space(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = 1
        res = 1
        for i in range(1, n):
            if dp == 1:
                if arr[i] != arr[i-1]: 
                    dp = dp+1
                else:
                    dp = 1
            elif arr[i-1] > arr[i] and arr[i-2] < arr[i-1] or \
                arr[i-1] < arr[i] and arr[i-2] > arr[i-1]:
                dp = dp+1
            elif arr[i-1] != arr[i]:
                dp = 2
            else:
                dp = 1
            res = max(res, dp)
           # print(i, arr[i], res, dp)
        return res      
    
    def maxTurbulenceSizeO1SpaceFaster(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp, res = 1, 1
        for i in range(1, n):
            if i > 1 and (arr[i-1] > arr[i] and arr[i-2] < arr[i-1] or \
                arr[i-1] < arr[i] and arr[i-2] > arr[i-1]):
                dp = dp + 1
            elif arr[i-1] != arr[i]:
                dp = 2
            else:
                dp = 1
            res = max(res, dp)
        return res      
        

if __name__ == "__main__":
    print(Solution().maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
    print(Solution().maxTurbulenceSize([4,8,12,16]))
    print(Solution().maxTurbulenceSize([100]))
    print(Solution().maxTurbulenceSizeO1Space([9,4,2,10,7,8,8,1,9]))
    print(Solution().maxTurbulenceSizeO1Space([4,8,12,16]))
    print(Solution().maxTurbulenceSizeO1Space([100]))
    print(Solution().maxTurbulenceSizeO1SpaceFaster([9,4,2,10,7,8,8,1,9]))
    print(Solution().maxTurbulenceSizeO1SpaceFaster([4,8,12,16]))
    print(Solution().maxTurbulenceSizeO1SpaceFaster([100]))