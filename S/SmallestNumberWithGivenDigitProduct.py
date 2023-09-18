'''

-Medium-

$$$


Given a positive integer n, return a string representing the smallest positive integer such that the product of its digits is equal to n, or "-1" if no such number exists.

 

Example 1:

Input: n = 105
Output: "357"
Explanation: 3 * 5 * 7 = 105. It can be shown that 357 is the smallest number with a product of digits equal to 105. So the answer would be "105".
Example 2:

Input: n = 7
Output: "7"
Explanation: Since 7 has only one digit, its product of digits would be 7. We will show that 7 is the smallest number with a product of digits equal to 7. Since the product of numbers 1 to 6 is 1 to 6 respectively, so "7" would be the answer.
Example 3:

Input: n = 44
Output: "-1"
Explanation: It can be shown that there is no number such that its product of digits is equal to 44. So the answer would be "-1".
 

Constraints:

1 <= n <= 1018






'''

class Solution:
    def smallestNumber(self, n: int) -> str:
        inf = str(10**18)
        if n < 10: return str(n)
        def helper(cur):
            # print(cur)
            if cur == 1:
                return ""
            ret = inf
            for i in range(2, 10):
                if cur % i == 0:
                    nxt = helper(cur//i)
                    # if nxt != 'aaa':
                    ret = min(ret, str(i)+nxt, key=int)
            return ret
        ans = helper(n)
        return "-1" if ans == inf else ans    

    def smallestNumber2(self, n: int) -> str:   
        cnt = [0] * 10
        for i in range(9, 1, -1):
            while n % i == 0:
                n //= i
                cnt[i] += 1
        if n > 1:
            return "-1"
        ans = "".join(str(i) * cnt[i] for i in range(2, 10))
        return ans if ans else "1"  
                              
import random

if __name__ == "__main__":
    print(Solution().smallestNumber(n=105))
    print(Solution().smallestNumber(n=7))
    print(Solution().smallestNumber(n=44))
    print(Solution().smallestNumber(n=378))
    N = 10000
    for _ in range(N):
        n = random.randint(1, 10**18)
        s1 = Solution().smallestNumber(n)
        s2 = Solution().smallestNumber2(n)
        # if s1 != s2:
        if s1 != '-1':
            print(n, s1, s2)

