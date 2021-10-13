'''
-Medium-

Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104

'''

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums)
        # self.mergeSort(nums)
        # self.bubbleSort(nums)
        # self.insertionSort(nums)
		# self.selectionSort(nums)
        #self.heapSort(nums)
        return nums

    def quickSort(self, nums):
        def helper(head, tail):
            if head >= tail: return 
            l, r = head, tail
            m = (r - l) // 2 + l
            pivot = nums[m]
            while r >= l:
                while r >= l and nums[l] < pivot: l += 1
                while r >= l and nums[r] > pivot: r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            print(pivot, nums, r, l, head, tail)
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums)-1)
        return
    
     
	# @mergeSort
    def mergeSort(self, nums): 
        if len(nums) > 1: 
            mid = len(nums)//2
            L = nums[:mid] 
            R = nums[mid:] 

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1

if __name__ == "__main__":
    #print(Solution().sortArray([5,1,1,2,0,0]))
    print(Solution().sortArray([5,9,17,2,7,6,11,20,10]))