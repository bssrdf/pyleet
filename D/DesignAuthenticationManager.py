'''
-Medium-
There is an authentication system that works with authentication tokens. For 
each session, the user will receive a new authentication token that will 
expire timeToLive seconds after the currentTime. If the token is renewed, 
the expiry time will be extended to expire timeToLive seconds after the 
(potentially different) currentTime.

Implement the AuthenticationManager class:

AuthenticationManager(int timeToLive) constructs the AuthenticationManager and 
sets the timeToLive.

generate(string tokenId, int currentTime) generates a new token with the given 
tokenId at the given currentTime in seconds.

renew(string tokenId, int currentTime) renews the unexpired token with the given 
tokenId at the given currentTime in seconds. If there are no unexpired tokens 
with the given tokenId, the request is ignored, and nothing happens.

countUnexpiredTokens(int currentTime) returns the number of unexpired tokens at 
the given currentTime.

Note that if a token expires at time t, and another action happens on time t 
(renew or countUnexpiredTokens), the expiration takes place before the other actions.

 

Example 1:


Input
["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew", "countUnexpiredTokens"]
[[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
Output
[null, null, null, 1, null, null, null, 0]

Explanation
AuthenticationManager authenticationManager = new AuthenticationManager(5); // Constructs the AuthenticationManager with timeToLive = 5 seconds.
authenticationManager.renew("aaa", 1); // No token exists with tokenId "aaa" at time 1, so nothing happens.
authenticationManager.generate("aaa", 2); // Generates a new token with tokenId "aaa" at time 2.
authenticationManager.countUnexpiredTokens(6); // The token with tokenId "aaa" is the only unexpired one at time 6, so return 1.
authenticationManager.generate("bbb", 7); // Generates a new token with tokenId "bbb" at time 7.
authenticationManager.renew("aaa", 8); // The token with tokenId "aaa" expired at time 7, and 8 >= 7, so at time 8 the renew request is ignored, and nothing happens.
authenticationManager.renew("bbb", 10); // The token with tokenId "bbb" is unexpired at time 10, so the renew request is fulfilled and now the token will expire at time 15.
authenticationManager.countUnexpiredTokens(15); // The token with tokenId "bbb" expires at time 15, and the token with tokenId "aaa" expired at time 7, so currently no token is unexpired, so return 0.
 

Constraints:

1 <= timeToLive <= 10^8
1 <= currentTime <= 10^8
1 <= tokenId.length <= 5
tokenId consists only of lowercase letters.
All calls to generate will contain unique values of tokenId.
The values of currentTime across all the function calls will be strictly increasing.
At most 2000 calls will be made to all functions combined.

'''

import heapq

class Session(object):
    def __init__(self, expirationTime):
        self.expTime = expirationTime
        self.delete = False
    def __lt__(self, other):
        return self.expTime < other.expTime 
    def __eq__(self, other):
        return self.expTime == other.expTime 

class AuthenticationManager(object):
    # 75%, 5% 

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.pq = []
        self.id2exp = {}
        self.timeToLive = timeToLive
        

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """        
        session = Session(currentTime+self.timeToLive)   
        heapq.heappush(self.pq, session)
        self.id2exp[tokenId] = session

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.id2exp:
            if self.id2exp[tokenId].expTime > currentTime:
                self.id2exp[tokenId].delete = True                
                session = Session(currentTime+self.timeToLive)   
                heapq.heappush(self.pq, session)
                self.id2exp[tokenId] = session
                

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        while self.pq and self.pq[0].expTime <= currentTime:
            heapq.heappop(self.pq)
        cnt = 0 
        for s in self.pq:
            if not s.delete: cnt += 1
        return cnt          
        
class AuthenticationManagerDictOnly(object):
    # 55%, 83%
    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.id2exp = {}
        self.timeToLive = timeToLive

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.id2exp[tokenId] = currentTime+self.timeToLive

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.id2exp:
            if self.id2exp[tokenId] > currentTime:                
                self.id2exp[tokenId] = currentTime+self.timeToLive
        

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """        
        cnt = 0 
        for s in self.id2exp:
            if self.id2exp[s] > currentTime:
                cnt += 1            
        return cnt          
        


if __name__ == "__main__":
# Your AuthenticationManager object will be instantiated and called as such:
    ''' 
    authenticationManager = AuthenticationManager(5) # Constructs the AuthenticationManager with timeToLive = 5 seconds.
    authenticationManager.renew("aaa", 1) # No token exists with tokenId "aaa" at time 1, so nothing happens.
    authenticationManager.generate("aaa", 2) # Generates a new token with tokenId "aaa" at time 2.
    print(authenticationManager.countUnexpiredTokens(6)) # The token with tokenId "aaa" is the only unexpired one at time 6, so return 1.
    authenticationManager.generate("bbb", 7) # Generates a new token with tokenId "bbb" at time 7.
    authenticationManager.renew("aaa", 8) # The token with tokenId "aaa" expired at time 7, and 8 >= 7, so at time 8 the renew request is ignored, and nothing happens.
    authenticationManager.renew("bbb", 10) # The token with tokenId "bbb" is unexpired at time 10, so the renew request is fulfilled and now the token will expire at time 15.
    print(authenticationManager.countUnexpiredTokens(15)) # The token with tokenId "bbb" expires at time 15, and the token with tokenId "aaa" expired at time 7, so currently no token is unexpired, so return 0.

    '''
    null = 'null'
    authenticationManager = AuthenticationManager(559) # Constructs the AuthenticationManager with timeToLive = 5 seconds.
    calls = ["renew","countUnexpiredTokens","renew","countUnexpiredTokens","countUnexpiredTokens","generate","generate","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","generate","renew","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","renew","countUnexpiredTokens","countUnexpiredTokens","renew","renew","renew","countUnexpiredTokens","generate","countUnexpiredTokens","generate","countUnexpiredTokens","renew","countUnexpiredTokens","countUnexpiredTokens","renew","generate","countUnexpiredTokens","renew","generate","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","generate","renew","renew","countUnexpiredTokens","countUnexpiredTokens","renew","countUnexpiredTokens","countUnexpiredTokens","generate","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","renew","renew","countUnexpiredTokens","countUnexpiredTokens","generate","renew","renew","countUnexpiredTokens","countUnexpiredTokens","renew","countUnexpiredTokens","renew","renew","generate","generate","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","renew","generate","countUnexpiredTokens","generate","renew","countUnexpiredTokens","generate","countUnexpiredTokens","countUnexpiredTokens","renew","generate","countUnexpiredTokens","countUnexpiredTokens","generate"]
    params = [["lv",15],[26],["vttaj",27],[36],[37],["mib",44],["r",55],[60],[81],[107],["jglr",109],["gewcr",113],[140],[143],[162],[181],["xwnxq",192],[196],[211],["pz",236],["k",248],["swptq",249],[250],["ig",288],[292],["iyzuk",293],[305],["s",312],[314],[317],["jgs",319],["huyk",321],[323],["kj",348],["rbww",349],[371],[372],[387],[409],[416],[440],[456],["rvijr",470],["swptq",478],["iqx",479],[484],[489],["jgs",496],[508],[532],["dqjm",553],[575],[602],[606],["wk",625],["dqjm",647],[659],[681],["wjj",689],["nsxwd",706],["qeqyy",715],[728],[759],["dfu",773],[788],["vttaj",807],["dqjm",816],["gk",823],["mz",838],[846],[852],[875],["pfu",881],["gkt",895],[903],["pujx",908],["iflm",917],[928],["k",931],[942],[948],["yx",949],["jywsu",966],[977],[985],["wk",999]]
    res = []
    for func, par in zip(calls, params):
        if func == "renew":
            authenticationManager.renew(par[0], par[1])
            res.append('null')
        if func == "countUnexpiredTokens":
            res.append(authenticationManager.countUnexpiredTokens(par[0]))
        if func == "generate":
            authenticationManager.generate(par[0], par[1])
            res.append('null')
    ans = [null,0,null,0,0,null,null,2,2,2,null,null,3,3,3,3,null,3,3,null,null,null,3,null,4,null,5,null,5,5,null,null,6,null,null,7,7,7,7,7,7,7,null,null,null,8,8,null,8,8,null,9,9,8,null,null,7,6,null,null,null,7,7,null,7,null,null,null,null,9,7,7,null,null,7,null,null,7,null,8,8,null,null,9,9,null]
    for r, a, c, p in zip(res, ans, calls, params):
        if r != a:
            print(r, a, c, p)







