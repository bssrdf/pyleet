'''

-Medium-
*Bit Manipulation*
*Sort*

You are given a string array features where features[i] is a single word representing the name 
of a feature of the latest product you are working on. You made a survey where users reported 
which features they like. You are given a string array responses, where responses[i] is a string 
containing space-separated words.

You want to sort the features according to their popularity. More formally, let appearances(word) 
be the number of is such that responses[i] contains word as a word. Then the x-th feature is 
more popular than the y-th feature if appearances(features[x]) > appearances(features[y]).

Return an array sortedFeatures consisting of the feature names sorted by their popularity. If 
the x-th and y-th features have the same popularity where x < y, then you should put the x-th 
feature before the y-th one.

Example 1:

Input: features = [“cooler”,”lock”,”touch”], responses = [“i like cooler cooler”,”lock touch cool”,”locker like touch”]

Output: [“touch”,”cooler”,”lock”]

Explanation: appearances(“cooler”) = 1, appearances(“lock”) = 1, appearances(“touch”) = 2. Since “cooler” and “lock” both had 1 appearance, “cooler” comes first because “cooler” came first in the features array.

Example 2:

Input: features = [“a”,”aa”,”b”,”c”], responses = [“a”,”a aa”,”a a a a a”,”b a”]

Output: [“a”,”aa”,”b”,”c”]

Constraints:

1 <= features.length <= 10^4
1 <= features[i].length <= 10
features contains no duplicates.
features[i] consists of lowercase letters.
1 <= responses.length <= 10^2
1 <= responses[i].length <= 10^3
responses[i] consists of lowercase letters and spaces.
responses[i] contains no two consecutive spaces.
responses[i] has no leading or trailing spaces.


'''
import heapq
class Solution(object):
    def sortedFeature(self, features, responses):
        m = {}
        for i,res in enumerate(responses):
            for w in res.split():
                if w in m:
                    m[w] |= 1 << i
                else:
                    m[w] = 1 << i
        def bits(n):
            cnt = 0
            while n > 0:
                cnt += n & 0x1
                n >>= 1
            return cnt 
        pairs = []
        for w in features:
            if w in m:
                pairs.append((-bits(m[w]),w))
            else:
                pairs.append((0,w))
        pairs.sort()
        return [p[1] for p in pairs]

if __name__=="__main__":
    features = ["cooler","lock","touch"]
    responses = ["i like cooler cooler","lock touch cool","locker like touch"]
    print(Solution().sortedFeature(features, responses))
    features = ['a','aa','b','c'] 
    responses = ['a','a aa','a a a a a','b a']
    print(Solution().sortedFeature(features, responses))



