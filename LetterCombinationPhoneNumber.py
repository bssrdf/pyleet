'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution(object):
    mapping={'0':'', '1':'', '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno', 
                  '7':'pqrs','8':'tuv','9':'wxyz'}
  
    def letterCombinations(self, digits):

        res = []
        if not digits:
            return res
        c=digits[0]
        subs = self.letterCombinations(digits[1:])
        for a in self.mapping[c]:
            if subs:
                for s in subs:
                    res.append(a+s)
            else:
                res.append(a)
        return res
        
if __name__ == "__main__":
    assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
