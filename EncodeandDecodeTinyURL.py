'''

-Medium-

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL such 
as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no 
restriction on how your encode/decode algorithm should work. You just need 
to ensure that a URL can be encoded to a tiny URL and the tiny URL can be 
decoded to the original URL.


'''
import random

class Codec:

    def __init__(self):
        self.dict = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.short2long = {}
        self.long2short = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long2short:
            return "http://tinyurl.com/" + self.long2short[longUrl]
        idx = 0
        randStr = ''
        for _ in range(6): randStr += self.dict[random.randint(0,len(self.dict)-1)]
        while randStr in self.short2long:
            randStr[idx] = self.dict[random.randint(0,len(self.dict)-1)]
            idx = (idx + 1) % 5
        self.short2long[randStr] = longUrl
        self.long2short[longUrl] = randStr
        return "http://tinyurl.com/" + randStr
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        randStr = shortUrl.split('/')[-1]
        return self.short2long[randStr] if randStr in self.short2long else shortUrl
        
if __name__ == "__main__":
# Your Codec object will be instantiated and called as such:
    url = 'https://leetcode.com/problems/design-tinyurl'
    codec = Codec()
    tiny = codec.encode(url)
    print(tiny)
    print(codec.decode(tiny))