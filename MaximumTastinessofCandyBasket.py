'''

-Medium-
*Binary Search*
*Sorting*
You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

Return the maximum tastiness of a candy basket.

 

Example 1:

Input: price = [13,5,1,8,21,2], k = 3
Output: 8
Explanation: Choose the candies with the prices [13,5,21].
The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
It can be proven that 8 is the maximum tastiness that can be achieved.
Example 2:

Input: price = [1,3,1], k = 2
Output: 2
Explanation: Choose the candies with the prices [1,3].
The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
It can be proven that 2 is the maximum tastiness that can be achieved.
Example 3:

Input: price = [7,7,7,7], k = 2
Output: 0
Explanation: Choosing any two distinct candies from the candies we have will result in a tastiness of 0.
 

Constraints:

2 <= k <= price.length <= 105
1 <= price[i] <= 109


'''

from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        P = price
        P.sort()
        left, right = 0, P[-1] - P[0] + 1
        def possible(m):
            cnt, j = 1, 0
            for i in range(1, len(P)):
                if P[i] - P[j] >= m:
                    cnt += 1
                    j = i
            return cnt >= k

        while left < right:
            mid = left + (right-left)//2
            if possible(mid):
                left = mid + 1
            else:
                right = mid
        return left-1





if __name__ == "__main__":
    print(Solution().maximumTastiness(price = [13,5,1,8,21,2], k = 3))
    print(Solution().maximumTastiness(price = [1,3,1], k = 2))
    print(Solution().maximumTastiness(price = [7,7,7,7], k = 2))