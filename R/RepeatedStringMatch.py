import math
class Solution:
    def repeatedStringMatch(self, a, b):        
        ans = math.ceil(len(b)/len(a))
        c = a*ans        
        if b in c:
           return ans
        if b in c+a:    
            return ans+1
        return -1

if __name__ == "__main__":
    print(Solution().repeatedStringMatch("abcd", "cdabcdab"))
    print(Solution().repeatedStringMatch("a", "aa"))
    print(Solution().repeatedStringMatch("a", "a"))
    print(Solution().repeatedStringMatch("abc", "wxyz"))
    print(Solution().repeatedStringMatch("abc", "cabcabca"))