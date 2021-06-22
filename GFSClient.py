'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):        
        # do intialization if necessary
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
            return res
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
        self.idx[filename] = next
        for i in range(n):
            self.writeChunk(filename, i, content[i*self.size:(i+1)*self.size])
