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
        def dfs(pos, k):       
  #          print('A', pos, k, bin(self.bitMask))
            if k == self.length: 
                self.bitMask |= 1 << pos
                self.masks.append(self.bitMask)
                self.bitMask &= ~(1 << pos)    
                return
            self.bitMask |= 1 << pos
            #for i in range(pos, len(self.s)):
            for i in range(pos+1, len(self.s)-(self.length-k)+1):
            #for i in range(pos, len(self.s)-k+1):
                dfs(i, k+1)
            self.bitMask &= ~(1 << pos)    
        for i in range(len(self.s)-self.length+1):
            dfs(i, 1)
        #print(self.masks)

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
        
class CombinationIterator2(object):
    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.s = characters
        self.combLength = combinationLength
        self.ch2Idx = {}
        self.st = []
        idx = 0
        self.result = ''
        for c in characters:
            self.st.append(c)
            self.result += c
            if len(self.result) == self.combLength:
                break
        for c in characters:
            self.ch2Idx[c] = idx
            idx += 1

    def next(self):
        """
        :rtype: str
        """
        currResult = self.result
        idx = len(self.s) - 1
        # keep on removing the last character from the stack/result till the position where idx can be moved ahead
        while self.st and self.ch2Idx[self.st[-1]] == idx: 
            self.st.pop()
            idx -= 1
            self.result = self.result[:-1]
        if not self.st: 
            print(currResult, self.result, self.st)
            return currResult # // there is no next result to pre-process
        idx = self.ch2Idx[self.st.pop()] # // we need to add elements after this idx
        self.result = self.result[:-1]
        
        while len(self.st) != self.combLength:
            idx += 1
            temp = self.s[idx]
            self.result += temp
            self.st.append(temp)
        print(currResult, self.result, self.st)
        return currResult

    def hasNext(self):
        return len(self.st) > 0

         

if __name__ == "__main__":
    '''
    itr = CombinationIterator("abcd", 2)
    print(itr.next())     # return "ab"
    print(itr.hasNext())  # return True
    print(itr.next())     # return "ac"
    print(itr.hasNext())  # return True
    print(itr.next())     # return "bc"
    print(itr.hasNext())  # return False
    '''
    itr = CombinationIterator2("abc", 2)
    print(itr.next())     # return "ab"
    print(itr.hasNext())  # return True
    print(itr.next())     # return "ac"
    print(itr.hasNext())  # return True
    print(itr.next())     # return "bc"
    print(itr.hasNext())  # return False
