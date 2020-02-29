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
                if len(s) < k:
                    break
                num = int(s[0:k])
                if num > 255 or k != len(str(num)):
                    continue
                self.helper(s[k:], n+1, out+s[0:k]+('' if n==3 else '.'), res)

if __name__=="__main__":
   print(Solution().restoreIpAddresses('25525511135'))


