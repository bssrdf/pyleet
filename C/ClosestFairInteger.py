'''

-Medium-


You are given a positive integer n.

We call an integer k fair if the number of even digits in k is equal to the number of odd digits in it.

Return the smallest fair integer that is greater than or equal to n.

 

Example 1:

Input: n = 2
Output: 10
Explanation: The smallest fair integer that is greater than or equal to 2 is 10.
10 is fair because it has an equal number of even and odd digits (one odd digit and one even digit).
Example 2:

Input: n = 403
Output: 1001
Explanation: The smallest fair integer that is greater than or equal to 403 is 1001.
1001 is fair because it has an equal number of even and odd digits (two odd digits and two even digits).
 

Constraints:

1 <= n <= 109

'''

class Solution:
    def closestFair(self, n: int) -> int:
        #wrong
        s = str(n)
        if len(s) == 1: return 10
        if len(s) % 2 == 1:
            return int('1'+'0'*((len(s)+1)//2)+'1'*(len(s) - (len(s)+1)//2))
        odd, even = 0, 0
        for c in s:
            if int(c) % 2 == 0:
                even += 1
            else:
                odd += 1    
        def get(less, more, b):            
            t = []
            for c in s[::-1]:
                if less < more and int(c) % 2 == b:
                    t.append(str(int(c)+1))
                    less += 1
                    more -= 1
                else:
                    t.append(c)
            return int(''.join(t[::-1])) 
        print(odd, even)
        if odd == even: return n
        elif odd < even:
            return get(odd, even, 0)
        else:
            return get(even, odd, 1)
    

    def closestFair2(self, n: int) -> int:
        a = b = k = 0
        t = n
        while t:
            if (t % 10) & 1:
                a += 1
            else:
                b += 1
            t //= 10
            k += 1
        # print(k, n)
        if k & 1:
            x = 10**k
            y = int('1' * (k >> 1) or '0')
            return x + y
        if a == b:
            return n
        return self.closestFair2(n + 1)


if __name__ == '__main__':
    # print(Solution().closestFair(403))
    # print(Solution().closestFair(4033))
    # print(Solution().closestFair2(4033))
    # print(Solution().closestFair(1111))
    # print(Solution().closestFair2(1111))
    # print(Solution().closestFair(324901))
    # print(Solution().closestFair(317901))
    print(Solution().closestFair2(317901))
    print(Solution().closestFair2(42457911))
