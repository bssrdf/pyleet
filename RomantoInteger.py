
'''


'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,
            'D':500,  'M':1000}
        m1 = {'V':'I', 'X':'I', 'L':'X', 'C':'X', 'D':'C', 'M':'C'}
        res = 0
        i = len(s)-1
        while i >= 0:
            if s[i] == 'I':
                res += m[s[i]]
                i -= 1
            elif s[i] in 'VXLCDM':
                if i-1 >= 0 and s[i-1] == m1[s[i]]:
                    res += m[s[i]] - m[s[i-1]]
                    i -= 2
                else:
                    res += m[s[i]]
                    i -= 1
            '''
            elif s[i] in 'LC':
                if i-1 >= 0 and s[i-1] in 'X':
                    res += m[s[i]] - m[s[i-1]]
                    i -= 2
                else:
                    res += m[s[i]]
                    i -= 1
            elif s[i] in 'DM':
                if i-1 >= 0 and s[i-1] in 'C':
                    res += m[s[i]] - m[s[i-1]]
                    i -= 2
                else:
                    res += m[s[i]]
                    i -= 1
            '''
        return res
    
if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIV"))
    print(Solution().romanToInt("DCXXI"))
                    