'''
-Hard-
*Binary Search*

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
            #print(enum)
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


print(Solution().countSmaller([5,2,6,1]))
print(Solution().countSmallerMergeSort([5,2,6,1]))