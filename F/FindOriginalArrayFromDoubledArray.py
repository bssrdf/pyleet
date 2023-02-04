'''

-Medium-

An integer array original is transformed into a doubled array changed by appending twice the 
value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a 
doubled array, return an empty array. The elements in original may be returned in any order.

 

Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
 

Constraints:

1 <= changed.length <= 10^5
0 <= changed[i] <= 10^5


'''

from typing import List
from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1: return []
        m = defaultdict(int)
        res = []
        for i in changed:
            if i%2 == 0 and i//2 in m:
                m[i//2] -= 1
                if m[i//2] == 0:
                    m.pop(i//2)
                res.append(i//2)
            elif i*2 in m:
                m[i*2] -= 1
                if m[i*2] == 0:
                    m.pop(i*2)
                res.append(i)
            else:
                m[i] += 1
        #print(m)        
        if not m: return res
        return []
    
    def findOriginalArray2(self, changed: List[int]) -> List[int]:
        n = len(changed)
        changed.sort()
        if n % 2 == 1: return []
        m = defaultdict(int)
        res = []
        for i in changed:
            j = i // 2
            if i%2 == 0 and j in m:
                m[j] -= 1
                if m[j] == 0:
                    m.pop(j)
                res.append(j)             
            else:
                m[i] += 1
        #print(m)        
        if not m: return res
        return []




        

if __name__=="__main__":
    #print(Solution().findOriginalArray([1,3,4,2,6,8]))
    #print(Solution().findOriginalArray([6,3,0,1]))
    #print(Solution().findOriginalArray([1]))
    print(Solution().findOriginalArray([4,4,16,20,8,8,2,10]))
    print(Solution().findOriginalArray2([4,4,16,20,8,8,2,10]))