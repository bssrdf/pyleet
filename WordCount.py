class Solution(object):
    def count(self, s):
        """
        :type S: str        
        :rtype: int
        """
        i = 0
        n = len(s)
        cnt = 0
        while i < n:           
            isWord = False        
            while i < n and s[i] != ' ':
                isWord = True
                i += 1
            if isWord: cnt += 1
            i += 1
        return cnt


if __name__ == "__main__":
    print(Solution().count("  leet  2  code   3"))
    print(Solution().count("  leet  2  code   3  "))
    print(Solution().count("leet  2  code   3"))
    print(Solution().count("leet2code3"))
    print(Solution().count("leet 2 code 3"))
    print(Solution().count("  "))
    print(Solution().count("leet  2  code   3  55"))
    
