'''
-Medium-

An abbreviation of a word follows the form <first letter><number><last letter>. 
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, find whether its abbreviation 
is unique in the dictionary. A word's abbreviation is unique if no other word 
from the dictionary has the same abbreviation.

Example: 

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
 

这道题让我们求独特的单词缩写，但是题目中给的例子不是很清晰，来看下面三种情况：

 

1. dictionary = {"dear"},  isUnique("door") -> false

2. dictionary = {"door", "door"}, isUnique("door") -> true

3. dictionary = {"dear", "door"}, isUnique("door") -> false


'''
from collections import defaultdict
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.m2 = defaultdict(set)
        for word in dictionary:
            abbr = self.abbreviation(word)
            self.m2[abbr].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if word == '': return True
        abbr = self.abbreviation(word)
        if abbr in self.m2:
            if len(self.m2[abbr]) > 1: return False
            elif word in self.m2[abbr]: return True
            return False
        return True

    def abbreviation(self, word):
        return word[0]+('' if len(word)<=2 else
                    str(len(word)-2))+word[-1]


if __name__=="__main__":
    wa = ValidWordAbbr(["deer", "door", "cake", "card"])
    print(wa.isUnique("dear"))
    print(wa.isUnique("cart"))
    print(wa.isUnique("cane"))
    print(wa.isUnique("make"))
    wa = ValidWordAbbr(["door", "door"])
    print(wa.isUnique("door"))

