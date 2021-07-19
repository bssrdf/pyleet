'''
-Hard-
*DP*
You are given an array of distinct positive integers locations where locations[i] represents the 
position of city i. You are also given integers start, finish and fuel representing the starting 
city, ending city, and the initial amount of fuel you have, respectively.

At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length 
and move to city j. Moving from city i to city j reduces the amount of fuel you have 
by |locations[i] - locations[j]|. Please notice that |x| denotes the absolute value of x.

Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any 
city more than once (including start and finish).

Return the count of all possible routes from start to finish.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
Output: 4
Explanation: The following are all possible routes, each uses 5 units of fuel:
1 -> 3
1 -> 2 -> 3
1 -> 4 -> 3
1 -> 4 -> 2 -> 3
Example 2:

Input: locations = [4,3,1], start = 1, finish = 0, fuel = 6
Output: 5
Explanation: The following are all possible routes:
1 -> 0, used fuel = 1
1 -> 2 -> 0, used fuel = 5
1 -> 2 -> 1 -> 0, used fuel = 5
1 -> 0 -> 1 -> 0, used fuel = 3
1 -> 0 -> 1 -> 0 -> 1 -> 0, used fuel = 5
Example 3:

Input: locations = [5,2,1], start = 0, finish = 2, fuel = 3
Output: 0
Explanation: It's impossible to get from 0 to 2 using only 3 units of fuel since the shortest route needs 4 units of fuel.
Example 4:

Input: locations = [2,1,5], start = 0, finish = 0, fuel = 3
Output: 2
Explanation: There are two possible routes, 0 and 0 -> 1 -> 0.
Example 5:

Input: locations = [1,2,3], start = 0, finish = 2, fuel = 40
Output: 615088286
Explanation: The total number of possible routes is 2615088300. Taking this number modulo 10^9 + 7 gives us 615088286.
 

Constraints:

2 <= locations.length <= 100
1 <= locations[i] <= 10^9
All integers in locations are distinct.
0 <= start, finish < locations.length
1 <= fuel <= 200

'''
from functools import reduce
import bisect

class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[0]*(fuel+1) for _ in range(len(locations))]
        for i in range(fuel+1):
            dp[finish][i] = 1
        for f in range(fuel+1):
            for i in range(len(locations)):
                for j in range(len(locations)):
                    if i == j: continue
                    d = abs(locations[i]-locations[j])
                    if f - d < 0: continue
                    dp[i][f] = (dp[i][f] + dp[j][f-d]) % MOD 
        return dp[start][fuel]

    def countRoutesFast(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """

        # %100
        MOD = 10**9+7
        s, f = locations[start], locations[finish]
        locations.sort()
        start, finish = bisect.bisect_left(locations, s), bisect.bisect_left(locations, f)

        left = [[0]*(fuel+1) for _ in range(len(locations))]  # left[i][f], last move is toward left to location i by f fuel
        right = [[0]*(fuel+1) for _ in range(len(locations))]  # right[i][f], last move is toward right to location i by f fuel
        for f in range(1, fuel+1):
            for j in range(len(locations)-1):
                d = locations[j+1]-locations[j]
                if f > d:
                    # left[j][f] = right[j+1][f-d(j, j+1)] + 2*right[j+2][f-d(j, j+2)] + ... + 2^(k-1)*right[j+k][f-d(j, j+k)]
                    # => left[j+1][f] = (right[j+2][f-d(j+1, j+2)] + 2*right[j+3][f-d(j+1, j+3)] + ... + 2^(k-2)*right[j+1+k-1][f-d(j+1, j+1+k-1)]
                    # => left[j+1][f-d(j, j+1)] = right[j+2][f-d(j, j+2)] + 2*right[j+3][f-d(j, j+3)] + ... + 2^(k-2)*right[j+k][f-d(j, j+k)]
                    # => left[j][f] = right[j+1][f-d(j, j+1)] + 2*left[j+1][f-d(j, j+1)]
                    left[j][f] = (right[j+1][f-d] + 2*left[j+1][f-d] % MOD) % MOD
                elif f == d:
                    left[j][f] = int(j+1 == start)
            for j in range(1, len(locations)):
                d = locations[j]-locations[j-1]
                if f > d:
                    # right[j][f] = left[j-1][f-d(j, j-1)] + 2*left[j-2][f-d(j, j-2)] + ... + 2^(k-1)*left[j-k][f-d(j, j-k)]
                    # => right[j-1][f] = left[j-2][f-d(j-1, j-2)] + 2*left[j-3][f-d(j-1, j-3)] + ... + 2^(k-2)*left[j-1-k+1][f-d(j-1, j-1-k+1)]
                    # => right[j-1][f-d(j, j-1)] = left[j-2][f-d(j, j-2)] + 2*left[j-3][f-d(j, j-3)] + ... + 2^(k-2)*left[j-k][f-d(j, j-k)]
                    # => right[j][f] = left[j-1][f-d(j, j-1)] + 2*right[j-1][f-d(j, j-1)]
                    right[j][f] = (left[j-1][f-d] + 2*right[j-1][f-d] % MOD) % MOD
                elif f == d:
                    right[j][f] = int(j-1 == start)
        result = int(start == finish)
        for f in range(1, fuel+1):
            result = ((result + left[finish][f]) % MOD + right[finish][f]) % MOD
        return result


if __name__ == "__main__":
    print(Solution().countRoutes(locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5))