
class Solution(object):

   def search(self, nums, target):
       left, right = 0, len(nums)-1
       while left <= right:
           mid = left + (right-left)//2
           if nums[mid] == target:
               return mid
           if nums[mid] < nums[right]:
               if nums[mid] < target and nums[right] >= target:
                   left = mid + 1
               else:
                   right = mid - 1
           else:
               if nums[left] <= target and nums[mid] > target:
                   right = mid - 1
               else:
                   left = mid + 1
       return -1


s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([3, 5, 1 ], 3))




        




