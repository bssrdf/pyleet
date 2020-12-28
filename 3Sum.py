"""
Given an array S of n integers, are there elements a, b, c in S such that 
a + b + c = 0? Find all unique triplets in the
array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
__author__ = 'Danyang'

from collections import defaultdict

class Solution:
    #def threeSum_duplicate(self, num):
    def threeSum(self, num):
        """
        Hash
        O(n^2)
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """
        d1 = defaultdict(list)      
        for i, n in enumerate(num):
            d1[n].append(i)        
        res = []
        for i, n in enumerate(num):
            target = -1*n
            for j, m in enumerate(num):
                if (target - m) in d1:
                    #if len(d1[target-m]) == 1:
                    if d1[target-m][0] != j and j != i and d1[target-m][0] != i:
                        c=[n, m, target-m]
                        #print target, c
                        c.sort()
                        if c not in res:
                            res.append(c)
                    
        return res


if __name__ == "__main__":
    #print Solution().threeSum([-1, 0, 1, 2, 3, -4])
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
