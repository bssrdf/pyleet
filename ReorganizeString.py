'''
-Medium-
*Heap*
*Greedy*

Given a string S, check if the letters can be rearranged so that two 
characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return 
the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

'''
from collections import Counter
import heapq
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        pq = []
        counter = Counter(S)
        res = ''
        for k,v in counter.items():
            if v > (len(S)+1)//2: return ""
            heapq.heappush(pq, (-v, k))
        while len(pq) >= 2:
            f1,c1 = heapq.heappop(pq)
            f2,c2 = heapq.heappop(pq)
            res += c1
            res += c2
            if f1+1 < 0: heapq.heappush(pq, (f1+1, c1))
            if f2+1 < 0: heapq.heappush(pq, (f2+1, c2))
        if len(pq) > 0: 
            f1,c1 = heapq.heappop(pq)
            res += c1
        return res


if __name__ == "__main__":
    print(Solution().reorganizeString("aab"))