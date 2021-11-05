'''
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 10^7


'''
import math

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        s = set()
        while True:
            a = (int)(math.log(n) / math.log(3))
            print('a: ', a)
            if a in s: return False
            s.add(a)
            n -= 3**a
            if n == 0 : return True  

    def checkPowersOfThree2(self, n: int) -> bool:
        T = n
        arr = [3^i for i in range(16)]            # [1,3,9,27,81,243,729...]                

        def dfs(idx, T):
            if (T < 0):        return False          
            if (T == 0):       return True        

            for i in range(idx,len(arr)):
                a = dfs(i+1, T-arr[i])

                if (a==True):   return a             
                if (a==False):  break              
                else:           continue             
        a = dfs(0, T)
        if a: return True
        else: return False

    def checkPowersOfThree3(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            else:
                n //= 3
        return True


if __name__ == "__main__":
    print(Solution().checkPowersOfThree(27))
    print(Solution().checkPowersOfThree(6574365))
    print(Solution().checkPowersOfThree2(27))
    print(Solution().checkPowersOfThree2(6574365))
    print(Solution().checkPowersOfThree3(27))
    print(Solution().checkPowersOfThree3(6574365))    

