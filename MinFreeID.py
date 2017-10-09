"""
"""
import bisect

__author__ = 'Daniel'


class Solution(object):    
    
    def helper(self, ids, l, r):
        if l == r:
            return l
        m = l+(r-l)/2
        left = l
        for right in range(l, r):
            if ids[right] <= m:
                t = ids[left]
                ids[left] = ids[right]
                ids[right] = t
                left += 1
        if left == m+1:
            l = m+1
        else:
            r = m
        return self.helper(ids, l, r)        
    
    def MinFreeID(self, IDs):
        return self.helper(IDs, 0, len(IDs))        
        

if __name__ == "__main__":
    L = [18, 4, 8, 9, 16, 1, 14, 7, 19, 3, 0, 5, 2, 11, 6]
    #L = [10, 4, 8, 9, 1, 7, 3, 0, 5, 2, 11, 6]
    print L
    print Solution().MinFreeID(L)
