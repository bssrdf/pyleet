# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl, htmlParser):        
        """
       : type startUrl: str
       : type  htmlParser: 'HtmlParser'
       : rtype List[str]
        """
        res = set()
        def getHost(url):
           return url.split('/')[2]       
        host = getHost(startUrl) 
        def dfs(url):
           res.add(url)
           urls = htmlParser.getUrls(url)
           for conns in urls:
               if url in res or getHost(url) != host:
                   continue
               dfs(conns)
        dfs(startUrl)
        return list(res)
       

