'''


-Medium-

*Sliding Window*
*Two Pointers*


Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 109

'''


from typing import List
from collections import Counter

class Solution:
    
    def countGood(self, nums: List[int], k: int) -> int:
        # Wrong
        n = len(nums)
        cnt = Counter()
        pairs = 0
        ans = 0
        for i in range(n):
            a = nums[i]
            pairs += cnt[a] 
            cnt[a] += 1
            # if cnt[a] % 2 == 0:
            
            if pairs >= k:
                ans += 1
            # print(i, pairs)
        i = 0
        # print(ans)
        # cnt = Counter()
        while i < n:
            a = nums[i]
            cnt[a] -= 1
            # if cnt[a] == 0:
                # i += 1
                # continue 
            
            pairs -= cnt[a]
            if pairs >= k:
                ans += 1
            i += 1
        return ans

    def countGood2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = Counter()
        pairs = 0
        ans = 0
        i = 0
        while i < n:
            a = nums[i]
            pairs += cnt[a] 
            cnt[a] += 1
            if pairs >= k:
                break
            i += 1
        if i == n: return 0
        j = 0
        while j < i:
            b = nums[j]                
            p = pairs
            pairs -= cnt[b] - 1 
            cnt[b] -= 1
            if pairs < k:
                pairs = p
                cnt[b] += 1
                break
            j += 1
        ans += j+1
        i += 1
        while i < n:
            a = nums[i]
            pairs += cnt[a] 
            cnt[a] += 1
            while j < i:
                b = nums[j]                
                p = pairs
                pairs -= cnt[b] - 1 
                cnt[b] -= 1
                if pairs < k:
                    pairs = p
                    cnt[b] += 1
                    break
                j += 1
            ans += j+1
            i += 1    
        return ans    
    

    def countGood3(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = Counter()
        ans, pairs = 0, 0
        i, j = 0, 0
        for i in range(n):
            a = nums[i]
            pairs += cnt[a] 
            cnt[a] += 1
            while j < i:
                b, p = nums[j], pairs                
                pairs -= cnt[b] - 1 
                cnt[b] -= 1
                if pairs < k:
                    pairs = p
                    cnt[b] += 1
                    break
                j += 1
            if pairs >= k:
                ans += j+1
        return ans    
    

    def countGood4(self, nums: List[int], k: int) -> int:
        # likely not working
        n = len(nums)
        cnt = Counter()
        ans, pairs = 0, 0
        i, j = 0, 0
        for i in range(n):
            a = nums[i]
            pairs += cnt[a] 
            cnt[a] += 1
            while j < i and pairs >= k:
                b = nums[j]
                pairs -= cnt[b] - 1 
                cnt[b] -= 1
                j += 1
            if pairs >= k:
                ans += j+1
        return ans    
                


if __name__=="__main__":          
    print(Solution().countGood2(nums = [3,1,4,3,2,2,4], k = 2))
    print(Solution().countGood3(nums = [3,1,4,3,2,2,4], k = 2))
    print(Solution().countGood2(nums = [1,1,1,1,1], k = 10))
    print(Solution().countGood3(nums = [1,1,1,1,1], k = 10))
    # print(Solution().countGood(snums = [2,1,3,1,2,2,3,3,2,2,1,1,1,3,1], k = 11))
    print(Solution().countGood2(nums = [2,1,3,1,2,2,3,3,2,2,1,1,1,3,1], k = 11))
    print(Solution().countGood3(nums = [2,1,3,1,2,2,3,3,2,2,1,1,1,3,1], k = 11))
    print(Solution().countGood2(nums = [2,3,1,3,2,3,3,3,1,1,3,2,2,2], k=18))
    print(Solution().countGood3(nums = [2,3,1,3,2,3,3,3,1,1,3,2,2,2], k=18))
    print(Solution().countGood2(nums = [2,3,3,3,3,1,3,1,3,2], k = 19))
    print(Solution().countGood3(nums = [2,3,3,3,3,1,3,1,3,2], k = 19))