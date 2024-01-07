'''
-Hard-

*Prefix Sum*

You are given a 0-indexed string s having an even length n.

You are also given a 0-indexed 2D integer array, queries, where queries[i] = [ai, bi, ci, di].

For each query i, you are allowed to perform the following operations:

Rearrange the characters within the substring s[ai:bi], where 0 <= ai <= bi < n / 2.
Rearrange the characters within the substring s[ci:di], where n / 2 <= ci <= di < n.
For each query, your task is to determine whether it is possible to make s a palindrome by performing the operations.

Each query is answered independently of the others.

Return a 0-indexed array answer, where answer[i] == true if it is possible to make s a palindrome by performing operations specified by the ith query, and false otherwise.

A substring is a contiguous sequence of characters within a string.
s[x:y] represents the substring consisting of characters from the index x to index y in s, both inclusive.
 

Example 1:

Input: s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]]
Output: [true,true]
Explanation: In this example, there are two queries:
In the first query:
- a0 = 1, b0 = 1, c0 = 3, d0 = 5.
- So, you are allowed to rearrange s[1:1] => abcabc and s[3:5] => abcabc.
- To make s a palindrome, s[3:5] can be rearranged to become => abccba.
- Now, s is a palindrome. So, answer[0] = true.
In the second query:
- a1 = 0, b1 = 2, c1 = 5, d1 = 5.
- So, you are allowed to rearrange s[0:2] => abcabc and s[5:5] => abcabc.
- To make s a palindrome, s[0:2] can be rearranged to become => cbaabc.
- Now, s is a palindrome. So, answer[1] = true.
Example 2:

Input: s = "abbcdecbba", queries = [[0,2,7,9]]
Output: [false]
Explanation: In this example, there is only one query.
a0 = 0, b0 = 2, c0 = 7, d0 = 9.
So, you are allowed to rearrange s[0:2] => abbcdecbba and s[7:9] => abbcdecbba.
It is not possible to make s a palindrome by rearranging these substrings because s[3:6] is not a palindrome.
So, answer[0] = false.
Example 3:

Input: s = "acbcab", queries = [[1,2,4,5]]
Output: [true]
Explanation: In this example, there is only one query.
a0 = 1, b0 = 2, c0 = 4, d0 = 5.
So, you are allowed to rearrange s[1:2] => acbcab and s[4:5] => acbcab.
To make s a palindrome s[1:2] can be rearranged to become abccab.
Then, s[4:5] can be rearranged to become abccba.
Now, s is a palindrome. So, answer[0] = true.
 

Constraints:

2 <= n == s.length <= 105
1 <= queries.length <= 105
queries[i].length == 4
ai == queries[i][0], bi == queries[i][1]
ci == queries[i][2], di == queries[i][3]
0 <= ai <= bi < n / 2
n / 2 <= ci <= di < n 
n is even.
s consists of only lowercase English letters.


'''

from typing import List

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)//2
        s1, s2 = s[:n], s[2*n:n-1:-1]
        diff = [n]*(n+1)
        DEB = False
        c1, c2 = [[0]*(n+1) for _ in range(26)], [[0]*(n+1) for _ in range(26)]
        for i,c in enumerate(s1):
            for j in range(26):
                if ord(c) - ord('a') == j:
                    c1[j][i+1] = c1[j][i] + 1
                else:
                    c1[j][i+1] = c1[j][i]
        for i,c in enumerate(s2):
            for j in range(26):
                if ord(c) - ord('a') == j:
                    c2[j][i+1] = c2[j][i] + 1
                else:
                    c2[j][i+1] = c2[j][i]
        t = -1
        for i in range(n):
            diff[i] = t+1
            if s1[i] != s2[i]:
               t = i
        diff[n] = t          
        def check(a,b):
            for i in range(26):
                x = c1[i][b+1] - c1[i][a]
                y = c2[i][b+1] - c2[i][a]
                if x != y:
                    return False 
            return True
        def check1(a, b, c):
            for i in range(26):
                x = c1[i][b+1] - c1[i][a]
                y = c2[i][c] - c2[i][a]
                if x < y:
                    return True 
            return False
        def check2(a, b, c):
            for i in range(26):
                x = c1[i][b+1] - c1[i][c+1]
                y = c2[i][b+1] - c2[i][a]
                if x > y:
                    return True 
            return False
        def check3(a, b, c):
            for i in range(26):
                x = c1[i][c] - c1[i][a]
                y = c2[i][b+1] - c2[i][a]
                if x > y:
                    return True 
            return False
        def check4(a, b, c):
            for i in range(26):
                x = c1[i][b+1] - c1[i][a]
                y = c2[i][b+1] - c2[i][c+1]
                if x < y:
                    return True 
            return False
        ans = [True]*len(queries)
        for i, (a1, b1, a2, b2) in enumerate(queries):
            a2, b2 = n - (b2 - n) - 1, n - (a2 - n) - 1
            if DEB: print(a1, b1, a2, b2)
            if b1 < a2:
                if diff[a1] != 0 or diff[a2] > b1+1 or diff[n] > b2:
                    if DEB: print('A')
                    ans[i] = False
                elif not check(a1, b1):
                    if DEB: print('B')                    
                    ans[i] = False
                elif not check(a2, b2):
                    if DEB: print('C')
                    ans[i] = False   
            elif b2 < a1:
                if diff[a2] != 0 or diff[a1] > b2+1 or diff[n] > b1:
                    if DEB: print('D')
                    ans[i] = False
                elif not check(a1, b1):
                    if DEB: print('E')
                    ans[i] = False
                elif not check(a2, b2):
                    if DEB: print('F')
                    ans[i] = False   
            elif a1 >= a2 and b1 <= b2:
                if diff[a2] != 0 or diff[n] > b2:
                    if DEB: print('F1')
                    ans[i] = False                   
                elif not check(a2, b2):
                    if DEB: print('F2')
                    ans[i] = False                   
            elif a2 >= a1 and b2 <= b1:
                if diff[a1] != 0 or diff[n] > b1:
                    if DEB: print('F3')
                    ans[i] = False                   
                elif not check(a1, b1):
                    if DEB: print('F4')
                    ans[i] = False                   
            elif b1 >= a2 and b1 < b2:
                if diff[a1] != 0 or diff[n] > b2:
                    ans[i] = False    
                elif not check(a1, b2):
                    if DEB: print('G')
                    ans[i] = False
                elif check1(a1, b1, a2) or check2(a2, b2, b1):
                    if DEB: print('H')
                    ans[i] = False    
            elif b2 >= a1 and b2 < b1:
                if diff[a2] != 0 or diff[n] > b1:
                    ans[i] = False    
                elif not check(a2, b1):
                    if DEB: print('L')
                    ans[i] = False
                elif check3(a2, b2, a1) or check4(a1, b1, b2):
                    if DEB: print('K')
                    ans[i] = False    
        return ans

        
if __name__ == "__main__":
    print(Solution().canMakePalindromeQueries(s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]]))
    print(Solution().canMakePalindromeQueries(s = "abcdef", queries = [[1,1,3,5],[0,2,5,5]]))
    print(Solution().canMakePalindromeQueries(s = "abbcdecbba", queries = [[0,2,7,9]]))
    print(Solution().canMakePalindromeQueries(s = "acbcab", queries = [[1,2,4,5]]))

    print(Solution().canMakePalindromeQueries(s = "bbccbb", queries = [[0,1,4,5]]))
    print(Solution().canMakePalindromeQueries(s = "adceaecd", queries = [[3,3,5,5],[0,1,4,6]]))
    print(Solution().canMakePalindromeQueries(s = "fxdqcfqdxc", queries = [[1,1,7,8],[1,1,5,9],[2,4,8,8],[0,4,6,8],[2,3,7,8],[2,4,5,9],[1,4,9,9]]))
    print(Solution().canMakePalindromeQueries(s = "fxdqcfqdxc", queries = [[2,3,7,8]]))
    print(Solution().canMakePalindromeQueries(s = "baabcaab", queries = [[0,1,5,5]]))