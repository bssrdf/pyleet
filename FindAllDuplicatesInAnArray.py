'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements 
appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

'''
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        N2 = 2*N
        ans = []
        for i in range(N):
            if nums[i] > N2:
                nums[nums[i]-N2-1] += N
            elif nums[i] > N:
                nums[nums[i]-N-1] += N
            else:
                nums[nums[i]-1] += N        
        for i,n in enumerate(nums):
            if n > N2:
                ans.append(i+1)
        return ans
        

if __name__ == '__main__':
    print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))

