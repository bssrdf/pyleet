'''
Given a chemical formula (given as a string), return the count of each atom.

The atomic element always starts with an uppercase character, then zero or 
more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count 
is greater than 1. If the count is 1, no digits will follow. For example, 
H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together to produce another formula. For example, 
H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also 
a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, return the count of all elements as a string in the 
following form: the first name (in sorted order), followed by its count 
(if that count is more than 1), followed by the second name (in sorted 
order), followed by its count (if that count is more than 1), and so on.
 

Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Example 4:

Input: formula = "Be32"
Output: "Be32"
 

Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.

'''

from collections import defaultdict

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """       

        def merge(m1, m2):
            for k in m2:
                if k in m1:
                    m1[k] += m2[k]
                else:
                    m1[k] = m2[k]                
         
        def helper(s):                                       
            i, num, n = 0, 0, len(s)        
            m = defaultdict(int)
            atoms = defaultdict(int)
            atom = ''
            def update():
                if atom:                                          
                    atoms[atom] += num if num > 0 else 1
                elif atoms:
                    for a in atoms:
                        atoms[a] *= num if num > 0 else 1 
                merge(m, atoms)
                atoms.clear()               

            while i < n:
                if ord('0') <= ord(s[i]) <= ord('9'):
                    num = 10*num+ord(s[i])-ord('0')                
                elif ord('a') <= ord(s[i]) <= ord('z'):    
                    atom += s[i]         
                elif ord('A') <= ord(s[i]) <= ord('Z'):
                    update()
                    num = 0
                    atom = s[i]    
                elif s[i] == '(':
                    update()
                    num = 0
                    atom = ''
                    j, cnt = i, 0
                    while i < n:
                        if s[i] == '(': cnt += 1
                        if s[i] == ')': cnt -= 1
                        if cnt == 0: break
                        i += 1
                    atoms = helper(s[j+1:i])               
                i += 1         
            update()            
            return m
        m = helper(formula)
        return ''.join([a+(str(m[a]) if m[a]>1 else '') 
                     for a in sorted(m.keys())])
        

if __name__ == "__main__":

#    '''
    print(Solution().countOfAtoms("H2O"))
    print(Solution().countOfAtoms("HO2"))
    print(Solution().countOfAtoms("Be32"))
    print(Solution().countOfAtoms("OHBe"))
    print(Solution().countOfAtoms("Mg(OH)2"))

    print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
#    '''
    s = "((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"
    print(Solution().countOfAtoms(s))