'''
-Medium-
*DP*
*Knapsack*

Given a non-empty array nums containing only positive integers, find if 
the array can be partitioned into two subsets such that the sum of 
elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''

class Solution(object):
    
    '''
    我们可以先对集合求和，得出sum，把问题转化为01背包问题：
    给一个可装载重量为sum/2的背包和N个物品，每个物品的重量为nums[i]。
    现在让你装物品，是否存在一种装法，能够恰好将背包装满？
    '''

    def canPartitionSpaceOpt(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        S = 0
        n = len(nums)        
        for i in nums:
            S += i
        if S%2 > 0: return False 
        S //= 2
        K = [False for x in range(S+1)]        
        # 背包没有空间的时候，就相当于装满了，        
        K[0] = True
        for i in range(1, n+1): 
            for w in range(S,nums[i-1]-1, -1): 
                K[w] = K[w] or K[w-nums[i-1]]                           
        return K[S] 


    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        S = 0
        n = len(nums)        
        for i in nums:
            S += i
        if S%2 > 0: return False 
        S //= 2
        K = [[False for x in range(S+1)] for x in range(n+1)]   
        #当没有物品可选择的时候，肯定没办法装满背包。      
        # K[0][:] = False
        # 背包没有空间的时候，就相当于装满了，
        for i in range(n+1):
            K[i][0] = True
        for i in range(1, n+1): 
            for w in range(nums[i-1], S+1): 
                # 背包容量不足，不能装入第 i个物品
                if w - nums[i-1] < 0:
                    K[i][w] = K[i-1][w]
                else:
                    K[i][w] = K[i-1][w] or K[i-1][w-nums[i-1]]                           
        return K[n][S] 


if __name__ == "__main__":
    print(Solution().canPartition([1,5,11,5]))
    print(Solution().canPartition([1,2,3,5]))
    print(Solution().canPartition([1,2,5]))
    print(Solution().canPartition([14,9,8,4,3,2]))

    print(Solution().canPartitionSpaceOpt([1,5,11,5]))
    print(Solution().canPartitionSpaceOpt([1,2,3,5]))
    print(Solution().canPartitionSpaceOpt([1,2,5]))
    print(Solution().canPartitionSpaceOpt([14,9,8,4,3,2]))
