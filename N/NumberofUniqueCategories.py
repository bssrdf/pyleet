'''
-Medium-
$$$


You are given an integer n and an object categoryHandler of class CategoryHandler.

There are nelements, numbered from 0 to n - 1. Each element has a category, and your task is to find the number of unique categories.

The class CategoryHandler contains the following function, which may help you:

boolean haveSameCategory(integer a, integer b): Returns true if a and b are in the same category and false otherwise. Also, if either a or b is not a valid number (i.e. it's greater than or equal to nor less than 0), it returns false.
Return the number of unique categories.

 

Example 1:

Input: n = 6, catagoryHandler = [1,1,2,2,3,3]
Output: 3
Explanation: There are 6 elements in this example. The first two elements belong to category 1, the second two belong to category 2, and the last two elements belong to category 3. So there are 3 unique categories.
Example 2:

Input: n = 5, catagoryHandler = [1,2,3,4,5]
Output: 5
Explanation: There are 5 elements in this example. Each element belongs to a unique category. So there are 5 unique categories.
Example 3:

Input: n = 3, catagoryHandler = [1,1,1]
Output: 1
Explanation: There are 3 elements in this example. All of them belong to one category. So there is only 1 unique category.
 

Constraints:

1 <= n <= 100




'''
from typing import Optional, List
from collections import Counter
# Definition for a category handler.
class CategoryHandler:
    def __init__(self, cat: List[int]) -> None:
        self.cat = cat
    def haveSameCategory(self, a: int, b: int) -> bool:
        if 0 <= a < len(self.cat) and 0 <= b < len(self.cat):             
            return self.cat[a] == self.cat[b]
        return False
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        cat = [-1]*n
        cnt = 0
        for i in range(n):
            for j in range(i+1,n):                
                if categoryHandler.haveSameCategory(i,j):                    
                    if cat[i] == -1 and cat[j] == -1:
                        cat[i], cat[j] = cnt, cnt
                        cnt += 1
                    elif cat[i] == -1:
                        cat[i] = cat[j]
                    elif cat[j] == -1:
                        cat[j] = cat[i] 
                    else:
                        cat[j] = cat[i] 
                else:
                    if cat[i] == -1 and cat[j] == -1:
                        cat[i] = cnt
                        cnt += 1
                        cat[j] = cnt
                        cnt += 1 
                    elif cat[i] == -1:
                        cat[i] = cnt 
                        cnt += 1
                    elif cat[j] == -1:
                        cat[j] = cnt
                        cnt += 1

                # print(i,j,cat)

        return len(Counter(cat))
    
    def numberOfCategories2(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        cat = list(range(1,n+1))
        for i in range(n):
            for j in range(i+1,n):                
                if categoryHandler.haveSameCategory(i,j):                    
                    cat[j] = cat[i] 
        return len(Counter(cat))
    
    def numberOfCategories3(
        self, n: int, categoryHandler: Optional['CategoryHandler']
    ) -> int:
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        for a in range(n):
            for b in range(a + 1, n):
                if categoryHandler.haveSameCategory(a, b):
                    p[find(a)] = find(b)
        return sum(i == x for i, x in enumerate(p))
    
if __name__ == "__main__":
    categoryHandler = CategoryHandler([1,1,2,2,3,3])
    print(Solution().numberOfCategories(6, categoryHandler))
    print(Solution().numberOfCategories2(6, categoryHandler))
    categoryHandler = CategoryHandler([1,2,3,4,5])
    print(Solution().numberOfCategories(5, categoryHandler))
    print(Solution().numberOfCategories2(5, categoryHandler))
    categoryHandler = CategoryHandler([1,1,1])
    print(Solution().numberOfCategories(3, categoryHandler))
    print(Solution().numberOfCategories2(3, categoryHandler))





        