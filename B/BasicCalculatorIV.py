'''

-Hard-

Given an expression such as expression = "e + 8 - a + 5" and an evaluation map such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]), return a list of tokens representing the simplified expression, such as ["-1*a","14"]

An expression alternates chunks and symbols, with a space separating each chunk and symbol.
A chunk is either an expression in parentheses, a variable, or a non-negative integer.
A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like "2x" or "-x".
Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.

For example, expression = "1 + 2 * 3" has an answer of ["7"].
The format of the output is as follows:

For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.
For example, we would never write a term like "b*a*c", only "a*b*c".
Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
For example, "a*a*b*c" has degree 4.
The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed.
An example of a well-formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"].
Terms (including constant terms) with coefficient 0 are not included.
For example, an expression of "0" has an output of [].
 

Example 1:

Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
Output: ["-1*a","14"]
Example 2:

Input: expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]
Output: ["-1*pressure","5"]
Example 3:

Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
Output: ["1*e*e","-64"]
 

Constraints:

1 <= expression.length <= 250
expression consists of lowercase English letters, digits, '+', '-', '*', '(', ')', ' '.
expression does not contain any leading or trailing spaces.
All the tokens in expression are separated by a single space.
0 <= evalvars.length <= 100
1 <= evalvars[i].length <= 20
evalvars[i] consists of lowercase English letters.
evalints.length == evalvars.length
-100 <= evalints[i] <= 100

'''
'''
Merge 2 sorted list (LC easy). Used to combine two polynomial terms inside the merge_term(self, term1, term2) function.
Sort array based on custom comparison key (LC easy). Used to rearrange the polynomial terms in the export_terms(self) function
Splitting string into tokens based on custom rule (LC Easy). Used in the generate_tokens(s) function to encapsulate the string parsing part of the problem.
Use a hash map to look up strings and replace them (LC Easy).
OOD design, overloading "+", "-", and "*" operators for a class (LC Medium).
Convert infix expression into a postfix expression using a stack (LC Medium). Used in the build_postfix(tokens) function
Deserialize a binary tree post-order traversal (LC Medium). Used in the evaluate(postfix) function. Recursively build the binary expression tree and use the OOD class to compute the result as we go.


'''

from typing import List

import re
class ExpressionNode:
    def __init__(self):
        self.terms = {}

    def set_term(self, term, coef):
        self.terms[term] = coef

    def merge_term(self, term1, term2):
        if term1 == "1":
            return term2
        if term2 == "1":
            return term1
        arr1 = term1.split("*")
        arr2 = term2.split("*")
        arr3 = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                arr3.append(arr1[i])
                i += 1
            else:
                arr3.append(arr2[j])
                j += 1
        if i < len(arr1):
            arr3 += arr1[i:]
        if j < len(arr2):
            arr3 += arr2[j:]
        return "*".join(arr3)

    def export_terms(self):
        arr = list(self.terms.keys())
        def reformat(term):
            if term == "1":
                return str(self.terms[term])
            return f"{self.terms[term]}*{term}"
        def cmp_key(term):
            if term == "1":
                return (0,)
            var = term.split("*")
            return (-len(var), *var)
        arr.sort(key=cmp_key)
        return [reformat(t) for t in arr]

    def clear_zeros(self):
        for term in list(self.terms.keys()):
            if self.terms[term] == 0:
                del self.terms[term]

    def __add__(self, other):
        new_node = ExpressionNode()
        for term in self.terms:
            if term in new_node.terms:
                new_node.terms[term] += self.terms[term]
            else:
                new_node.terms[term] = self.terms[term]
        for term in other.terms:
            if term in self.terms:
                new_node.terms[term] += other.terms[term]
            else:
                new_node.terms[term] = other.terms[term]

        new_node.clear_zeros()
        return new_node

    def __sub__(self, other):
        new_node = ExpressionNode()
        for term in self.terms:
            if term in new_node.terms:
                new_node.terms[term] += self.terms[term]
            else:
                new_node.terms[term] = self.terms[term]
        for term in other.terms:
            if term in self.terms:
                new_node.terms[term] -= other.terms[term]
            else:
                new_node.terms[term] = -other.terms[term]

        new_node.clear_zeros()
        return new_node

    def __mul__(self, other):
        new_node = ExpressionNode()
        for t1 in self.terms:
            for t2 in other.terms:
                t3 = self.merge_term(t1, t2)
                if t3 not in new_node.terms:
                    new_node.terms[t3] = 0
                new_node.terms[t3] += self.terms[t1] * other.terms[t2]

        new_node.clear_zeros()
        return new_node

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        lookup = {a: b for a, b in zip(evalvars, evalints)}
        operators = {
            "+": 0,
            "-": 0,
            "*": 1,
        }
        def get_tokens(s):
            i = 0
            for j, c in enumerate(s):
                if c == " ":
                    if i < j:
                        yield s[i:j]
                    i = j + 1
                elif c in "()+-*":
                    if i < j:
                        yield s[i:j]
                    yield c
                    i = j + 1
            if i < len(s):
                yield s[i:]

        def build_postfix(tokens):
            postfix = []
            ops = []
            modifier = 0
            for t in tokens:
                if t == "(" or t == ")":
                    modifier += (2 if t == "(" else -2)
                elif t in operators:
                    cur = modifier + operators[t]
                    while len(ops) > 0 and ops[-1][1] >= cur:
                        postfix.append( ops.pop()[0] )
                    ops.append( (t, cur) )
                else:
                    postfix.append(t)
            while len(ops) > 0:
                postfix.append( ops.pop()[0] )
            return postfix

        def evaluate(postfix):
            val = postfix.pop()
            node = ExpressionNode()
            if re.fullmatch("-?[\d]+", val):
                node.set_term("1", int(val))
            elif val not in operators:
                node.set_term(val, 1)
            else:
                right = evaluate(postfix)
                left = evaluate(postfix)
                if val == "+":
                    return left + right
                elif val == "-":
                    return left - right
                else:
                    return left * right
            return node

        tokens = list(get_tokens(expression))
        for i, token in enumerate(get_tokens(expression)):
            if token in lookup:
                tokens[i] = str(lookup[token])

        #print(tokens)
        postfix = build_postfix(tokens)
        #print(postfix)
        node = evaluate(postfix)
        node.clear_zeros()
        #print(node.terms)
        return node.export_terms()

    
if __name__ == "__main__": 
    print(Solution().basicCalculatorIV(expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]))

        