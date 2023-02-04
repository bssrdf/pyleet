'''

-Medium-
*Prefix Sum*

You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.

 

Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]
 

Constraints:

1 <= arr.length, queries.length <= 3 * 104
1 <= arr[i] <= 109
queries[i].length == 2
0 <= lefti <= righti < arr.length



'''

from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        # zeros, ones = [[0]*31 for _ in range(n+1)], [[0]*31 for _ in range(n+1)]
        ones = [[0]*31 for _ in range(n+1)]
         
        for i, a in enumerate(arr):
            for j in range(30, -1, -1):  
                # bit = (a >> j) & 1
                # zeros[i+1][j] = zeros[i][j] + (bit == 0)
                ones[i+1][j] = ones[i][j] + (a >> j) & 1
        ans = []
        for l, r in queries:
            num = 0
            for j in range(31):
                # z = (zeros[r+1][j]-zeros[l][j]) % 2   
                o = (ones[r+1][j]-ones[l][j]) % 2  
                if o == 1:
                   num |= 1 << j 
            ans.append(num)
        return ans

    def xorQueries2(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        xors = [[0] for _ in range(n)]
        x = arr[0]
        xors[0] = x
        for i in range(1, n):
            xors[i] = xors[i-1] ^ arr[i]
        ans = []
        for l, r in queries:
            ans.append((xors[r] ^ xors[l-1]) if l >= 1 else xors[r])
        return ans         





if __name__ == "__main__":
    print(Solution().xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))
    print(Solution().xorQueries2(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))
        