'''
-Easy-

Given a matrix, find a element that appear in all the rows in the matrix.You can assume 
that there is only one such element.

样例
Example 1:

Input :
[
  [2,5,3],
  [3,2,1],
  [1,3,5]
]
Output : 3

'''

class Solution:
    """
    @param Matrix: the input
    @return: the element which appears every row
    """
    def FindElements(self, Matrix):
        # write your code here
        m = {}        
        for i in range(len(Matrix)):
            for j in range(len(Matrix[0])):
                if Matrix[i][j] not in m:
                    m[Matrix[i][j]] = 1<<i
                else:
                    m[Matrix[i][j]] |= 1<<i
               
        ans = 0
        mask = int('1'*len(Matrix),2)        
        for i in m:
            if m[i] & mask == mask:
                ans = i
                break
        return ans 


if __name__=="__main__":
    print(Solution().FindElements([[1,2,3,4],[4,5,6,7],[2,2,1,4],[4,4,3,9]]))