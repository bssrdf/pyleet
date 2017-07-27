"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""
__author__ = 'Danyang'
class Solution:
    def permute(self, num):
        """
        Catalan
        :param num: a list of integer
        :return: a list of lists of integers
        """
        result = []        
        self.dfs(num, [], result)
        return result
        
    def dfs(self, seq, current, res):        
        if not seq:
            res.append(current)
            return
        #print seq
        for i,v in enumerate(seq):            
            self.dfs(seq[:i]+seq[i+1:], current+[v], res)         
                
   
if __name__=="__main__":
    print Solution().permute([1, 2, 3, 4])
    