'''
-Medium-

Given an array A of integers, for each integer A[i] we need to choose either
x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and 
the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
 

Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000

'''

import sys
class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        """
        尽量使原数组中的较小的数字加K，较大的数字减K，所以最好是先给原数组排个序，
        然后在数组的某个位置i为界限，将原数组分为两段，前面所有的数字都加K，后面所有
        的数字都减K。则前半段 [0, i] 中的最大值是 A[i]+K，最小值是 A[0]+K，后半段 
        [i+1, n-1] 范围内的最大值是 A[n-1]-K，最小值是 A[i+1]-K，所以整个数组的最
        大值是 A[i]+K 和 A[n-1]-K 中的较大值，最小值是 A[0]+K 和 A[i+1]-K 中的较
        小值，二者做差就是可能的结果了，遍历所有的i，用每次计算出的差值来更新结果 
        res 即可
        """
        A.sort()
        n = len(A)
        left, right = A[0]+K, A[n-1]-K
        res = A[-1] - A[0]
        for i in range(n-1):
            high = max(right, A[i]+K)
            low  = min(left, A[i+1]-K)
            res = min(res, high-low)
        return res

        


if __name__ == "__main__":
    print(Solution().smallestRangeII([1,3,6], 3))
    print(Solution().smallestRangeII([0,10], 2))