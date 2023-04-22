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
    
    def lexicalOrder2(self, n):
        # 研究序列[1,10,11,12,13,2,3,4,5,6,7,8,9]，找出字典序的规律。

        # 规律1：不考虑上限，元素1后面跟什么元素？10, 100 … 也就是不断乘以10。

        # 规律2：如果99是上限，那么10后面的元素不能是100了，该怎么办？答案是11，也就是加1，
        # 这样个位上的数变大了。如果加1导致进位的话，虽然个位数变0，但十位上的数会变大，
        # 总之肯定字典序往后移。但此时得到的并不是下一个的目标，因为把其末尾的0去掉会得到
        # 字典序相对更前的数。砍掉0之后就可以重复规律1的操作了。

        # 规律3：如果上限是19，那么19后面的元素就不能是20了，该怎么办？答案是将19除以10，
        # 然后再重复规律2（也就是加1），也就是得到2，之后又可以重复规律1了。
        cur = 1
        res = [0]*n
        for i in range(n):
            res[i] = cur
            if cur*10 <= n: 
                cur *= 10
            else:
                if cur + 1 > n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0:
                    cur //= 10    
        return res            


if __name__ == "__main__":
    print(Solution().lexicalOrder(113))

    

