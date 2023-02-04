'''

-Medium-

Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.

 

Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3
 

Constraints:

1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase letters.




'''

from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def compress(s):
            cnt, last, sc = 0, 'Z', []
            for c in s:
                if c != last:
                    sc.append([last, cnt])
                    last = c
                    cnt = 1
                else:
                    cnt += 1
            sc.append([last, cnt])
            return sc
        def match(sc1, s2):
            sc2 = compress(s2)
            if len(sc1) != len(sc2): return False
            for i in range(1, len(sc1)):
                if sc1[i][0] != sc2[i][0]:
                    return False
                if sc1[i][1] < sc2[i][1]: 
                    return False
                if sc1[i][1] == 2 and sc2[i][1] != 2:
                    return False
            return True        
        sc = compress(s)             
        
        return sum(1 if match(sc, w) else 0 for w in words)





if __name__ == "__main__":
    print(Solution().expressiveWords(s = "heeellooo", words = ["hello", "hi", "helo"]))
    print(Solution().expressiveWords( s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]))
        