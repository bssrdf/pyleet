'''
-Medium-
*Binary Search*

Given a matrix mat where every row is sorted in increasing order, return the 
smallest common element in all rows.

If there is no common element, return -1.

 

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
 

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in increasing order.


'''

class Solution(object):
    def smallestCommonElement(self, mat): 
        m, n = len(mat), len(mat[0])
        indices = [0]*m
        curNum = 0
        count = 0
        while True:
            for i in range(m):
                curNum = max(curNum, mat[i][indices[i]])
            count = 0
            for i in range(m):
                if mat[i][indices[i]] == curNum:
                    count += 1
                elif mat[i][indices[i]] < curNum:
                    indices[i] += 1
                    if indices[i] >= n:
                        return -1
            if count == m:
                return curNum

    def smallestCommonElement2(self, mat): 
        m, n = len(mat), len(mat[0])
        def search(A, x):
            l, r = 0, n  
            while l < r:
                mid = l + (r-l)//2
                if A[mid] == x:
                    return True
                elif A[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return False

        for num in mat[0]:
            found = True
            for i in range(1,m):
                if not search(mat[i], num):
                    found = False
                    break
            if found: return num
        return -1





if __name__ == "__main__":
    matrix = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
    print(Solution().smallestCommonElement(matrix))
    print(Solution().smallestCommonElement2(matrix))