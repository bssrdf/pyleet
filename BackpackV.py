'''

-Medium-

Given n items with size nums[i] which an integer array and all positive numbers. An integer 
target denotes the size of a backpack. Find the number of possible fill the backpack.

Each item may only be used once

样例
Given candidate items [1,2,3,3,7] and target 7,

A solution set is: 
[7]
[1, 3, 3]
return 2


'''

class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        A = nums
        m = target
        n = len(A)
        f = [0] * (m + 1)
        f[0] = 1
        for i in range(1, n + 1):
            for j in range(m, A[i-1]-1, -1):
                if j >= A[i - 1]:
                    f[j] += f[j - A[i - 1]]
        return f[m]
