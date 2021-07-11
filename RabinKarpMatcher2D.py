
'''
Searches for a 2D pattern in a 2D text. Assumes that both the pattern and the 
text are rectangles of characters.
O(Mr * Nr * Nc), where Mr is the pattern row length, Nr is the text row length 
and Nc is the text column length

'''
MOD = 10**9+7

class RabinKarp2D(object):

    def __init__(self, rad, pattern):
        #Radix of the alphabet. Assumes ASCII characters
        self.RADIX = rad
        self.pattern = pattern
        self.height = len(pattern)
        self.width = len(pattern[0])
        self.factors = [0]*(self.height - 1 + self.width - 1 + 1)
        self.factors[0] = 1
        for i in range(1, len(self.factors)):
            self.factors[i] = (self.RADIX * self.factors[i - 1]) % MOD
        self.patternHash = self.hash(pattern)

    def hash(self, data):
        result = 0
        for i in range(self.height):
            rowHash = 0
            for j in range(self.width):
                rowHash = (self.RADIX * rowHash + data[i][j]) % MOD
            result = (self.RADIX * result + rowHash) % MOD
        return result

    def check(self, text, i, j):
        x, y = i, j
        for a in range(self.height):
            for b in range(self.width):
                if text[x][y] != self.pattern[a][b]:
                    return False
                y += 1
            x += 1
            y = j
        return True

    def search(self, text):
        rowStartHash = self.hash(text)
        hash = rowStartHash
        for i in range(len(text) - self.height):
            if hash == self.patternHash and self.check(text, i, 0):
                return [i, 0]
            for j in range(len(text[0]) - self.width):
                hash = self.shiftRight(hash, text, i, j);
                if hash == self.patternHash and self.check(text, i, j + 1):
                    return [i, j + 1]
            rowStartHash = self.shiftDown(rowStartHash, text, i);
            hash = rowStartHash
        return None
        
    ''' Given the hash of the block at i, j, returns the hash of the block at i + 1, j.'''
    def shiftDown(self, hash, text, i):
        # TODO You have to write this
        return -1
	
    ''' Given the hash of the block at i, j, returns the hash of the block at i, j + 1. '''
    def shiftRight(self, hash, text, i, int ) :
        # TODO You have to write this
        return -1



