'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution(object):
    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        O(n) worst case 
        """
        l = 0
        n = len(nums)
        r = n-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                left=mid
                while left >= l:
                    if nums[left] != target:
                        break
                    left -= 1
                right=mid
                while right <= r:
                    if nums[right] != target:
                        break
                    right += 1
                return [left+1, right-1]
            
        return [-1, -1]
                
    def searchRange2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        O(logn) worst and average case 
        """
        l = 0
        n = len(nums)
        r = n-1
        while l < r:
            mid = (r+l)/2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        if nums[l] != target:
            return [-1, -1]
        else:
            left = l
        r = n-1    
        while l < r:
            mid = (r+l)/2+1
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid
        right = r
        return [left, right]

if __name__ == "__main__":
    #assert Solution().searchRange2([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    print(Solution().searchRange1([5, 7, 7, 8, 8, 10], 6))
    print(Solution().searchRange1([5, 7, 7, 8, 8, 10], 8))
    #assert Solution().searchRange2([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    #assert Solution().searchRange2([5, 7, 7, 8, 8, 10], 7) == [1, 2]
    #assert Solution().searchRange2([5, 7, 7, 8, 8, 10], 10) == [5, 5]
