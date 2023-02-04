'''
-Hard-

Given a string num that contains only digits and an integer target, return all possibilities 
to add the binary operators '+', '-', or '*' between the digits of num so that the resultant 
expression evaluates to the target value.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
 

Constraints:

1 <= num.length <= 10
num consists of only digits.
-2^31 <= target <= 2^31 - 1

'''

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        def helper(num, diff, curNum, out):
            if len(num) == 0 and curNum == target:
                res.append(out)
                return
            for i in range(1, len(num)+1):
                cur = num[:i]                
                if len(cur) > 1 and cur[0] == '0': return
                nxt = num[i:]
              #  if num == '23': print(i, cur, nxt, len(out))
                if len(out) > 0:
                    helper(nxt, int(cur), curNum + int(cur), out + "+" + cur)
                    helper(nxt, -int(cur), curNum - int(cur), out + "-" + cur)
                    helper(nxt, diff * int(cur), (curNum - diff) + diff * int(cur), out + "*" + cur)
                else:
                    helper(nxt, int(cur), int(cur), cur)
        helper(num, 0, 0, "")
        return res
    
        
if __name__ == "__main__":
    print(Solution().addOperators(num = "123", target = 6))
    print(Solution().addOperators(num = "123", target = 123))
    print(Solution().addOperators(num = "000", target = 0))