'''

-Medium-
*DP*
*Sliding Window*

There are some prizes on the X-axis. You are given an integer array prizePositions that is sorted in non-decreasing order, where prizePositions[i] is the position of the ith prize. There could be different prizes at the same position on the line. You are also given an integer k.

You are allowed to select two segments with integer endpoints. The length of each segment must be k. You will collect all prizes whose position falls within at least one of the two selected segments (including the endpoints of the segments). The two selected segments may intersect.

For example if k = 2, you can choose segments [1, 3] and [2, 4], and you will win any prize i that satisfies 1 <= prizePositions[i] <= 3 or 2 <= prizePositions[i] <= 4.
Return the maximum number of prizes you can win if you choose the two segments optimally.

 

Example 1:

Input: prizePositions = [1,1,2,2,3,3,5], k = 2
Output: 7
Explanation: In this example, you can win all 7 prizes by selecting two segments [1, 3] and [3, 5].
Example 2:

Input: prizePositions = [1,2,3,4], k = 0
Output: 2
Explanation: For this example, one choice for the segments is [3, 3] and [4, 4], and you will be able to get 2 prizes. 
 

Constraints:

1 <= prizePositions.length <= 105
1 <= prizePositions[i] <= 109
0 <= k <= 109 
prizePositions is sorted in non-decreasing order.



'''

from typing import List
from collections import defaultdict, deque
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        # Wrong
        pP = prizePositions
        mp = defaultdict(int)
        for i in pP:
            mp[i] += 1
        xaxis = sorted(mp)
        arr = []
        for x in xaxis:
            arr.append(mp[x])
        print(xaxis)
        print(arr)
        t, inv = 0, []
        mx = 0
        que = deque()
        for i in range(len(xaxis)):
            t += arr[i]
            while que and que[0][0] < xaxis[i] - k:
                t -= que[0][1]
                que.popleft()
            if mx < t:
                mx = t
                inv = [(que[0][0], xaxis[i]) if que else (xaxis[i], xaxis[i])]
            elif mx == t:
                inv.append((que[0][0], xaxis[i]) if que else (xaxis[i], xaxis[i]))
            que.append((xaxis[i], arr[i]))
        print(inv)

        return 0    

    def maximizeWin2(self, prizePositions: List[int], k: int) -> int:
        A = prizePositions
        dp = [0] * (len(A) + 1)
        res = 0
        j = 0
        for i, a in enumerate(A):
            while A[j] < A[i] - k: j += 1
            dp[i + 1] = max(dp[i], i - j + 1)
            res = max(res, i - j + 1 + dp[j])
        return res


if __name__ == '__main__':
    print(Solution().maximizeWin(prizePositions = [1,1,2,2,3,3,5], k = 2))