'''
-Hard-

Under a grammar given below, strings can represent a set of lowercase words.  
Let's use R(expr) to denote the set of words the expression represents.

Grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma delimited list of 2 or more expressions, we take the 
union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each 
word at most once)
When we concatenate two expressions, we take the set of possible concatenations 
between two words where the first word comes from the first expression and 
the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", 
"acdfh", "acefg", "acefh"}

Formally, the 3 rules for our grammar:

For every lowercase letter x, we have R(x) = {x}
For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) 
= R(e_1) ∪ R(e_2) ∪ ...
For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in 
R(e_1) × R(e_2)}, where + denotes concatenation, and × denotes the cartesian 
product.
Given an expression representing a set of words under the given grammar, 
return the sorted list of words that the expression represents.

 

Example 1:

Input: "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]
Example 2:

Input: "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.
 

Constraints:

1 <= expression.length <= 60
expression[i] consists of '{', '}', ','or lowercase English letters.
The given expression represents a set of words based on the grammar given 
in the description.


'''


class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        """
        The general idea is to use recursion on input string.
        if nothing obvious pops up, consider letting
        recursion function process one character each time        
        """
        n = len(expression)
        res = []
        # base case: only one char left, return it as the single item 
        # in the list
        if n <= 1:
            res.append(expression)
            return res

        def helper(s):
            ans = []
            i, cnt = 0, 0
            for j in range(len(s)):
                if s[j] == ',':
                    if cnt == 0:
                       ans.append(s[i:j])
                       i = j + 1
                elif s[j] == '{':
                    cnt += 1
                elif s[j] == '}':
                    cnt -= 1
            ans.append(s[i:])
            #print(s, ans)
            return ans
        
        if expression[0] == '{':
            i, cnt = 0, 0
            while i < n:
                if expression[i] == '{': cnt += 1
                if expression[i] == '}': cnt -= 1
                if cnt == 0: break
                i += 1
            # if the current char is '{', first extract a list of substrs 
            # seperated by '{' and its corresponding '}' 
            # the list is for all individual strs seperated by ','    
            subs = helper(expression[1:i])
            uni = set()
            for s in subs:
                # use a set to unionize each of these substrs 
                # here call the the function itself to process the substrs
                # Rule #2
                uni.update(self.braceExpansionII(s))
            # then call recursion again to process the rest of the expression    
            rest = self.braceExpansionII(expression[i+1:])
            # form the cartesion product from the set and the rest
            # Rule #3
            for s1 in uni:
                for s2 in rest:
                    res.append(s1+s2)
        else:
            prev = expression[0]
            subs = self.braceExpansionII(expression[1:])
            for s in subs:
                res.append(prev+s)
        res.sort()
        return res


if __name__ == "__main__":
    print(Solution().braceExpansionII("{a,b}{c,{d,e}}"))
    #print(Solution().braceExpansionII("{{a,z},a{b,c},{ab,z}}"))