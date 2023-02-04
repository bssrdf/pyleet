"""
-Easy-

"""

class Solution(object):
    """
    return true if str1 is a subsequence of str2;
    false otherwise
    """ 
    def isSubsequence(self, str1, str2):
        m, n = len(str1), len(str2)
        i, j = 0, 0
        while i < m and j < n:
            if str1[i] == str2[j]: i += 1
            j += 1
        return i == m



if __name__ == "__main__":
    print(Solution().isSubsequence("bade", "abcdebdde"))
    S = "spbmtkwqpftyahhnughzxscpavtqymtbanjyybdlhbphfrycpytsgzoeunvxaxuwbmecthomrjgmbvaoyjxxefmtxaxgwswdjdjlkpzsuirbujvhesfzdklgkulkmfnlofytaszwtxacnffvszmobxwmlhaxporskwzrvgmdpneggxqidqsdgvcprcnkdrxtsktibilbtggpazwuddhrgsmaspelglhausmfnyksdfyrwtpftrgtw"
    T = "asgvamuyus"
    print(Solution().isSubsequence(T,S))

