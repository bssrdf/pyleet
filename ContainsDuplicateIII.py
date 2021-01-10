'''
-Medium-

*Sort*
*OrderedMap*

Given an array of integers, find out whether there are two distinct indices 
i and j in the array such that the absolute difference between nums[i] and
nums[j] is at most t and the absolute difference between i and j is at 
most k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
 


'''

from sortedcontainers import SortedDict

class Solution(object):

    def containsNearbyAlmostDuplicateOrderMap(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        m = SortedDict()
        j = 0
        for i in range(len(nums)):
            # only need to consider index range [i-k, i]
            if i - j > k: 
                m.pop(nums[j])
                j += 1
            # abs(nums[i]-nums[j]) <= t --> nums[i] - t < nums[j]
            # if nums[j] < nums[i]-t, abs(nums[i]-nums[j]) <= t won't hold
            # search for an index where nums[a] first >= nums[i]-t
            a = m.bisect_left(nums[i] - t)            
            keys = m.keys()
            if a < len(m) and abs(keys[a] - nums[i]) <= t: 
                return True                
            m[nums[i]] = i
        return False

        

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        '''
        The idea is like the bucket sort algorithm. Suppose we have 
        consecutive buckets covering the range of nums with each bucket 
        a width of (t+1). If there are two item with difference <= t, 
        one of the two will happen:

            (1) the two in the same bucket
            (2) the two in neighbor buckets
        '''

        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in range(n):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            print(i, nums[i], m, d)
            if i >= k: 
                del d[nums[i - k] // w]
            print('bucket size is ',len(d))
        return False

if __name__ == "__main__":
    #print(Solution().containsNearbyAlmostDuplicate([1,5,9,13,1,5,9], 3, 3))
    print(Solution().containsNearbyAlmostDuplicateOrderMap([1,5,9,1,5,9], 2, 3))
    print(Solution().containsNearbyAlmostDuplicateOrderMap([1,0,1,1], 1, 2))
    print(Solution().containsNearbyAlmostDuplicateOrderMap([1,2,3,1], 3, 0))