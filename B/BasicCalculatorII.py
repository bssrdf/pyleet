'''
-Medium-
*stack*

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / 
operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)        
        res = 0
        op = '+'
        num = 0
        st = []
        i = 0
        while i < n:
            if ord('0') <= ord(s[i]):
                num = 10*num+ord(s[i])-ord('0')  
            if (ord(s[i]) < ord('0') and s[i] != ' ') or i == n-1:
                if op == '+': st.append(num) 
                if op == '-': st.append(-num) 
                if op == '*' or op == '/':
                    if op == '*':
                        tmp = st[-1] * num  
                    elif st[-1] > 0: 
                        tmp = st[-1] // num
                    else:
                        tmp = -((-st[-1]) // num)
                    st.pop()
                    st.append(tmp)
                op = s[i]
                num = 0                
            i += 1        
        for i in st:     
            res += i    
        return res

if __name__ == "__main__":
    print(Solution().calculate("3+2*2"))
    print(Solution().calculate("14-3/2"))
           