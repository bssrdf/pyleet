class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        for cur in range(len(nums)):
            if nums[cur]:
                t = nums[cur]
                nums[cur] = nums[lastNonZeroFoundAt]
                nums[lastNonZeroFoundAt] = t  
                lastNonZeroFoundAt += 1
            print(lastNonZeroFoundAt)
        return

if __name__ == "__main__":
    a = [0,1,0,3,12]
    print(a)
    Solution().moveZeroes(a)
    print(a)
