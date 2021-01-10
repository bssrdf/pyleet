'''
-Medium-

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size 
may be as large as 5,000,000.

'''

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]        
        """
        '''
        The general idea is to perform a DFS search for numbers <= n
        in a specific lexicographical order: so start with 1, 10, 100... 
        and then 2, 20, 200.. etc. 

        '''
        res = []
        def helper(cur):
            if cur > n: return
            res.append(cur)
            for i in range(10):
                if cur*10+i <= n:
                    # go deeper (or larger number)
                    helper(cur*10+i)
                else:
                    break
        for i in range(1,10): # ordered as 1..9
            helper(i)
        return res


if __name__ == "__main__":
    print(Solution().lexicalOrder(113))

    

