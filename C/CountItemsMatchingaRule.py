'''
-Easy-
You are given an array items, where each items[i] = [typei, colori, namei] 
describes the type, color, and name of the ith item. You are also given a rule 
represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

 

Example 1:

Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
Example 2:

Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
 

Constraints:

1 <= items.length <= 10^4
1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
ruleKey is equal to either "type", "color", or "name".
All strings consist only of lowercase letters.

'''

from collections import defaultdict

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        color = defaultdict(int)
        typ  = defaultdict(int)
        name = defaultdict(int)
        for t,c,n in items:
            color[c] += 1 
            typ[t] += 1
            name[n] += 1
        #print(m)
        if ruleKey == 'color': return color[ruleValue] 
        if ruleKey == 'type': return  typ[ruleValue] 
        if ruleKey == 'name': return name[ruleValue] 

    def countMatchesCleanCode(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        rule = {'type' : 0, 'color' : 1, 'name' : 2}
        cnt, index = 0, rule[ruleKey]
        for item in items:
            if item[index] == ruleValue:
                cnt += 1
        return cnt

if __name__ == "__main__":
    print(Solution().countMatches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))