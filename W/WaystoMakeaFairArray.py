'''

-Medium-

You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. 
Notice that the index of the elements may change after the removal.

For example, if nums = [6,1,7,4,1]:

Choosing to remove index 1 results in nums = [6,7,4,1].
Choosing to remove index 2 results in nums = [6,1,4,1].
Choosing to remove index 4 results in nums = [6,1,7,4].
An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

Return the number of indices that you could choose such that after the removal, nums is fair.

 

Example 1:

Input: nums = [2,1,6,4]
Output: 1
Explanation:
Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
There is 1 index that you can remove to make nums fair.
Example 2:

Input: nums = [1,1,1]
Output: 3
Explanation: You can remove any index and the remaining array is fair.
Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: You cannot make a fair array after removing any index.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4


'''

class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preO = [0]
        preE = [0]
        for i,v in enumerate(nums):
            if i % 2 == 0: 
                preO.append(preO[-1]+v)
                preE.append(preE[-1])
            else: 
                preE.append(preE[-1]+v)
                preO.append(preO[-1])
        ans = 0
        for i in range(1, len(nums)+1):
            sumO = preO[i-1]-preO[0] + preE[-1]-preE[i]
            sumE = preE[i-1]-preE[0] + preO[-1]-preO[i]
            if sumO == sumE: ans += 1
        return ans
      
    def waysToMakeFairO1Space(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd = sum(nums[0: :2])
        even = sum(nums[1: :2])
        
        oddbefore = 0; evenbefore = 0
        count = 0
        
        for i in range(len(nums)) :
            
            if i % 2 == 0 :    
                evenafter = even - evenbefore
                oddafter = odd - oddbefore - nums[i]
            else:
                evenafter = even - evenbefore - nums[i]
                oddafter = odd - oddbefore
                
            if oddbefore + evenafter == evenbefore + oddafter :
                count += 1
                
            if i % 2 == 0 :
                oddbefore += nums[i]
            else:
                evenbefore += nums[i]
                
        return count





        
if __name__ == "__main__":
    print(Solution().waysToMakeFair([2,1,6,4]))
    print(Solution().waysToMakeFair([1,1,1]))
    print(Solution().waysToMakeFairO1Space([2,1,6,4]))
    print(Solution().waysToMakeFairO1Space([1,1,1]))