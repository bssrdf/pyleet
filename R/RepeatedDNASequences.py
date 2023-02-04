'''
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', 
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify 
repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur 
more than once in a DNA molecule.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.

'''
from collections import defaultdict
class Solution(object):
    
    def findRepeatedDnaSequencesEncode(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        """
        这里可以用两位来表示一个字符，00 表示A，01 表示C，10 表示G，11 表示T，
        那么总共需要 20 位就可以表示十个字符流
        """
        if len(s) < 11:
            return []
        char2bit = {'A':0, 'C':1, 'G':2, 'T':3}       
        res = []        
        s1 = set()
        s2 = set()
        val = 0
        for i in range(10):
            val = val<<2 | char2bit[s[i]]
        s1.add(val)
        mask = (1<<20) - 1
        #format(val, "#022b")
        #print(f"{val:#022b}")
        for i in range(10, len(s)):            
            #print(f"{val:#024b}") 
            #print(f"{(val<<2):#024b}") 
            #print(f"{(val<<2) & mask:#024b}")
            #print('============================')
            #print(bin(char2bit[s[i]]))
            val = ((val<<2) & mask) | char2bit[s[i]]
            #print(bin(val))
            if val in s2: continue
            if val in s1:
                res.append(s[i-9:i+1])
                s2.add(val)
            else:
                s1.add(val)
        return res

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 11:
            return []
        count = defaultdict(int)
        res = set()
        count[s[:10]] += 1
        for i in range(1, len(s)-9):
            cur = s[i:i+10]
            count[cur] += 1
            if count[cur] >= 2:
                res.add(cur)
        return list(res)



if __name__ == "__main__":
    #print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    #print(Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA"))
    print(Solution().findRepeatedDnaSequencesEncode("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    #print(Solution().findRepeatedDnaSequencesEncode("AAAAAAAAAAAAA"))