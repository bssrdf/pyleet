'''
-Medium-

*DP*

Given an array of integers nums, find the maximum length of a subarray where the product of 
all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

 

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
Example 4:

Input: nums = [-1,2]
Output: 1
Example 5:

Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9



'''

from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        prod = 1 if nums[0] >= 0 else -1
        res = 0
        maxPosLen = 1 if nums[0] > 0 else 0
        maxNegLen = 1 if nums[0] < 0 else 0
        res = max(0, maxPosLen)
        #print(prod, maxPosLen, maxNegLen, res)
        for i in nums[1:]:
            if i == 0:
                maxPosLen, maxNegLen = 0, 0
                prod = 1
            else:
                if prod < 0 and i < 0:
                    maxPosLen = maxNegLen + 1                      
                    prod = 1                    
                elif prod > 0 and i > 0:
                    maxPosLen += 1                      
                elif prod < 0 and i > 0:     
                    maxNegLen += 1
                    maxPosLen = 1
                else: # prod > 0, i < 0
                    maxNegLen = maxPosLen + 1
                    prod = -1
                res = max(res, maxPosLen) 
            print(i, prod, maxPosLen, maxNegLen, res)  
        return res   

    def getMaxLen2(self, nums: List[int]) -> int:
        i, j, A = 0, 0, nums
        res, n = 0, len(A)
        while j < n:
            firstNeg, lastNeg, totalNeg = -1, -1, 0
            while j < n and A[j] != 0:
                if A[j] < 0:
                    if firstNeg == -1:
                        firstNeg = j
                    lastNeg = j
                    totalNeg += 1
                j += 1
            if firstNeg != -1 or j > i:
                if totalNeg % 2 == 0:
                    res = max(res, j-i)
                else:
                    res = max(res, j-firstNeg-1, lastNeg-i)
            i = j+1
            j = i
        return res
    
    def getMaxLenDP(self, nums: List[int]) -> int:
        # "pos[i]", "neg[i]" represent longest consecutive numbers ending with nums[i] 
        # forming a positive/negative product.
        n = len(nums)
        pos, neg = [0] * n, [0] * n
        if nums[0] > 0: pos[0] = 1
        if nums[0] < 0: neg[0] = 1
        ans = pos[0]
        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = 1 + pos[i - 1]
                neg[i] = (1 + neg[i - 1]) if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = (1 + neg[i - 1]) if neg[i - 1] > 0 else 0
                neg[i] = 1 + pos[i - 1]
            ans = max(ans, pos[i])
        return ans
    
    def getMaxLenDPO1Space(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = 0, 0
        if nums[0] > 0: pos = 1
        if nums[0] < 0: neg = 1
        ans = pos
        for i in range(1, n):
            if nums[i] > 0:
                pos = 1 + pos
                neg = 1 + neg if neg > 0 else 0
            elif nums[i] < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
            else:
                pos, neg = 0, 0
            ans = max(ans, pos)
        return ans



    


        

if __name__ == '__main__':
    #print(Solution().getMaxLen([1,-2,-3,4]))
    #print(Solution().getMaxLen([-1,2]))
    #print(Solution().getMaxLen([-1,-2,-3,0,1]))
    print(Solution().getMaxLen2([10000]))
    print(Solution().getMaxLen2([-1,-2,-3,0,1]))
    #print(Solution().getMaxLen([1,2,3,5,-6,4,0,10]))
    print(Solution().getMaxLen2([1,2,3,5,-6,4,0,10]))
    #print(Solution().getMaxLen([5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]))
    print(Solution().getMaxLen2([5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]))
    print(Solution().getMaxLenDP([5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]))
