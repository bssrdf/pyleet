'''
-Medium-

Give n items and an array, num[i] indicate the size of ith item. An integer target denotes 
the size of backpack. Find the number of ways to fill the backpack.

Each item may be chosen unlimited number of times

样例
Example1

Input: nums = [2,3,6,7] and target = 7
Output: 2
Explanation:
Solution sets are: 
[7]
[2, 2, 3]
Example2

Input: nums = [2,3,4,5] and target = 7
Output: 3
Explanation:
Solution sets are: 
[2, 5]
[3, 4]
[2, 2, 3]



'''

class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        A = nums
        m = target
        n = len(A)
        f = [0] * (m + 1)
        f[0] = 1
        for i in range(1, n + 1):
            for j in range(1, m+1):
                if j >= A[i - 1]:
                    f[j] += f[j - A[i - 1]]
        return f[m]
