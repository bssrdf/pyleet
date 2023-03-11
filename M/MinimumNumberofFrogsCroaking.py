'''
-Medium-

You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

Return the minimum number of different frogs to finish all the croaks in the given string.

A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

 

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
 

Constraints:

1 <= croakOfFrogs.length <= 105
croakOfFrogs is either 'c', 'r', 'o', 'a', or 'k'.



'''

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt, frogs, max_frogs = [0]*5, 0, 0
        s = 'croak'
        for c in croakOfFrogs:
            i = s.index(c)
            cnt[i] += 1
            if c == s[0]:
                frogs += 1
            if i > 0 and cnt[i-1] < cnt[i]:
                return -1
            if c == s[-1]:
                frogs -= 1
            max_frogs = max(max_frogs, frogs)
        return max_frogs if frogs == 0 else -1  


if __name__ == '__main__':
    print(Solution().minNumberOfFrogs( croakOfFrogs = "crcoakroak"))