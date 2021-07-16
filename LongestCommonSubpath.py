'''
-Hard-

There is a country of n cities numbered from 0 to n - 1. In this country, there is a road connecting every pair of cities.

There are m friends numbered from 0 to m - 1 who are traveling through the country. Each one of them will take a path consisting of some cities. Each path is represented by an integer array that contains the visited cities in order. The path may contain a city more than once, but the same city will not be listed consecutively.

Given an integer n and a 2D integer array paths where paths[i] is an integer array representing the path of the ith friend, return the length of the longest common subpath that is shared by every friend's path, or 0 if there is no common subpath at all.

A subpath of a path is a contiguous sequence of cities within that path.

 

Example 1:

Input: n = 5, paths = [[0,1,2,3,4],
                       [2,3,4],
                       [4,0,1,2,3]]
Output: 2
Explanation: The longest common subpath is [2,3].
Example 2:

Input: n = 3, paths = [[0],[1],[2]]
Output: 0
Explanation: There is no common subpath shared by the three paths.
Example 3:

Input: n = 5, paths = [[0,1,2,3,4],
                       [4,3,2,1,0]]
Output: 1
Explanation: The possible longest common subpaths are [0], [1], [2], [3], and [4]. All have a length of 1.
 

Constraints:

1 <= n <= 10^5
m == paths.length
2 <= m <= 10^5
sum(paths[i].length) <= 10^5
0 <= paths[i][j] < n
The same city is not listed multiple times consecutively in paths[i].

'''

class Solution(object):
    def longestCommonSubpath(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: int
        """
        MOD = 2**63-1
        d = 65535
        left, right = 0, min([len(p) for p in paths])+1
        spaths = []
        for path in paths:
            spaths.append(''.join([chr(c) for c in path]))
        def commonPath(L):
            q = pow(d, L, MOD)             
            m = {}
            for path in spaths:
                h = 0
                ml = {} 
                for i in range(L):
                    h = (h*d+ord(path[i]))%MOD
                if h not in m: m[h] = 1                    
                else: m[h] += 1
                ml[h] = 1
                for i in range(L, len(path)):
                    h = (d*h - q*ord(path[i-L]) + ord(path[i])) % MOD
                    if h in m:
                        if h not in ml:
                            m[h] += 1
                            ml[h] = 1
                    else:
                        m[h] = 1
                        if h not in ml:
                            ml[h] = 1   
            for k in m:
                if m[k] == len(spaths): return True
            return False

            
        while left < right:            
            mid = left + (right - left) // 2
            #print('A', left, right, mid)
            if commonPath(mid): left = mid + 1
            else: right = mid
            #print('B', left, right, mid)
        #print(left, right, mid)
        return left-1 if left > 0 else 0

        
if __name__ == "__main__":
    print(Solution().longestCommonSubpath(n = 5, paths = [[0,1,2,3,4],
                       [2,3,4],
                       [4,0,1,2,3]]))
    print(Solution().longestCommonSubpath(3, [[0],[1],[2]]))
    print(Solution().longestCommonSubpath(n = 5, paths = [[0,1,2,3,4],
                       [4,3,2,1,0]]))
    
    paths = [[340,88,187,280,359,397,300,255,258,201,301,17,245,124,380,206,345,377,191],[224,300,255,258,201,301,17,245,124,380,206,339,260,55,398,83,266,201,189],[375,15,240,22,157,360,314,300,255,258,201,301,17,245,124,380,206,303,296],[331,87,86,257,116,6,300,255,258,201,301,17,245,124,380,206,394,102,276],[118,207,263,176,295,180,235,137,300,255,258,201,301,17,245,124,380,206,337]]
    print(Solution().longestCommonSubpath(405, paths))
    paths = [[0,1,0,1,0,1,0,1,0,1,0,1],
             [0,1,2,0,1,2,0,1,2]]
    print(Solution().longestCommonSubpath(3, paths))