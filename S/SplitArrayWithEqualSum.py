'''
-Hard-
*DP*

Given an array with n integers, you need to find if there are triplets 
(i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) 
should be equal.
where we define that subarray (L, R) represents a slice of the original 
array starting from the element indexed L to the element indexed R.

Example:
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Note:

1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].

'''

class Solution(object):
    def splitArray(self, nums):
        N = len(nums)
        if N < 7: 
            return False        
        sm = [0]*(N+1)
        for i,n in enumerate(nums):
            sm[i+1] = sm[i]+n        
        sum2num = {}
        for j in range(3,N-3):            
            for i in range(1,j-1):               
                if sm[i]-sm[0] == sm[j]-sm[i+1]:
                    sum2num[sm[i]-sm[0]] = i
            for k in range(j+2,N-1):
                if sm[k]-sm[j+1] == sm[N]-sm[k+1]:
                    if sm[k]-sm[j+1] in sum2num:
                       return True        
        return False 



if __name__ == "__main__":
    print(Solution().splitArray([1,3,2,1,3,2,1,3,2,1,3]))
    print(Solution().splitArray([1,2,1,2,1,2,1]))