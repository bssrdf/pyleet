'''

In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the 
distance to the closest person.  If there are multiple such seats, they sit 
in the seat with the lowest number.  (Also, if no one is in the room, then 
the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() 
returning an int representing what seat the student sat in, and 
ExamRoom.leave(int p) representing that the student in seat number p now 
leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have 
a student sitting in seat p.

 

Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], 
[[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.
​​​​​​​

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times 
across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently 
sitting in seat number p.

'''

from sortedcontainers import SortedSet

class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.n = N
        self.spots = SortedSet()        

    def seat(self):
        """
        :rtype: int
        """
        start, mx, idx = 0, 0, 0
        for i in self.spots:
            if start == 0:
                if mx < i - start:
                    mx = i - start
                    idx = 0
            else:
                if mx < (i - start + 1) // 2:
                    mx = (i - start + 1) // 2
                    idx = start + mx - 1
            start = i + 1

        if start > 0 and mx < self.n - start:
            mx = self.n - start
            idx = self.n - 1        
        self.spots.add(idx)
        return idx

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.spots.discard(p)

class ExamRoom2(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.n = N
        self.startMap = {}
        self.endMap = {}
        def distance(s):
            x, y = s    
            if x == -1: return y
            if y == N:  return N - 1 - x
            # 中点和端点之间的长度
            return (y - x) // 2
        self.spots = SortedSet([(-1, N)], key=lambda seg: (distance(seg), -seg[0]))        
    
    def addSeg(self, seg):
        self.spots.add(seg)
        self.startMap[seg[0]] = seg
        self.endMap[seg[1]] = seg

    def removeSeg(self, seg):
        self.spots.remove(seg)
        self.startMap.pop(seg[0],None)
        self.endMap.pop(seg[1], None)

    def seat(self):
        """
        :rtype: int
        """
        x, y = self.spots[-1]
        if x == -1:
            seat = 0
        elif y == self.n:
            seat = self.n-1
        else:
            seat = x + (y-x)//2
        left = (x, seat)
        right = (seat, y)
        self.removeSeg((x,y))
        self.addSeg(left)
        self.addSeg(right)
        return seat   
        

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        right = self.startMap[p]
        left = self.endMap[p]
        merged = (left[0], right[1])
        self.removeSeg(left)
        self.removeSeg(right)
        self.addSeg(merged)
        

if __name__ == "__main__":
# Your ExamRoom object will be instantiated and called as such:
    obj = ExamRoom(10)
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    obj.leave(4)
    print(obj.seat())

    obj = ExamRoom2(10)
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    obj.leave(4)
    print(obj.seat())