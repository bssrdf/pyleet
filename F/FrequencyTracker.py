'''

-Medium-
*Hash Table*


Design a data structure that keeps track of the values in it and answers some queries regarding their frequencies.

Implement the FrequencyTracker class.

FrequencyTracker(): Initializes the FrequencyTracker object with an empty array initially.
void add(int number): Adds number to the data structure.
void deleteOne(int number): Deletes one occurence of number from the data structure. The data structure may not contain number, and in this case nothing is deleted.
bool hasFrequency(int frequency): Returns true if there is a number in the data structure that occurs frequency number of times, otherwise, it returns false.
 

Example 1:

Input
["FrequencyTracker", "add", "add", "hasFrequency"]
[[], [3], [3], [2]]
Output
[null, null, null, true]

Explanation
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(3); // The data structure now contains [3]
frequencyTracker.add(3); // The data structure now contains [3, 3]
frequencyTracker.hasFrequency(2); // Returns true, because 3 occurs twice

Example 2:

Input
["FrequencyTracker", "add", "deleteOne", "hasFrequency"]
[[], [1], [1], [1]]
Output
[null, null, null, false]

Explanation
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(1); // The data structure now contains [1]
frequencyTracker.deleteOne(1); // The data structure becomes empty []
frequencyTracker.hasFrequency(1); // Returns false, because the data structure is empty

Example 3:

Input
["FrequencyTracker", "hasFrequency", "add", "hasFrequency"]
[[], [2], [3], [1]]
Output
[null, false, null, true]

Explanation
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.hasFrequency(2); // Returns false, because the data structure is empty
frequencyTracker.add(3); // The data structure now contains [3]
frequencyTracker.hasFrequency(1); // Returns true, because 3 occurs once

 

Constraints:

1 <= number <= 105
1 <= frequency <= 105
At most, 2 * 105 calls will be made to add, deleteOne, and hasFrequency in total.


'''
from collections import Counter, defaultdict


class FrequencyTracker:

    def __init__(self):
        self.cnt = Counter()
        self.freq = defaultdict(set)
        
    def add(self, number: int) -> None:
        if self.cnt[number] > 0:
           self.freq[self.cnt[number]].remove(number)    
        self.cnt[number] += 1
        self.freq[self.cnt[number]].add(number)

    def deleteOne(self, number: int) -> None:
        f = self.cnt[number]
        if f == 0: return
        self.freq[f].remove(number)
        self.cnt[number] -= 1
        if self.cnt[number] > 0:
            self.freq[self.cnt[number]].add(number)


    def hasFrequency(self, frequency: int) -> bool:
        return len(self.freq[frequency]) > 0
        

if __name__ == '__main__':
    frequencyTracker = FrequencyTracker()
    frequencyTracker.add(3) # The data structure now contains [3]
    frequencyTracker.add(3) # The data structure now contains [3, 3]
    print(frequencyTracker.hasFrequency(2)) # Returns true, because 3 occurs twice
    frequencyTracker = FrequencyTracker()
    print(frequencyTracker.hasFrequency(2)) # Returns false, because the data structure is empty
    frequencyTracker.add(3) # The data structure now contains [3]
    print(frequencyTracker.hasFrequency(1)) # Returns true, because 3 occurs once