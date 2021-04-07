'''
-Medium-

Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a 
string characters of sorted distinct lowercase English letters and a number combinationLength 
as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.
 

Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
 

Constraints:

1 <= combinationLength <= characters.length <= 15
All the characters of characters are unique.
At most 10^4 calls will be made to next and hasNext.
It's guaranteed that all calls of the function next are valid.

'''


class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.s = characters
        self.length = combinationLength
        self.bitMask = 0
        self.masks = []
        self.idx = 0
        def dfs(s, pos, k):            
            if k == self.length: 
                self.bitMask |= 1 << pos
                self.masks.append(self.bitMask)
                self.bitMask &= ~(1 << pos)    
                return
            self.bitMask |= 1 << pos
            #for i in range(pos+1, len(s)):
            for i in range(pos+1, len(s)-(self.length-k)+1):
                dfs(s, i, k+1)
            self.bitMask &= ~(1 << pos)    
        for i in range(len(self.s)-self.length+1):
            dfs(self.s, i, 1)

    def next(self):
        """
        :rtype: str
        """
        bit = self.masks[self.idx]
        self.idx += 1
        ans = ''
        for i in range(len(self.s)):
            if bit & (1<<i):
                ans += self.s[i]
        return ans
                

        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.masks)


if __name__ == "__main__":
    itr = CombinationIterator("abcd", 2)
    print(itr.next())     # return "ab"
    print(itr.hasNext())  # return True
    print(itr.next())     # return "ac"
    print(itr.hasNext())  # return True
    print(itr.next())     # return "bc"
    print(itr.hasNext())  # return False
