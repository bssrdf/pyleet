'''

-Medium-
*Hash Table*
*Circular Array*

You are given a 0-indexed array nums containing n integers.

At each second, you perform the following operation on the array:

For every index i in the range [0, n - 1], replace nums[i] with either nums[i], nums[(i - 1 + n) % n], or nums[(i + 1) % n].
Note that all the elements get replaced simultaneously.

Return the minimum number of seconds needed to make all elements in the array nums equal.

 

Example 1:

Input: nums = [1,2,1,2]
Output: 1
Explanation: We can equalize the array in 1 second in the following way:
- At 1st second, replace values at each index with [nums[3],nums[1],nums[3],nums[3]]. After replacement, nums = [2,2,2,2].
It can be proven that 1 second is the minimum amount of seconds needed for equalizing the array.
Example 2:

Input: nums = [2,1,3,3,2]
Output: 2
Explanation: We can equalize the array in 2 seconds in the following way:
- At 1st second, replace values at each index with [nums[0],nums[2],nums[2],nums[2],nums[3]]. After replacement, nums = [2,3,3,3,3].
- At 2nd second, replace values at each index with [nums[1],nums[1],nums[2],nums[3],nums[4]]. After replacement, nums = [3,3,3,3,3].
It can be proven that 2 seconds is the minimum amount of seconds needed for equalizing the array.
Example 3:

Input: nums = [5,5,5,5]
Output: 0
Explanation: We don't need to perform any operations as all elements in the initial array are the same.
 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 109


'''
from typing import List
from collections import Counter, defaultdict

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n = len(nums)
        mx = max(cnt)
        # print(mx)
        left = [-1]*n
        right = [-1]*n
        pos = -n
        for i in range(n):
            if nums[i] != mx:
                left[i] = i - pos
            else:
                pos = i
        pos = n
        for i in range(n-1, -1, -1):
            if nums[i] != mx:
                right[i] = pos - i
            else:
                pos = i
        print(left)
        print(right)
        ans = 0
        for i in range(n):
            if left[i] != -1:
                ans = max(ans, min(left[i], right[i]))

        return ans
    

    def minimumSeconds2(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n = len(nums)
        maxes, t = [], 0
        for c in cnt:
            if cnt[c] > t:
                t = cnt[c]
                maxes = [c]
            elif cnt[c] == t:
                maxes.append(c)
        # print(mx)
        def check(mx):
            print('check: ',mx)
            left = [-1]*n
            right = [-1]*n
            pos = -n
            for i in range(2*n):            
                if nums[(i+n)%n] == mx:                
                    pos = i                
                if i >= n:
                    if nums[i-n] != mx:
                        left[i-n] = i - pos      
                # print(i, pos, left)    
            pos = n
            for i in range(2*n-1, -1, -1):
                if nums[(i+n)%n] == mx:                
                    pos = i                
                if i < n:
                    if nums[i] != mx:
                        right[i] = pos - i      
                
            print(left)
            print(right)
            ans = 0
            for i in range(n):
                if left[i] != -1:
                    ans = max(ans, min(left[i], right[i]))
            print('ans is ', ans)
            return ans
        if len(maxes) == n:
            return check(maxes[0])
        elif len(cnt) == 1:
            return 0
        ret = 10**6
        for mx in maxes:
            ret = min(ret, check(mx))
        return ret 
    
    def minimumSeconds3(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for c in cnt:
            cnt[c] = 0  
        n = len(nums)
        A = nums + nums
        ind = {}
        for i in range(len(A)):
            if A[i] in ind:                
                cnt[A[i]] = max(cnt[A[i]], (i - ind[A[i]])//2)
            ind[A[i]] = i  
        return min(cnt.values())




if __name__ == "__main__":
    # print(Solution().minimumSeconds2(nums = [2,1,3,3,2]))
    # print(Solution().minimumSeconds2(nums = [1,2,1,2]))
    # print(Solution().minimumSeconds2(nums = [5,5,5,5]))
    # print(Solution().minimumSeconds2(nums = [5,3,13]))
    # print(Solution().minimumSeconds2(nums = [5,3,4,13]))
    # print(Solution().minimumSeconds2(nums = [3,19,8,12]))
    # print(Solution().minimumSeconds2([8,8,9,10,9]))

    print(Solution().minimumSeconds3([4,3,3]))
    print(Solution().minimumSeconds3([1, 19, 19, 7, 1]))
    print(Solution().minimumSeconds3([1,11,11,11,19,12,8,7,19]))