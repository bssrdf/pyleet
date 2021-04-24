'''
-Hard-
*DP*
Given an array of integers and a number k, find k non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.

The subarray should contain at least one number


Example 1:

Input:

nums = [1,2,3]
k = 1
Output:

6
Explanation:

1 + 2 + 3 = 6
Example 2:

Input:

nums = [-1,4,-2,3,-2,3]
k = 2
Output:

8
Explanation:

4 + (3 + -2 + 3) = 8

'''

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    # 分析：与Best Time to Buy and Sell Stock IV类似，两个数组分别记录包含当前值的本地最优解和全局最优解。
    # local[i][j]代表从0到nums中第i个数字处，分成j个数组后，和的最大值,且必须包括第i个数字，这样可以排除
    # 第i个数组包含在前一个数组中的情况。global[i][j]代表从0到nums第i个数字处，分成j个数组后, 不一定包含
    # 第i个元素的最大和。
    # 二维数组动态规划的状态转移方程为：

    #local[i][j] = Math.max(local[i - 1][j], global[i - 1][j - 1]) + nums[i - 1];

    #global[i][j] = Math.max(global[i - 1][j], local[i][j]);

    def maxSubArray(self, nums, k):
        # write your code here
        if k > len(nums): return 0
        n = len(nums)

        local = [[0]*(k+1) for _ in range(n+1)]
        glob  = [[0]*(k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            local[i][0] = -float('inf')
            for j in range(1, k+1):
                if j > i:
                    # 前j－1个元素不可能找到不重叠的j个子数组，因此初始化为最小值，以防后面被取到
                    local[i][j] = -float('inf')
                    glob [i][j] = -float('inf')
                    continue
                # 有两种情况，第一种是第i个元素自己组成一个子数组，则要在前i－1个元素中找k－1个子数组，
                # 第二种情况是第i个元素属于前一个元素的子数组，因此要在i－1个元素中找k个子数组（并且必须
                # 包含第i－1个元素，这样第i个元素才能合并到最后一个子数组中），取两种情况里面大的那个。
                local[i][j] = max(local[i-1][j], glob[i-1][j-1]) + nums[i-1]
                if i == j:
                    glob[i][j] = local[i][j]
                else:
                    # 有两种情况，第一种是不包含第i个元素，所以要在前i－1个元素中找k个子数组，第二种情况
                    # 为包含第i个元素，在i个元素中找k个子数组且必须包含第i个元素，取两种情况里面大的那个。
                    glob[i][j] = max(glob[i-1][j],local[i][j])
        return glob[n][k]

if __name__ == "__main__":
    print(Solution().maxSubArray([-1,4,-2,3,-2,3], 2))
