'''

-Medium-


Labeling System
Amazon is looking to develop a new labeling system in the fulfilment centers. 
New labels will be devised from the original string labels. Given the original 
string label, construct a new string by rearranging the original string and 
deleting characters as needed. Return the alphabetically-largest string that 
can be constructed respecting the limit as to how many consecutive characters 
can be the same (represented by k).

"Alphabetically-largest" is defined in reverse alphabetical order (e.g., b 
is "larger" than a, c is "larger" than b, etc.) from left to right (e.g.,
 "ba" is larger than "ab").

Write an algorithm to return the alphabetically-largest string that can 
be constructed respecting the
above limits.

Input
The input to the function/method consists of two arguments:
originalLabel, a string representing the original string label;
charLimit, an integer representing the maximum number of identical consecutive characters the new string can have (k).

Output
Return a string representing the alphabetically largest string that can be constructed that has no
more than k identical consecutive characters.



'''

class Solution(object):
    def relabel(self, originalLabel: str, charLimit: int) -> str:
        newLabel = ''
        oldLabel = sorted(originalLabel, reverse=True)
        print('original reversed',oldLabel)
        refChar = oldLabel[0]
        numSimChars = 0         # tracks how many times the current letter has been repeated
        q = []                  # a queue that tracks letters that are cut-off when max number of letters is exceeded
        for char in oldLabel:
            # Look out for any change in the letter to restart counting repeated letters
            if char != refChar:
                refChar = char
                numSimChars = 1
            else:
                numSimChars += 1

            # Add letters that exceed the limit to the queue
            if numSimChars > charLimit:
                q.append(char)
                continue

            # Add current letter to the new label
            newLabel += char

            # Add letters from the queue if there are any
            nAddedFromQ = 0
            if q:
                while q and (nAddedFromQ < charLimit):
                    newLabel += q.pop(0)
                    nAddedFromQ += 1
                numSimChars = 0
        
        return newLabel

if __name__ == "__main__":
    print(Solution().relabel("daaaacbtttsggggjhhk", 3))