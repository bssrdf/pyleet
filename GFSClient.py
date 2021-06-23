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