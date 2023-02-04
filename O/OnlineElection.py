'''
-Medium-

You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at 
time times[i].

For each query at a time t, find the person that was leading the election at time t. Votes cast at time t 
will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the TopVotedCandidate class:

TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
int q(int t) Returns the number of the person that was leading the election at time t according to the 
mentioned rules.
 

Example 1:

Input
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
Output
[null, 0, 1, 1, 0, 0, 1]

Explanation
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
topVotedCandidate.q(15); // return 0
topVotedCandidate.q(24); // return 0
topVotedCandidate.q(8); // return 1

 

Constraints:

1 <= persons.length <= 5000
times.length == persons.length
0 <= persons[i] < persons.length
0 <= times[i] <= 10^9
times is sorted in a strictly increasing order.
times[0] <= t <= 10^9
At most 104 calls will be made to q.

'''
from typing import List
import bisect

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.n = len(persons)
        self.times = times
        votes = [0]*self.n
        leading = 0
        self.winner = []
        for p in persons:            
            votes[p] += 1
            if votes[p] >= votes[leading]:
                leading = p
            self.winner.append(leading)

    def q(self, t: int) -> int:
        idx = bisect.bisect_left(self.times, t)
        if idx < self.n and t == self.times[idx]: return self.winner[idx]
        return self.winner[idx-1]
        
if __name__ == "__main__":
    topVotedCandidate = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(topVotedCandidate.q(3))# // return 0, At time 3, the votes are [0], and 0 is leading.
    print(topVotedCandidate.q(12))# // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
    print(topVotedCandidate.q(25))# // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
    print(topVotedCandidate.q(15))# // return 0
    print(topVotedCandidate.q(10))# // return 1
    print(topVotedCandidate.q(24))# // return 0
    print(topVotedCandidate.q(8))# // return 1

