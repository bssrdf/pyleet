'''
-Easy-



'''


class Solution:
    def finalString(self, s: str) -> str:
        sr = ''.join(reversed(s))
        def helper(s):
            if not s: return ""
            rev, i = 0, 0
            ret = ''
            while i < len(s) and s[i] != 'i':
                ret += s[i]
                i += 1                
            while i < len(s) and s[i] == 'i':                
                rev = 1 - rev
                i += 1
            res = helper(s[i:])    
            return ret + ''.join(reversed(res)) if rev else ret + res
        ans = helper(sr)              
        return ''.join(reversed(ans))
    





        
    
if __name__ == "__main__":
    print(Solution().finalString(s = "string"))
    print(Solution().finalString(s = "poiinter"))
    print(Solution().finalString(s = "viwif"))