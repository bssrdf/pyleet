'''
-Hard-

You have n bulbs in a row numbered from 1 to n. Initially, all the bulbs are turned off. We turn on 
exactly one bulb every day until all bulbs are on after n days.

You are given an array bulbs of length n where bulbs[i] = x means that on the (i+1)th day, we will 
turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

Given an integer k, return the minimum day number such that there exists two turned on bulbs that 
have exactly k bulbs between them that are all turned off. If there isn't such day, return -1.

 

Example 1:

Input: bulbs = [1,3,2], k = 1
Output: 2
Explanation:
On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.
Example 2:

Input: bulbs = [1,2,3], k = 1
Output: -1
 

Constraints:

n == bulbs.length
1 <= n <= 2 * 10^4
1 <= bulbs[i] <= n
bulbs is a permutation of numbers from 1 to n.
0 <= k <= 2 * 10^4

'''
import bisect
class Solution:
    """
    @param flowers: the place where the flower will open in that day
    @param k:  an integer
    @return: in which day meet the requirements
    """
    def kEmptySlots(self, flowers, k):
        # Write your code here
        active = []
        for day, flower in enumerate(flowers, 1):
            i = bisect.bisect(active, flower)
            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.insert(i, flower)
        return -1

    def kEmptySlotsSlidingWindow(self, flowers, k):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day
        print(days)
        ans = float('inf')
        left, right = 0, k+1
        while right < len(days):
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i+k+1
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right+k+1

        return ans if ans < float('inf') else -1


if __name__ == "__main__":
    print(Solution().kEmptySlots([1,3,2], 1))
    print(Solution().kEmptySlotsSlidingWindow([1,3,2], 1))