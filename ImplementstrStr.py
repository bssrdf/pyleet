'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Subscribe to see which companies asked this question
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            find = True
            for j in range(len(needle)):
                #print i, j, haystack[i+j], needle[j]
                if haystack[i+j] != needle[j]:
                    find = False
                    break
            if find:
                return i
        return -1




if __name__ == "__main__":
    #assert Solution().strStr("abcdefg", "ab") == 0
    #assert Solution().strStr("abcdefg", "bc") == 1
    #assert Solution().strStr("abcdefg", "cd") == 2
    assert Solution().strStr("abcdefg", "fg") == 5
    #assert Solution().strStr("abcdefg", "bcf") == -1
    assert Solution().strStr("a", "a") == 0
