'''
-Medium-
*Backtracking*

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two 
numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 
is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
 

Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?



'''

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        out = []
        def helper(num, start, out):
            #if self.res: return
            print(start, out)
            if start >= len(num) and len(out) >= 3:
                return True
            for i in range(start, len(num)):
                cur = num[start:i+1]
                if len(cur) > 1 and cur[0] == '0': break
                t = int(cur)
                length = len(out)
                #if t > INT_MAX: break
                if length >= 2 and t != out[length - 1] + out[length - 2]: continue
                out.append(t)
                if helper(num, i + 1, out):
                    return True
                out.pop()
            return False    
        return helper(num, 0, out)
    
if __name__ == "__main__":  
    #print(Solution().isAdditiveNumber("199100199"))
    #print(Solution().isAdditiveNumber("221474836472147483649"))
    print(Solution().isAdditiveNumber("11111111111011111111111"))