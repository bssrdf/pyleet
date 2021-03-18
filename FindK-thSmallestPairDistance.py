'''
-Hard-

Given an integer array, return the k-th smallest distance among all the pairs. 
The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.

'''

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        def kSmallest(m):
            i, cnt = 0, 0
            for j in range(1, len(nums)):
                while nums[j]-nums[i] > m:
                    i += 1
                cnt += j-i
            return cnt
        l, r = 0, nums[-1]-nums[0]
        while l < r:
            mid = l + (r-l)//2
            if kSmallest(mid) >= k:
                r = mid
            else:
                l = mid+1
        return l

if __name__ == "__main__":
    print(Solution().smallestDistancePair([1,3,1], 1))
    print(Solution().smallestDistancePair([1, 5, 3, 2], 3))