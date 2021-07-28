'''
-Medium-

For some fixed n, an array nums is beautiful if it is a permutation of the 
integers 1, 2, ..., n, such that:

For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].

Given n, return any beautiful array nums.  (It is guaranteed that one exists.)

 

Example 1:

Input: n = 4
Output: [2,1,4,3]
Example 2:

Input: n = 5
Output: [3,1,2,5,4]
 

Note:

1 <= n <= 1000


'''

class Solution(object):
    def beautifulArrayWrong(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def helper(l, r):
            if l == r: return [l]
            mid = l + (r-l)//2
            left = helper(l, mid)
            right = helper(mid+1, r)
            return left[::-1]+right[::-1]
        return helper(1,n)
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [1]
        while len(res) < n:
            t = []
            for i in res:
                if 2*i-1 <= n:
                    t.append(2*i-1)
            for i in res:
                if 2*i <= n:
                    t.append(2*i)
            res = t
        return res
        

if __name__ == "__main__":
    print(Solution().beautifulArray(6))