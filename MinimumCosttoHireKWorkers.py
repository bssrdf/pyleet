'''
-Hard-
*Greedy*
*Sort*
*Priority Queue*

here are n workers.  The i-th worker has a quality[i] and a minimum wage expectation 
wage[i].

Now we want to hire exactly k workers to form a paid group.  When hiring a group of 
k workers, we must pay them according to the following rules:

1) Every worker in the paid group should be paid in the ratio of their quality compared 
to other workers in the paid group.
2) Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above 
conditions.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 

Note:

1 <= k <= n <= 10000, where n = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.


'''
import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        ratio = [x/y for x,y in zip(wage, quality)]
        h, qSum, res = [], 0, float('inf')
        for r, q in sorted(zip(ratio, quality)):
            qSum += q
            heapq.heappush(h, -q)
            if len(h) > k:
                qSum -= -1*heapq.heappop(h) # heap contains k smallest qualities
            if len(h) == k:
                res = min(res, r*qSum) # qSum is the sum of k smallest qualities
                                       # r is the maximum of ratio so far due to sort
                                       # using a max r makes sure condition 2) is satisfied
        return res


if __name__ == "__main__":
    print(Solution().mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2))
    print(Solution().mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3))