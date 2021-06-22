'''
-Medium-
*DFS*

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]


'''

class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """
    def getFactorsMLE(self, n):
        # write your code here
        # MLE
        res = [] 
        def dfs(i, start, path):
            if i == 1: 
                if len(path) > 1:
                    res.append(path[:])
                return
            for j in range(start, i+1):
                if i % j == 0:
                    dfs(i//j, j, path+[j])
        dfs(n, 2, [])
        return res

    #def __init__(self):
    #    self.factors = dict()

    def getFactors(self, n):
        # write your code here
        if n == 1:
            return []
        #elif n in self.factors:
        #    return self.factors[n]
        else:
            res = list()
            for f in range(2, int(n**(0.5)) + 1):
                if n % f == 0:
                    residue = n // f
                    res.append([f, residue])
                    for l in self.getFactors(residue):
                        if l[0] >= f:
                            res.append([f] + l)
            return res
      


if __name__ == "__main__":
    print(Solution().getFactors(37))
    print(Solution().getFactors(12))
    print(Solution().getFactors(23848713))