'''
Given an array of integers nums containing n + 1 integers where each 
integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate 
number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1

'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast, t = nums[0], nums[nums[0]], 0
        #count = 0
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            #count += 1
            #print(count, slow, fast)
            if slow == fast: break        
        while True:
            slow = nums[slow]
            t = nums[t]
            if slow == t: break        
        return slow

    def findDuplicateBIT(self, nums):
        res, n = 0, len(nums)
        for i in range(32):
            bit = (1 << i)
            cnt1, cnt2 = 0, 0
            for k in range(n):
                if (k & bit) > 0: cnt1 += 1
                if (nums[k] & bit) > 0: cnt2 += 1            
            if cnt2 > cnt1: res += bit
        
        return res

from random import shuffle

if __name__=="__main__":
    #print(Solution().findDuplicate([1,3,4,2,2]))
    L = [i for i in range(1,101)]
    shuffle(L)
    #print(L[25])
    L += [L[25]]
    print('duplicate = ', L[25])
    print('length = ',len(L))
    print(sorted(L))
    print(Solution().findDuplicateBIT(L))
    print(Solution().findDuplicate(L))
    


