'''
-Medium-

'order' and 'str' are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that 
they match the order that order was sorted. More specifically, if x occurs before y in order, then x 
should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input: 
order = "cba"
str = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. 
"dcba", "cdba", "cbda" are also valid outputs.
 

Note:

order has length at most 26, and no character is repeated in order.
str has length at most 200.
order and str consist of lowercase letters only.

'''

from collections import Counter

class Solution(object):
    def customSortString(self, order, str):
        """
        :type order: str
        :type str: str
        :rtype: str
        """
        cnt = Counter(str)
        oset = set(order)
        res = ''
        for c in order:
            if c in cnt:
                res += c*cnt[c]
        for k in cnt:
            if k not in oset:
                res += k*cnt[k]
        return res



if __name__ == "__main__":
    print(Solution().customSortString(order = "cba", str = "abcd"))