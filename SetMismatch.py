'''
-Easy-

You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another 
number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the 
form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4

'''

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) 
        m = {i:1 for i in range(1,n+1)}
        for i in nums:
            m[i] += 1            
        twice, missing = -1, -1
        for v,f in m.items():
            if f == 3: twice = v
            if f == 1: missing = v

        return [twice, missing]

    def findErrorNumsO1Sapce(self, nums):

        res = [-1, -1]
        for i in nums:
           if nums[abs(i) - 1] < 0: res[0] = abs(i)
           else: nums[abs(i) - 1] *= -1
           print(i, abs(i), nums)
        for i in range(len(nums)):
           if nums[i] > 0: res[1] = i+1
        return res



if __name__ == "__main__":
    print(Solution().findErrorNums([1,2,2,4]))
    print(Solution().findErrorNums([1,1]))
    print(Solution().findErrorNums([2,2]))
    print(Solution().findErrorNumsO1Sapce([2,1,2,4]))