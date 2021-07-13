
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
        #self.factors = [0]*(self.height - 1 + self.width - 1 + 1)
        self.factors = [0]*self.width
        self.factors[0] = 1
        for i in range(1, len(self.factors)):
            self.factors[i] = (self.RADIX * self.factors[i - 1]) % MOD
        self.patternHash = self.hash(pattern)
        #print('pattern hash = ', self.patternHash)
        #print('factors = ', self.factors)

    def hash(self, data):
        result = 0
        for i in range(self.height):
            rowHash = 0
            for j in range(self.width):
                rowHash = (self.RADIX * rowHash + ord(data[i][j])) % MOD
            #result = (self.RADIX * result + rowHash) % MOD
            result  += rowHash
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
        #print(rowStartHash)
        hash = rowStartHash
        for i in range(len(text)-self.height+1):
            if i > 0:
                # Remove previous row from rolling hash
                for j in range(self.width):
                    #hash = (hash + MOD - self.factors[self.width - 1 -j] 
                    #        * ord(text[i-1][j])%MOD) % MOD
                    hash = (hash - self.factors[self.width - 1 -j] 
                            * ord(text[i-1][j])%MOD) % MOD
                # Add next row in rolling hash
                for j in range(self.width):
                    hash = (hash + self.factors[self.width - 1 -j] 
                            * ord(text[i+self.height-1][j])) % MOD    
            textHash = hash
            if textHash == self.patternHash and self.check(text, i, 0):
                return [i, 0]
            for j in range(self.width, len(text[0])):
                # Remove previous column from rolling hash
                for k in range(self.height):                    
                    textHash = (textHash + MOD - self.factors[self.width-1] 
                            * ord(text[i+k][j-self.width])%MOD) % MOD
                # Add next column in rolling hash
                for k in range(self.height):
                    if k == 0:
                        textHash = (textHash*self.RADIX + ord(text[i+k][j])) % MOD    
                    else:
                        textHash = (textHash + ord(text[i+k][j])) % MOD 
                '''
                if i == 1 and j - self.width + 1 == 2:
                    print(textHash)
                    print(self.check(text, i, j - self.width + 1))
                if textHash == self.patternHash:
                    print(i, j)
                '''
                if textHash == self.patternHash and self.check(text, i, j - self.width + 1):
                    return [i, j - self.width + 1]

            '''    
            if hash == self.patternHash and self.check(text, i, 0):
                return [i, 0]
            for j in range(len(text[0]) - self.width):
                hash = self.shiftRight(hash, text, i, j)
                if hash == self.patternHash and self.check(text, i, j + 1):
                    return [i, j + 1]
            rowStartHash = self.shiftDown(rowStartHash, text, i)
            hash = rowStartHash
            '''
        return None

class RabinKarp2DV2(object):

    def __init__(self, rad, pattern):
        #Radix of the alphabet. Assumes ASCII characters
        self.RADIX = rad
        self.pattern = pattern
        self.height = len(pattern)
        self.width = len(pattern[0])
        self.factors = [0]*((self.height - 1)+(self.width - 1) + 1)
        self.factors[0] = 1
        for i in range(1, len(self.factors)):
            self.factors[i] = (self.RADIX * self.factors[i - 1]) % MOD
        self.patternHash = self.hash(pattern)
        #print('pattern hash = ', self.patternHash)
        #print('factors = ', self.factors)

    def hash(self, data):
        result = 0
        for i in range(self.height):
            rowHash = 0
            for j in range(self.width):
                rowHash = (self.RADIX * rowHash + ord(data[i][j])) % MOD
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
        #print(rowStartHash)
        hash = rowStartHash
        for i in range(len(text)-self.height+1):            
            if hash == self.patternHash and self.check(text, i, 0):
                return [i, 0]
            for j in range(len(text[0]) - self.width):
                hash = self.shiftRight(hash, text, i, j)
                if hash == self.patternHash and self.check(text, i, j + 1):
                    return [i, j + 1]
            rowStartHash = self.shiftDown(rowStartHash, text, i)
            hash = rowStartHash
        return None
        
    ''' Given the hash of the block at i, j, returns the hash of the block at i + 1, j.'''
    def shiftDown(self, hash, text, i):
        # TODO You have to write this
        # Remove previous row from rolling hash
        for j in range(self.width):
            #hash = (hash + MOD - self.factors[self.width - 1 -j] 
            #        * ord(text[i-1][j])%MOD) % MOD
            hash = (hash - self.factors[self.width + self.height - 1 - j] 
                    * ord(text[i][j])%MOD) % MOD
        for j in range(self.width):
            hash = (hash + self.factors[self.width - j] 
                    * ord(text[i+self.height][j])%MOD) % MOD
        return hash
	
    ''' Given the hash of the block at i, j, returns the hash of the block at i, j + 1. '''
    def shiftRight(self, hash, text, i, j) :
        # TODO You have to write this
        for k in range(self.height):                    
            hash = (hash + MOD - self.factors[self.width+self.height-1-k] 
                    * ord(text[i+k][j])%MOD) % MOD
        # Add next column in rolling hash
        for k in range(self.height):
            if k == 0:
                hash = (hash*self.RADIX + ord(text[i+k][j+self.width])) % MOD    
            else:
                hash = (hash + ord(text[i+k][j+self.width])) % MOD 
        return -1

class RabinKarp2DV3(object):

    def __init__(self, rad, pattern):
        #Radix of the alphabet. Assumes ASCII characters
        self.RADIX = rad
        self.pattern = pattern
        self.height = len(pattern)
        self.width = len(pattern[0])
        self.factors = [0]*((self.height - 1)+(self.width - 1) + 1)
        self.factors[0] = 1
        for i in range(1, len(self.factors)):
            self.factors[i] = (self.RADIX * self.factors[i - 1]) % MOD
        self.patternHash = self.hash(pattern)
        #print('pattern hash = ', self.patternHash)
        #print('factors = ', self.factors)

    def hash2D(self, data, hash1d):
        for i in range(self.height):
            hash1d[i] = 0
            for j in range(self.width):
                hash1d[i] = (self.RADIX * hash1d[i] + ord(data[i][j])) % MOD

    def rehash2D(self, data, hash1d, j):
        for i in range(self.height):
            hash1d[i] = (hash1d[i] + MOD - self.factors[self.width-1] 
                    * ord(data[i][j])%MOD) % MOD
            hash1d[i] = (hash1d[i]+ ord(data[i][j+self.width])) % MOD

    def hash(self, data):
        result = 0
        for i in range(self.height):
            rowHash = 0
            for j in range(self.width):
                rowHash = (self.RADIX * rowHash + ord(data[i][j])) % MOD
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
        #print(rowStartHash)
        hash = rowStartHash
        for i in range(len(text)-self.height+1):            
            if hash == self.patternHash and self.check(text, i, 0):
                return [i, 0]
            for j in range(len(text[0]) - self.width):
                hash = self.shiftRight(hash, text, i, j)
                if hash == self.patternHash and self.check(text, i, j + 1):
                    return [i, j + 1]
            rowStartHash = self.shiftDown(rowStartHash, text, i)
            hash = rowStartHash
        return None
        
    ''' Given the hash of the block at i, j, returns the hash of the block at i + 1, j.'''
    def shiftDown(self, hash, text, i):
        # TODO You have to write this
        # Remove previous row from rolling hash
        for j in range(self.width):
            #hash = (hash + MOD - self.factors[self.width - 1 -j] 
            #        * ord(text[i-1][j])%MOD) % MOD
            hash = (hash - self.factors[self.width + self.height - 1 - j] 
                    * ord(text[i][j])%MOD) % MOD
        for j in range(self.width):
            hash = (hash + self.factors[self.width - j] 
                    * ord(text[i+self.height][j])%MOD) % MOD
        return hash
	
    ''' Given the hash of the block at i, j, returns the hash of the block at i, j + 1. '''
    def shiftRight(self, hash, text, i, j) :
        # TODO You have to write this
        for k in range(self.height):                    
            hash = (hash + MOD - self.factors[self.width+self.height-1-k] 
                    * ord(text[i+k][j])%MOD) % MOD
        # Add next column in rolling hash
        for k in range(self.height):
            if k == 0:
                hash = (hash*self.RADIX + ord(text[i+k][j+self.width])) % MOD    
            else:
                hash = (hash + ord(text[i+k][j+self.width])) % MOD 
        return -1


if __name__ == "__main__":

    pattern1 = ["RE",
                "NE"]
    pattern2 = ["AB",
                "RE"]

    text1 =["ABCD",
            "RERE",
            "DRNE",
            "XPQZ"]
    matcher = RabinKarp2D(256, pattern1)
    print(matcher.search(text1))
