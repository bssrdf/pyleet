'''
Find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Maximum Subarray Sum extension, sign needed to be considered
4 DP ingredients

state:

max_product[i]: max subarray product ending at nums[i]
min_product[i]: min subarray product ending at nums[i]

transfer equation:

max_product[i] = getMax(max_product[i-1] * nums[i], min_product[i-1] * nums[i], nums[i])
min_product[i] = getMin(max_product[i-1] * nums[i], min_product[i-1] * nums[i], nums[i])

Initialization:

max_product[0] = min_product[0] = nums[0]

Result:

maximum of max_product[i] in each loop

'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """       
        
        maxp,curMin,curMax = nums[0],nums[0],nums[0]         
        for j in range(1, len(nums)):
            temp = curMax
            #print curMin, curMax, curMax*nums[j],curMin*nums[j],nums[j]
            curMax = max(nums[j], curMax*nums[j], curMin*nums[j])
            curMin = min(nums[j], temp*nums[j], curMin*nums[j])            
            #print curMin, curMax
            maxp = max(maxp, curMax)
       # print maxp
        return maxp


if __name__ == "__main__":
    assert Solution().maxProduct([2, 3, -2, 4, 4]) == 16
    assert Solution().maxProduct([2, 3, -2, -3]) == 36
    assert Solution().maxProduct([2, 3, 0, -2, -3 ]) == 6
    assert Solution().maxProduct([2, 3, 0, -2, -5, -3]) == 15