'''

-Medium-

You are given two positive integers n and target.

An integer is considered beautiful if the sum of its digits is less than or equal to target.

Return the minimum non-negative integer x such that n + x is beautiful. The input will be generated such that it is always possible to make n beautiful.

 

Example 1:

Input: n = 16, target = 6
Output: 4
Explanation: Initially n is 16 and its digit sum is 1 + 6 = 7. After adding 4, n becomes 20 and digit sum becomes 2 + 0 = 2. It can be shown that we can not make n beautiful with adding non-negative integer less than 4.
Example 2:

Input: n = 467, target = 6
Output: 33
Explanation: Initially n is 467 and its digit sum is 4 + 6 + 7 = 17. After adding 33, n becomes 500 and digit sum becomes 5 + 0 + 0 = 5. It can be shown that we can not make n beautiful with adding non-negative integer less than 33.
Example 3:

Input: n = 1, target = 1
Output: 0
Explanation: Initially n is 1 and its digit sum is 1, which is already smaller than or equal to target.
 

Constraints:

1 <= n <= 1012
1 <= target <= 150
The input will be generated such that it is always possible to make n beautiful.



'''



class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def helper(n):
            digits = list(str(n))
            i, sm = 0, 0
            while i < len(digits):
                sm += int(digits[i])
                if sm > target:
                    break
                i += 1
            if i == len(digits):
                return n
            j, carry, res = i-1, 1, []            
            while j >= 0:
                if int(digits[j]) + carry >= 10:
                    res.append(str(int(digits[j]) + carry - 10))
                    carry = 1                
                else:                
                    res.append(str(int(digits[j]) + carry))
                    carry = 0
                j -= 1    
            if carry:
                res.append('1')
            t = ''.join(res[::-1])+'0'*(len(digits)-i)
            if sum(int(r) for r in res) > target:
                return helper(int(t))
            else:
                return int(t) 
        num = helper(n)
        return num - n
    

    def makeIntegerBeautiful2(self, n: int, target: int) -> int:
        A = []
        t = n
        while t > 0:
            A.append(t % 10)
            t //= 10
        if sum(A) <= target: return 0
        A.append(0)
        ret, p = 0, 1
        for i in range(len(A)-1):
            ret += (10-A[i])*p
            A[i] = 0
            A[i+1] += 1
            p *= 10
            if A[i+1] == 10: continue
            print(ret, A)
            if sum(A) <= target: return ret 
        return ret


if __name__ == "__main__":   
    print(Solution().makeIntegerBeautiful2(n = 467, target = 17))        
    print(Solution().makeIntegerBeautiful(n = 467, target = 6))        
    print(Solution().makeIntegerBeautiful(n = 467, target = 16))        

        
    print(Solution().makeIntegerBeautiful(n = 16, target = 6))        
    print(Solution().makeIntegerBeautiful(n = 1, target = 1))        

    print(Solution().makeIntegerBeautiful(n = 8, target = 2))        
    print(Solution().makeIntegerBeautiful(n = 19, target = 1))        
    print(Solution().makeIntegerBeautiful2(n = 19, target = 1))        
    print(Solution().makeIntegerBeautiful(n = 20, target = 1))        

    # print(Solution().makeIntegerBeautiful2(n = 20, target = 1))        