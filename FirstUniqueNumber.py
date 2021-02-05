'''

-Medium-

You have a queue of integers, you need to retrieve the first unique integer in the queue.
Implement the FirstUnique class:
FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 
if there is no such integer.
void add(int value) insert value to the queue.
Example 1:
Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]
Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
Example 2:
Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]
Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17
Example 3:
Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]
Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1
Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.

'''

from collections import (deque, Counter)

class FirstUnique(object):

    def __init__(self, nums):
        self.dq = deque(nums)
        self.count = Counter(nums)

    def showFirstUnique(self):
        while self.dq and self.count[self.dq[0]] > 1:
            self.dq.popleft()
        return self.dq[0] if self.dq else -1
    
    def add(self, num):
        if num in self.count:
            self.count[num] += 1
        else:
            self.count[num] = 1
        if self.count[num] < 3:
           self.dq.append(num)


if __name__ == "__main__":

    firstUnique = FirstUnique([2,3,5])
    print(firstUnique.showFirstUnique())  # return 2
    firstUnique.add(5)            # the queue is now [2,3,5,5]
    print(firstUnique.showFirstUnique()) # return 2
    firstUnique.add(2)            # the queue is now [2,3,5,5,2]
    print(firstUnique.showFirstUnique()) # return 3
    firstUnique.add(3)            # the queue is now [2,3,5,5,2,3]
    print(firstUnique.showFirstUnique()) # return -1

    firstUnique = FirstUnique([809])
    print(firstUnique.showFirstUnique())
    firstUnique.add(809)          
    print(firstUnique.showFirstUnique())


    firstUnique = FirstUnique([7,7,7,7,7,7])
    print(firstUnique.showFirstUnique())
    firstUnique.add(7)          
    firstUnique.add(3)          
    firstUnique.add(3)          
    firstUnique.add(7)          
    firstUnique.add(17)          
    print(firstUnique.showFirstUnique())