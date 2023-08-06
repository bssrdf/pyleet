'''

-Medium-



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
        A = nums + nums + nums
        ind = {}
        for i in range(3*n):
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