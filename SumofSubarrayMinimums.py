'''

-Medium-
*DP*

*Monotonic Queue*

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) 
subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4

'''

class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res, n, M = 0,  len(arr), 10**9 + 7
        st = [-1]
        dp = [0]*(n + 1)
        for i in range(1,n+1):
            while st[-1] != -1 and arr[st[-1]] >= arr[i-1]:
                st.pop()
            dp[i] = (dp[st[-1] + 1] + (i - 1 - st[-1]) * arr[i-1]) % M
            st.append(i-1)
            res = (res + dp[i]) % M
        return res
    
    def sumSubarrayMins2(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        s = []
        A = [0] + arr + [0]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                print(A[j], i, j, k)
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10**9 + 7)
        
if __name__ == "__main__":
    print(Solution().sumSubarrayMins([3,1,2,4]))
    print(Solution().sumSubarrayMins2([3,1,2,4]))
    print(Solution().sumSubarrayMins([3,1,2,6,4]))