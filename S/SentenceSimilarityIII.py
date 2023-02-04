'''
-Medium-

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
For example, "Hello World", "HELLO", "hello world hello world" are all sentences. Words consist of 
only uppercase and lowercase English letters.

Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence 
(possibly empty) inside one of these sentences such that the two sentences become equal. For example, 
sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting 
"my name is" between "Hello" and "Jane" in sentence2.

Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. 
Otherwise, return false.

 

Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
Example 2:

Input: sentence1 = "of", sentence2 = "A lot of words"
Output: false
Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.
Example 3:

Input: sentence1 = "Eating right now", sentence2 = "Eating"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
Example 4:

Input: sentence1 = "Luky", sentence2 = "Lucccky"
Output: false
 

Constraints:

1 <= sentence1.length, sentence2.length <= 100
sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
The words in sentence1 and sentence2 are separated by a single space.


'''

from collections import deque

class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        words1, words2 = sentence1.split(), sentence2.split()
        n1, n2 = map(len, (words1, words2))
        if n1 > n2:
            return self.areSentencesSimilar(sentence2, sentence1)
        i = 0
        while i < n1 and words1[i] == words2[i]:
            i += 1
        while i < n1 and words1[i] == words2[n2 - n1 + i]:
            i += 1
        return i == n1

    def areSentencesSimilarQueue(self, sentence1: str, sentence2: str) -> bool:
        dq1, dq2 = map(deque, (sentence1.split(), sentence2.split()))
        while dq1 and dq2 and dq1[0] == dq2[0]:
            dq1.popleft()
            dq2.popleft()
        while dq1 and dq2 and dq1[-1] == dq2[-1]:       
            dq1.pop()
            dq2.pop()
        return not dq1 or not dq2    

if __name__ == "__main__":
   # print(Solution().areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley"))
   # print(Solution().areSentencesSimilar(sentence1 = "of", sentence2 = "A lot of words"))
   # print(Solution().areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating"))
   # print(Solution().areSentencesSimilar(sentence1 = "Luky", sentence2 = "Lucccky"))
    s1 = "Y ggUFOmtf woKuTtO W uwJZ Zan wgm zprl Kgn mAY xLlCH phA UIVKIohfw al g m"
    s2 = "Jfa jfvmGU bKSSX uQ AmTzbBW EF jdc ft Z g VcM oNlI jeX q mNG YnUgGSnejt Y"
    print(Solution().areSentencesSimilar(sentence1 = s1, sentence2 = s2))
    print(Solution().areSentencesSimilarQueue(sentence1 = s1, sentence2 = s2))
