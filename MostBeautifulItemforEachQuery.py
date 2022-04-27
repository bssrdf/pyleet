'''

-Medium-
*Sorting*
*Binary Search*
*DP*

You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

 

Example 1:

Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]
Explanation:
- For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
  The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
  The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
  Hence, the answer for them is the maximum beauty of all items, i.e., 6.
Example 2:

Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
Output: [4]
Explanation: 
The price of every item is equal to 1, so we choose the item with the maximum beauty 4. 
Note that multiple items can have the same price and/or beauty.  
Example 3:

Input: items = [[10,1000]], queries = [5]
Output: [0]
Explanation:
No item has a price less than or equal to 5, so no item can be chosen.
Hence, the answer to the query is 0.
 

Constraints:

1 <= items.length, queries.length <= 105
items[i].length == 2
1 <= pricei, beautyi, queries[j] <= 109


'''

from typing import List
import bisect
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n, MAX = len(items), 10**9+1
        items.sort()
        A, minb = [0]*n, 0
        for i, (_, b) in enumerate(items):
            if minb < b:
                minb = b
            A[i] = minb
        ans = []
        for q in queries:
            idx = bisect.bisect_right(items, [q, MAX])
            if idx > 0:
                ans.append(A[idx-1])
            else:
                ans.append(0)
        return ans 
    
    def maximumBeauty2(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        items.sort()
        A, minb = [0]*n, 0
        for i, (_, b) in enumerate(items):
            if minb < b:
                minb = b
            A[i] = minb
        ans = [0]*len(queries)
        m = []
        for i in range(len(queries)):
            m.append((queries[i], i))
        m.sort(reverse = True)
        for q,i in m:
            while items and items[-1][0] > q:
                items.pop()
                A.pop()
            if A:            
                ans[i] = A[-1]
        return ans 



             





if __name__ == "__main__":
    items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
    queries = [1,2,3,4,5,6]
    # print(Solution().maximumBeauty(items, queries))
    # items = [[1,2],[1,2],[1,3],[1,4]]; queries = [1]
    # print(Solution().maximumBeauty(items, queries))
    items = [[10,1000]]; queries = [5]
    print(Solution().maximumBeauty(items, queries))
    print(Solution().maximumBeauty2(items, queries))
    # items = [[1,1],[1,1000000000],[1,1000000000]]; queries = [1000000000]
    # print(Solution().maximumBeauty(items, queries))
    items = [[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]]
    queries =[885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]
    print(Solution().maximumBeauty(items, queries))
    print(Solution().maximumBeauty2(items, queries))
        