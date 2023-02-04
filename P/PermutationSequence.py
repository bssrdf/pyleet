'''
-Hard-

*Math*

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following 
sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!

'''
import math
class Solution(object):
    def getPermutationMath(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = [i for i in range(1, n+1)]
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation
        
        

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1,n+1)]
        if k == 1: return ''.join([str(i) for i in nums])
        for _ in range(k-1):
            self.nextPermutation(nums)
        return ''.join([str(i) for i in nums])
        

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        i, j = n - 2,  n - 1
        while i >= 0 and nums[i] >= nums[i + 1]: i -= 1 
        if i >= 0:
            while nums[j] <= nums[i]: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        i, j = i+1, n-1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

if __name__ == "__main__":
    print(Solution().getPermutation(3,3))
    print(Solution().getPermutation(4,9))
    print(Solution().getPermutationMath(4,9))