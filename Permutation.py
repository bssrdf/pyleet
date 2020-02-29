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

    def A_n_k(self, a, n, k, depth, used, curr, ans):
      if depth == k: #end condition
         print curr
         ans.append(curr[:]) # use deepcopy because curr is tracking all partial solution, it eventually become []
         return
 
      for i in range(n):
        if not used[i]:
      # generate the next solution from curr
          curr.append(a[i])
          used[i] = True
      #print(curr)
      # move to the next solution
          self.A_n_k(a, n, k, depth+1, used, curr, ans)
     
      #backtrack to previous partial state
          curr.pop()
      #print('backtrack: ', curr)
          used[i] = False
      return 
                
   
if __name__=="__main__":
    print Solution().permute([1, 2, 3, 4])
    