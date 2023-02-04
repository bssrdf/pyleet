'''


-Medium-

A good meal is a meal that contains exactly two different food items with a 
sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the 
deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good 
meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they 
have the same deliciousness value.

 

Example 1:

Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and 
(1,7) with 3 ways.
 

Constraints:

1 <= deliciousness.length <= 10^5
0 <= deliciousness[i] <= 2^20

'''

class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        deliciousness.sort()
        n = len(deliciousness)
        def count(d):
            m, cnt = {}, 0
            for i in deliciousness:
                if d-i in m:
                    cnt += m[d-i]
                m[i] = m.setdefault(i,0)+1
            return cnt
        def count2(d):
            dl = deliciousness
            cnt, j, k = 0, 0, n-1 
            while j < k:
                if dl[j] > d: break
                if dl[j] + dl[k] < d : j += 1
                elif dl[j] + dl[k] > d: k -= 1
                else: 
                    l, r = 1, 1
                    while j+l < k and dl[j+l] == dl[j]: l += 1
                    while k-r >= j+l and dl[k-r] == dl[k]: r += 1   
                    cnt += (k-j+1)*(k-j)//2 if dl[k] == dl[j] else l*r
                    j += l
                    k -= r
            return cnt
        k, res = 1, 0
        while k <= max(deliciousness)*2:
            #res = (res+count(k)%MOD)%MOD
            res = (res+count2(k)%MOD)%MOD
            k *= 2
        return res


        
if __name__ == "__main__":
    print(Solution().countPairs([1,3,5,7,9]))