'''
-Medium-
%Amazon*

A customer wants to buy a pair of jeans, a pair of shoes, a skirt, and a 
top but has a limited budget in dollars. Given different pricing options 
for each product, determine how many options our customer has to buy 1 of 
each product. You cannot spend more money than the budgeted amount.

Example
priceOfJeans = [2, 3]
priceOfShoes = [4]
priceOfSkirts = [2, 3]
priceOfTops = [1, 2]
budgeted = 10

The customer must buy shoes for 4 dollars since there is only one option. 
This leaves 6 dollars to spend on the other 3 items. Combinations of 
prices paid for jeans, skirts, and tops respectively that add up to 6 dollars 
or less are [2, 2, 2], [2, 2, 1], [3, 2, 1], [2, 3, 1]. There are 4 ways 
the customer can purchase all 4 items.

Function Description

Complete the getNumberOfOptions function in the editor below. The function must 
return an integer which represents the number of options present to buy 
the four items.

getNumberOfOptions has 5 parameters:
int[] priceOfJeans: An integer array, which contains the prices of the pairs of jeans available.
int[] priceOfShoes: An integer array, which contains the prices of the pairs of shoes available.
int[] priceOfSkirts: An integer array, which contains the prices of the skirts available.
int[] priceOfTops: An integer array, which contains the prices of the tops available.
int dollars: the total number of dollars available to shop with.

Constraints

1 ≤ a, b, c, d ≤ 10^3
1 ≤ dollars ≤ 10^9
1 ≤ price of each item ≤ 10^9
Note: a, b, c and d are the sizes of the four price arrays

'''
from collections import defaultdict
class Solution(object):
    def getNumberOfOptions(self, priceOfJeans, priceOfShoes,
             priceOfSkirts, priceOfTops, dollars):
        p1 = [p+q for p in priceOfJeans for q in priceOfShoes]
        print(p1)
        p2 = [p+q for p in priceOfSkirts for q in priceOfTops]
        print(p2)
        m = defaultdict(int)
        res = 0
        for p in p1:
            m[p] += 1
        
        for p in p2:
            if dollars - p in m:
                res += m[dollars-p]

        return res

    def getNumberOfOptions2(self, priceOfJeans, priceOfShoes,
             priceOfSkirts, priceOfTops, dollars):
        dp = [0 for _ in range(dollars + 1)] # you can trim this too, looking at max/min pairs, but unnecessary.
        count = 0

        for a in priceOfJeans:
            for b in priceOfShoes:
                if 0 <= a + b <= dollars:
                    dp[a+b] += 1

        for i in range(1, dollars+1):
            dp[i] += dp[i-1]
            
        for c in priceOfSkirts:
            for d in priceOfTops:
                if 0 <= dollars - (c + d) <= dollars:
                    count += dp[dollars - (c + d)]
                
        return count

if __name__ == "__main__":
    print(Solution().getNumberOfOptions2([2, 3], [4], [2, 3], [1, 2], 10))