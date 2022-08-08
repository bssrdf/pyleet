'''

-Hard-
*Greedy*

You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.

 

Example 1:

Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0. 
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109

'''

from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # Wrong solution
        n, mi = len(nums), nums[-1]
        cnt =  0
        for i in range(n-2, -1, -1):
            # print(i, nums[i], cnt, mi)
            if nums[i] > mi:
                k = nums[i] % mi                
                if k == 0:
                    cnt += nums[i] // mi - 1   
                else:
                    m = mi - k
                    cnt += nums[i] // mi   
                    if m % 2 == 0:
                        mi = mi - m // 2                        
                    else:
                        mi = mi - (m+1) // 2
            else:
                mi = nums[i]   
            # print(i, nums[i], cnt, mi)
        return cnt

    def minimumReplacement2(self, nums: List[int]) -> int:
        n, mi = len(nums), nums[-1]
        cnt =  0
        for i in range(n-2, -1, -1):
            if nums[i] > mi:
                m, k = divmod(nums[i], mi)                
                if k == 0:
                    cnt += m - 1   
                else:
                    cnt += m 
                    mi = nums[i] // (m + 1)                                            
            else:
                mi = nums[i]   
        return cnt



if __name__ == "__main__":
    print(Solution().minimumReplacement(nums = [1,2,3,4,5]))
    print(Solution().minimumReplacement(nums = [3,9,3]))
    print(Solution().minimumReplacement(nums = [3,10,3]))
    print(Solution().minimumReplacement(nums = [3,11,3]))
    print(Solution().minimumReplacement(nums = [3,9,2]))

    nums = [368,112,2,282,349,127,36,98,371,79,309,221,175,262,224,215,230,250,84,269,384,328,118,97,17,105,342,344,242,160,394,17,120,335,76,101,260,244,378,375,164,190,320,376,197,398,353,138,362,38,54,172,3,300,264,165,251,24,312,355,237,314,397,101,117,268,36,165,373,269,351,67,263,332,296,13,118,294,159,137,82,288,250,131,354,261,192,111,16,139,261,295,112,121,234,335,256,303,328,242,260,346,22,277,179,223]
    print(Solution().minimumReplacement(nums = nums))
    print(Solution().minimumReplacement2(nums = [1,2,3,4,5]))
    print(Solution().minimumReplacement2(nums = [3,9,3]))
    print(Solution().minimumReplacement2(nums = [3,10,3]))
    print(Solution().minimumReplacement2(nums = [3,11,3]))
    print(Solution().minimumReplacement2(nums = [3,9,2]))
    print(Solution().minimumReplacement2(nums = nums))
        