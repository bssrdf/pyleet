'''
-Medium-

*Greedy*

Given two integers n and k, you need to construct a list which contains n different 
positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, 
|a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, 
and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, 
and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 10^4.


'''

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        i, j = 1, n
        while i <= j: 
            if k > 1: 
                # greedily form a distinct pair by alternating with a small and a big number
                if k % 2 > 0:
                    res.append(i)
                    i += 1
                else:
                    res.append(j)
                    j -= 1
                k -= 1
            else: # once k is 1, form the only difference of 1 with an ascending order
                res.append(i)
                i += 1 
        return res


    def constructArrayTLE(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        visited = [0]*(n+1)
        distinct = {}
        self.res = None
        def dfs(i, path): # i is the position         
            if i > n: 
                if len(distinct.keys()) == k:
                    #print('set:',distinct)
                    self.res = path[:]
                return 
            for j in range(1, n+1): # j is the number put on position i
                if visited[j] == 0:
                    if path:
                     #   print('a', path)
                        d = abs(j-path[-1])
                        distinct[d] = distinct.setdefault(d,0)+1 
                    #if len(distinct.keys()) == k: continue
                    visited[j] = 1 
                    dfs(i+1, path+[j])
                    visited[j] = 0
                    if path:
                      #  print('b', path)
                        if d in distinct:
                           distinct[d] -= 1
                           if distinct[d] == 0:
                               distinct.pop(d)
        dfs(1, [])
        return self.res   

if __name__ == "__main__":
    print(Solution().constructArray(3,2))
    print(Solution().constructArray(10,4))
