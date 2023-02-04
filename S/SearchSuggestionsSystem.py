'''
-Medium-

Given an array of strings products and a string searchWord. We want to design 
a system that suggests at most three product names from products after each 
character of searchWord is typed. Suggested products should have common prefix 
with the searchWord. If there are more than three products with a common 
prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of 
searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], 
searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.

'''

from collections import defaultdict
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        m = defaultdict(set)
        for product in products:
            for i in range(len(product)):
                pre = product[:i+1] 
                m[pre].add(product)
        res = []
        for i in range(len(searchWord)):
            pre = searchWord[:i+1]
            res.append(sorted(m[pre])[:3]) 
        return res
    
    def suggestedProductsTrieHeap(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        import collections
        import heapq
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.h = []
            
            def add_sugesstion(self, product):
                if len(self.h) < 3:
                    heapq.heappush(self.h, MaxHeapStr(product))
                else:
                    heapq.heappushpop(self.h, MaxHeapStr(product))
            
            def get_suggestion(self):
                return sorted(self.h, reverse = True)
        
        class MaxHeapStr(str):
            def __init__(self, string): self.string = string
            def __lt__(self,other): return self.string > other.string
            def __eq__(self,other): return self.string == other.string
        
        root = TrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_sugesstion(p)
        
        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.get_suggestion())
        return result

    def suggestedProductsPrefixBinarySearch(self, A, word):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        """
        Intuition
        In a sorted list of words,
        for any word A[i],
        all its sugested words must following this word in the list.

        For example, if A[i] is a prefix of A[j],
        A[i] must be the prefix of A[i + 1], A[i + 2], ..., A[j]

        Explanation
        With this observation,
        we can binary search the position of each prefix of search word,
        and check if the next 3 words is a valid suggestion.
        """
        # 96%
        import bisect
        A.sort()
        res, prefix, i = [], '', 0
        for c in word:
            prefix += c
            i = bisect.bisect_left(A, prefix, i)
            res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
        return res


        

if __name__ == "__main__":
    print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], 
                      "mouse"))