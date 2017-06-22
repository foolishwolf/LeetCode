class Codec:

    def __init__(self):
        self.l2s = {}
        self.s2l = {}
        self.cnt = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.l2s:
            shortCode = str(self.cnt)
            self.l2s[longUrl] = shortCode
            self.s2l[shortCode] = longUrl
            self.cnt += 1
        else:
            shortCode = 'http://tinyurl.com/' + self.l2s[longUrl]
        return shortCode


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.s2l[shortUrl.split('/')[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

urlList = ['test1', 'test2', 'test3', 'test10']
codec = Codec()
for url in urlList:
    shortUrl = codec.encode(url)
    longUrl = codec.decode(shortUrl)
    print longUrl