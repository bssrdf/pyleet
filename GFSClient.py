'''
-Medium-

Implement a simple client for GFS (Google File System, a distributed file system), it 
provides the following methods:

read(filename). Read the file with given filename from GFS.
write(filename, content). Write a file with given filename & content to GFS.
There are two private methods that already implemented in the base class:

readChunk(filename, chunkIndex). Read a chunk from GFS.
writeChunk(filename, chunkIndex, chunkData). Write a chunk to GFS.
To simplify this question, we can assume that the chunk size is chunkSize bytes. 
(In a real world system, it is 64M). The GFS Client's job is splitting a file into 
multiple chunks (if need) and save to the remote GFS server. chunkSize will be given 
in the constructor. You need to call these two private methods to implement read & write 
methods.

样例
GFSClient(5)
read("a.txt")
>> null
write("a.txt", "World")
>> You don't need to return anything, but you need to call writeChunk("a.txt", 0, "World") to write a 5 bytes chunk to GFS.
read("a.txt")
>> "World"
write("b.txt", "111112222233")
>> You need to save "11111" at chunk 0, "22222" at chunk 1, "33" at chunk 2.
write("b.txt", "aaaaabbbbb")
read("b.txt")
>> "aaaaabbbbb"

'''


# Definition of BaseGFSClient
from collections import defaultdict
class BaseGFSClient:
    def __init__(self):
        #self.chunks = []
        self.files = defaultdict(list)
    def readChunk(self, filename, chunkIndex):
        return self.files[filename][chunkIndex] 
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
        if filename in self.files:
            if chunkIndex < len(self.files[filename]):
                self.files[filename][chunkIndex] = content
            else:
                self.files[filename].append(content)
        self.files[filename].append(content)



class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):        
        # do intialization if necessary
        super().__init__()
        self.size = chunkSize
        self.idx = {}

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        # write your code here
        res = ''
        if filename not in self.idx:
            return None
        n = self.idx[filename]
        for i in range(n):
            res += self.readChunk(filename, i)
        return res

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        # write your code here
        n = len(content) // self.size + 1
        self.idx[filename] = n
        for i in range(n):
            #print(content[i*self.size:(i+1)*self.size])
            self.writeChunk(filename, i, content[i*self.size:(i+1)*self.size])

if __name__ == "__main__":
    gfc = GFSClient(5)
    print(gfc.read("a.txt"))
    gfc.write("a.txt", "World")
    print(gfc.read("a.txt"))
    gfc.write("b.txt", "111112222233")
    print(gfc.read("b.txt"))
    gfc.write("b.txt", "aaaaabbbbb")
    print(gfc.read("b.txt"))