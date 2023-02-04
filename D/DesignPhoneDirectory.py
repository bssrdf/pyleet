'''

-Medium-

Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);


'''

from collections import deque

class PhoneDirectory(object):

    def __init__(self, n):
        self.q = deque([i for i in range(n)])
        self.rec = set([i for i in range(n)])
    
    def get(self):
        if not self.q: return -1
        num = self.q.popleft()
        self.rec.remove(num)
        return num
    
    def check(self, n):
        return n in self.rec

    def release(self, n):
        if n in self.rec: return
        self.q.append(n)
        self.rec.add(n)

if __name__ == "__main__":
    directory = PhoneDirectory(3)
    print(directory.get())
    print(directory.get())
    print(directory.check(2))
    print(directory.get())
    print(directory.check(2))
    directory.release(2)
    print(directory.check(2))





