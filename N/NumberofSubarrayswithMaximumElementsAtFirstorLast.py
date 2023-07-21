'''

Amazon OA

Given an array, find the number of sub-arrays that have the maximum element as either the first/last element of the sub-array.e.g.Input array: [3,1,3,5]One of the Subarrays of Input array: [3,1,3]Max Element: 3Is 3 either the first / last element of the sub-array - YesSo its a valid sub-array

sub-arrays that satisfy this condition = [3],[3,1],[3,1,3],[3,1,3,5],[1],[1,3],[1,3,5],[3],[3,5],[5]In each group the maximum element is in either the first or last position.

'''
from typing import List


def decreasingQueue(A):
    n = len(A)
    queue = []
    firstLargerToLeft = [-1]*len(A)
    firstLargerToRight = [-1]*len(A)
    firstLargerIndexToLeft = [-1]*len(A)
    firstLargerIndexToRight = [n]*len(A)
    for i,v in enumerate(A):
        while queue and A[queue[-1]] < v:
            k = queue.pop()
            firstLargerToRight[k] = v
            firstLargerIndexToRight[k] = i
            
        if queue:
            firstLargerToLeft[i] = A[queue[-1]]
            firstLargerIndexToLeft[i] = queue[-1]
        queue.append(i)
    return firstLargerToLeft, firstLargerToRight, firstLargerIndexToLeft, firstLargerIndexToRight
    



class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        A = nums 
        _, _, firstLargerIndexToLeft, firstLargerIndexToRight = decreasingQueue(A)
        mark = [0]*(len(A)+1)
        for i in range(len(A)):
            mark[firstLargerIndexToRight[i]] -= 1
            mark[i+1] += 1
        # print('mark', mark)
        res = [0]*len(A)
        res[0] = mark[0]   
        for i in range(1, len(A)):
            res[i] = res[i-1] + mark[i]
        # print(res)
        print(firstLargerIndexToLeft)
        ans = 1
        for i in range(1, len(A)):
            ans += (i-firstLargerIndexToLeft[i]) + res[i]
        return ans     
    
    def numberOfSubarrays2(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            ans += 1
            mx = nums[i]
            for j in range(i+1,n):
                mx = max(mx, nums[j])
                if mx == nums[i] or mx == nums[j]:
                    ans += 1
        return ans



        
if __name__ == "__main__":
    # print(Solution().numberOfSubarrays(nums= [3,1]))
    print(Solution().numberOfSubarrays(nums= [3,1,3,5]))
    # print(Solution().numberOfSubarrays2(nums= [3,1,3,5]))
    # print(Solution().numberOfSubarrays(nums= [3,1,3,5,4]))
    # print(Solution().numberOfSubarrays2(nums= [3,1,3,5,4]))
    # print(Solution().numberOfSubarrays(nums= [4,1,3,5]))
    # print(Solution().numberOfSubarrays2(nums= [4,1,3,5]))
    # print(Solution().numberOfSubarrays(nums= [4,4,2,1,3,5]))
    # print(Solution().numberOfSubarrays2(nums= [4,4,2,1,3,5]))
    # nums = list(range(1, 11))
    # print(Solution().numberOfSubarrays(nums= nums))
    # print(Solution().numberOfSubarrays2(nums= nums))
    nums=[7,5,10,8,9,5,3,7]
    print(Solution().numberOfSubarrays(nums= nums))
    print(Solution().numberOfSubarrays2(nums= nums))
    


