'''
-Easy-

Given a sorted integer array nums, where the range of elements are in the 
inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]


'''
import sys
class Solution(object):
    def missingRangesAC(self, nums, lower, upper):
        res = []
        for num in nums:
            if num > lower: 
                res.append(str(lower) + ("->" + str(num - 1) if (num - 1) > lower else ""))
            if num == upper: return res
            lower = num + 1
        if lower <= upper:
            res.append(str(lower) + ("->" + str(upper) if upper > lower else "")) 
        return res

    def missingRanges(self, nums, lower, upper):
        res = []        
        nums += [sys.maxsize]
        for i in range(len(nums)-1):
            l = max(lower, nums[i])
            r = min(upper, nums[i+1])
            if r-l > 2:
                    if l == nums[-2]:
                        res.append(str(l+1)+'->'+str(r))
                    else:
                        res.append(str(l+1)+'->'+str(r-1))
            elif r-l == 2:
                res.append(str(l+1))       
        return res






if __name__ == "__main__":
    print(Solution().missingRanges([0, 1, 3, 50, 75], 0, 99))
    print(Solution().missingRangesAC([0, 1, 3, 50, 75], 0, 99))




