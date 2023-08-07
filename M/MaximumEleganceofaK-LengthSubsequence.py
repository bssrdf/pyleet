'''

-Hard-
*Greedy*
*Sorting*

You are given a 0-indexed 2D integer array items of length n and an integer k.

items[i] = [profiti, categoryi], where profiti and categoryi denote the profit and category of the ith item respectively.

Let's define the elegance of a subsequence of items as total_profit + distinct_categories2, where total_profit is the sum of all profits in the subsequence, and distinct_categories is the number of distinct categories from all the categories in the selected subsequence.

Your task is to find the maximum elegance from all subsequences of size k in items.

Return an integer denoting the maximum elegance of a subsequence of items with size exactly k.

Note: A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order.

 

Example 1:

Input: items = [[3,2],[5,1],[10,1]], k = 2
Output: 17
Explanation: In this example, we have to select a subsequence of size 2.
We can select items[0] = [3,2] and items[2] = [10,1].
The total profit in this subsequence is 3 + 10 = 13, and the subsequence contains 2 distinct categories [2,1].
Hence, the elegance is 13 + 22 = 17, and we can show that it is the maximum achievable elegance. 
Example 2:

Input: items = [[3,1],[3,1],[2,2],[5,3]], k = 3
Output: 19
Explanation: In this example, we have to select a subsequence of size 3. 
We can select items[0] = [3,1], items[2] = [2,2], and items[3] = [5,3]. 
The total profit in this subsequence is 3 + 2 + 5 = 10, and the subsequence contains 3 distinct categories [1,2,3]. 
Hence, the elegance is 10 + 32 = 19, and we can show that it is the maximum achievable elegance.
Example 3:

Input: items = [[1,1],[2,1],[3,1]], k = 3
Output: 7
Explanation: In this example, we have to select a subsequence of size 3. 
We should select all the items. 
The total profit will be 1 + 2 + 3 = 6, and the subsequence contains 1 distinct category [1]. 
Hence, the maximum elegance is 6 + 12 = 7.  
 

Constraints:

1 <= items.length == n <= 105
items[i].length == 2
items[i][0] == profiti
items[i][1] == categoryi
1 <= profiti <= 109
1 <= categoryi <= n 
1 <= k <= n



'''

from typing import List

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        #Wrong
        A = sorted(items, reverse = True)
        n = len(A)
        i, j = 0, 0
        used = set()
        cat = 1
        used.add(A[0][1])
        ans = A[0][0]
        # ans = 0
        taken = set()
        i, j = 1, 1
        cnt = 1
        print(A)
        if cnt == k: return ans + cat**2                 
        while i < n:
            if A[i][1] not in used:
                ans += A[i][0]
                used.add(A[i][1])
                cat += 1
                i += 1
                cnt += 1
                if cnt == k: break                 
                continue
            j = max(j, i+1)
            
            while j < n and A[j][1] in used:
                j += 1      
            print(i,j,cat)
            if i < n and j < n:
                if A[i][0] - A[j][0] >= 2*cat+1:
                    ans += A[i][0]
                    i += 1
                else:
                    ans += A[j][0]
                    taken.add(j)
                    cat += 1
                    used.add(A[j][1])
                    j += 1
                cnt += 1    
                if cnt == k: break        
            elif j == n:
                ans += A[i][0] if i not in taken else 0
                i += 1            
                cnt += 1 if i not in taken else 0
                if cnt == k: break                 
            print(i, j, cnt, ans, taken) 

        print(ans, cat)
        return ans + cat**2
    
    def findMaximumElegance2(self, items: List[List[int]], k: int) -> int:
        items = sorted(items, key=lambda v: -v[0])
        res = cur = 0
        A = []
        seen = set()
        for i, (p, c) in enumerate(items):
            if i < k: # choose the first k elements
                if c in seen:
                    A.append(p) # A contains duplicated categories in descending order
                cur += p
            elif c not in seen: # for all i >= k, the only way to get a bigger profit
                if not A: break # is to add a new category, remove the smallest one that is in duplicated cat
                cur += p - A.pop()
            seen.add(c)
            res = max(res, cur + len(seen) * len(seen)) # check all possible solutions
        return res
    



if __name__ == "__main__":
    # print(Solution().findMaximumElegance(items = [[3,2],[5,1],[10,1]], k = 2))
    # print(Solution().findMaximumElegance(items = [[3,1],[3,1],[2,2],[5,3]], k = 3))
    # print(Solution().findMaximumElegance(items = [[1,1],[2,1],[3,1]], k = 3))
    # print(Solution().findMaximumElegance(items = [[1,1],[8,1],[3,3]], k = 3))

    # print(Solution().findMaximumElegance(items = [[3,3],[9,2],[1,3]], k =3))
    # print(Solution().findMaximumElegance(items = [[1,1],[4,1]], k = 1))
    # print(Solution().findMaximumElegance(items = [[4,4],[10,4],[8,4],[7,2]], k = 4))


    print(Solution().findMaximumElegance(items = [[2,2],[8,6],[10,6],[2,4],[9,5],[4,5]], k = 4))