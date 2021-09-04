'''
-Medium-

Create an inverted index with given documents.

Ensure that data does not include punctuation.

样例
Given a list of documents with id and content. (class Document)
Return an inverted index (HashMap with key is the word and value is a list of document ids).
Example 1:

Input:
[
  {
    "id": 1,
    "content": "This is the content of document 1 it is very short"
  },
  {
    "id": 2,
    "content": "This is the content of document 2 it is very long bilabial bilabial heheh hahaha ..."
  },
]
Output:
{
   "This": [1, 2],
   "is": [1, 2],
   ...
}
Example 2:

Input:
[
  {
    "id": 1,
    "content": "you are young"
  },
  {
    "id": 2,
    "content": "you are handsome"
  },
]
Output:
{
   "are": [1, 2],
   ...
}



'''


'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''

from collections import defaultdict
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        m = defaultdict(set)
        for doc in docs:
            s = doc.content.split()
            for c in s:
                m[c].add(doc.id)
        
        return {c:sorted(list(m[c])) for c in m}