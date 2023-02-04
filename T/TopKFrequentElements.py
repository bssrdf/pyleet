'''
-Medium-

*Heap*

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the 
array's size.
It's guaranteed that the answer is unique, in other words the set of the top k 
frequent elements is unique. You can return the answer in any order.


'''



import heapq
from collections import defaultdict
from collections import Counter
class Solution(object):
    def topKFrequentCounter(self, nums, k):
        return list(list(zip(*Counter(nums).most_common(k)))[0])

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = []
        m = defaultdict(int)
        for i in nums:
            m[i] += 1
        for i in m:
            heapq.heappush(q, (-m[i], i))
        res = []
        for i in range(k):
            _, num = heapq.heappop(q)
            res.append(num)
        return res

if __name__ == "__main__":
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))
    print(Solution().topKFrequentCounter([1,1,1,2,2,3], 2))