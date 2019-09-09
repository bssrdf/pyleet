'''
Given an array nums, we call (i, j) an important reverse pair if i < j 
and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2 
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.


'''

from collections import deque

class Solution(object):    

    def reversePairsBIT(self, nums):

        res = 0
        copy = sorted(nums)
        bit = [0] * (len(nums) + 1)        

        def search(i):
            sum = 0
            while i < len(bit):
                sum += bit[i]
                i += i & (-i)
            return sum

        def insert(i):
            while i > 0:
                bit[i] += 1
                i -= i & (-i)

        def index(a, val):
            l, r = 0, len(a)-1
            while l <= r:
                m = l + (r-l)//2
                if a[m] >= val:
                    r = m-1
                else:
                    l = m+1
            return l+1

        for ele in nums:
            c = index(copy, 2*ele+1) 
            a = search(c)
            res += a
            b = index(copy, ele)
            insert(b)
            print(ele, res, a, b, c, bit)
        return res
        
    def reversePairs(self, nums):
        count = [0]
        def merge(nums):
            if len(nums) <= 1: return nums
            
            left, right = merge(nums[:len(nums)//2]), merge(nums[len(nums)//2:])
            l = r = 0
            
            while l < len(left) and r < len(right):
                if left[l] <= 2 * right[r]:
                    l += 1
                else:
                    count[0] += len(left) - l
                    r += 1
            return sorted(left+right)

        merge(nums)
        return count[0]
        



print(Solution().reversePairs([1,3,2,3,1]))
print(Solution().reversePairs([2,4,3,5,1]))
print(Solution().reversePairsBIT([2,4,3,5,1]))