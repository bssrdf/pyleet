'''

-Hard-
*Greedy*
*Stack*
*Hash Table*

Given two strings s and t, transform string s into string t using the following operation any number of times:

Choose a non-empty substring in s and sort it in place so the characters are in ascending order.
For example, applying the operation on the underlined substring in "14234" results in "12344".
Return true if it is possible to transform s into t. Otherwise, return false.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "84532", t = "34852"
Output: true
Explanation: You can transform s into t using the following sort operations:
"84532" (from index 2 to 3) -> "84352"
"84352" (from index 0 to 2) -> "34852"
Example 2:

Input: s = "34521", t = "23415"
Output: true
Explanation: You can transform s into t using the following sort operations:
"34521" -> "23451"
"23451" -> "23415"
Example 3:

Input: s = "12345", t = "12435"
Output: false
 

Constraints:

s.length == t.length
1 <= s.length <= 105
s and t consist of only digits.



'''

from collections import defaultdict

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        idx, pos = [[] for _ in range(10)], [0 for _ in range(10)]
        for i, ch in enumerate(s):
            idx[int(ch)].append(i)
        for ch in t:
            d = int(ch)
            if pos[d] >= len(idx[d]):
                return False
            for i in range(d):
                if pos[i] < len(idx[i]) and idx[i][pos[i]] < idx[d][pos[d]]:
                    return False
            pos[d] += 1
        return True
    
    def isTransformable2(self, s: str, t: str) -> bool:
        # Probably the hardest part is to realize that: 
        # For every digit in t you find the first occurrence in s. Call that 
        # current digit as key. You need to make sure in s, no digit smaller 
        # than key appears to the left.
        # As we check one-by-one, we need to remove the digits we considered from s. 
        # In order to do this operation constant time, store all indices in reversed 
        # form using stack in the first loop (backward pass over s). Then use the .pop() 
        # operation in the second loop (forward pass over t).

        # places: this stores the indices of every digit from 0 to 9
        places = defaultdict(list)
        for i in reversed(range(len(s))):
            key = int(s[i])
            places[key].append(i)
        
        for e in t: #we loop over t and check every digit
            key = int(e) # current digit
            if not places[key]: # digit is not in s, return False
                return False 
            i = places[key][-1] #location of current digit
            for j in range(key): #only loop over digits smaller than current digit
                if places[j] and places[j][-1] < i: #there is a digit smaller than current digit, return false
                    return False
            places[key].pop()
        return True



if __name__ == "__main__":
    print(Solution().isTransformable(s = "84532", t = "34852"))
    print(Solution().isTransformable(s = "12345", t = "12435"))