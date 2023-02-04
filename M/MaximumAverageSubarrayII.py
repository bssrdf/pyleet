'''
-Hard-
*Binary Search*


Given an array consisting of n integers, find the contiguous subarray whose 
length is greater than or equal to k that has the maximum average value. And 
you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10^-5 will be accepted.

'''

class Solution(object):
    def findMaxAverageTLE(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        sums = nums[:]
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]
        res = sums[k - 1] / k
        for i in range(k, n):
            t = sums[i]
            if t > res * (i + 1): res = t / (i + 1)
            for j in range(i - k, -1, -1):
                t = sums[i] -  sums[j]
                if t > res * (i - j) : res = t / (i - j)
        return res

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # O(nlog(max-min))
        n = len(nums)
        sums = [0] * (n+1)
        left = min(nums)
        right = max(nums)
        while right - left > 1.e-5:
            minSum, mid = 0, left + (right - left) / 2
            check = False
            for i in range(1,n+1):
                sums[i] = sums[i - 1] + nums[i - 1] - mid
                if i >= k: minSum = min(minSum, sums[i - k])
                if i >= k and sums[i] > minSum: # there exists a subarray with length >= k and
                    check = True                # its average > mid
                    break 
            if check: left = mid
            else: right = mid
#        print(left, right)
        return right

if __name__ == "__main__":
    print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
    print(Solution().findMaxAverage([-1,0,1], 3))