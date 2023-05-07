'''

-Medium-
*Counting*

There is a 0-indexed array nums of length n. Initially, all elements are uncolored (has a value of 0).

You are given a 2D integer array queries where queries[i] = [indexi, colori].

For each query, you color the index indexi with the color colori in the array nums.

Return an array answer of the same length as queries where answer[i] is the number of adjacent elements with the same color after the ith query.

More formally, answer[i] is the number of indices j, such that 0 <= j < n - 1 and nums[j] == nums[j + 1] and nums[j] != 0 after the ith query.

 

Example 1:

Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
Output: [0,1,1,0,2]
Explanation: Initially array nums = [0,0,0,0], where 0 denotes uncolored elements of the array.
- After the 1st query nums = [2,0,0,0]. The count of adjacent elements with the same color is 0.
- After the 2nd query nums = [2,2,0,0]. The count of adjacent elements with the same color is 1.
- After the 3rd query nums = [2,2,0,1]. The count of adjacent elements with the same color is 1.
- After the 4th query nums = [2,1,0,1]. The count of adjacent elements with the same color is 0.
- After the 5th query nums = [2,1,1,1]. The count of adjacent elements with the same color is 2.
Example 2:

Input: n = 1, queries = [[0,100000]]
Output: [0]
Explanation: Initially array nums = [0], where 0 denotes uncolored elements of the array.
- After the 1st query nums = [100000]. The count of adjacent elements with the same color is 0.
 

Constraints:

1 <= n <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= indexi <= n - 1
1 <=  colori <= 105


'''

from typing import List

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        cnt, ans, arr = 0, [0]*len(queries), [0]*n
        for i in range(len(queries)):
            j, k = queries[i]
            if k == arr[j]:
                ans[i] = cnt 
                continue
            if arr[j] == 0:
                arr[j] = k 
                if j > 0 and arr[j-1] == arr[j]:
                    cnt += 1
                if j < n-1 and arr[j+1] == arr[j]:
                    cnt += 1
            else:    
                if j > 0: 
                    if arr[j-1] == arr[j]:
                        cnt -= 1
                    elif arr[j-1] == k:
                        cnt += 1
                if j < n-1:
                    if arr[j+1] == arr[j]:
                        cnt -= 1
                    elif arr[j+1] == k:
                        cnt += 1
                arr[j] = k    
            ans[i] = cnt
        return ans    
    
    def colorTheArray2(self, n: int, queries: List[List[int]]) -> List[int]:
        cnt, ans, arr = 0, [0]*len(queries), [-1]+[0]*n+[-1]
        for i in range(len(queries)):
            j, k = queries[i]
            j += 1
            if k == arr[j]:
                ans[i] = cnt 
                continue
            if arr[j] == 0:
                arr[j] = k 
                if arr[j-1] == arr[j]:
                    cnt += 1
                if arr[j+1] == arr[j]:
                    cnt += 1
            else:    
                if arr[j-1] == arr[j]:
                    cnt -= 1
                elif arr[j-1] == k:
                    cnt += 1
                if arr[j+1] == arr[j]:
                    cnt -= 1
                elif arr[j+1] == k:
                    cnt += 1
                arr[j] = k 
            ans[i] = cnt
        return ans    


if __name__ == '__main__':
    print(Solution().colorTheArray2(n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]))
    # print(Solution().colorTheArray(n = 1, queries = [[0,100000]]))
    n = 17
    queries = [[11,3],[5,1],[16,2],[4,4],[5,1],[13,2],[15,1],[15,3],[8,1],[14,4],[1,3],[6,2],[8,2],[2,2],[3,4],[7,1],[10,2],[14,3],[6,5],[3,5],[5,5],[9,2],[2,3],[3,3],[4,1],[12,1],[0,4],[16,4],[8,1],[14,3],[15,3],[12,1],[11,5],[3,1],[2,4],[10,1],[14,5],[15,5],[5,2],[8,1],[6,5],[10,2]]
    # print(Solution().colorTheArray(n = n, queries = queries))
    sol = Solution().colorTheArray(n = n, queries = queries)
    ans = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,1,2,4,5,6,6,6,6,6,6,6,6,6,6,6,5,4,3,4,3,3,3,4]
    for i,j, (idx,num) in zip(sol, ans, queries):
        if i != j:
            print(i, j, idx, num)