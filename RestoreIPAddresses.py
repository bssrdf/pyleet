'''
-Medium-

*DFS*

Given a string s containing only digits, return all possible valid IP 
addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is 
between 0 and 255, separated by single dots and cannot have leading zeros. 
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and 
"0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

0 <= s.length <= 3000
s consists of digits only.

'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.helper(s, 0, '', res)
        return res
    def helper(self, s, n, out, res):
        if n == 4:
            if not s:
                res.append(out)
                return
        else:
            for k in range(1, 4):
                if len(s) < k: break
                num = int(s[0:k])
                # k != len(str(num)) will get rid of cases 
                # which start with 0 (e.g. '01') but allow a single '0' 
                if num > 255 or k != len(str(num)):
                    continue
                self.helper(s[k:], n+1, out+s[0:k]+('' if n==3 else '.'), res)

if __name__=="__main__":
   print(Solution().restoreIpAddresses('25525511135'))
   print(Solution().restoreIpAddresses('255255110135'))
   print(Solution().restoreIpAddresses("101023"))


