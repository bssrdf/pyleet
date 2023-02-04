
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
                #print(i, j, textHash, self.patternHash)
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
        self.factors_col = [0]*(self.height)
        self.factors_row = [0]*(self.width)
        self.factors_col[0] = 1
        for i in range(1, len(self.factors_col)):
            self.factors_col[i] = (self.RADIX * self.factors_col[i - 1]) % MOD
        self.factors_row[0] = 1
        for i in range(1, len(self.factors_row)):
            self.factors_row[i] = (self.RADIX * self.factors_row[i - 1]) % MOD
        hash1d_p = [0]*self.width
        self.hash2D(self.pattern, hash1d_p, self.width)
        self.patternHash = self.SingleHash(hash1d_p)
        #print('pattern hash = ', self.patternHash)
        #print('factors = ', self.factors)

    def hash2D(self, data, hash1d, hei):
        for i in range(hei):
            hash1d[i] = 0
            for j in range(self.height):
                hash1d[i] = (self.RADIX * hash1d[i] + ord(data[j][i])) % MOD

    def rehash2D(self, data, hash1d, hei, j):
        for i in range(hei):
            hash1d[i] = self.RADIX*((hash1d[i] + MOD - self.factors_col[self.height-1] 
                    * ord(data[j][i])%MOD) % MOD) % MOD
            hash1d[i] = (hash1d[i] + ord(data[j+self.height][i])) % MOD

    def SingleHash(self, hash1d):
        res = 0
        for i in range(self.width):            
            res = (self.RADIX * res + hash1d[i]) % MOD
        return res

    def SingleReHash(self, hash, hash1d, pos):
        hash = self.RADIX*((hash + MOD - self.factors_row[self.width-1]*hash1d[pos]%MOD) % MOD) % MOD 
        hash = (hash + hash1d[pos+self.width]) % MOD   
        return hash
    
    
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
        hash1d = [0]*len(text[0])
        for i in range(len(text)-self.height+1):            
            if i == 0:
                self.hash2D(text, hash1d, len(text[0]))
            else:
                self.rehash2D(text, hash1d, len(text[0]), i-1)
            textHash = 0
            for j in range(len(text[0]) - self.width+1):
                if j == 0:
                    textHash = self.SingleHash(hash1d)
                else:
                    textHash = self.SingleReHash(textHash, hash1d, j-1)
                #print(i, j, textHash, patternHash)
                if textHash == self.patternHash and self.check(text, i, j):
                    return [i, j]
        return None

class BruteForce(object):

    def __init__(self, pattern):
        self.pattern = pattern
        self.height = len(pattern)
        self.width = len(pattern[0])
        
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
        for i in range(len(text)-self.height+1):                        
            for j in range(len(text[0]) - self.width+1):
                if self.check(text, i, j):
                    return [i, j]
        return None




    
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
    matcher = RabinKarp2DV3(256, pattern1)
    print(matcher.search(text1))
    pattern2 = ["ERE",
                "RNE"]
    matcher = RabinKarp2DV3(256, pattern2)
    print(matcher.search(text1))
    matcher = BruteForce(pattern2)
    print(matcher.search(text1))

    import random
    import string
    import time
    chars = string.ascii_uppercase
    im, jm = 1000, 2000
    text = []
    for i in range(im):
        s = ''
        for j in range(jm):
            s += random.choice(chars)
        text.append(s)        
    for t in text:
        print(t)
    pattern = []
    for i in range(40):
        pattern.append(text[357+i][478:478+60])
    for p in pattern:
        print(p)
    start_time = time.time()
    matcher = RabinKarp2DV3(256, pattern)
    print(matcher.search(text))
    print("--- %s seconds ---" % (time.time() - start_time))    
    start_time = time.time()
    matcher = BruteForce(pattern)
    print(matcher.search(text))
    print("--- %s seconds ---" % (time.time() - start_time))    
    #matcher = RabinKarp2D(256, pattern)
    #print(matcher.search(text))




