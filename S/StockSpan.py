'''
The stock span problem is a financial problem where we have a series of n 
daily price quotes for a stock and we need to calculate span of stock’s 
price for all n days. 

The span Si of the stock’s price on a given day i is defined as the maximum 
number of consecutive days just before the given day, for which the price 
of the stock on the current day is less than or equal to its price on the 
given day.

For example, if an array of 7 days prices is given as {100, 80, 60, 70, 
60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 
2, 1, 4, 6}


我们还可以使用栈来做，里面放一个 pair 对儿，分别是当前的股价和之前比其小的连续天数。
在 next 函数中，使用一个 cnt 变量，初始化为1。还是要个 while 循环，其实核心的本质
都是一样的，循环的条件首先是栈不能为空，并且栈顶元素的股价小于等于当前股价，那么 cnt 
就加上栈顶元素的连续天数，可以感受到跟上面解法在这里的些许不同之处了吧，之前是一直找到
第一个大于当前股价的天数在数组中的位置，然后相减得到连续天数，这里是在找的过程中直接
累加连续天数，最终都可以得到正确的结果，参见代码如下：


'''

class Solution(object):
    def span(self, prices):        
        st = []
        res = []
        for i in prices:
            cnt = 1
            while st and st[-1][0] <= i:
                if i == 85:
                    print(st)
                cnt += st[-1][1]
                st.pop()
            st.append((i, cnt))
            res.append(cnt)
        return res


print(Solution().span([100, 80, 60, 70, 60, 75, 85]))

