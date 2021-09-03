'''

-Medium-

A shopkeeper needs to complete a sales task. He arranges the items for sale in a row.
Starting from the left, the shopkeeper subtracts the price of the first lower or the same price 
item on the right side of the item from its full price.
If there is no item to the right that costs less than or equal to the current item's price, the 
current item is sold at full price.
You should return the actual selling price of each item.

The length of Prices is within range: [1, 100000]
Prices[i] is within range: [1, 1000000]
样例
Example 1:

Input:
Prices = [2, 3, 1, 2, 4, 2]
Output: 
[1, 2, 1, 0, 2, 2]
Explanation: 
The item 0 and 1 are each discounted by 1 unit, The item 3 at 2 units, is discounted 2 units, as would the item 4 at 4 units. 
Example 2:

Input:
Prices = [1, 2, 3, 4, 5]
Output:
[1, 2, 3, 4, 5]
Explanation: 
each item should keep full price beacause there are not equal or lower priced items to  the right

'''

class Solution:
    """
    @param prices: a list of integer
    @return: return the actual prices
    """
    def FinalDiscountedPrice(self, prices):
        # write your code here
        stack = []
        n = len(prices)
        rightSmaller = [-1]*n
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                rightSmaller[idx] = prices[i]
            stack.append(i)
        res = prices[:]
        for i, p in enumerate(prices):
            if rightSmaller[i] != -1: res[i] -= rightSmaller[i]                             

        return res



if __name__=="__main__":
    Prices = [2, 3, 1, 2, 4, 2]
    print(Solution().FinalDiscountedPrice(Prices))
    Prices = [1, 2, 3, 4, 5]
    print(Solution().FinalDiscountedPrice(Prices))