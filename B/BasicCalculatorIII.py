'''
-Hard-
*Stack*

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the 
plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / 
operators , open ( and closing parentheses ) and empty spaces . The 
integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate 
results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12

'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)        
        curRes, res = 0, 0
        op = '+'
        num = 0        
        i = 0
        while i < n:
            if ord('0') <= ord(s[i]) <= ord('9'):
                num = 10*num+ord(s[i])-ord('0')                
            elif s[i] == '(':
                j, cnt = i, 0
                while i < n:
                    if s[i] == '(': cnt += 1
                    if s[i] == ')': cnt -= 1
                    if cnt == 0: break
                    i += 1
                num = self.calculate(s[j+1:i])               
                
            if s[i] == '+' or s[i] == '-'  or s[i] == '*' or s[i] == '/' \
                or i == n-1:                
                if op == '+': curRes += num  
                if op == '-': curRes -= num  
                if op == '*': curRes *= num  
                if op == '/':
                    if curRes > 0: 
                        curRes  //= num
                    else:
                        curRes = -((-curRes) // num)
                if s[i] == '+' or s[i] == '-' or i == n-1:
                    res += curRes
                    curRes = 0
                op = s[i]
                num = 0                         
            i += 1 
        
        return res

if __name__ == "__main__":
    #print(Solution().calculate("5+5*2"))
    print(Solution().calculate("2*(5+5*2)/3+(6/2+8)"))
    print(Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))