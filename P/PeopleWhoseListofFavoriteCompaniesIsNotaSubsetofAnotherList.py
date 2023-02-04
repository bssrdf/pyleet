'''
-Medium-
*Bit Mask*
Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites 
companies for the ith person (indexed from 0).

Return the indices of people whose list of favorite companies is not a subset of any 
other list of favorites companies. You must return the indices in increasing order.

 

Example 1:

Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
Output: [0,1,4] 
Explanation: 
Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].
Example 2:

Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
Output: [0,1] 
Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].
Example 3:

Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
Output: [0,1,2,3]
 

Constraints:

1 <= favoriteCompanies.length <= 100
1 <= favoriteCompanies[i].length <= 500
1 <= favoriteCompanies[i][j].length <= 20
All strings in favoriteCompanies[i] are distinct.
All lists of favorite companies are distinct, that is, If we sort alphabetically each list then favoriteCompanies[i] != favoriteCompanies[j].
All strings consist of lowercase English letters only.


'''
from typing import List
from collections import defaultdict

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        A = favoriteCompanies
        n = len(A)
        res = []
        for i in range(n):
            isSub = False
            for j in range(n):
                if i != j and len(A[i]) <= len(A[j]) and set(A[i]) <= set(A[j]):
                    isSub = True
                    break
            if not isSub:                    
                res.append(i)
        return res
    
    def peopleIndexes2(self, favoriteCompanies: List[List[str]]) -> List[int]:
        A = favoriteCompanies
        for a in A:
            a.sort()
        n = len(A)
        res = []
        def isSubset(a, b):
            if len(a) > len(b): return False
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)
        for i in range(n):
            isSub = False
            for j in range(n):
                if i != j and isSubset(A[i], A[j]):
                    isSub = True
                    break
            if not isSub:                    
                res.append(i)
        return res
    
    def peopleIndexes3(self, favoriteCompanies: List[List[str]]) -> List[int]:
        A = favoriteCompanies
        m, res = defaultdict(int), []
        n, idx = len(A), 1
        for a in A:
            for c in a:
                if c in m: continue
                m[c] = idx
                idx += 1
        vec = [] 
        for a in A:
            bit = 0
            for c in a:
                bit |= 1 << m[c]
            vec.append(bit)

        for i in range(n):
            isSub = False
            for j in range(n):
                if i == j: continue
                if vec[i] & vec[j] == vec[i]:
                    isSub = True
                    break
            if not isSub:                    
                res.append(i)
        return res
            
        

    

if __name__ == "__main__":   
    favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
    print(Solution().peopleIndexes(favoriteCompanies))
    print(Solution().peopleIndexes3(favoriteCompanies))
        