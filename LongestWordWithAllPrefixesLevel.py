'''

-Medium-


Given an array of strings words, find the longest string in words such that 
every prefix of it is also in words.

For example, let words = ["a", "app", "ap"]. The string "app" has 
prefixes "ap" and "a", all of which are in words.
Return the string described above. If there is more than one string with 

the same length, return the lexicographically smallest one, and if 
no string exists, return "".

Example 1:

Input: words = [“k”,”ki”,”kir”,”kira”, “kiran”]

Output: “kiran”

Explanation: “kiran” has prefixes “kira”, “kir”, “ki”, and “k”, and all of them appear in words.

Example 2:

Input: words = [“a”, “banana”, “app”, “appl”, “ap”, “apply”, “apple”]

Output: “apple”

Explanation: Both “apple” and “apply” have all their prefixes in words. However, “apple” is lexicographically smaller, so we return that.

Example 3:

Input: words = [“abc”, “bc”, “ab”, “qwe”]

Output: “”

Constraints:

1 <= words.length <= 10^5
1 <= words[i].length <= 10^5
1 <= sum(words[i].length) <= 10^5
'''

from collections import defaultdict

class TrieNode(defaultdict):
    def __init__(self):
        super().__init__(TrieNode)
        self.terminal = False


class Solution(object):

    def longestWord(self, words):
        self.ans = ""
        root = TrieNode()
        for word in words:
            node = root
            n = len(word)
            for c in word:
                node = node[c]
            node.terminal = True 
        def dfs(node, sb):
            if node.terminal and len(sb) > len(self.ans):
                self.ans = sb
            for c in sorted(node.keys()):
                if node[c].terminal:                    
                    dfs(node[c], sb+c)
        dfs(root, '')
        return self.ans            
            




if __name__ == '__main__':
    print(Solution().longestWord(["k","ki","kir","kira", "kiran"]))
    print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
    print(Solution().longestWord(["abc", "bc", "ab", "qwe"]))