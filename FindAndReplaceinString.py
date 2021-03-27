'''
-Medium-


'''

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res = ''
        t = sorted(zip(indexes, sources, targets), key = lambda x: x[0])
        indexes = [x[0] for x in t]
        sources = [x[1] for x in t]
        targets = [x[2] for x in t]
        start, i = 0, 0 
        while start < len(S):            
            if i < len(sources) and start == indexes[i]:
                end = start+len(sources[i])
                if S[start:end] == sources[i]:                                
                    res += targets[i]
                else:
                    res += S[start:end]
                start = end    
                i += 1
            else:
                res += S[start]
                start += 1
        return res
if __name__ == "__main__":
    print(Solution().findReplaceString(S = "abcd", indexes = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]))
    print(Solution().findReplaceString(S = "abcd", indexes = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]))
    print(Solution().findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"],["s","so","bfr"]))