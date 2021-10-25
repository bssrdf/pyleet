'''

-Medium-

Design a queue-like data structure that moves the most recently used element to the 
end of the queue.

Implement the MRUQueue class:

MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].

fetch(int k) moves the kth element (1-indexed) to the end of the queue and returns it.
 

Example 1:

Input:
["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]
Output:
[null, 3, 6, 2, 2]

Explanation:
MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3rd element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5th element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2nd element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // The 8th element (2) is already at the end of the queue so just return it.
 

Constraints:

1 <= n <= 2000
1 <= k <= n
At most 2000 calls will be made to fetch.
 

Follow up: Finding an O(n) algorithm per fetch is a bit easy. 
Can you find an algorithm with a better complexity for each fetch call?


'''

class MRUQueue(object):

    def __init__(self, n):
        self.nums = [i for i in range(1,n+1)]

    def fetch(self, k):
        res = self.nums[k-1]
        self.nums[k-1:-1] = self.nums[k:]
        self.nums[-1] = res
        return res

class BIT(object):  # 0-indexed.
    def __init__(self, n):
        MAX_CALLS = 2000
        self.__bit = [0]*(n+MAX_CALLS+1)  # Extra one for dummy node.
        for i in range(1, len(self.__bit)):
            self.__bit[i] = (1 if i-1 < n else 0) + self.__bit[i-1]
        for i in reversed(range(1, len(self.__bit))):
            last_i = i - (i & -i)
            self.__bit[i] -= self.__bit[last_i]

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

    def binary_lift(self, k):
        floor_log2_n = len(self.__bit).bit_length()-1
        pow_i = 2**floor_log2_n
        total = pos = 0  # 1-indexed
        for i in reversed(range(floor_log2_n+1)):  # O(logN)
            if pos+pow_i < len(self.__bit) and not (total+self.__bit[pos+pow_i] >= k):
                total += self.__bit[pos+pow_i]
                pos += pow_i
            pow_i >>= 1
        return (pos+1)-1  # 0-indexed


# fenwick / bit solution
class MRUQueue2(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.__bit = BIT(n)
        self.__lookup = {i:i+1 for i in range(n)}
        self.__curr = n
        
    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """
        pos = self.__bit.binary_lift(k)  
        val = self.__lookup.pop(pos)
        self.__bit.add(pos, -1)
        self.__bit.add(self.__curr, 1)
        self.__lookup[self.__curr] = val     
        self.__curr += 1
        return val

# Time:  ctor:  O(n)
# Space: fetch: O(sqrt(n))
import collections
import math


# sqrt decomposition solution
class MRUQueue3(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.__buckets = [collections.deque() for _ in range(int(math.ceil(n**0.5)))]
        for i in range(n):
            self.__buckets[i//len(self.__buckets)].append(i+1)

    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """
        k -= 1
        left, idx = divmod(k, len(self.__buckets))
        val = self.__buckets[left][idx]
        del self.__buckets[left][idx]
        self.__buckets[-1].append(val)
        for i in reversed(range(left, len(self.__buckets)-1)):
            x = self.__buckets[i+1].popleft()
            self.__buckets[i].append(x)
        return val

if __name__ == "__main__":
    mRUQueue = MRUQueue(8) #  // Initializes the queue to [1,2,3,4,5,6,7,8].
    print(mRUQueue.fetch(3))# // Moves the 3rd element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
    print(mRUQueue.fetch(5))#  // Moves the 5th element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
    print(mRUQueue.fetch(2))# // Moves the 2nd element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
    print(mRUQueue.fetch(8))# // The 8th element (2) is already at the end of the queue so just return it.
    mRUQueue = MRUQueue2(8) #  // Initializes the queue to [1,2,3,4,5,6,7,8].
    print(mRUQueue.fetch(3))# // Moves the 3rd element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
    print(mRUQueue.fetch(5))#  // Moves the 5th element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
    print(mRUQueue.fetch(2))# // Moves the 2nd element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
    print(mRUQueue.fetch(8))# // The 8th element (2) is already at the end of the queue so just return it.