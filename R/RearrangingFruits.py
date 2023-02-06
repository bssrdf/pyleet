'''
-Hard-

You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is min(basket1[i],basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return the minimum cost to make both the baskets equal or -1 if impossible.

 

Example 1:

Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
Output: 1
Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
Example 2:

Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
Output: -1
Explanation: It can be shown that it is impossible to make both the baskets equal.
 

Constraints:

basket1.length == bakste2.length
1 <= basket1.length <= 105
1 <= basket1[i],basket2[i] <= 109


'''

from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Wrong
        cnt1, cnt2 = Counter(basket1), Counter(basket2)
        cnt = cnt1 + cnt2
        for c in cnt:
            if cnt[c] % 2: return -1
        arr1 = sorted(cnt1)
        arr2 = sorted(cnt2)
        # arr  = sorted(cnt.items())
        # i1, j1 = 0, len(arr1)-1
        # i2, j2 = 0, len(arr2)-1
        ans = 0
        i, j = 0, len(arr2)-1
        while i < len(arr1) and j >= 0:
            while i < len(arr1) and cnt1[arr1[i]] <= cnt2[arr1[i]]:
                i += 1
            if i == len(arr1): break
            mov = (cnt1[arr1[i]] - cnt2[arr1[i]]) // 2
            while j >= 0 and cnt1[arr2[j]] >= cnt2[arr2[j]]:
                j -= 1
            if j == -1: break
            mov1 = (cnt2[arr2[j]] - cnt1[arr2[j]]) // 2
            
            x = min(arr1[i], arr2[j])
            print(i,j,mov, mov1, arr1[i], arr2[j],x)
            print('A', cnt1, cnt2)
            if mov <= mov1:
                ans += mov * x                                  
                cnt2[arr2[j]] -= mov
                cnt1[arr2[j]] += mov
                cnt1[arr1[i]] -= mov
                cnt2[arr1[i]] += mov
                i += 1
                if mov == mov1: 
                    j -= 1
            else:
                ans += mov1 * x                   
                cnt1[arr1[i]] -= mov1
                cnt2[arr1[i]] += mov1
                cnt2[arr2[j]] -= mov1
                cnt1[arr2[j]] += mov1
                j -= 1
            print('B', ans, cnt1, cnt2)
        print(i,j,ans)
        print(cnt1, cnt2)        
        return ans
    
    def minCost2(self, basket1: List[int], basket2: List[int]) -> int:
        # Wrong
        cnt1, cnt2 = Counter(basket1), Counter(basket2)
        cnt = cnt1 + cnt2
        for c in cnt:
            if cnt[c] % 2: return -1
        mi = min(min(basket1), min(basket2))
        # arr1 = sorted(cnt1)
        # arr2 = sorted(cnt2)
        ans = 0
        for a in cnt:
            if a != mi:
                ans += mi * abs(cnt1[a] - cnt2[a])//2
        return ans 
    
    def minCost3(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter(basket1)
        for x in basket2: cnt[x] -= 1
        last = []
        for k, v in cnt.items():
            # if v is odd, an even distribution is never possible
            if v % 2 != 0:
                return -1
            # the count of transferred k is |v|/2
            last += [k] * abs(v // 2)
        # find the min of two input arrays as the intermediate
        minx = min(basket1 + basket2)
        # Use quickselect instead of sort can get a better complexity
        last.sort()
        # The first half may be the cost
        return sum(min(2*minx, x) for x in last[0:len(last)//2])






if __name__ == '__main__':
    print(Solution().minCost2(basket1 = [4,2,2,2], basket2 = [1,4,1,2]))
    print(Solution().minCost2(basket1 = [2,3,4,1], basket2 = [3,2,5,1]))
    print(Solution().minCost2(basket1 = [5,8,15,7], basket2 = [5,7,8,15]))
    print(Solution().minCost2(basket1 = [84,80,43,8,80,88,43,14,100,88],    
                             basket2 = [32,32,42,68,68,100,42,84,14,8]))
    print(Solution().minCost2(basket1 = [4,4,4,4,3], basket2 =[5,5,5,5,3]))
            