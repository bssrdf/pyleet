'''
-Hard-
*Binary Search*
*Fenwick Tree*

You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller 
elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

这道题给定我们一个数组，让我们计算每个数字右边所有小于这个数字的个数，目测我们
不能用 brute force，OJ 肯定不答应，那么我们为了提高运算效率，首先可以使用用二
分搜索法，思路是将给定数组从最后一个开始，用二分法插入到一个新的数组，这样新数组
就是有序的，那么此时该数字在新数组中的坐标就是原数组中其右边所有较小数字的个数，

'''

import bisect

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sortedList = []
        for num in nums[::-1]:
            position=bisect.bisect_left(sortedList, num)
            result.append(position)
            bisect.insort(sortedList,num)
        return result[::-1]

    def countSmallerMergeSort(self, nums):
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                # merge left and right part in reverse order
                for i in range(len(enum))[::-1]: 
                    # because the reverse order, always consider the last
                    # element of left and right
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            print(half,enum)
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
    
    def countSmallerBIT(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        res = [0]*n
        offset = min(nums)
        if offset <= 0:
            offset = (-offset)+1
            for i in range(n):
                nums[i] += offset
        BIT = [0]*(max(nums) + 1)
        def update(index, val):
            while index < len(BIT):
                BIT[index] += val
                index += index & (-index)
        def getPrefixSum(index):
            sm = 0
            while index > 0:
                sm += BIT[index]
                index -= index & (-index)
            return sm
        for i in nums:
            update(i, 1)
        for i in range(n):
            update(nums[i], -1) 
            res[i] = getPrefixSum(nums[i]-1)
        return res
    
    def countSmallerBIT2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        res = [0]*n
        A = sorted(nums)        
        BIT = [0]*(n + 1)
        def update(index, val):
            while index < len(BIT):
                BIT[index] += val
                index += index & (-index)
        def query(index):
            sm = 0
            while index > 0:
                sm += BIT[index]
                index -= index & (-index)
            return sm        
        for i in range(n-1, -1, -1):            
            res[i] = query(bisect.bisect_left(A, nums[i]))
            update(bisect.bisect_left(A, nums[i])+1, 1) 
        return res
        
        



#print(Solution().countSmaller([5,2,6,1]))
#print(Solution().countSmallerMergeSort([5,2,6,1]))
print(Solution().countSmallerBIT([5,2,6,1]))
print(Solution().countSmallerBIT2([5,2,6,1]))
#print(Solution().countSmallerBIT([-1]))
print(Solution().countSmallerBIT([-1, -1]))
print(Solution().countSmallerBIT2([-1, -1]))
print(Solution().countSmallerBIT([0, 1, 2]))
print(Solution().countSmallerBIT2([0, 1, 2]))