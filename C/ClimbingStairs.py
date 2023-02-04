class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        else:            
            f0 = 1
            f1 = 2
            i = 2
            while i < n:
                f =  f0 + f1
                f0 = f1
                f1 = f 
                i += 1
            return f
            
if __name__ == "__main__":
    print(Solution().climbStairs(5))