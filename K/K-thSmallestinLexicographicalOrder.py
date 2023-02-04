'''
-Hard-

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109


'''


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:        
        cur, k = 1, k-1
        def calSteps(n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n+1, n2) - n1
                n1 *= 10
                n2 *= 10
            return steps
        while k > 0:
            steps = calSteps(cur, cur+1)
            # print(k, steps, cur)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur

if __name__ == "__main__":
    print(Solution().findKthNumber(n = 13, k = 2))
    print(Solution().findKthNumber(n = 103, k = 10))
        